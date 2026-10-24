"""SIM-R7-C4: bookkeeping and graph analyses of the unified framework (Report 7) on the Cycle-4 ledger and link register (28 links incl. L28).
strict(), essential(), ess_rule(), components(), lenses(), ledger() are copied from SIM-R7-C3. New in Cycle 4: (a) does Y06 (loneliness <->
depression, Mendelian randomization) give Report 2 an Established link? (b) Body x Justice cell; (c) lens placement of the new Cycle-4 claims;
(d) diminishing-returns audit and a cross-cycle trend of new claims and sources; (e) register completeness; (f) gate inputs.
Report 7's own Cycle-4 claims (C4-R7-*) are written FROM these results, so they are excluded from the inputs (ledger(..., skip='C4-R7-'))
and reruns stay identical. These test the consistency of our own records, not any claim about the world."""
import sys, os, csv, glob, json, re, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "tools")); import runner as R
RID = {"R1 Body": "R1", "R2 Mind": "R2", "R3 Soul": "R3", "R4 Spirit": "R4", "R5 Consciousness": "R5", "R6 Earth": "R6", "R7 Unified": "R7", "All": "ALL"}
BEING = {"R1": "Body", "R2": "Mind", "R3": "Soul", "R4": "Spirit", "R5": "Consciousness"}
def ledger(cyc, skip="C4-R7-"):
    out = {}
    for f in sorted(glob.glob(os.path.join(cyc, "Report-*", "claims", "claims.csv"))):
        for r in csv.DictReader(open(f, encoding="utf-8")):
            if skip and r["claim_id"].startswith(skip): continue
            out[r["claim_id"]] = r
    return out
def ids(s): return [x.strip() for x in (s or "").split(";") if x.strip()]
def strict(link, L):
    if link["framework_label"] != "Established": return link["framework_label"], []
    bad = [c for c in ids(link["basis"]) if c not in L or L[c]["framework_label"] != "Established"]
    return ("Plausible" if bad else "Established"), bad
def rep_of(cid): m = re.search(r"-(R\d)-", cid); return m.group(1) if m else None
def essential(link):
    b = ids(link["basis"]); ends = {RID.get(link["from"]), RID.get(link["to"])}
    if len(b) == 1: return set(b)
    ess = set()
    for e in ends:
        mine = [c for c in b if rep_of(c) == e]
        if len(mine) == 1: ess.add(mine[0])
    return ess
def components(nodes, edges):
    par = {n: n for n in nodes}
    def f(x):
        while par[x] != x: x = par[x]
        return x
    for a, b in edges: par[f(a)] = f(b)
    g = {}
    for n in nodes: g.setdefault(f(n), []).append(n)
    return sorted(sorted(v) for v in g.values())
def lenses(text, rules):
    return {k for k, terms in rules.items() if any(re.search(r"\b" + t, text, re.I) for t in terms)}
