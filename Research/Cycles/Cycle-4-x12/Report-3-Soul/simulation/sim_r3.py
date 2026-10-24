"""SIM-R3-C4: stability of the Cycle-1 soul-conception typology (15 conceptions x 12 attributes, coding A) under resampling and analysis
choices. The carried item 'R3 independent human coder' CANNOT be done by this research agent (no second human is available); that remains
open and is disclosed. This simulation asks a narrower question that needs no second coder: is the 4-cluster partition a stable feature of
coding A, or an artefact of attribute choice, single conceptions, uncertain cells, k, linkage or distance? Coder C (lexicon, Cycle 3, same
agent) is used only in iteration 10. ari() and cluster() are copied unchanged from SIM-R3-C3. The analysis describes the structure of
DESCRIPTIONS of doctrines; it says nothing about whether any soul exists."""
import sys, os, json, csv, numpy as np
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import pdist, squareform
from scipy.special import comb
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "tools")); import runner as R
C3IT7 = os.path.join(HERE, "..", "..", "..", "Cycle-3-x9", "Report-3-Soul", "simulation", "iter-7", "outputs", "results.json")
def ari(a, b):
    a = np.asarray(a); b = np.asarray(b); ua, ia = np.unique(a, return_inverse=True); ub, ib = np.unique(b, return_inverse=True)
    C = np.zeros((len(ua), len(ub))); np.add.at(C, (ia, ib), 1)
    s = comb(C, 2).sum(); sa = comb(C.sum(1), 2).sum(); sb = comb(C.sum(0), 2).sum(); e = sa*sb/comb(len(a), 2); mx = (sa+sb)/2
    return 1.0 if mx == e else float((s-e)/(mx-e))
def cluster(M, k=4): return fcluster(linkage(np.nan_to_num(pdist(M.astype(bool), "jaccard"), nan=0.0), "average"), k, "maxclust")
def cluster_g(M, k=4, method="average", metric="jaccard"):
    return fcluster(linkage(np.nan_to_num(pdist(M.astype(bool), metric), nan=0.0), method), k, "maxclust")
def silhouette(M, lab, metric="jaccard"):
    Dm = squareform(np.nan_to_num(pdist(M.astype(bool), metric), nan=0.0)); s = []
    if len(set(lab.tolist())) < 2: return 0.0
    for i in range(len(lab)):
        same = (lab == lab[i]); same[i] = False
        if not same.any(): s.append(0.0); continue
        a = Dm[i, same].mean(); b = min(Dm[i, lab == c].mean() for c in set(lab.tolist()) if c != lab[i]); s.append((b-a)/max(a, b) if max(a, b) > 0 else 0.0)
    return float(np.mean(s))
def load(H, P):
    rows = list(csv.DictReader(open(os.path.join(H, P["coding_a"])))); cols = [c for c in rows[0] if c[0] == "A" and c[1].isdigit()]
    A = np.array([[int(r[c]) for c in cols] for r in rows]); unc = [[c.strip() for c in (r["uncertain_cells"] or "").split(";") if c.strip()] for r in rows]
    U = np.array([[int(c.split("_")[0] in u) for c in cols] for u in unc]); return rows, cols, A, U
def coder_c(Wd, ids, cols, size):
    C = np.zeros((len(ids), len(cols)), int)
    for i, cid in enumerate(ids):
        hits = set(a for w in Wd["conceptions"][cid]["windows"] for a in w["hits"][str(size)])
        for j, c in enumerate(cols): C[i, j] = int(c in hits)
    return C
