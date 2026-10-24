"""SIM-R7 (Cycle 1+): consistency audit of the Cycle ledger, robustness of the cross-report link graph, and mechanical rejection screening.
It checks bookkeeping and the structure of argument; it cannot show that any link is true."""
import sys, os, json, csv, glob, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools")); import runner as R
split = lambda s: [x.strip() for x in s.split(";") if x.strip()]
def load(C):
    reg = {r["source_id"]: r for r in csv.DictReader(open(f"{C}/Provenance/SOURCE_REGISTER.csv"))}
    claims = []; [claims.extend(csv.DictReader(open(p))) for p in sorted(glob.glob(f"{C}/Report-*/claims/claims.csv"))]
    links = list(csv.DictReader(open(glob.glob(f"{C}/Report-7*/maps/link_register.csv")[0])))
    sims = {}
    for rec in glob.glob(f"{C}/Report-*/simulation/iter-*/EXECUTION_RECORD.json"):
        j = json.load(open(rec)); sims[f"{j['sim_id']}/iter-{j['iteration']}"] = {c["id"]: c["result"] for c in j["pre_registered_checks"]}
    c0 = os.path.join(C, "..", "Cycle-0-Baseline")
    for rec in glob.glob(f"{c0}/Report-*/simulation/EXECUTION_RECORD.json"):
        j = json.load(open(rec)); sims["C0:"+j["sim_id"]] = {c["id"]: c["result"] for c in j["pre_registered_checks"]}
    return reg, claims, links, sims
def connected(nodes, edges):
    adj = {n: set() for n in nodes}
    for a, b in edges: adj[a].add(b); adj[b].add(a)
    seen = {nodes[0]}; st = [nodes[0]]
    while st:
        for m in adj[st.pop()]:
            if m not in seen: seen.add(m); st.append(m)
    return len(seen) == len(nodes), sorted(set(nodes)-seen)
