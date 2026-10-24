"""SIM-R3-C2: agreement between the Cycle-1 coding of soul conceptions (coder A) and a Cycle-2 codebook re-coding of a
pre-registered random sample of 48 cells (coder B), and what the disagreement does to the Cycle-1 typology.
IMPORTANT: coder A and coder B are the same research agent (B followed a written codebook, required a quoted passage per cell,
and did not view A's values while coding). This is therefore an intra-rater / codebook re-coding reliability check, NOT
inter-rater reliability. A blank form for an independent human coder is provided in research/pass-5/.
Measures agreement about DESCRIPTIONS of doctrines; says nothing about whether any soul exists."""
import sys, os, json, csv, numpy as np
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import pdist
from scipy.special import comb
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools")); import runner as R
def ari(a, b):
    a = np.asarray(a); b = np.asarray(b); ua, ia = np.unique(a, return_inverse=True); ub, ib = np.unique(b, return_inverse=True)
    C = np.zeros((len(ua), len(ub))); np.add.at(C, (ia, ib), 1)
    s = comb(C, 2).sum(); sa = comb(C.sum(1), 2).sum(); sb = comb(C.sum(0), 2).sum(); e = sa*sb/comb(len(a), 2); mx = (sa+sb)/2
    return 1.0 if mx == e else float((s-e)/(mx-e))
def cluster(M, k=4): return fcluster(linkage(np.nan_to_num(pdist(M.astype(bool), "jaccard"), nan=0.0), "average"), k, "maxclust")
def kappa(a, b):
    a = np.asarray(a); b = np.asarray(b); po = float(np.mean(a == b)); pa = a.mean(); pb = b.mean(); pe = pa*pb+(1-pa)*(1-pb)
    return (po-pe)/(1-pe) if pe < 1 else 1.0, po
def kripp_alpha_nominal(a, b):
    v = np.concatenate([a, b]); n = len(v); n1 = v.sum(); n0 = n-n1
    Do = np.mean(a != b); De = 2*n0*n1/(n*(n-1)); return 1-Do/De if De > 0 else 1.0
def load(H, P):
    rows = list(csv.DictReader(open(os.path.join(H, P["coding_a"])))); cols = [c for c in rows[0] if c[0] == "A" and c[1].isdigit()]
    A = np.array([[int(r[c]) for c in cols] for r in rows]); ids = [r["id"] for r in rows]
    S = json.load(open(os.path.join(H, P["sample"]))); B = {(r["id"], r["attribute"]): r for r in csv.DictReader(open(os.path.join(H, P["coding_b"])))}
    a, b, u, cells = [], [], [], []
    for s in S:
        i = ids.index(s["id"]); j = cols.index(s["attribute"]); r = B[(s["id"], s["attribute"])]
        a.append(A[i, j]); b.append(int(r["code_b"])); u.append(int(r["uncertain_b"])); cells.append((i, j))
    return rows, cols, A, ids, S, np.array(a), np.array(b), np.array(u), cells
