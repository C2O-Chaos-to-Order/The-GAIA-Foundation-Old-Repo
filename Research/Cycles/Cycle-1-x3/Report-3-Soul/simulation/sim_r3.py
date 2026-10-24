"""SIM-R3 (Cycle 1+): robustness of an interpretive single-coder typology of soul conceptions.
Measures similarity between coded DESCRIPTIONS of doctrines; says nothing about whether any soul exists."""
import sys, os, json, itertools, numpy as np, pandas as pd
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import pdist, squareform
from scipy.special import comb
def adjusted_rand_score(a, b):
    a = np.asarray(a); b = np.asarray(b); ua, ia = np.unique(a, return_inverse=True); ub, ib = np.unique(b, return_inverse=True)
    C = np.zeros((len(ua), len(ub))); np.add.at(C, (ia, ib), 1)
    s = comb(C, 2).sum(); sa = comb(C.sum(1), 2).sum(); sb = comb(C.sum(0), 2).sum(); e = sa*sb/comb(len(a), 2); mx = (sa+sb)/2
    return 1.0 if mx == e else float((s-e)/(mx-e))
def silhouette_score(D, lab, metric="precomputed"):
    lab = np.asarray(lab); s = []
    for i in range(len(lab)):
        same = (lab == lab[i]); same[i] = False
        if not same.any(): s.append(0.0); continue
        a = D[i, same].mean(); b = min(D[i, lab == g].mean() for g in set(lab) if g != lab[i]); s.append((b-a)/max(a, b) if max(a, b) > 0 else 0.0)
    return float(np.mean(s))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools")); import runner as R
def load(path):
    df = pd.read_csv(path, keep_default_na=False); cols = [c for c in df.columns if c[0] == "A" and c[1].isdigit()]
    X = df[cols].values.astype(float); unc = np.zeros_like(X, dtype=bool)
    for r, s in enumerate(df.uncertain_cells):
        for a in (s.split(";") if s else []): unc[r, [c.split("_")[0] for c in cols].index(a)] = True
    return df, cols, X, unc
def variant(X, unc, how):
    M = X.copy()
    if how == "as_coded": return M
    if how == "uncertain_as_0": M[unc] = 0; return M
    if how == "uncertain_as_1": M[unc] = 1; return M
    if how == "uncertain_as_half": M[unc] = 0.5; return M
    if how == "drop_uncertain_attributes":  # keep only attributes with <=2 uncertain cells
        keep = unc.sum(0) <= 2; return M[:, keep]
    raise ValueError(how)
def dist(M, metric):
    if metric == "jaccard":
        if not np.isin(M, [0, 1]).all(): metric = "cityblock"   # fractional cells: fall back to L1 (recorded)
        else: return pdist(M.astype(bool), "jaccard")
    if metric in ("hamming", "cityblock"): return pdist(M, "cityblock")/M.shape[1]
    if metric == "dice": return pdist(M.astype(bool), "dice") if np.isin(M, [0, 1]).all() else pdist(M, "cityblock")/M.shape[1]
    return pdist(M, metric)
def cluster(M, metric, method, k):
    if method == "ward": Z = linkage(M, "ward")          # ward requires Euclidean geometry on the raw coding
    else: Z = linkage(np.nan_to_num(dist(M, metric), nan=0.0), method)
    return fcluster(Z, k, "maxclust")
