"""SIM-R7-C3: bookkeeping and graph analyses of the unified framework (Report 7) on the Cycle-3 ledger and link register.
(1) strict Established-link rule (reproduced from SIM-R7-C2); (2) a pre-registered definition of 'essential' basis claims (carried item):
a basis claim is ESSENTIAL for a link if it is the only basis claim from its report among the link's endpoint reports, or the only basis
claim of the link; the 'essential rule' then requires every essential basis claim to be Established and not Contested/Indeterminate, and at
least one Established basis claim from each endpoint report (one for a within-report link); (3) label-flip sensitivity; (4) graph
connectivity; (5) Being x Lens matrix coverage; (6) two-method lens placement (keyword rule v1.0.1 vs hand coding, carried item; same agent);
(7) GAIA separability audit; (8) diminishing-returns audit. These test the consistency of our own records, not any claim about the world."""
import sys, os, csv, glob, json, re, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "tools")); import runner as R
RID = {"R1 Body": "R1", "R2 Mind": "R2", "R3 Soul": "R3", "R4 Spirit": "R4", "R5 Consciousness": "R5", "R6 Earth": "R6", "R7 Unified": "R7", "All": "ALL"}
BEING = {"R1": "Body", "R2": "Mind", "R3": "Soul", "R4": "Spirit", "R5": "Consciousness"}
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
def rep_of(cid): m = re.search(r"-(R\d)-", cid); return m.group(1) if m else None
def essential(link):
    b = ids(link["basis"]); ends = {RID.get(link["from"]), RID.get(link["to"])}
    if len(b) == 1: return set(b)
    ess = set()
    for e in ends:
        mine = [c for c in b if rep_of(c) == e]
        if len(mine) == 1: ess.add(mine[0])
    return ess
def ess_rule(link, L):
    if link["framework_label"] != "Established": return link["framework_label"], []
    b = ids(link["basis"]); ends = {RID.get(link["from"]), RID.get(link["to"])}
    bad = [c for c in essential(link) if c not in L or L[c]["framework_label"] != "Established" or L[c]["conclusion_status"] in ("Contested", "Indeterminate")]
    for e in ends:
        if e in ("R7", "ALL"): continue
        if not any(rep_of(c) == e and c in L and L[c]["framework_label"] == "Established" for c in b): bad.append(f"no Established basis from {e}")
    return ("Plausible" if bad else "Established"), bad
def components(nodes, edges):
    par = {n: n for n in nodes}
    def f(x):
        while par[x] != x: x = par[x]
        return x
    for a, b in edges: par[f(a)] = f(b)
    g = {}
    for n in nodes: g.setdefault(f(n), []).append(n)
    return sorted(sorted(v) for v in g.values())
def kappa(a, b):
    a = np.asarray(a); b = np.asarray(b); po = float(np.mean(a == b)); pa = a.mean(); pb = b.mean(); pe = pa*pb+(1-pa)*(1-pb)
    return ((po-pe)/(1-pe) if pe < 1 else 1.0), po
def lenses(text, rules):
    return {k for k, terms in rules.items() if any(re.search(r"\b" + t, text, re.I) for t in terms)}
