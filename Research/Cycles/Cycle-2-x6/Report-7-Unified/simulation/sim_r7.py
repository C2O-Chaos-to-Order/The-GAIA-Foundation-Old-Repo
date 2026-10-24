"""SIM-R7-C2: bookkeeping and structure checks for the Cycle-2 synthesis (no empirical content).
(1) the stricter Established-link rule pre-registered in Cycle 1 ('an Established link needs every essential basis claim Established';
applied in its strict reading: every basis claim); (2) separability of the science links from the GAIA motherthread;
(3) a structural parallel between SIM-R1-C2 and SIM-R6-C2; (4)-(6) consistency audits of the Cycle-2 register and ledger."""
import sys, os, json, csv, glob, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools")); import runner as R
def ledger(cyc):
    out = {}
    for f in sorted(glob.glob(os.path.join(cyc, "Report-*", "claims", "claims.csv"))):
        for r in csv.DictReader(open(f, encoding="utf-8")): out[r["claim_id"]] = r
    return out
def ids(s): return [x.strip() for x in (s or "").split(";") if x.strip()]
def strict(link, L):
    if link["framework_label"] != "Established": return link["framework_label"], []
    bad = [c for c in ids(link["basis"]) if c not in L or L[c]["framework_label"] != "Established"]
    return ("Plausible" if bad else "Established"), bad
def connected(nodes, edges):
    if not nodes: return True
    adj = {n: set() for n in nodes}
    for a, b in edges:
        if a in adj and b in adj: adj[a].add(b); adj[b].add(a)
    seen = set(); st = [next(iter(nodes))]
    while st:
        n = st.pop()
        if n in seen: continue
        seen.add(n); st += list(adj[n]-seen)
    return seen == set(nodes)