def part(lab, ids): return tuple(sorted(tuple(sorted(i for i, l in zip(ids, lab) if l == g)) for g in set(lab)))
def main():
    P, prev, H = R.start(sys.argv[1]); t0 = R.now(); X_ = P["experiments"]; res = {}; chk = []
    df, cols, X, unc = load(os.path.join(H, P["coding_file"])); ids = list(df.id); n = len(ids)
    base = part(cluster(X, "jaccard", "average", 4), ids); res["base_partition_jaccard_average_k4"] = base
    res["shape"] = [n, len(cols)]; res["uncertain_cells"] = int(unc.sum())
    if "codings" in X_:
        c = X_["codings"]; out = {}
        for how in c["variants"]:
            for metric in c["metrics"]:
                M = variant(X, unc, how); lab = cluster(M, metric, "average", c["k"]); out[f"{how}|{metric}"] = dict(partition=part(lab, ids), ARI_vs_base=adjusted_rand_score(cluster(X, "jaccard", "average", c["k"]), lab))
        aris = [v["ARI_vs_base"] for v in out.values()]
        res["codings"] = dict(results=out, ARI_min=min(aris), ARI_median=float(np.median(aris)), n_identical_to_base=sum(v["partition"] == base for v in out.values()), n=len(out))
        chk.append(R.chk("C1", "report how many coding/metric variants reproduce the base partition (reporting)", [res["codings"]["n_identical_to_base"], len(out)], True, kind="reporting"))
        chk.append(R.chk("C2", "typology is coding-robust only if median ARI vs base >= 0.8 (pre-registered robustness bar)", res["codings"]["ARI_median"], res["codings"]["ARI_median"] >= 0.8, kind="hypothesis"))
    if "methods" in X_:
        m = X_["methods"]; out = {}; sil = {}
        for method in m["linkages"]:
            for k in m["k"]:
                lab = cluster(X, "jaccard", method, k)
                D = squareform(dist(X, "jaccard")); s = silhouette_score(D, lab, metric="precomputed") if 1 < len(set(lab)) < n else None
                out[f"{method}|k{k}"] = dict(partition=part(lab, ids), silhouette=s, ARI_vs_base=adjusted_rand_score(cluster(X, "jaccard", "average", 4), lab) if k == 4 else None)
        k4 = [v["ARI_vs_base"] for kk, v in out.items() if kk.endswith("|k4")]
        best = max((v["silhouette"], kk) for kk, v in out.items() if v["silhouette"] is not None)
        res["methods"] = dict(results=out, ARI_k4_by_linkage=dict(zip([kk for kk in out if kk.endswith("|k4")], k4)), best_silhouette=dict(value=best[0], setting=best[1]))
        chk.append(R.chk("M1", "at k=4, alternative linkages agree with the average-linkage base (median ARI >= 0.8)", float(np.median(k4)), float(np.median(k4)) >= 0.8, kind="hypothesis"))
        chk.append(R.chk("M2", "cluster structure is weak if best silhouette < 0.25 (reporting; Kaufman-Rousseeuw rule of thumb)", best, True, kind="reporting"))
    if "consensus" in X_:
        cs = X_["consensus"]; rng = np.random.default_rng(cs["seed"]); co = np.zeros((n, n)); cnt = 0; same = 0
        for _ in range(cs["draws"]):
            M = X.copy(); flip = unc & (rng.random(X.shape) < cs["flip_prob"]); M[flip] = 1-M[flip]
            method = cs["linkages"][rng.integers(len(cs["linkages"]))]; metric = cs["metrics"][rng.integers(len(cs["metrics"]))]; k = cs["k"][rng.integers(len(cs["k"]))]
            lab = cluster(M, metric, method, k); co += lab[:, None] == lab[None, :]; cnt += 1; same += part(lab, ids) == base
        co /= cnt; pairs = sorted([(ids[i], ids[j], round(float(co[i, j]), 3)) for i in range(n) for j in range(i+1, n) if co[i, j] >= cs["pair_threshold"]], key=lambda x: -x[2])
        Zc = linkage(squareform(1-co, checks=False), "average"); cons = part(fcluster(Zc, cs["consensus_k"], "maxclust"), ids)
        res["consensus"] = dict(draws=cnt, base_recurrence=same/cnt, stable_pairs=pairs, consensus_partition=cons,
                               coclustering=pd.DataFrame(co, index=ids, columns=ids).round(3).to_dict())
        chk.append(R.chk("K1", "report base-partition recurrence across codings x metrics x linkages x k (reporting)", same/cnt, True, kind="reporting"))
        chk.append(R.chk("K2", "a stable core exists: at least one pair co-clusters in >= pair_threshold of draws", len(pairs), len(pairs) > 0, kind="hypothesis"))
        if "C15" in ids:
            nb = [p for p in pairs if "C15" in p[:2]]; res["consensus"]["C15_stable_partners"] = nb
            chk.append(R.chk("K3", "adding C15 (Jain jiva) is reported with its stable partners (reporting)", nb, True, kind="reporting"))
    chk.append(R.chk("E1", "coding matrix complete (0/1 only) and every row has a source", dict(shape=list(X.shape), sourced=bool((df.source.str.len() > 0).all())), bool(np.isin(X, [0, 1]).all() and (df.source.str.len() > 0).all())))
    freq = {c: int((X[:, k] == 1).sum()) for k, c in enumerate(cols)}; res["attribute_frequency"] = freq
    chk.append(R.chk("E3", "no attribute is shared by all conceptions (no universal definition in this coding)", max(freq.values()), max(freq.values()) < n, kind="hypothesis"))
    R.finish(H, P, res, chk, t0)
if __name__ == "__main__": main()