def main():
    P, prev, H = R.start(sys.argv[1]); t0 = R.now(); X = P["experiments"]; res = {}; chk = []
    C3 = os.path.normpath(os.path.join(H, P["cycle_dir"])); L = ledger(C3)
    reg = list(csv.DictReader(open(os.path.normpath(os.path.join(H, P["input_register"])), encoding="utf-8")))
    if "reproduce" in X:
        e = X["reproduce"]; C2 = os.path.normpath(os.path.join(H, e["c2_dir"])); L2 = ledger(C2)
        reg2 = list(csv.DictReader(open(os.path.join(C2, "Report-7-Unified", "maps", "link_register.csv"), encoding="utf-8")))
        c2r = json.load(open(os.path.join(C2, "Report-7-Unified", "simulation", "iter-1", "outputs", "results.json")))["downgraded"]
        # C2 iteration 1 applied the rule to the C1 labels; the C2 register already carries the downgraded labels, so re-derive from C1 labels
        reg1 = {r["link_id"]: r for r in csv.DictReader(open(os.path.join(C2, "..", "Cycle-1-x3", "Report-7-Unified", "maps", "link_register.csv"), encoding="utf-8"))}
        mine = [l["link_id"] for l in reg2 if strict(dict(l, framework_label=reg1[l["link_id"]]["framework_label"]), L2)[0] != reg1[l["link_id"]]["framework_label"]]
        chk.append(R.chk("V1", "copied strict rule reproduces the Cycle-2 downgrades (L04, L08, L16) from the Cycle-1 labels and Cycle-2 ledger", [mine, c2r], sorted(mine) == sorted(c2r)))
        toyL = {"a": {"framework_label": "Established", "conclusion_status": "Supported"}, "b": {"framework_label": "Plausible", "conclusion_status": "Supported"}}
        t = [essential({"basis": "C0-R1-01;C0-R1-02;C0-R2-01", "from": "R1 Body", "to": "R2 Mind"}), essential({"basis": "C0-R1-01", "from": "R1 Body", "to": "R1 Body"})]
        chk.append(R.chk("V2", "essential-claim definition on toy links: {R2 sole claim} for a 2+1 basis; the single claim for a 1-claim basis", [sorted(x) for x in t], t[0] == {"C0-R2-01"} and t[1] == {"C0-R1-01"}))
    if "strict_c3" in X:
        out = []
        for l in reg:
            new, bad = strict(l, L); out.append(dict(link_id=l["link_id"], old=l["framework_label"], new=new, bad=bad))
        res["strict_rule"] = out; dn = [o["link_id"] for o in out if o["old"] != o["new"]]; res["downgraded"] = dn
        chk.append(R.chk("H2", "no Established link in the Cycle-3 register is downgraded by the strict rule (new Cycle-3 evidence weakens no E link)", dn, not dn, kind="hypothesis"))
        missing = sorted({c for l in reg for c in ids(l["basis"]) if c not in L})
        chk.append(R.chk("V3", "every basis claim of every link resolves to a Cycle-3 ledger claim", missing, not missing))
    if "essential" in X:
        C1reg = {r["link_id"]: r for r in csv.DictReader(open(os.path.normpath(os.path.join(H, X["essential"]["c1_register"])), encoding="utf-8"))}
        out = []
        for l in reg:
            base = dict(l, framework_label=C1reg[l["link_id"]]["framework_label"]) if l["link_id"] in C1reg else l
            s_new, _ = strict(base, L); e_new, bad = ess_rule(base, L)
            out.append(dict(link_id=l["link_id"], pre_rule=base["framework_label"], strict=s_new, essential_rule=e_new, essential=sorted(essential(l)), reasons=bad))
        res["essential"] = out; restored = [o["link_id"] for o in out if o["pre_rule"] == "Established" and o["strict"] != "Established" and o["essential_rule"] == "Established"]
        res["restored_by_essential_rule"] = restored
        chk.append(R.chk("H3", "under the pre-registered essential-claim rule, at least one of the three links downgraded in Cycle 2 (L04, L08, L16) would be Established", [(o["link_id"], o["essential"], o["reasons"]) for o in out if o["link_id"] in ("L04", "L08", "L16")], len(restored) > 0, kind="hypothesis"))
        chk.append(R.chk("H3r", "report links whose label differs between strict and essential rules", [(o["link_id"], o["strict"], o["essential_rule"]) for o in out if o["strict"] != o["essential_rule"]], True, kind="reporting"))
    if "flip" in X:
        e = X["flip"]; rng = np.random.default_rng(e["seed"]); Elinks = [l for l in reg if l["framework_label"] == "Established"]; fr = []
        for _ in range(e["draws"]):
            Lf = {k: dict(v) for k, v in L.items()}
            for k in Lf:
                if Lf[k]["framework_label"] == "Established" and rng.random() < e["p"]: Lf[k]["framework_label"] = "Plausible"
            fr.append(np.mean([strict(l, Lf)[0] != "Established" for l in Elinks]))
        m = float(np.median(fr)); res["flip"] = dict(median_fraction_downgraded=m, p=e["p"], n_E_links=len(Elinks), q90=float(np.quantile(fr, 0.9)))
        chk.append(R.chk("H4", f"if each Established claim were wrongly labelled with probability {e['p']}, the median share of Established links that downgrade is <= 0.5", [m, res["flip"]["q90"]], m <= 0.5, kind="hypothesis"))
    if "graph" in X:
        nodes = ["R1", "R2", "R3", "R4", "R5", "R6"]; edges = [(RID[l["from"]], RID[l["to"]]) for l in reg if l["framework_label"] == "Established" and RID[l["from"]] in nodes and RID[l["to"]] in nodes]
        comps = components(nodes, edges); res["E_components"] = comps; r2 = [c for c in comps if "R2" in c][0]
        chk.append(R.chk("H5", "with the three new Cycle-3 links, Report 2 (Mind) joins another report through Established links", comps, len(r2) > 1, kind="hypothesis"))
    if "matrix" in X:
        e = X["matrix"]; rules = json.load(open(os.path.normpath(os.path.join(H, e["lens_rules"]))))["lenses"]
        prevm = {(r["being"], r["lens"]): r for r in csv.DictReader(open(os.path.normpath(os.path.join(H, e["v2_matrix"])), encoding="utf-8"))}
        cnt = {}
        for cid, r in L.items():
            b = BEING.get(r["report"])
            if not b: continue
            for ln in lenses(r["wording"], rules): cnt.setdefault((b, ln), []).append(cid)
        newly = [f"{b}x{ln}" for (b, ln), v in prevm.items() if v["flag"] == "EMPTY" and cnt.get((b, ln))]
        still = [f"{b}x{ln}" for (b, ln), v in prevm.items() if not cnt.get((b, ln))]
        res["matrix"] = dict(newly_populated=newly, still_empty=still, counts={f"{b}x{ln}": len(v) for (b, ln), v in cnt.items()})
        chk.append(R.chk("H6", "at least 3 of the 6 Being x Lens cells that were EMPTY in Maps v2 are populated by Cycle-3 claims (keyword rule)", [newly, still], len(newly) >= 3, kind="hypothesis"))
    if "lens_two_method" in X:
        e = X["lens_two_method"]; rules = json.load(open(os.path.normpath(os.path.join(H, e["lens_rules"]))))["lenses"]
        sample = json.load(open(os.path.join(H, e["sample"]))); hand = {r["claim_id"]: r for r in csv.DictReader(open(os.path.join(H, e["hand"]), encoding="utf-8"))}
        import subprocess
        redraw = subprocess.run([sys.executable, os.path.join(H, "..", "draw_lens_sample.py")], capture_output=True, text=True)
        chk.append(R.chk("V4", "the 40-claim sample is reproducible from its seed (redrawn file identical)", redraw.returncode, redraw.returncode == 0 and json.load(open(os.path.join(H, e["sample"]))) == sample))
        out = {}
        for ln in rules:
            a = [int(ln in lenses(L[c]["wording"], rules)) for c in sample]; b = [int(hand[c][ln]) for c in sample]
            k, po = kappa(a, b); out[ln] = dict(kappa=(None if np.isnan(k) else k), agreement=po, rule_n=sum(a), hand_n=sum(b))
        ks = [v["kappa"] for v in out.values() if v["kappa"] is not None]; mk = float(np.mean(ks)) if ks else None; res["lens_two_method"] = dict(per_lens=out, mean_kappa=mk)
        chk.append(R.chk("H7", "keyword rule and hand coding agree at least moderately on lens placement (mean Cohen kappa over lenses >= 0.41)", [mk, {k: (v["kappa"], v["rule_n"], v["hand_n"]) for k, v in out.items()}], mk is not None and mk >= 0.41, kind="hypothesis"))
    if "gaia" in X:
        bad = [(l["link_id"], c) for l in reg if l["framework_label"] == "Established" for c in ids(l["basis"]) if c in L and L[c]["framework_label"] in ("Philosophical/Spiritual", "Hypothetical")]
        res["gaia_separability"] = bad
        chk.append(R.chk("H8", "separability of science from the motherthread: no Established link rests on a Philosophical/Spiritual or Hypothetical claim", bad, not bad, kind="hypothesis"))
    if "diminishing" in X:
        e = X["diminishing"]; L2 = ledger(os.path.normpath(os.path.join(H, e["c2_dir"]))); ch = [c for c in L2 if c in L and (L2[c]["framework_label"], L2[c]["conclusion_status"]) != (L[c]["framework_label"], L[c]["conclusion_status"])]
        noted = [c for c in L2 if c in L and L[c].get("c3_change", "Carried unchanged.") != "Carried unchanged."]
        res["diminishing"] = dict(n_carried=len(L2), changed_label_or_status=ch, with_c3_note=len(noted), n_new=len([c for c in L if c.startswith("C3-")]))
        chk.append(R.chk("H9", "real new work changes something: at least one claim carried from Cycle 2 changes label or status in Cycle 3", [len(ch), len(L2), len(noted)], len(ch) > 0, kind="hypothesis"))
    R.finish(H, P, res, chk, t0)
if __name__ == "__main__": main()