def main():
    P, prev, H = R.start(sys.argv[1]); t0 = R.now(); X = P["experiments"]; res = {}; chk = []
    C2 = os.path.normpath(os.path.join(H, P["cycle_dir"])); L = ledger(C2)
    reg_in = list(csv.DictReader(open(os.path.normpath(os.path.join(H, P["input_register"])), encoding="utf-8")))
    if prev: res["carried_from_prev"] = {k: prev[k] for k in P.get("carry", []) if k in prev}
    if "strict_rule" in X:
        toyL = {"a": {"framework_label": "Established"}, "b": {"framework_label": "Plausible"}}
        t1 = strict({"framework_label": "Established", "basis": "a"}, toyL)[0]; t2 = strict({"framework_label": "Established", "basis": "a;b"}, toyL)[0]; t3 = strict({"framework_label": "Plausible", "basis": "a"}, toyL)[0]
        chk.append(R.chk("SR0", "rule on toy cases: E<-{E} stays E; E<-{E,P} becomes P; non-E links untouched", [t1, t2, t3], [t1, t2, t3] == ["Established", "Plausible", "Plausible"]))
        out = []
        for l in reg_in:
            new, bad = strict(l, L); out.append(dict(link_id=l["link_id"], frm=l["from"], to=l["to"], old=l["framework_label"], new=new, non_established_basis=[(c, L[c]["framework_label"] if c in L else "missing") for c in bad]))
        res["strict_rule"] = out; res["downgraded"] = [o["link_id"] for o in out if o["old"] != o["new"]]
        r2 = [o for o in out if "R2 Mind" in (o["frm"], o["to"])]; r2E = [o["link_id"] for o in r2 if o["new"] == "Established"]
        res["r2_established_after_rule"] = r2E
        chk.append(R.chk("SR1", "report links downgraded by the strict rule and the non-Established basis claims that cause it", [(o["link_id"], o["non_established_basis"]) for o in out if o["old"] != o["new"]], True, kind="reporting"))
        chk.append(R.chk("SR2", "C1 open question: R2 Mind keeps at least one Established link under the strict rule", r2E, len(r2E) >= 1, kind="hypothesis"))
    if "separability" in X:
        new = {o["link_id"]: o["new"] for o in (prev or {}).get("strict_rule", [])} or {l["link_id"]: l["framework_label"] for l in reg_in}
        nodes = {f"R{i}" for i in range(1, 7)}; edges_EP = []; edges_E = []
        for l in reg_in:
            a = l["from"].split()[0]; b = l["to"].split()[0] if l["to"] != "All" else None
            lab = new.get(l["link_id"], l["framework_label"])
            if b and a in nodes and b in nodes and a != b:
                if lab in ("Established", "Plausible"): edges_EP.append((a, b))
                if lab == "Established": edges_E.append((a, b))
        cEP = connected(nodes, edges_EP); cE = connected(nodes, edges_E)
        comps = []; seen = set(); adj = {n: set() for n in nodes}
        for a_, b_ in edges_E: adj[a_].add(b_); adj[b_].add(a_)
        for n in sorted(nodes):
            if n in seen: continue
            grp = set(); st = [n]
            while st:
                m = st.pop()
                if m in grp: continue
                grp.add(m); st += list(adj[m]-grp)
            seen |= grp; comps.append(sorted(grp))
        res["separability"] = dict(edges_EP=edges_EP, edges_E=edges_E, connected_EP=cEP, connected_E=cE, components_E=comps)
        chk.append(R.chk("SP1", "without GAIA (Philosophical/Spiritual motherthread) and PS/H links, Reports 1-6 remain connected through Established/Plausible links alone", cEP, cEP, kind="hypothesis"))
        chk.append(R.chk("SP2", "report connectivity using Established links only (after the strict rule)", comps, True, kind="reporting"))
    if "parallel" in X:
        e = X["parallel"]; ld = lambda p: json.load(open(os.path.normpath(os.path.join(H, p))))
        r1 = ld(e["r1_iter4"]); r6a = ld(e["r6_iter1"]); r6b = ld(e["r6_iter6"])
        p0 = [o["peak"] for o in r1["setpoint_adaptation"] if o["rate"] == 0][0]
        r1_unb = min(o["peak"] for o in r1["setpoint_adaptation"] if o["rate"] > 0 and o["bound"] is None)/p0
        r1_bd = max(o["peak"] for o in r1["setpoint_adaptation"] if o["rate"] > 0 and o["bound"] is not None)/p0
        w0 = r6a["no_adaptation_width"]; r6_unb = max(w for r, w in r6a["unbounded_by_rate"] if r > 0)/w0
        r6s = r6b["robustness_summary"]
        a = r1_unb >= 1.5 and r6_unb < 0.8; b = r1_bd <= 1.2 and r6s["frac_constrained_ok"] >= 0.8
        res["parallel"] = dict(r1_unbounded_peak_ratio=r1_unb, r1_bounded_peak_ratio=r1_bd, r6_unbounded_best_width_ratio=r6_unb, r6_constrained_ok_fraction=r6s["frac_constrained_ok"])
        chk.append(R.chk("PA1", "structural parallel (L01): in BOTH toys unbounded adaptation of the reference degrades regulation and bounded adaptation preserves it", [a, b], a and b, kind="hypothesis"))
    if "register_consistency" in X:
        e = X["register_consistency"]; reg = list(csv.DictReader(open(os.path.normpath(os.path.join(H, e["c2_register"])), encoding="utf-8")))
        rule = {o["link_id"]: o["new"] for o in json.load(open(os.path.normpath(os.path.join(H, e["rule_results"]))))["strict_rule"]}
        mism = [(l["link_id"], l["framework_label"], rule.get(l["link_id"])) for l in reg if rule.get(l["link_id"]) != l["framework_label"]]
        chk.append(R.chk("RC1", "every link label in the Cycle-2 register equals the strict-rule output of iteration 1", mism, not mism))
        recs = {}
        for f in glob.glob(os.path.join(C2, "Report-*", "simulation", "iter-*", "EXECUTION_RECORD.json")):
            r = json.load(open(f))
            for c in r["pre_registered_checks"]: recs[f"{r['sim_id']}/iter-{r['iteration']}#{c['id']}"] = c["result"]
        unres = [(l["link_id"], s) for l in reg for s in ids(l.get("c2_sim_checks", "")) if s not in recs]
        chk.append(R.chk("RC2", "every c2_sim_checks reference in the register resolves to an executed check", unres, not unres))
        missing_basis = [(l["link_id"], c) for l in reg for c in ids(l["basis"]) + ids(l.get("c2_evidence", "")) if c not in L]
        chk.append(R.chk("RC3", "every basis and c2_evidence claim id exists in the Cycle-2 ledger", missing_basis, not missing_basis))
    if "transition" in X:
        e = X["transition"]; L1 = ledger(os.path.normpath(os.path.join(H, e["c1_dir"])))
        lost = [c for c in L1 if c not in L]
        chk.append(R.chk("T0", "no Cycle-1 claim is lost in the Cycle-2 ledger", lost, not lost))
        trans = {}; changed = []
        for c, r in L1.items():
            k = f"{r['framework_label']} -> {L[c]['framework_label']}"; trans[k] = trans.get(k, 0)+1
            if r["framework_label"] != L[c]["framework_label"] or r["conclusion_status"] != L[c]["conclusion_status"]: changed.append(c)
        new = [c for c in L if c not in L1]; frac = len(changed)/len(L1)
        res["transition"] = dict(n_c1=len(L1), n_c2=len(L), n_new=len(new), label_transitions=trans, changed=changed, frac_changed=frac,
                                 new_by_label={lab: sum(L[c]["framework_label"] == lab for c in new) for lab in ("Established", "Plausible", "Philosophical/Spiritual", "Hypothetical")})
        chk.append(R.chk("T1", "diminishing-returns probe: Cycle 2 changes the label or status of <= 5% of carried claims", [len(changed), len(L1), frac], frac <= 0.05, kind="hypothesis"))
    if "audit" in X:
        recs = {}
        for f in glob.glob(os.path.join(C2, "Report-*", "simulation", "iter-*", "EXECUTION_RECORD.json")):
            r = json.load(open(f))
            for c in r["pre_registered_checks"]: recs[f"{r['sim_id']}/iter-{r['iteration']}#{c['id']}"] = c["result"]
        reg = {r["source_id"]: r for r in csv.DictReader(open(os.path.join(C2, "Provenance", "SOURCE_REGISTER.csv"), encoding="utf-8"))}
        unres = []; ns_bad = []; acc = []; empty = []
        for c, r in L.items():
            for s in ids(r["source_ids"]):
                if s.startswith("SIM-") and "-C2/" in s:
                    if s not in recs: unres.append((c, s))
                    elif recs[s] == "Not supported" and "not supported" not in r["wording"].lower(): ns_bad.append((c, s))
                elif not s.startswith("SIM-") and not s.startswith("C0:") and s not in reg: unres.append((c, s))
            if c.startswith("C2-") and r["framework_label"] == "Established":
                lit = [s for s in ids(r["source_ids"]) if not s.startswith(("SIM-", "C0:", "G"))]
                if lit and not any(reg[s]["access_mode"].startswith("full") for s in lit if s in reg): acc.append(c)
            if not r["counterevidence_limits"].strip(): empty.append(c)
        chk.append(R.chk("AU1", "every Cycle-2 simulation reference and every literature id in the ledger resolves", unres, not unres))
        chk.append(R.chk("AU2", "every claim citing a 'Not supported' check says 'not supported' in its wording", ns_bad, not ns_bad))
        chk.append(R.chk("AU3", "every new Established literature claim has at least one full-text source", acc, not acc))
        chk.append(R.chk("AU4", "no claim has an empty counterevidence/limits field (Cycle-1 warning Q1 closed)", empty, not empty))
        res["audit"] = dict(n_claims=len(L), n_checks_indexed=len(recs))
    R.finish(H, P, res, chk, t0)
if __name__ == "__main__": main()
