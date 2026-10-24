"""Phases track support (gaia_tools 0.6.0, data model 1.5.0): load, validate, claim-source check, re-run and map the
Research/Tracks/Phases/<Phase>/Cycle-<L>-<x N | Baseline>/ folders (five phase reports x six fields of knowledge).

Layout (same 'track run layout' as data model 1.4.0, with fields in place of topics):
  <Phase>/Cycle-<L>-*/<Field folder>/claims/claims.csv, sources/sources.csv, simulation/iter-<k>/{SPEC.md, EXECUTION_RECORD.json}
  <Phase>/Cycle-<L>-*/Provenance/SOURCE_REGISTER.csv, Links/link_register.csv
IDs: claim <PH><L>-<FIELD>-nn (e.g. DV0-NAT-01); SIM citation SIM-<PH>-<FIELD>-<L>/iter-<k>#<check>; sources P01.. (plus reused main/K IDs).

Usage:
  python -m gaia_tools.phases validate <Research dir> [--out f.json]
  python -m gaia_tools.phases claimsource <Research dir> <cycle id, e.g. DV0> [--snapshots DIR] [--out f.json]
  python -m gaia_tools.phases rerun <Research dir> <cycle id> [--python PATH] [--out f.json]
  python -m gaia_tools.phases maps <Research dir> <out dir> --version-label "..."   (maps_all + phase overlay)
Research tooling only: no service, no deployment; it never modifies the records it checks (reruns use a temporary copy)."""
import argparse, collections, glob, hashlib, json, os, re, shutil, subprocess, sys, tempfile
from . import data as D
from .claimsource import parse_phrases, phrase_found

FIELDS = {"NAT": "Natural-Sciences", "FOR": "Formal-Sciences", "SOC": "Social-Sciences", "APP": "Applied-Sciences",
          "HUM": "Humanities", "PHI": "Philosophy-Spirituality"}
PHASES = {"DV": "Divergence", "IN": "Insurgence", "AL": "Allegiance", "CV": "Convergence", "AS": "Ascendence"}
CYCLE_DIR = re.compile(r"^Cycle-(?P<l>[0A-D])-(Baseline|x(3|6|9|12))$")
SIM_REF = re.compile(r"^SIM-(?P<ph>DV|IN|AL|CV|AS)-(?P<f>NAT|FOR|SOC|APP|HUM|PHI)-(?P<l>[0A-D])/iter-(?P<it>\d+)#(?P<chk>[A-Za-z0-9_.]+)$")
CLAIM_FIELDS = ["claim_id", "field", "wording", "claim_class", "framework_label", "conclusion_status", "source_ids", "locator", "confidence",
                "counterevidence_limits", "operationalization", "being", "cross_links", "verification_phrases", "change_vs_prev_cycle"]
CLASSES = ("Empirical", "Mathematical/computational", "Historical", "Interpretive/philosophical", "Spiritual/theological", "Simulation")
BEINGS = ("Body", "Mind", "Soul", "Spirit", "Consciousness", "")
LINK_FIELDS = ["link_id", "from", "to", "link_type", "framework_label", "basis", "statement", "status"]


def phase_cycles(research_dir):
    """[(cycle id e.g. 'DV0'/'DVA', path, phase name)] ordered by phase order then cycle letter."""
    out = []; order = list(PHASES.values())
    for code, name in PHASES.items():
        for p in glob.glob(os.path.join(research_dir, "Tracks", "Phases", name, "Cycle-*")):
            m = CYCLE_DIR.match(os.path.basename(p))
            if m and os.path.isdir(p): out.append((code + m.group("l"), p, name))
    return sorted(out, key=lambda t: (order.index(t[2]), "0ABCD".index(t[0][-1])))


def claims(cp):
    rows = []
    for f, d in FIELDS.items():
        p = os.path.join(cp, d, "claims", "claims.csv")
        if os.path.exists(p):
            for r in D.read_csv(p): r["_file"] = os.path.relpath(p, cp); rows.append(r)
    return rows


def sources(cp):
    f = os.path.join(cp, "Provenance", "SOURCE_REGISTER.csv"); return D.read_csv(f) if os.path.exists(f) else []


def links(cp):
    f = os.path.join(cp, "Links", "link_register.csv"); return D.read_csv(f) if os.path.exists(f) else []