def main():
    P, prev, H = R.start(sys.argv[1]); t0 = R.now(); X = P["experiments"]; res = {}; chk = []
    C = os.path.abspath(os.path.join(H, "..", "..", "..")); reg, claims, links, sims = load(C); ids = {c["claim_id"]: c for c in claims}
    if "consistency" in X:
        req = ["claim_id", "report", "wording", "claim_class", "framework_label", "conclusion_status", "source_ids", "confidence", "verification_phrases"]
        bad_fields = [c["claim_id"] for c in claims if any(not (c.get(k) or "").strip() for k in req)]
        bad_vocab = [c["claim_id"] for c in claims if c["claim_class"] not in P["classes"] or c["conclusion_status"] not in P["statuses"] or c["framework_label"] not in P["labels"]]
        bad_map = [c["claim_id"] for c in claims if c["framework_label"] in P["labels"] and c["conclusion_status"] not in P["label_status_map"][c["framework_label"]]]
        unres, e_sim, self_c, ns_unstated = [], [], [], []
        for c in claims:
            for s in split(c["source_ids"]):
                if s.startswith(("SIM-", "C0:SIM-")):
                    key, _, ck = s.partition("#")
                    if key.startswith(P["sim_id"]): self_c.append((c["claim_id"], s)); continue
                    if key not in sims or (ck and ck not in sims[key]): unres.append((c["claim_id"], s)); continue
                    if c["framework_label"] == "Established" and (not ck or sims[key][ck] == "Fail"): e_sim.append((c["claim_id"], s))
                    if ck and sims[key][ck] == "Not supported" and "not supported" not in c["wording"].lower(): ns_unstated.append((c["claim_id"], s))
                elif s not in reg: unres.append((c["claim_id"], s))
        lit = lambda c: [s for s in split(c["source_ids"]) if s in reg]
        e_access = [c["claim_id"] for c in claims if c["framework_label"] == "Established" and lit(c) and not any(reg[s]["access_mode"].startswith("full text") for s in lit(c))]
        e_framework = [c["claim_id"] for c in claims if c["framework_label"] == "Established" and lit(c) and not any("SIM-" in s for s in split(c["source_ids"])) and all(reg[s]["source_type"] == "project governing document" for s in lit(c))]
        dup = len(claims)-len(ids)
        lk_bad = [l["link_id"] for l in links if any(not (l.get(k) or "").strip() for k in P["link_required"]) or l["framework_label"] not in P["labels"]
                  or l["link_type"] not in P["link_types"] or any(b not in ids for b in split(l["basis"]))]
        lk_sim_bad = [(l["link_id"], s) for l in links for s in split(l.get("c1_sim_checks", "")) if s.partition("#")[0] not in sims or s.partition("#")[2] not in sims[s.partition("#")[0]]]
        types_missing = [t for t in P["link_types"] if t not in {l["link_type"] for l in links}]
        cons = dict(n_claims=len(claims), n_links=len(links), n_sources=len(reg), missing_fields=bad_fields, bad_vocab=bad_vocab, label_status_mismatch=bad_map, duplicates=dup,
                    unresolved=unres, established_on_failed_sim=e_sim, not_supported_unstated=ns_unstated, established_without_full_text=e_access, established_framework_only=e_framework, self_citations=self_c,
                    links_bad=lk_bad, links_bad_sim_refs=lk_sim_bad, link_types_missing=types_missing,
                    label_counts={s: sum(c["framework_label"] == s for c in claims) for s in P["labels"]}, status_counts={s: sum(c["conclusion_status"] == s for c in claims) for s in P["statuses"]},
                    per_report={r: sum(c["report"] == r for c in claims) for r in sorted({c["report"] for c in claims})},
                    link_label_counts={s: sum(l["framework_label"] == s for l in links) for s in P["labels"]})
        res["consistency"] = cons
        chk.append(R.chk("K1", "all claims complete, controlled vocabulary, label-status mapping, unique ids", [bad_fields, bad_vocab, bad_map, dup], not bad_fields and not bad_vocab and not bad_map and dup == 0))
        chk.append(R.chk("K2", "every source and SIM#check citation resolves to the register or a Cycle execution record", unres, not unres))
        chk.append(R.chk("K3", "no Established claim cites a failed validation check or an unspecified check; any cited 'Not supported' outcome is stated as 'not supported' in the wording", [e_sim, ns_unstated], not e_sim and not ns_unstated))
        chk.append(R.chk("K4", "Cycle-1 access rule: every Established literature claim has at least one full-text source", e_access, not e_access))
        chk.append(R.chk("K5", "no Established claim rests only on project governing documents (claims with simulation evidence are exempt: the run is the evidence)", e_framework, not e_framework))
        chk.append(R.chk("K6", "link register complete, all link types present, every basis claim and SIM check resolves", [lk_bad, lk_sim_bad, types_missing], not lk_bad and not lk_sim_bad and not types_missing))
    if "graph" in X:
        nodes = P["reports"]; rep = lambda s: s.split()[0]
        filters = {"all": lambda l: True, "no_PS_or_H": lambda l: l["framework_label"] in ("Established", "Plausible"),
                   "basis_all_established": lambda l: all(ids[b]["framework_label"] == "Established" for b in split(l["basis"])),
                   "basis_has_established": lambda l: any(ids[b]["framework_label"] == "Established" for b in split(l["basis"]))}
        out = {}
        for name, fl in filters.items():
            E = [(rep(l["from"]), rep(l["to"])) for l in links if fl(l) and rep(l["from"]) in nodes and rep(l["to"]) in nodes]
            ok, miss = connected(nodes, E); out[name] = dict(n_links=len([l for l in links if fl(l)]), connected=ok, isolated=miss)
        res["graph"] = out
        chk.append(R.chk("N1", "R1-R7 are connected by the full link register", out["all"], out["all"]["connected"]))
        chk.append(R.chk("N2", "graph stays connected when Philosophical/Spiritual and Hypothetical links are removed", out["no_PS_or_H"], out["no_PS_or_H"]["connected"], kind="hypothesis"))
        chk.append(R.chk("N3", "graph stays connected using only links whose every basis claim is Established", out["basis_all_established"], out["basis_all_established"]["connected"], kind="hypothesis"))
    if "rejection" in X:
        rows = []
        for l in links:
            tests = split(l.get("c1_sim_checks", "")); outc = {t: sims[t.partition("#")[0]][t.partition("#")[2]] for t in tests}
            weak = [b for b in split(l["basis"]) if ids[b]["conclusion_status"] in ("Contested", "Indeterminate")]
            flag = "pressure: simulation test not supported" if any(v in ("Not supported", "Fail") for v in outc.values()) else ("pressure: contested/indeterminate basis" if weak else "no rejection trigger observed")
            rows.append(dict(link_id=l["link_id"], label=l["framework_label"], sim_outcomes=outc, contested_basis=weak, screen=flag))
        res["rejection"] = rows
        n_p = sum(r["screen"] != "no rejection trigger observed" for r in rows)
        chk.append(R.chk("J1", "every Plausible/Hypothetical link names a rejection criterion and at least one Cycle-1 test (simulation check or literature test)", None,
                         all((l.get("rejection_criterion") or "").strip() and ((l.get("c1_sim_checks") or "").strip() or (l.get("c1_literature_test") or "").strip()) for l in links if l["framework_label"] in ("Plausible", "Hypothetical"))))
        chk.append(R.chk("J2", "report links under pressure from Cycle-1 tests", [(r["link_id"], r["screen"]) for r in rows if r["screen"] != "no rejection trigger observed"], True, kind="reporting"))
        res["rejection_summary"] = dict(n_links=len(rows), n_under_pressure=n_p)
    R.finish(H, P, res, chk, t0)
if __name__ == "__main__": main()
