"""Track support (gaia_tools 0.5.0, data model 1.4.0): load, validate, claim-source check, re-run and map the
Research/Tracks/<track>/Cycle-<L>-x<N>/ folders (first track: Soul-Spirit-Subconscious-Consciousness).

Track layout:
  <track>/Cycle-<L>-x<N>/<Topic>/claims/claims.csv, <Topic>/sources/sources.csv, <Topic>/simulation/iter-<k>/{SPEC.md, EXECUTION_RECORD.json}
  <track>/Cycle-<L>-x<N>/Provenance/SOURCE_REGISTER.csv, <track>/Cycle-<L>-x<N>/Links/link_register.csv
Track SIM citation: SIM-<TOPIC>-<L>/iter-<k>#<check>, e.g. SIM-SOUL-A/iter-2#H1.

Usage:
  python -m gaia_tools.tracks validate <Research dir> [--out f.json]
  python -m gaia_tools.tracks claimsource <Research dir> <track cycle id, e.g. TA> [--snapshots DIR] [--out f.json]
  python -m gaia_tools.tracks rerun <Research dir> <track cycle id> [--python PATH] [--out f.json]"""
import argparse, glob, hashlib, json, os, re, shutil, subprocess, sys, tempfile
from . import data as D
from .claimsource import parse_phrases, phrase_found

TOPICS = {"SOUL": "Soul", "SPIRIT": "Spirit", "SUBC": "Subconscious", "CONS": "Consciousness"}
TRACK_SIM_REF = re.compile(r"^SIM-(?P<topic>SOUL|SPIRIT|SUBC|CONS)-(?P<cyc>[A-Z])/iter-(?P<it>\d+)#(?P<chk>[A-Za-z0-9_.]+)$")
CLAIM_FIELDS = ["claim_id", "topic", "wording", "claim_class", "framework_label", "conclusion_status", "source_ids", "locator", "confidence",
                "counterevidence_limits", "deepens", "cross_links", "verification_phrases", "change_vs_prev_track_cycle"]
LINK_FIELDS = ["link_id", "from", "to", "link_type", "framework_label", "basis", "statement", "status"]


def track_cycles(research_dir):
    """[(id, path, track name)] e.g. ('TA', .../Cycle-A-x3, 'Soul-Spirit-Subconscious-Consciousness'), ordered by letter."""
    out = []
    for p in glob.glob(os.path.join(research_dir, "Tracks", "*", "Cycle-*-x*")):
        m = re.match(r"Cycle-([A-Z])-x(\d+)$", os.path.basename(p))
        if m and os.path.isdir(p):
            out.append(("T" + m.group(1), p, os.path.basename(os.path.dirname(p))))
    return sorted(out, key=lambda t: (t[2], t[0]))


def claims(cp):
    rows = []
    for t, d in TOPICS.items():
        f = os.path.join(cp, d, "claims", "claims.csv")
        if os.path.exists(f):
            for r in D.read_csv(f):
                r["_file"] = os.path.relpath(f, cp); rows.append(r)
    return rows


def sources(cp):
    f = os.path.join(cp, "Provenance", "SOURCE_REGISTER.csv")
    return D.read_csv(f) if os.path.exists(f) else []


def links(cp):
    f = os.path.join(cp, "Links", "link_register.csv")
    return D.read_csv(f) if os.path.exists(f) else []


def runs(cp, tid):
    out = []
    for t, d in TOPICS.items():
        for rec in sorted(glob.glob(os.path.join(cp, d, "simulation", "iter-*", "EXECUTION_RECORD.json")), key=lambda p: int(p.split("iter-")[1].split(os.sep)[0])):
            r = json.load(open(rec)); h = os.path.dirname(rec)
            out.append(dict(sim_id=r["sim_id"], cycle=tid, topic=t, iteration=r["iteration"], directory=os.path.relpath(h, cp),
                            spec=os.path.relpath(os.path.join(h, "SPEC.md"), cp), execution_record=os.path.relpath(rec, cp),
                            script=os.path.relpath(glob.glob(os.path.join(os.path.dirname(h), "sim_*.py"))[0], cp),
                            spec_sha256=r["spec_sha256"], params_sha256=r["params_sha256"], results_sha256=r["results_sha256"],
                            n_checks=r["n_checks"], results={k: sum(c["result"] == k for c in r["pre_registered_checks"])
                                                             for k in ("Pass", "Fail", "Supported", "Not supported", "Reported", "Indeterminate")}))
    return out


