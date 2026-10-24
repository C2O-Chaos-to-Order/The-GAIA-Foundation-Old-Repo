"""SIM-R3-C3: a third, methodologically different coder ('coder C') for the soul-conception typology (carried item 'R3 independent coder').
Coder C is a fixed lexicon rule applied to text windows around each conception's key terms in the cited sources (extract_windows.py;
the lexicon and key terms were written before coding and before looking at agreement). A cell is coded 1 if any window hits the
attribute's lexicon. IMPORTANT: coder C was designed by the same research agent that made codings A (Cycle 1) and B (Cycle 2), so this is
NOT independent human inter-rater reliability; it is a different-method check. A lexicon hit is also not understanding: 'immortal' in a
window may occur in a denial. The analysis describes agreement about DESCRIPTIONS of doctrines; it says nothing about whether any soul exists.
kappa, kripp_alpha_nominal, ari, cluster and the A/B loader are copied unchanged from SIM-R3-C2."""
import sys, os, json, csv, numpy as np
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import pdist
from scipy.special import comb
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "tools")); import runner as R
C2IT1 = os.path.join(HERE, "..", "..", "..", "Cycle-2-x6", "Report-3-Soul", "simulation", "iter-1", "outputs", "results.json")
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
def fleiss(M):
    """M: items x raters binary. Fleiss' kappa for 2 categories."""
    n = M.shape[1]; p1 = M.mean(); P = ((M.sum(1)**2 + (n-M.sum(1))**2 - n)/(n*(n-1))).mean(); Pe = p1**2+(1-p1)**2
    return float((P-Pe)/(1-Pe)) if Pe < 1 else 1.0
def load(H, P):
    rows = list(csv.DictReader(open(os.path.join(H, P["coding_a"])))); cols = [c for c in rows[0] if c[0] == "A" and c[1].isdigit()]
    A = np.array([[int(r[c]) for c in cols] for r in rows]); ids = [r["id"] for r in rows]
    S = json.load(open(os.path.join(H, P["sample"]))); B = {(r["id"], r["attribute"]): r for r in csv.DictReader(open(os.path.join(H, P["coding_b"])))}
    a, b, u, cells = [], [], [], []
    for s in S:
        i = ids.index(s["id"]); j = cols.index(s["attribute"]); r = B[(s["id"], s["attribute"])]
        a.append(A[i, j]); b.append(int(r["code_b"])); u.append(int(r["uncertain_b"])); cells.append((i, j))
    return rows, cols, A, ids, S, np.array(a), np.array(b), np.array(u), cells
def coder_c(Wd, ids, cols, size):
    C = np.zeros((len(ids), len(cols)), int)
    for i, cid in enumerate(ids):
        hits = set(a for w in Wd["conceptions"][cid]["windows"] for a in w["hits"][str(size)])
        for j, c in enumerate(cols): C[i, j] = int(c in hits)
    return C
