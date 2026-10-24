"""Claim-source checker (offline; optional local snapshot phrase search).

Usage:  python -m gaia_tools.claimsource <Research dir> <cycle id> [--snapshots DIR] [--out report.json]
Per claim it checks:
  K-resolve   every cited source / simulation check resolves (literature IDs in SOURCE_REGISTER;
              SIM IDs to pre-registered checks; 'C0:' to the Cycle-0 records)
  K-access    an Established claim that rests on literature cites at least one full-text source
              (the Cycle-1 access rule; applied to Cycle >= 1 only - Cycle 0 predates the rule)
  K-sim       an Established claim may not cite a check whose result is 'Fail';
              a claim citing a 'Not supported' check must say 'not supported' in its wording
  K-phrase    (only with --snapshots) each 'SOURCE|phrase' in verification_phrases occurs in the
              text snapshot <DIR>/<SOURCE>.txt (whitespace-normalized, case-insensitive);
              a missing snapshot is Indeterminate, never Pass.
Result per check: Pass / Fail / Indeterminate / n/a. Network access is never used."""
import argparse, json, os, re, sys
from . import data as D


def parse_phrases(field):
    """'SRC|phrase || SRC|phrase' -> ['SRC|phrase', ...]. Fields starting 'n/a' (simulation claims) give [].
    (0.1.0 split on ';', which mis-parsed the ' || ' separator used in the ledgers; fixed in 0.2.0.)"""
    f = (field or "").strip()
    if not f or f.lower().startswith("n/a"):
        return []
    return [p.strip() for p in f.split("||") if "|" in p]


def _norm(t):
    return re.sub(r"\s+", " ", t).strip().lower()


def phrase_found(phrase, text):
    """Ledger phrases are regular expressions (e.g. '8\\.7 million'); match case-insensitively on whitespace-normalised
    text, falling back to a literal substring test if the phrase is not a valid regex."""
    t = _norm(text); p = _norm(phrase)
    try:
        return re.search(p, t) is not None or p in t
    except re.error:
        return p in t


def check(research_dir, cycle_id, snapshots=None):
    cyc = dict(D.cycles(research_dir)); cp = cyc[cycle_id]
    reg = {s["source_id"]: s for s in D.sources(cp)}
    checks = D.check_index(cp, cycle_id)
    c0 = D.check_index(cyc["C0"], "C0") if "C0" in cyc else {}
    n_cycle = int(cycle_id[1:])
    out = []
    for r in D.claims(cp):
        ids = D.split_ids(r["source_ids"]); res = {}
        unresolved, lit, sim_results = [], [], []
        for sid in ids:
            m = D.SIM_REF.match(sid)
            if m:
                c = D.lookup_sim(sid, cycle_id, lambda x: checks if x == cycle_id else (c0 if x == "C0" else
                                 (D.check_index(cyc[x], x) if x in cyc else {})))
                if c is None:
                    unresolved.append(sid)
                else:
                    sim_results.append((sid, c["result"]))
            elif sid in reg:
                lit.append(sid)
            else:
                unresolved.append(sid)
        res["K-resolve"] = "Fail" if unresolved else "Pass"
        if r["framework_label"] == "Established" and n_cycle >= 1 and any(not s.startswith("G") for s in lit):
            res["K-access"] = "Pass" if any(reg[s]["access_mode"].startswith("full") for s in lit) else "Fail"
        else:
            res["K-access"] = "n/a"
        bad = [s for s, x in sim_results if x == "Fail"] if r["framework_label"] == "Established" else []
        ns = [s for s, x in sim_results if x == "Not supported"]
        if sim_results:
            res["K-sim"] = "Fail" if bad or (ns and "not supported" not in r["wording"].lower()) else "Pass"
        else:
            res["K-sim"] = "n/a"
        if snapshots:
            phr = parse_phrases(r["verification_phrases"])
            if not phr:
                res["K-phrase"] = "n/a"
            else:
                rs = []
                for p in phr:
                    sid, phrase = p.split("|", 1)
                    f = os.path.join(snapshots, f"{sid.strip()}.txt")
                    rs.append("Indeterminate" if not os.path.exists(f) else
                              ("Pass" if phrase_found(phrase, open(f, encoding="utf-8", errors="ignore").read()) else "Fail"))
                res["K-phrase"] = "Fail" if "Fail" in rs else ("Indeterminate" if "Indeterminate" in rs else "Pass")
        out.append(dict(claim_id=r["claim_id"], label=r["framework_label"], results=res, unresolved=unresolved,
                        not_supported_cited=ns))
    summ = {}
    for o in out:
        for k, v in o["results"].items():
            summ.setdefault(k, {}).setdefault(v, 0); summ[k][v] += 1
    return dict(cycle=cycle_id, n_claims=len(out), summary=summ,
                n_fail=sum("Fail" in o["results"].values() for o in out), claims=out)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("research_dir"); ap.add_argument("cycle"); ap.add_argument("--snapshots"); ap.add_argument("--out")
    a = ap.parse_args(argv)
    r = check(a.research_dir, a.cycle, a.snapshots)
    if a.out:
        open(a.out, "w").write(json.dumps(r, indent=1, ensure_ascii=False) + "\n")
    print(json.dumps(r["summary"]), "claims with a Fail:", r["n_fail"])
    for o in r["claims"]:
        if "Fail" in o["results"].values():
            print("FAIL", o["claim_id"], o["results"], o["unresolved"])
    return 0 if r["n_fail"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