def runs(cp, cid):
    out = []
    for f, d in FIELDS.items():
        recs = glob.glob(os.path.join(cp, d, "simulation", "iter-*", "EXECUTION_RECORD.json"))
        for rec in sorted(recs, key=lambda p: int(p.split("iter-")[1].split(os.sep)[0])):
            r = json.load(open(rec)); h = os.path.dirname(rec)
            out.append(dict(sim_id=r["sim_id"], cycle=cid, field=f, iteration=r["iteration"], directory=os.path.relpath(h, cp),
                            spec=os.path.relpath(os.path.join(h, "SPEC.md"), cp), execution_record=os.path.relpath(rec, cp),
                            script=os.path.relpath(glob.glob(os.path.join(os.path.dirname(h), "sim_*.py"))[0], cp),
                            spec_sha256=r["spec_sha256"], params_sha256=r["params_sha256"], results_sha256=r["results_sha256"], n_checks=r["n_checks"],
                            results={k: sum(c["result"] == k for c in r["pre_registered_checks"]) for k in ("Pass", "Fail", "Supported", "Not supported", "Reported")}))
    return out


def _index(research_dir):
    idx = {}
    for cid, cp, _ in phase_cycles(research_dir):
        for s in runs(cp, cid):
            for c in json.load(open(os.path.join(cp, s["execution_record"])))["pre_registered_checks"]:
                idx[f"{s['sim_id']}/iter-{s['iteration']}#{c['id']}"] = c
    return idx


def validate(research_dir):
    """E1 fields, E2 label, E3 duplicate id, E4 unresolved citation, E5 Established citing a Fail check, E6 'Not supported' not stated,
    E7 Established literature claim without a full-text source, E8 SPEC changed after execution, E9 link label/endpoint,
    E10 claim_class or being not in the allowed set; W1 empty limits, W2 field/ID mismatch, W3 empty operationalization."""
    errs, warns = [], []; idx = _index(research_dir)
    nodes = set(FIELDS) | set(PHASES) | set(D.REPORTS) | {"MR", "GAIA", "SOUL", "SPIRIT", "SUBC", "CONS"}
    for cid, cp, ph in phase_cycles(research_dir):
        reg = {s["source_id"]: s for s in sources(cp)}; seen = set()
        for r in claims(cp):
            k = r.get("claim_id")
            if [x for x in r if not x.startswith("_")] != CLAIM_FIELDS: errs.append((cid, "E1", k, "fields differ")); continue
            if r["framework_label"] not in D.LABELS: errs.append((cid, "E2", k, r["framework_label"]))
            if k in seen: errs.append((cid, "E3", k, "duplicate"))
            seen.add(k)
            if not k.startswith(f"{cid}-{r['field']}-"): warns.append((cid, "W2", k, r["field"]))
            if r["claim_class"] not in CLASSES or r["being"] not in BEINGS: errs.append((cid, "E10", k, r["claim_class"] + "/" + r["being"]))
            lit, res = [], []
            for s in D.split_ids(r["source_ids"]):
                if SIM_REF.match(s):
                    (res.append(idx[s]["result"]) if s in idx else errs.append((cid, "E4", k, s)))
                elif s in reg: lit.append(s)
                else: errs.append((cid, "E4", k, s))
            if r["framework_label"] == "Established" and "Fail" in res: errs.append((cid, "E5", k, "cites a Fail check"))
            if "Not supported" in res and "not supported" not in r["wording"].lower(): errs.append((cid, "E6", k, "Not supported not stated"))
            if r["framework_label"] == "Established" and lit and not any(reg[s]["access_mode"].startswith("full") for s in lit):
                errs.append((cid, "E7", k, "no full-text source"))
            if not r["counterevidence_limits"].strip(): warns.append((cid, "W1", k, "empty limits"))
            if not r["operationalization"].strip(): warns.append((cid, "W3", k, "empty operationalization"))
        for s in runs(cp, cid):
            if hashlib.sha256(open(os.path.join(cp, s["spec"]), "rb").read()).hexdigest() != s["spec_sha256"]:
                errs.append((cid, "E8", s["directory"], "SPEC.md changed after execution"))
        for l in links(cp):
            if l["framework_label"] not in D.LABELS or l["from"] not in nodes or l["to"] not in nodes: errs.append((cid, "E9", l["link_id"], "label/endpoint"))
    return dict(n_cycles=len(phase_cycles(research_dir)), n_errors=len(errs), n_warnings=len(warns), errors=errs, warnings=warns)