def main():
    P, prev, H = R.start(sys.argv[1]); t0 = R.now(); X = P["experiments"]; res = {}; chk = []; k = P["iteration"]
    C4 = os.path.normpath(os.path.join(H, P["cycle_dir"])); L = ledger(C4); CY = os.path.dirname(C4)
    reg = list(csv.DictReader(open(os.path.normpath(os.path.join(H, P["input_register"])), encoding="utf-8")))
    if k == 1:
        C3 = os.path.join(CY, "Cycle-3-x9"); L3 = ledger(C3, skip=None); reg3 = list(csv.DictReader(open(os.path.join(C3, "Report-7-Unified", "maps", "link_register_input.csv"), encoding="utf-8")))
        c3r = json.load(open(os.path.join(C3, "Report-7-Unified", "simulation", "iter-2", "outputs", "results.json")))["downgraded"]
        mine = [l["link_id"] for l in reg3 if strict(l, L3)[0] != l["framework_label"]]
        chk.append(R.chk("V1", "copied strict rule reproduces the Cycle-3 iteration-2 result (no Established link downgraded) on the Cycle-3 ledger and register", [mine, c3r], mine == c3r))
        t = [essential({"basis": "C0-R1-01;C0-R1-02;C0-R2-01", "from": "R1 Body", "to": "R2 Mind"}), essential({"basis": "C0-R1-01", "from": "R1 Body", "to": "R1 Body"})]
        chk.append(R.chk("V2", "essential-claim definition on toy links (as in Cycle 3)", [sorted(x) for x in t], t[0] == {"C0-R2-01"} and t[1] == {"C0-R1-01"}))
    elif k == 2:
        out = [dict(link_id=l["link_id"], old=l["framework_label"], new=strict(l, L)[0], bad=strict(l, L)[1]) for l in reg]
        res["strict_rule"] = out; dn = [o["link_id"] for o in out if o["old"] != o["new"]]; res["downgraded"] = dn
        chk.append(R.chk("H2", "no Established link in the Cycle-4 register is downgraded by the strict rule", dn, not dn, "hypothesis"))
        missing = sorted({c for l in reg for c in ids(l["basis"]) if c not in L})
        chk.append(R.chk("V3", "every basis claim of every link resolves to a Cycle-4 ledger claim", missing, not missing))
    elif k == 3:
        r2 = [(l["link_id"], l["from"], l["to"], strict(l, L)[0]) for l in reg if "R2 Mind" in (l["from"], l["to"])]
        l28 = [x for x in r2 if x[0] == "L28"]; res.update(r2_links=r2, basis_labels={c: L[c]["framework_label"] for c in ids([l for l in reg if l["link_id"] == "L28"][0]["basis"])})
        ok = any(x[3] == "Established" and (x[1] != x[2]) for x in r2)
        chk.append(R.chk("H3", "the Cycle-4 MR evidence (Y06) gives Report 2 an Established link to another report", [r2, res["basis_labels"]], ok, "hypothesis"))
    elif k == 4:
        e = X["flip"]; Elinks = [l for l in reg if l["framework_label"] == "Established"]; out = {}
        for p in e["p"]:
            rng = np.random.default_rng(e["seed"]); fr = []
            for _ in range(e["draws"]):
                Lf = {kk: dict(v) for kk, v in L.items()}
                for kk in Lf:
                    if Lf[kk]["framework_label"] == "Established" and rng.random() < p: Lf[kk]["framework_label"] = "Plausible"
                fr.append(np.mean([strict(l, Lf)[0] != "Established" for l in Elinks]))
            out[str(p)] = dict(median=float(np.median(fr)), q90=float(np.quantile(fr, .9)))
        res["flip"] = dict(by_p=out, n_E_links=len(Elinks))
        chk.append(R.chk("H4", "even at a 20% claim-mislabelling rate, the median share of Established links that downgrade is <= 0.5", out, out[str(e["p"][-1])]["median"] <= .5, "hypothesis"))
    elif k == 5:
        nodes = ["R1", "R2", "R3", "R4", "R5", "R6"]; edges = [(RID[l["from"]], RID[l["to"]]) for l in reg if l["framework_label"] == "Established" and RID[l["from"]] in nodes and RID[l["to"]] in nodes]
        comps = components(nodes, edges); res["E_components"] = comps; r2 = [c for c in comps if "R2" in c][0]
        chk.append(R.chk("H5", "with L28, Report 2 (Mind) joins another report through Established links", comps, len(r2) > 1, "hypothesis"))
    elif k == 6:
        e = X["matrix"]; rules = json.load(open(os.path.normpath(os.path.join(H, e["lens_rules"]))))["lenses"]
        prevm = {(r["being"], r["lens"]): r for r in csv.DictReader(open(os.path.normpath(os.path.join(H, e["v3_matrix"])), encoding="utf-8"))}
        cnt = {}
        for cid, r in L.items():
            b = BEING.get(r["report"])
            if not b: continue
            for ln in lenses(r["wording"], rules): cnt.setdefault((b, ln), []).append(cid)
        new4 = {f"{b}x{ln}": [c for c in v if c.startswith("C4-")] for (b, ln), v in cnt.items()}
        still_empty = [f"{b}x{ln}" for (b, ln) in prevm if not cnt.get((b, ln))]; under = [f"{b}x{ln}" for (b, ln) in prevm if 0 < len(cnt.get((b, ln), [])) < 3]
        res["matrix"] = dict(body_justice=cnt.get(("Body", "Justice"), []), still_empty=still_empty, under_researched=under, cells_with_c4_claims={kk: v for kk, v in new4.items() if v})
        chk.append(R.chk("H6", "the one Being x Lens cell still EMPTY in Maps v3 (Body x Justice) is populated by Cycle-4 claims (keyword rule v1.0.1)", [res["matrix"]["body_justice"], still_empty], bool(res["matrix"]["body_justice"]), "hypothesis"))
    elif k == 7:
        e = X["lens_new"]; rules = json.load(open(os.path.normpath(os.path.join(H, e["lens_rules"]))))["lenses"]
        new = {c: sorted(lenses(r["wording"], rules)) for c, r in L.items() if c.startswith("C4-")}; share = float(np.mean([bool(v) for v in new.values()]))
        res["lens_new"] = dict(placements=new, share_with_lens=share, n=len(new))
        chk.append(R.chk("H7", "at least half of the new Cycle-4 claims (R1-R6) receive at least one lens under keyword rule v1.0.1", [share, len(new)], share >= .5, "hypothesis"))
    elif k == 8:
        bad = [(l["link_id"], c) for l in reg if l["framework_label"] == "Established" for c in ids(l["basis"]) if c in L and L[c]["framework_label"] in ("Philosophical/Spiritual", "Hypothetical")]
        res["gaia_separability"] = bad
        chk.append(R.chk("H8", "separability of science from the motherthread: no Established link rests on a Philosophical/Spiritual or Hypothetical claim", bad, not bad, "hypothesis"))
    elif k == 9:
        L3 = ledger(os.path.join(CY, "Cycle-3-x9"), skip=None); ch = [c for c in L3 if c in L and (L3[c]["framework_label"], L3[c]["conclusion_status"]) != (L[c]["framework_label"], L[c]["conclusion_status"])]
        noted = [c for c in L3 if c in L and L[c].get("c4_change", "Carried unchanged.") != "Carried unchanged."]; miss = [c for c in L3 if c not in L]
        res["diminishing"] = dict(n_carried=len(L3), changed_label_or_status=ch, with_c4_note=len(noted), dropped=miss, n_new_r1_r6=len([c for c in L if c.startswith("C4-")]))
        chk.append(R.chk("H9", "real new work changes something: at least one claim carried from Cycle 3 changes label or status in Cycle 4", [len(ch), len(L3), len(noted)], len(ch) > 0, "hypothesis"))
    elif k == 10:
        reg_s = list(csv.DictReader(open(os.path.join(C4, "Provenance", "SOURCE_REGISTER.csv"), encoding="utf-8")))
        src = {c: sum(r["cycle_added"] == c for r in reg_s) for c in ("C1", "C2", "C3", "C4")}
        newc = {c: len([x for x in L if x.startswith(c + "-")]) for c in ("C1", "C2", "C3", "C4")}
        res["trend"] = dict(new_sources=src, new_claims_excl_C4_R7=newc)
        chk.append(R.chk("H10", "diminishing returns: Cycle 4 adds fewer new sources and fewer new claims (R1-R6) than Cycle 3", res["trend"], src["C4"] < src["C3"] and newc["C4"] < newc["C3"], "hypothesis"))
    elif k == 11:
        empty = [l["link_id"] for l in reg if not l.get("c4_status")]; unres = sorted({c for l in reg for c in ids(l.get("c4_evidence")) if c not in L})
        chk.append(R.chk("V4", "register completeness: every link has a Cycle-4 status and every Cycle-4 evidence claim resolves", [empty, unres], not empty and not unres))
    elif k == 12:
        recs = sorted(glob.glob(os.path.join(C4, "Report-[1-6]-*", "simulation", "iter-*", "EXECUTION_RECORD.json"))) + [os.path.join(H, "..", f"iter-{i}", "EXECUTION_RECORD.json") for i in range(1, 12)]
        cs = [c for f in recs for c in json.load(open(f))["pre_registered_checks"]]
        v = [c for c in cs if c["kind"] == "validation"]; h = [c for c in cs if c["kind"] == "hypothesis"]
        res["gate_inputs"] = dict(runs=len(recs) + 1, validation_pass=sum(c["result"] == "Pass" for c in v), validation=len(v), supported=sum(c["result"] == "Supported" for c in h), hypotheses=len(h),
                                  independent_review="not performed", independent_human_coding="not possible for this agent", gate="INDETERMINATE (Indeterminate is never Pass)")
        chk.append(R.chk("H12", "all validation checks across Cycle-4 runs (R1-R6 and R7 iterations 1-11) pass", [res["gate_inputs"]["validation_pass"], len(v)], all(c["result"] == "Pass" for c in v), "hypothesis"))
        chk.append(R.chk("G0", "gate inputs (the gate stays INDETERMINATE without independent review)", res["gate_inputs"], True, "reporting"))
    R.finish(H, P, res, chk, t0)
if __name__ == "__main__": main()