def main():
    P, prev, H = R.start(sys.argv[1]); t0 = R.now(); X = P["experiments"]; res = {}; chk = []
    rows, cols, A, ids, S, a, b, u, cells = load(H, P); Wd = json.load(open(os.path.join(H, P["windows"]))); z = P["window_size"]
    C = coder_c(Wd, ids, cols, z); c = np.array([C[i, j] for i, j in cells]); res["coder_c_prevalence"] = float(C.mean()); res["coder_a_prevalence"] = float(A.mean())
    if "reproduce" in X:
        c2 = json.load(open(C2IT1)); k, po = kappa(a, b)
        chk.append(R.chk("V1", "copied loader and kappa reproduce the Cycle-2 A-vs-B kappa on the 48-cell sample (|diff| < 1e-9)", [k, c2["kappa"]], abs(k-c2["kappa"]) < 1e-9))
        fk = fleiss(np.array([[1, 1], [0, 0], [1, 0], [0, 1]]*5)); kk, _ = kappa(np.array([1, 0, 1, 0]*5), np.array([1, 0, 0, 1]*5))
        chk.append(R.chk("V2", "Fleiss kappa with 2 raters is within 0.03 of Cohen kappa on a balanced test table (they differ slightly by definition)", [fk, kk], abs(fk-kk) < 0.03))
        nw = {cid: len(v["windows"]) for cid, v in Wd["conceptions"].items()}; res["windows_per_conception"] = nw
        chk.append(R.chk("C0", "report conceptions with no or one window (coder C can only code 0 there)", [k for k, v in nw.items() if v <= 1], True, kind="reporting"))
    if "c_vs_a" in X:
        k, po = kappa(A.ravel(), C.ravel()); res["c_vs_a"] = dict(kappa=k, agreement=po, n=int(A.size))
        chk.append(R.chk("H2", "coder C agrees with coding A at least moderately on all 180 cells (Cohen kappa >= 0.41)", [k, po], k >= 0.41, kind="hypothesis"))
    if "c_vs_b" in X:
        k, po = kappa(b, c); res["c_vs_b"] = dict(kappa=k, agreement=po); ka, pa = kappa(a, c); res["c_vs_a_sample"] = dict(kappa=ka, agreement=pa)
        chk.append(R.chk("H3", "coder C agrees with codebook coding B at least moderately on the 48 sampled cells (kappa >= 0.41)", [k, po], k >= 0.41, kind="hypothesis"))
    if "three_coders" in X:
        M = np.stack([a, b, c], 1); fk = fleiss(M); res["fleiss_abc"] = fk; res["fleiss_ab"] = fleiss(M[:, :2])
        chk.append(R.chk("H4", "three-coder Fleiss kappa (A, B, C) on the sample >= 0.41", [fk, res["fleiss_ab"]], fk >= 0.41, kind="hypothesis"))
    if "per_attribute" in X:
        out = {}
        for j, col in enumerate(cols):
            k, po = kappa(A[:, j], C[:, j]); out[col] = dict(kappa=(None if np.isnan(k) else k), agreement=po, a_prev=float(A[:, j].mean()), c_prev=float(C[:, j].mean()))
        res["per_attribute"] = out; n_ok = sum(1 for v in out.values() if v["kappa"] is not None and v["kappa"] >= 0.2)
        chk.append(R.chk("H5", "at least half of the 12 attributes reach kappa >= 0.2 between A and C", n_ok, n_ok >= 6, kind="hypothesis"))
    if "window_sensitivity" in X:
        out = {}
        for zz in Wd["sizes"]:
            Cz = coder_c(Wd, ids, cols, zz); k, po = kappa(A.ravel(), Cz.ravel()); out[str(zz)] = dict(kappa=k, agreement=po, prevalence=float(Cz.mean()))
        res["window_sensitivity"] = out; ks = [v["kappa"] for v in out.values()]
        chk.append(R.chk("H6", "A-vs-C kappa changes by < 0.1 across window sizes 300/600/1200 characters (robust to window size)", ks, max(ks)-min(ks) < 0.1, kind="hypothesis"))
    if "typology" in X:
        e = X["typology"]; la = cluster(A, e["k"]); lc = cluster(C, e["k"]); v = ari(la, lc); res["typology"] = dict(ari=v, labels_a=la.tolist(), labels_c=lc.tolist())
        chk.append(R.chk("H7", "the Cycle-1 typology (4 clusters) is recovered from coder C's coding (ARI >= 0.5)", v, v >= 0.5, kind="hypothesis"))
    if "certainty" in X:
        cert = u == 0; agree_c = (b == c)
        r1 = float(agree_c[cert].mean()) if cert.any() else None; r0 = float(agree_c[~cert].mean()) if (~cert).any() else None; res["certainty"] = dict(certain=r1, uncertain=r0, n_certain=int(cert.sum()))
        chk.append(R.chk("H8", "coder C agrees with B more on cells B marked certain than on cells B marked uncertain (difference >= 0.1)", [r1, r0], r1 is not None and r0 is not None and r1-r0 >= 0.1, kind="hypothesis"))
    if "permutation" in X:
        e = X["permutation"]; rng = np.random.default_rng(e["seed"]); k0, _ = kappa(A.ravel(), C.ravel()); null = []
        for _ in range(e["n"]):
            Cp = C.copy()
            for j in range(Cp.shape[1]): Cp[:, j] = rng.permutation(Cp[:, j])  # keeps each attribute's prevalence
            null.append(kappa(A.ravel(), Cp.ravel())[0])
        q = float(np.quantile(null, 0.95)); res["permutation"] = dict(observed=k0, null_q95=q, p=float(np.mean(np.array(null) >= k0)))
        chk.append(R.chk("H9", "A-vs-C agreement exceeds chance: observed kappa above the 95th percentile of a within-attribute permutation null", [k0, q], k0 > q, kind="hypothesis"))
    R.finish(H, P, res, chk, t0)
if __name__ == "__main__": main()