def main():
    P, prev, H = R.start(sys.argv[1]); t0 = R.now(); X = P["experiments"]; res = {}; chk = []; k = P["iteration"]
    rows, cols, A, U = load(H, P); base = cluster(A, P["k"]); res["base_labels"] = base.tolist()
    if k == 1:
        c3 = json.load(open(C3IT7))["typology"]["labels_a"]
        chk.append(R.chk("V1", "copied cluster() reproduces the Cycle-3 iteration-7 labels for coding A exactly", [base.tolist(), c3], base.tolist() == c3))
        t = [ari([1, 1, 2, 2, 3, 3], [5, 5, 7, 7, 9, 9]), ari([1, 1, 1, 2, 2, 2], [1, 2, 1, 2, 1, 2])]
        chk.append(R.chk("V2", "ARI = 1 for a relabelled identical partition and <= 0 for an orthogonal one", t, abs(t[0]-1) < 1e-12 and t[1] <= 0))
        res["n_uncertain_cells"] = int(U.sum()); res["cluster_sizes"] = {str(c): int((base == c).sum()) for c in set(base.tolist())}
        chk.append(R.chk("C0", "number of cells coder A marked uncertain, and cluster sizes", [int(U.sum()), res["cluster_sizes"]], True, "reporting"))
    elif k in (2, 11):
        e = X["bootstrap_attributes"]; rng = np.random.default_rng(e["seed"]); v = []
        for _ in range(e["n"]):
            j = rng.integers(0, A.shape[1], A.shape[1]); v.append(ari(base, cluster(A[:, j], P["k"])))
        m = float(np.mean(v)); res["bootstrap_attr"] = dict(mean_ari=m, q05=float(np.quantile(v, .05)), share_ge_0_65=float(np.mean(np.array(v) >= .65)))
        if k == 2: chk.append(R.chk("H2", "resampling the 12 attributes with replacement (1000 draws) leaves the partition largely intact: mean ARI vs the original >= 0.65", res["bootstrap_attr"], m >= .65, "hypothesis"))
        else:
            p2 = json.load(open(os.path.join(H, "..", "iter-2", "outputs", "results.json")))["bootstrap_attr"]["mean_ari"]; res["iter2"] = p2
            chk.append(R.chk("H11", "replication of iteration 2 with a new seed and 2x draws: |diff in mean ARI| <= 0.03", [m, p2], abs(m-p2) <= .03, "hypothesis"))
    elif k == 3:
        v = []
        for i in range(A.shape[0]):
            keep = np.arange(A.shape[0]) != i; v.append(ari(base[keep], cluster(A[keep], P["k"])))
        res["jackknife"] = dict(ari=v, mean=float(np.mean(v)), min=float(np.min(v)), worst=rows[int(np.argmin(v))]["id"])
        chk.append(R.chk("H3", "dropping any one conception leaves the others' partition intact on average (mean ARI >= 0.8)", [res["jackknife"]["mean"], res["jackknife"]["min"], res["jackknife"]["worst"]], np.mean(v) >= .8, "hypothesis"))
    elif k == 4:
        out = {str(kk): dict(silhouette=silhouette(A, cluster(A, kk)), ari_vs_k4=ari(base, cluster(A, kk))) for kk in X["ks"]}
        best = max(out, key=lambda kk: out[kk]["silhouette"]); res.update(by_k=out, best_k=best)
        chk.append(R.chk("H4", "k = 4 (the Cycle-1 choice) has the highest mean silhouette among k = 2..7", [best, {kk: round(v["silhouette"], 3) for kk, v in out.items()}], best == "4", "hypothesis"))
    elif k == 5:
        out = {m: ari(base, cluster_g(A, P["k"], method=m)) for m in X["methods"]}; res["by_linkage"] = out
        chk.append(R.chk("H5", "other linkage methods (complete, single, weighted) give a similar partition (ARI >= 0.5 vs average linkage for each)", out, all(v >= .5 for v in out.values()), "hypothesis"))
    elif k == 6:
        e = X["flip_uncertain"]; rng = np.random.default_rng(e["seed"]); v = []
        for _ in range(e["n"]):
            Af = A.copy(); f = (U == 1) & (rng.random(A.shape) < e["p"]); Af[f] = 1 - Af[f]; v.append(ari(base, cluster(Af, P["k"])))
        m = float(np.mean(v)); res["flip_uncertain"] = dict(mean_ari=m, q05=float(np.quantile(v, .05)), n_uncertain=int(U.sum()))
        chk.append(R.chk("H6", "flipping each cell coder A marked uncertain with probability 0.5 leaves the partition largely intact (mean ARI >= 0.65)", res["flip_uncertain"], m >= .65, "hypothesis"))
    elif k == 7:
        out = {mt: ari(base, cluster_g(A, P["k"], metric=mt)) for mt in X["metrics"]}; res["by_metric"] = out
        chk.append(R.chk("H7", "simple-matching (Hamming) and Dice distances give a similar partition to Jaccard (ARI >= 0.5 each)", out, all(v >= .5 for v in out.values()), "hypothesis"))
    elif k == 8:
        e = X["consensus"]; rng = np.random.default_rng(e["seed"]); n = A.shape[0]; co = np.zeros((n, n))
        for _ in range(e["n"]):
            j = rng.integers(0, A.shape[1], A.shape[1]); l = cluster(A[:, j], P["k"]); co += (l[:, None] == l[None, :])
        co /= e["n"]; stable = {}
        for c in sorted(set(base.tolist())):
            mem = np.nonzero(base == c)[0]; core = [rows[i]["id"] for i in mem if len(mem) > 1 and np.mean([co[i, j] for j in mem if j != i]) >= .8]
            stable[str(c)] = dict(members=[rows[i]["id"] for i in mem], stable_core=core)
        res["consensus"] = stable; ok = all(len(v["stable_core"]) >= 2 for v in stable.values() if len(v["members"]) >= 2)
        chk.append(R.chk("H8", "every multi-member cluster has a stable core of >= 2 conceptions that co-cluster in >= 80% of attribute bootstraps", stable, ok, "hypothesis"))
    elif k == 9:
        e = X["null"]; rng = np.random.default_rng(e["seed"]); s0 = silhouette(A, base); null = []
        for _ in range(e["n"]):
            Ap = A.copy()
            for j in range(A.shape[1]): Ap[:, j] = rng.permutation(Ap[:, j])
            null.append(silhouette(Ap, cluster(Ap, P["k"])))
        q = float(np.quantile(null, .95)); res["null"] = dict(observed=s0, null_q95=q, p=float(np.mean(np.array(null) >= s0)))
        chk.append(R.chk("H9", "the typology has more structure than chance: observed silhouette above the 95th percentile of a within-attribute permutation null", [s0, q], s0 > q, "hypothesis"))
    elif k == 10:
        e = X["coder_c"]; Wd = json.load(open(os.path.join(H, P["windows"]))); C = coder_c(Wd, [r["id"] for r in rows], cols, e["window"]); bc = cluster(C, P["k"])
        rng = np.random.default_rng(e["seed"]); v = []
        for _ in range(e["n"]):
            j = rng.integers(0, C.shape[1], C.shape[1]); v.append(ari(bc, cluster(C[:, j], P["k"])))
        res["coder_c"] = dict(ari_a_vs_c=ari(base, bc), boot_mean_ari_c=float(np.mean(v)))
        chk.append(R.chk("H10r", "coder C's own partition: ARI vs coding A, and its own attribute-bootstrap stability (same agent, lexicon; not independent)", res["coder_c"], True, "reporting"))
    elif k == 12:
        t = {}
        for kk in (2, 3, 5, 6, 7, 9):
            r = json.load(open(os.path.join(H, "..", f"iter-{kk}", "EXECUTION_RECORD.json"))); t[f"iter-{kk}"] = [c["result"] for c in r["pre_registered_checks"] if c["kind"] == "hypothesis"][0]
        res["summary"] = t; n = sum(v == "Supported" for v in t.values())
        chk.append(R.chk("H12", "consolidation: the typology is stable as a feature of coding A - at least 5 of the 6 robustness tests (iterations 2, 3, 5, 6, 7, 9) supported", [n, t], n >= 5, "hypothesis"))
    R.finish(H, P, res, chk, t0)
if __name__ == "__main__": main()