def claimsource(research_dir, cid, snapshots=None):
    cp = {c: p for c, p, _ in phase_cycles(research_dir)}[cid]; reg = {s["source_id"]: s for s in sources(cp)}; idx = _index(research_dir); out = []
    for r in claims(cp):
        res = {}; ids = D.split_ids(r["source_ids"]); unresolved = [s for s in ids if not (SIM_REF.match(s) and s in idx) and s not in reg]
        res["K-resolve"] = "Fail" if unresolved else "Pass"
        lit = [s for s in ids if s in reg]
        res["K-access"] = ("Pass" if any(reg[s]["access_mode"].startswith("full") for s in lit) else "Fail") if r["framework_label"] == "Established" and lit else "n/a"
        sims = [idx[s]["result"] for s in ids if s in idx]
        res["K-sim"] = "n/a" if not sims else ("Fail" if (r["framework_label"] == "Established" and "Fail" in sims) or
                                                ("Not supported" in sims and "not supported" not in r["wording"].lower()) else "Pass")
        if snapshots:
            phr = parse_phrases(r["verification_phrases"]); rs = []
            for p in phr:
                sid, phrase = p.split("|", 1); f = os.path.join(snapshots, sid.strip() + ".txt")
                rs.append("Indeterminate" if not os.path.exists(f) else ("Pass" if phrase_found(phrase, open(f, encoding="utf-8", errors="ignore").read()) else "Fail"))
            res["K-phrase"] = "n/a" if not phr else ("Fail" if "Fail" in rs else ("Indeterminate" if "Indeterminate" in rs else "Pass"))
        out.append(dict(claim_id=r["claim_id"], label=r["framework_label"], results=res, unresolved=unresolved))
    summ = {}
    for o in out:
        for k, v in o["results"].items(): summ.setdefault(k, {}).setdefault(v, 0); summ[k][v] += 1
    return dict(cycle=cid, n_claims=len(out), summary=summ, n_fail=sum("Fail" in o["results"].values() for o in out), claims=out)


def rerun(research_dir, cid, python=sys.executable):
    cp = {c: p for c, p, _ in phase_cycles(research_dir)}[cid]
    tmp = tempfile.mkdtemp(prefix="gaia-phase-rerun-"); dst = os.path.join(tmp, os.path.basename(cp))
    shutil.copytree(cp, dst, ignore=shutil.ignore_patterns("__pycache__")); rep = []
    for s in runs(cp, cid):
        old = json.load(open(os.path.join(cp, s["execution_record"]))); sd = os.path.join(dst, os.path.dirname(s["directory"]))
        p = subprocess.run([python, os.path.basename(s["script"]), f"iter-{s['iteration']}"], cwd=sd, capture_output=True, text=True)
        new = json.load(open(os.path.join(dst, s["execution_record"])))
        row = dict(sim_id=s["sim_id"], iteration=s["iteration"], exit=p.returncode, results_identical=old["results_sha256"] == new["results_sha256"],
                   checks_identical=[(c["id"], c["result"]) for c in old["pre_registered_checks"]] == [(c["id"], c["result"]) for c in new["pre_registered_checks"]],
                   params_identical=old["params_sha256"] == new["params_sha256"], spec_identical=old["spec_sha256"] == new["spec_sha256"])
        if p.returncode: row["stderr_tail"] = p.stderr[-400:]
        rep.append(row)
    shutil.rmtree(tmp, ignore_errors=True)
    ok = all(r["exit"] == 0 and r["results_identical"] and r["checks_identical"] and r["params_identical"] and r["spec_identical"] for r in rep)
    return dict(cycle=cid, n_runs=len(rep), all_identical=ok, runs=rep)