def main():
    P, prev, H = R.start(sys.argv[1]); t0 = R.now(); X = P["experiments"]; res = {}; chk = []
    rows, cols, A, ids, S, a, b, u, cells = load(H, P); res["n_cells"] = len(a)
    if prev: res["carried_from_prev"] = {k: prev[k] for k in P.get("carry", []) if k in prev}
    if "agreement" in X:
        e = X["agreement"]; rng = np.random.default_rng(e["sample_seed"]); redraw = []
        for c in cols:
            idx = rng.choice(len(rows), 4, replace=False); redraw += [(rows[i]["id"], c) for i in sorted(idx)]
        chk.append(R.chk("K0", "the 48-cell sample is exactly reproducible from its pre-registered seed", len(redraw), redraw == [(s["id"], s["attribute"]) for s in S]))
        kt, _ = kappa(np.array([1]*20+[1]*5+[0]*10+[0]*15), np.array([1]*20+[0]*5+[1]*10+[0]*15))
        chk.append(R.chk("K00", "kappa implementation: 2x2 table [[20,5],[10,15]] gives 0.4", kt, abs(kt-0.4) < 1e-12))
        k, po = kappa(a, b); res["kappa"] = k; res["percent_agreement"] = po
        res["disagreements"] = [dict(id=S[i]["id"], attribute=S[i]["attribute"], a=int(a[i]), b=int(b[i]), b_uncertain=int(u[i])) for i in range(len(a)) if a[i] != b[i]]
        chk.append(R.chk("H1", f"A-B Cohen's kappa >= {e['kappa_min']} ('substantial' on Cohen's scale as reported in W07)", [k, po], k >= e["kappa_min"], kind="hypothesis"))
        chk.append(R.chk("H1r", "report disagreements", res["disagreements"], True, kind="reporting"))
    if "bootstrap" in X:
        e = X["bootstrap"]; rng = np.random.default_rng(e["seed"]); ks = []
        for _ in range(e["B"]):
            i = rng.integers(0, len(a), len(a)); ks.append(kappa(a[i], b[i])[0])
        lo, hi = np.percentile(ks, [2.5, 97.5]); al = kripp_alpha_nominal(a, b); res["bootstrap"] = dict(ci95=[lo, hi], alpha=al, kappa=kappa(a, b)[0])
        chk.append(R.chk("H2", f"bootstrap 95% CI lower bound for kappa >= {e['lower_min']} (W08 recommends bootstrap CIs)", [lo, hi], lo >= e["lower_min"], kind="hypothesis"))
        chk.append(R.chk("H2r", "report Krippendorff's alpha (nominal, 2 coders, no missing)", al, True, kind="reporting"))
    if "by_certainty" in X:
        e = X["by_certainty"]; kc, pc = kappa(a[u == 0], b[u == 0]); ku, pu = kappa(a[u == 1], b[u == 1])
        res["by_certainty"] = dict(certain=dict(n=int((u == 0).sum()), kappa=kc, agree=pc), uncertain=dict(n=int((u == 1).sum()), kappa=ku, agree=pu))
        chk.append(R.chk("H3", "agreement is higher where coder B found an explicit passage: kappa(certain) >= kappa(uncertain) + 0.2", [kc, ku], kc >= ku+0.2, kind="hypothesis"))
        chk.append(R.chk("H3r", "share of sampled cells for which the cited source was silent or needed inference (coder B 'uncertain')", float(u.mean()), True, kind="reporting"))
    if "prevalence" in X:
        p_a = float(a.mean()); p_b = float(b.mean()); po = float(np.mean(a == b)); n11 = int(((a == 1) & (b == 1)).sum()); n00 = int(((a == 0) & (b == 0)).sum())
        n10 = int(((a == 1) & (b == 0)).sum()); n01 = int(((a == 0) & (b == 1)).sum()); N = len(a)
        res["prevalence"] = dict(table=[[n11, n10], [n01, n00]], prevalence_index=abs(n11-n00)/N, bias_index=abs(n10-n01)/N, PABAK=2*po-1, p1_a=p_a, p1_b=p_b)
        chk.append(R.chk("H4", "the disagreement is directional (bias index >= 0.1: one coder codes 1 more often)", res["prevalence"]["bias_index"], res["prevalence"]["bias_index"] >= 0.1, kind="hypothesis"))
        chk.append(R.chk("H4r", "report 2x2 table, PABAK, prevalence and bias indices", res["prevalence"], True, kind="reporting"))
    if "typology" in X:
        e = X["typology"]; base = cluster(A); Ab = A.copy()
        for (i, j), v in zip(cells, b): Ab[i, j] = v
        sub = ari(base, cluster(Ab)); rng = np.random.default_rng(e["seed"]); nd = int((a != b).sum()); null = []
        allc = [(i, j) for i in range(A.shape[0]) for j in range(A.shape[1])]
        for _ in range(e["reps"]):
            M = A.copy(); pick = rng.choice(len(allc), nd, replace=False)
            for p_ in pick: i, j = allc[p_]; M[i, j] = 1-M[i, j]
            null.append(ari(base, cluster(M)))
        res["typology"] = dict(ARI_with_B_substituted=sub, n_flipped=nd, null_random_flips=dict(median=float(np.median(null)), p05=float(np.percentile(null, 5)), p95=float(np.percentile(null, 95))))
        chk.append(R.chk("H5", "the C1 typology survives substituting coder B on the sampled cells (ARI >= 0.8, the C1 robustness bar)", sub, sub >= 0.8, kind="hypothesis"))
        chk.append(R.chk("H5r", "report the null distribution of ARI for the same number of random flips", res["typology"]["null_random_flips"], True, kind="reporting"))
    if "tolerance" in X:
        e = X["tolerance"]; base = cluster(A); rng = np.random.default_rng(e["seed"]); allc = [(i, j) for i in range(A.shape[0]) for j in range(A.shape[1])]; out = []
        for nf in e["flips"]:
            v = []
            for _ in range(e["reps"]):
                M = A.copy()
                for p_ in rng.choice(len(allc), nf, replace=False): i, j = allc[p_]; M[i, j] = 1-M[i, j]
                v.append(ari(base, cluster(M)))
            out.append(dict(flips=nf, median_ARI=float(np.median(v))))
        thr = next((o["flips"] for o in out if o["median_ARI"] < 0.8), None); nd = int((a != b).sum())
        rate = nd/len(a); expected = rate*A.size; res["tolerance"] = dict(curve=out, flips_where_median_ARI_below_0_8=thr, sample_disagreement_rate=rate, expected_full_matrix_disagreements=expected)
        chk.append(R.chk("H6", "extrapolated full-matrix disagreements (sample rate x 180 cells) stay below the flip count at which median ARI drops under 0.8", [expected, thr], thr is not None and expected < thr, kind="hypothesis"))
    R.finish(H, P, res, chk, t0)
if __name__ == "__main__": main()