def check_index(cp, tid):
    idx = {}
    for s in runs(cp, tid):
        r = json.load(open(os.path.join(cp, s["execution_record"])))
        for c in r["pre_registered_checks"]:
            idx[f"{s['sim_id']}/iter-{s['iteration']}#{c['id']}"] = c
    return idx


def _all_index(research_dir):
    idx = {}
    for tid, cp, _ in track_cycles(research_dir):
        idx.update(check_index(cp, tid))
    return idx


def validate(research_dir):
    """Errors (E*) and warnings (W*) for every track cycle. E1 missing/extra claim fields, E2 unknown label, E3 duplicate id,
    E4 unresolved source/SIM citation, E5 claim citing a Fail check labelled Established, E6 cites a 'Not supported' check
    without saying 'not supported', E7 Established literature claim without a full-text source, E8 SPEC hash mismatch,
    E9 link with unknown label or endpoint; W1 empty limits, W2 topic/ID mismatch."""
    errs, warns = [], []; idx = _all_index(research_dir)
    for tid, cp, track in track_cycles(research_dir):
        reg = {s["source_id"]: s for s in sources(cp)}; seen = set()
        for r in claims(cp):
            cid = r.get("claim_id")
            if list(k for k in r if not k.startswith("_")) != CLAIM_FIELDS: errs.append((tid, "E1", cid, "fields differ from CLAIM_FIELDS"))
            if r["framework_label"] not in D.LABELS: errs.append((tid, "E2", cid, r["framework_label"]))
            if cid in seen: errs.append((tid, "E3", cid, "duplicate"))
            seen.add(cid)
            if not cid.startswith(f"{tid}-{r['topic']}-"): warns.append((tid, "W2", cid, r["topic"]))
            lit, res = [], []
            for s in D.split_ids(r["source_ids"]):
                if TRACK_SIM_REF.match(s):
                    if s not in idx: errs.append((tid, "E4", cid, s))
                    else: res.append(idx[s]["result"])
                elif s in reg: lit.append(s)
                else: errs.append((tid, "E4", cid, s))
            if r["framework_label"] == "Established" and "Fail" in res: errs.append((tid, "E5", cid, "cites a Fail check"))
            if "Not supported" in res and "not supported" not in r["wording"].lower(): errs.append((tid, "E6", cid, "Not supported not stated"))
            if r["framework_label"] == "Established" and [s for s in lit if not s.startswith("G")] and not any(reg[s]["access_mode"].startswith("full") for s in lit):
                errs.append((tid, "E7", cid, "no full-text source"))
            if not r["counterevidence_limits"].strip(): warns.append((tid, "W1", cid, "empty limits"))
        for s in runs(cp, tid):
            if hashlib.sha256(open(os.path.join(cp, s["spec"]), "rb").read()).hexdigest() != s["spec_sha256"]:
                errs.append((tid, "E8", s["directory"], "SPEC.md changed after execution"))
        nodes = set(TOPICS) | set(D.REPORTS) | {"MR", "GAIA"}
        for l in links(cp):
            if l["framework_label"] not in D.LABELS or l["from"] not in nodes or l["to"] not in nodes: errs.append((tid, "E9", l["link_id"], "label/endpoint"))
    return dict(n_errors=len(errs), n_warnings=len(warns), errors=errs, warnings=warns)


def claimsource(research_dir, tid, snapshots=None):
    tc = {t: p for t, p, _ in track_cycles(research_dir)}; cp = tc[tid]; reg = {s["source_id"]: s for s in sources(cp)}; idx = _all_index(research_dir)
    out = []
    for r in claims(cp):
        res = {}; ids = D.split_ids(r["source_ids"]); unresolved = [s for s in ids if not (TRACK_SIM_REF.match(s) and s in idx) and s not in reg]
        res["K-resolve"] = "Fail" if unresolved else "Pass"
        lit = [s for s in ids if s in reg and not s.startswith("G")]
        res["K-access"] = ("Pass" if any(reg[s]["access_mode"].startswith("full") for s in lit) else "Fail") if r["framework_label"] == "Established" and lit else "n/a"
        sims = [idx[s]["result"] for s in ids if s in idx]
        res["K-sim"] = "n/a" if not sims else ("Fail" if (r["framework_label"] == "Established" and "Fail" in sims) or
                                                ("Not supported" in sims and "not supported" not in r["wording"].lower()) else "Pass")
        if snapshots:
            phr = parse_phrases(r["verification_phrases"])
            if not phr: res["K-phrase"] = "n/a"
            else:
                rs = []
                for p in phr:
                    sid, phrase = p.split("|", 1); f = os.path.join(snapshots, sid.strip() + ".txt")
                    rs.append("Indeterminate" if not os.path.exists(f) else ("Pass" if phrase_found(phrase, open(f, encoding="utf-8", errors="ignore").read()) else "Fail"))
                res["K-phrase"] = "Fail" if "Fail" in rs else ("Indeterminate" if "Indeterminate" in rs else "Pass")
        out.append(dict(claim_id=r["claim_id"], label=r["framework_label"], results=res, unresolved=unresolved))
    summ = {}
    for o in out:
        for k, v in o["results"].items(): summ.setdefault(k, {}).setdefault(v, 0); summ[k][v] += 1
    return dict(track_cycle=tid, n_claims=len(out), summary=summ, n_fail=sum("Fail" in o["results"].values() for o in out), claims=out)