def maps(research_dir, out_dir, label):
    """maps_all over all earlier work, then the phase overlay: latest cycle of each phase is placed on the Phase axis
    (organisational placement by report scope) and on Being only where the claim names a Being domain ('being' column)."""
    from . import maps_all as MA, maps as M
    r = MA.build(research_dir, out_dir, label); rules = json.load(open(os.path.join(os.path.dirname(__file__), "lens_rules.json")))
    pcs = phase_cycles(research_dir); latest = {}
    for cid, cp, ph in pcs: latest[ph] = (cid, cp)
    pl_p = os.path.join(out_dir, "matrix", "claim_placement.csv"); place = D.read_csv(pl_p); new = []
    for ph, (cid, cp) in latest.items():
        for c in claims(cp):
            ls = M.lenses_for(c["wording"], rules)
            new.append(dict(claim_id=c["claim_id"], report=f"Phase {ph} / {FIELDS[c['field']]}", label=c["framework_label"],
                            being=c["being"] or f"outside Being axis (field {c['field']})", lenses=";".join(ls) or "Unassigned",
                            alchemy="Unassigned (undefined: G01 9.3 / 12 Q3)", phase=ph, source_set=f"phase cycle {cid}"))
    M._csv(pl_p, place + new, ["claim_id", "report", "label", "being", "lenses", "alchemy", "phase", "source_set"])
    pf = []
    for ph in PHASES.values():
        for f, fd in FIELDS.items():
            cs = [p for p in new if p["phase"] == ph and p["report"].endswith(fd)]
            cnt = collections.Counter(D.LABELS[p["label"]] for p in cs)
            pf.append(dict(phase=ph, field=fd, n_claims=len(cs), E=cnt["E"], P=cnt["P"], PS=cnt["PS"], H=cnt["H"],
                           cycle=latest.get(ph, ("", ""))[0], flag="EMPTY (not yet researched)" if ph not in latest else ("EMPTY" if not cs else ("UNDER-RESEARCHED (no E/P claim)" if cnt["E"] + cnt["P"] == 0 else "populated"))))
    M._csv(os.path.join(out_dir, "matrix", "phase_x_field_30.csv"), pf, ["phase", "field", "n_claims", "E", "P", "PS", "H", "cycle", "flag"])
    pl = []
    for ph in PHASES.values():
        for l in M.AXES["Lens"]:
            cs = [p for p in new if p["phase"] == ph and l in p["lenses"].split(";")]
            cnt = collections.Counter(D.LABELS[p["label"]] for p in cs)
            pl.append(dict(phase=ph, lens=l, n_claims=len(cs), E=cnt["E"], P=cnt["P"], PS=cnt["PS"], H=cnt["H"], claim_ids=";".join(p["claim_id"] for p in cs)))
    M._csv(os.path.join(out_dir, "matrix", "phase_x_lens_25.csv"), pl, ["phase", "lens", "n_claims", "E", "P", "PS", "H", "claim_ids"])
    cells = D.read_csv(os.path.join(out_dir, "matrix", "intersections_625.csv"))
    for c in cells:
        cs = [p for p in new if p["phase"] == c["phase"] and c["lens"] in p["lenses"].split(";") and p["being"] == c["being"]]
        c["phase_claims_in_being_phase_lens_projection"] = len(cs)
    M._csv(os.path.join(out_dir, "matrix", "intersections_625.csv"), cells, list(cells[0].keys()))
    gp = os.path.join(out_dir, "graph", "link_graph.json"); g = json.load(open(gp)); ids = {n["id"] for n in g["nodes"]}
    for code, name in list(PHASES.items()) + list(FIELDS.items()):
        if code not in ids and (code in FIELDS or name in latest):
            g["nodes"].append(dict(id=code, label=("Phase: " if code in PHASES else "Field: ") + name, kind="phase" if code in PHASES else "field of knowledge"))
    for ph, (cid, cp) in latest.items():
        for l in links(cp):
            g["edges"].append(dict(id=l["link_id"], source=l["from"], target=l["to"], type=l["link_type"], label_code=D.LABELS[l["framework_label"]],
                                   framework_label=l["framework_label"], basis=l["basis"], statement=l["statement"], status=l["status"], origin=f"phase cycle {cid}"))
    M._json(gp, g)
    chp = os.path.join(out_dir, "changes", "changes.csv"); ch = D.read_csv(chp)
    for i, (cid, cp, ph) in enumerate(pcs):
        for c in claims(cp):
            ch.append(dict(kind="claim", id=c["claim_id"], cycle=cid, report=f"Phase {ph}", prev_label="", label=c["framework_label"], change=c["change_vs_prev_cycle"], pressure="", note=c["field"]))
    M._csv(chp, ch, ["kind", "id", "cycle", "report", "prev_label", "label", "change", "pressure", "note"])
    sp = os.path.join(out_dir, "simulations", "simulations_index.json"); idx = json.load(open(sp))
    for cid, cp, ph in pcs:
        for s in runs(cp, cid): s["track"] = "Phases/" + ph; idx.append(s)
    M._json(sp, idx)
    return dict(base=r, phase_claims_placed=len(new), phase_cycles=[c for c, _, _ in pcs], phase_x_field=pf, phase_x_lens=pl, sims=len(idx))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0]); ap.add_argument("cmd", choices=["validate", "claimsource", "rerun", "maps"])
    ap.add_argument("research_dir"); ap.add_argument("arg", nargs="?"); ap.add_argument("--snapshots"); ap.add_argument("--python", default=sys.executable)
    ap.add_argument("--out"); ap.add_argument("--version-label")
    a = ap.parse_args(argv)
    if a.cmd == "validate": r = validate(a.research_dir)
    elif a.cmd == "claimsource": r = claimsource(a.research_dir, a.arg, a.snapshots)
    elif a.cmd == "rerun": r = rerun(a.research_dir, a.arg, a.python)
    else:
        r = maps(a.research_dir, a.arg, a.version_label); print(json.dumps(dict(phase_claims_placed=r["phase_claims_placed"], phase_cycles=r["phase_cycles"], sims=r["sims"]))); return 0
    if a.out:
        with open(a.out, "w", newline="\n") as f: json.dump(r, f, indent=1, ensure_ascii=False); f.write("\n")
    s = {k: v for k, v in r.items() if k in ("n_cycles", "n_errors", "n_warnings", "n_claims", "summary", "n_fail", "n_runs", "all_identical")}
    print(json.dumps(s)); return 1 if r.get("n_errors") or r.get("n_fail") or r.get("all_identical") is False else 0


if __name__ == "__main__":
    sys.exit(main())