def rerun(research_dir, tid, python=sys.executable):
    tc = {t: p for t, p, _ in track_cycles(research_dir)}; cp = tc[tid]
    tmp = tempfile.mkdtemp(prefix="gaia-track-rerun-"); dst = os.path.join(tmp, os.path.basename(cp))
    shutil.copytree(cp, dst, ignore=shutil.ignore_patterns("__pycache__")); rep = []
    for s in runs(cp, tid):
        old = json.load(open(os.path.join(cp, s["execution_record"]))); sd = os.path.join(dst, os.path.dirname(s["directory"]))
        p = subprocess.run([python, os.path.basename(s["script"]), f"iter-{s['iteration']}"], cwd=sd, capture_output=True, text=True)
        new = json.load(open(os.path.join(dst, s["execution_record"])))
        row = dict(sim_id=s["sim_id"], iteration=s["iteration"], exit=p.returncode,
                   results_identical=old["results_sha256"] == new["results_sha256"],
                   checks_identical=[(c["id"], c["result"]) for c in old["pre_registered_checks"]] == [(c["id"], c["result"]) for c in new["pre_registered_checks"]],
                   params_identical=old["params_sha256"] == new["params_sha256"], spec_identical=old["spec_sha256"] == new["spec_sha256"])
        if p.returncode: row["stderr_tail"] = p.stderr[-400:]
        rep.append(row)
    shutil.rmtree(tmp, ignore_errors=True)
    ok = all(r["exit"] == 0 and r["results_identical"] and r["checks_identical"] and r["params_identical"] and r["spec_identical"] for r in rep)
    return dict(track_cycle=tid, n_runs=len(rep), all_identical=ok, runs=rep)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0]); sp = ap.add_subparsers(dest="cmd", required=True)
    a1 = sp.add_parser("validate"); a1.add_argument("research_dir"); a1.add_argument("--out")
    a2 = sp.add_parser("claimsource"); a2.add_argument("research_dir"); a2.add_argument("cycle"); a2.add_argument("--snapshots"); a2.add_argument("--out")
    a3 = sp.add_parser("rerun"); a3.add_argument("research_dir"); a3.add_argument("cycle"); a3.add_argument("--python", default=sys.executable); a3.add_argument("--out")
    a = ap.parse_args(argv)
    r = validate(a.research_dir) if a.cmd == "validate" else (claimsource(a.research_dir, a.cycle, a.snapshots) if a.cmd == "claimsource" else rerun(a.research_dir, a.cycle, a.python))
    if a.out: open(a.out, "w", newline="\n").write(json.dumps(r, indent=1, ensure_ascii=False) + "\n")
    if a.cmd == "validate": print(f"{r['n_errors']} errors, {r['n_warnings']} warnings"); [print(*e) for e in r["errors"]]; return 1 if r["n_errors"] else 0
    if a.cmd == "claimsource": print(json.dumps(r["summary"]), "claims with a Fail:", r["n_fail"]); [print("FAIL", o["claim_id"], o["results"]) for o in r["claims"] if "Fail" in o["results"].values()]; return 1 if r["n_fail"] else 0
    for x in r["runs"]: print(x["sim_id"], x["iteration"], "exit", x["exit"], "results", x["results_identical"], "checks", x["checks_identical"])
    print("ALL IDENTICAL" if r["all_identical"] else "DIFFERENCES FOUND", f"({r['n_runs']} runs)"); return 0 if r["all_identical"] else 1


if __name__ == "__main__":
    sys.exit(main())
