"""SIM-<PH>-HUM: Humanities simulations (Phases track). Usage: python sim_hum.py iter-<k>."""
import os, sys, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
import track_runner as R
chk = R.chk

def lexical_divergence(P, rng):
    """Two daughter languages split T millennia ago; each of M meanings is replaced independently in each lineage at rate
    r*g per millennium, g ~ Gamma(shape a, mean 1) across meanings (a = 0 means homogeneous). Shared-cognate fraction C; the
    constant-rate (glottochronological) estimate T_hat = -ln C / (2 r). Formal check of a dating method, not a model of Andic (P06)."""
    out = {}
    for a in P["shapes"]:
        Ts, Cs = [], []
        for _ in range(P["reps"]):
            g = np.ones(P["M"]) if a == 0 else rng.gamma(a, 1 / a, P["M"])
            keep = (rng.random(P["M"]) < np.exp(-P["r"] * g * P["T"])) & (rng.random(P["M"]) < np.exp(-P["r"] * g * P["T"]))
            C = max(keep.mean(), 1 / P["M"]); Cs.append(C); Ts.append(-np.log(C) / (2 * P["r"]))
        exp_C = np.exp(-2 * P["r"] * P["T"]) if a == 0 else (1 + 2 * P["r"] * P["T"] / a) ** (-a)
        out[str(a)] = dict(mean_C=float(np.mean(Cs)), analytic_C=float(exp_C), mean_T_hat=float(np.mean(Ts)), bias=float(np.mean(Ts) / P["T"] - 1))
    h, het = out["0"], out[str(P["shapes"][-1])]
    c = [chk("V1", "homogeneous rates: mean T_hat within 5% of the true T", h["bias"], abs(h["bias"]) <= 0.05),
         chk("V2", "simulated mean shared-cognate fraction within 0.02 of the analytic value for every shape", max(abs(v["mean_C"] - v["analytic_C"]) for v in out.values()),
             max(abs(v["mean_C"] - v["analytic_C"]) for v in out.values()) <= 0.02),
         chk("H1", f"rate heterogeneity (shape {P['shapes'][-1]}) makes the constant-rate estimate underestimate T by >= 10%", het["bias"], het["bias"] <= -0.10, "hypothesis"),
         chk("R1", "results by shape", out, True, "reporting")]
    return out, c

def list_size(P, rng):
    """P12's 'conventional size' formula n = N U^2 p(1-p) / (N eps^2 + U^2 p(1-p)) (its Eq. 8) checked against P12's Table 1,
    plus a simulation of how list size limits a cognate-based split-time estimate: two languages share each list meaning with
    probability C = exp(-2 r T); T_hat = -ln(C_hat)/(2 r). Rate r is illustrative (not from a source read in this track)."""
    def n_conv(N, U, eps, p=0.5): return N * U ** 2 * p * (1 - p) / (N * eps ** 2 + U ** 2 * p * (1 - p))
    t1 = dict(strict=n_conv(5000, 1.96, 0.05), relaxed=n_conv(4000, 1.645, 0.1))
    Ctrue = np.exp(-2 * P["r"] * P["T"]); out = {}
    for M in P["list_sizes"]:
        Ch = rng.binomial(M, Ctrue, P["reps"]) / M; Ch = np.maximum(Ch, 1 / M); Th = -np.log(Ch) / (2 * P["r"])
        lo, hi = np.quantile(Th, [0.025, 0.975]); out[str(M)] = dict(mean_C=float(Ch.mean()), sd_C=float(Ch.std(ddof=1)), T_q025=float(lo), T_q975=float(hi),
                                                                  half_width_rel=float((hi - lo) / 2 / P["T"]))
    k = P["tol_se"]; m0 = str(P["list_sizes"][-1]); se = np.sqrt(Ctrue * (1 - Ctrue) / int(m0) / P["reps"])
    c = [chk("V1", "Eq. 8 reproduces P12 Table 1: 356.750 (eps 0.05, alpha 0.05, N 5000) and 66.526 (eps 0.1, alpha 0.1, N 4000) within 0.01", t1,
             abs(t1["strict"] - 356.750) <= 0.01 and abs(t1["relaxed"] - 66.526) <= 0.01),
         chk("V2", f"list size {m0}: simulated mean shared fraction within {k} standard errors of exp(-2rT) = {Ctrue:.4f}", [out[m0]["mean_C"], k * se], abs(out[m0]["mean_C"] - Ctrue) <= k * se),
         chk("H1", f"with a 100-meaning list the 95% range of T_hat is within +/-{P['h1']:.0%} of T (sampling error alone)", out.get("100", {}).get("half_width_rel"),
             out.get("100", {}).get("half_width_rel", 9) <= P["h1"], "hypothesis"),
         chk("R1", "T_hat 95% range by list size", {k2: [v["T_q025"], v["T_q975"]] for k2, v in out.items()}, True, "reporting")]
    return dict(table1=t1, by_size=out, C_true=float(Ctrue)), c

def recurrence_threshold(P, rng):
    """P12's binomial principle for a recurrent sound correspondence (its Eq. 11): P(X >= k) for X ~ Bin(n, p), p = pA pB.
    Reproduces P12's worked example (n 100, p 0.006, k 4 -> 0.0032), checks it by Monte Carlo, and recomputes the smallest k
    with P(X >= k) < alpha on a grid of p to see whether P12's reported ranges (k = 2 on [0.0002, 0.0015), k = 3 on [0.0015, 0.0043))
    are reproduced at alpha = 0.01 (P12 does not state alpha for its Figure 5; 0.01 is our pre-registered reading)."""
    from scipy.stats import binom
    n = P["n"]; ex = float(binom.sf(3, n, 0.006)); sims = rng.binomial(n, 0.006, P["mc"]); mc = float((sims >= 4).mean()); se = np.sqrt(ex * (1 - ex) / P["mc"])
    grid = np.round(np.arange(0.0001, 0.0500001, 0.0001), 4); thr = []
    for p in grid:
        k = 1
        while binom.sf(k - 1, n, p) >= P["alpha"]: k += 1
        thr.append(k)
    thr = np.array(thr); r2 = grid[thr == 2]; r3 = grid[thr == 3]
    res = dict(exact=ex, mc=mc, mc_se=float(se), k2_range=[float(r2.min()), float(r2.max())] if len(r2) else None, k3_range=[float(r3.min()), float(r3.max())] if len(r3) else None)
    t = P["tol_se"]
    c = [chk("V1", "exact P(X >= 4 | n 100, p 0.006) rounds to P12's 0.0032", round(ex, 4), round(ex, 4) == 0.0032),
         chk("V2", f"Monte Carlo frequency within {t} standard errors of the exact value", [mc, ex, t * se], abs(mc - ex) <= t * se),
         chk("H1", "alpha 0.01 reproduces P12's ranges: k = 2 exactly on grid points 0.0002..0.0014 and k = 3 on 0.0015..0.0042", [res["k2_range"], res["k3_range"]],
             res["k2_range"] == [0.0002, 0.0014] and res["k3_range"] == [0.0015, 0.0042], "hypothesis"),
         chk("R1", "threshold ranges", res, True, "reporting")]
    return res, c

def stemma_copying(P, rng):
    """Manuscript copying as divergence (cf. P13): a balanced copying tree of depth d from an archetype of M word positions;
    each copy changes each position with probability mu to a new variant (infinite alleles). Optional contamination: a fraction
    'cont_frac' of positions in 'cont_leaves' leaves is copied from a random leaf of the other half of the tree. Reconstructs a
    tree by average-linkage (UPGMA) clustering of Hamming distances and scores the fraction of leaf triplets resolved correctly."""
    from scipy.cluster.hierarchy import linkage, to_tree
    from itertools import combinations
    d = P["depth"]; L = 2 ** d; out = {}
    def true_trip(a, b, c):  # which pair is closest in the balanced tree (largest common prefix length of binary leaf index)
        def lca(x, y): return d - int(x ^ y).bit_length()
        s = {(a, b): lca(a, b), (a, c): lca(a, c), (b, c): lca(b, c)}; m = max(s.values()); w = [k for k, v in s.items() if v == m]
        return w[0] if len(w) == 1 else None
    for lab, cf in (("clean", 0.0), ("contaminated", P["cont_frac"])):
        accs = []; diffs = []
        for rep in range(P["reps"]):
            nodes = [np.zeros(P["M"], dtype=np.int64)]; nxt = 1
            for lev in range(d):
                new = []
                for x in nodes:
                    for _ in range(2):
                        y = x.copy(); ch = rng.random(P["M"]) < P["mu"]; y[ch] = np.arange(nxt, nxt + ch.sum()); nxt += ch.sum(); new.append(y)
                        if lev == 0: diffs.append(int((y != x).sum()))
                nodes = new
            leaves = np.array(nodes)
            if cf > 0:
                for i in rng.choice(L, P["cont_leaves"], replace=False):
                    other = rng.integers(0, L // 2) + (0 if i >= L // 2 else L // 2); pos = rng.random(P["M"]) < cf; leaves[i, pos] = nodes[other][pos]
            D = (leaves[:, None, :] != leaves[None, :, :]).mean(2); iu = np.triu_indices(L, 1)
            tr = to_tree(linkage(D[iu], "average")); dep = {}
            def walk(nd, path):
                if nd.is_leaf(): dep[nd.id] = path; return
                walk(nd.left, path + "0"); walk(nd.right, path + "1")
            walk(tr, "")
            def rec_pair(a, b, c):
                def cp(x, y): return len(os.path.commonprefix([dep[x], dep[y]]))
                s = {(a, b): cp(a, b), (a, c): cp(a, c), (b, c): cp(b, c)}; m = max(s.values()); w = [k for k, v in s.items() if v == m]
                return w[0] if len(w) == 1 else None
            tot = ok = 0
            for a, b, c in combinations(range(L), 3):
                t = true_trip(a, b, c)
                if t is None: continue
                tot += 1; ok += rec_pair(a, b, c) == t
            accs.append(ok / tot)
        out[lab] = dict(acc=accs, mean_acc=float(np.mean(accs)), mean_first_copy_diffs=float(np.mean(diffs)) if diffs else None, sd_diffs=float(np.std(diffs, ddof=1)) if len(diffs) > 1 else None, n_diffs=len(diffs))
    cl = out["clean"]; k = P["tol_se"]; exp = P["M"] * P["mu"]; se = np.sqrt(P["M"] * P["mu"] * (1 - P["mu"]) / cl["n_diffs"])
    c = [chk("V1", f"mean changes per copy within {k} standard errors of M mu = {exp:g}", [cl["mean_first_copy_diffs"], k * se], abs(cl["mean_first_copy_diffs"] - exp) <= k * se),
         chk("H1", f"without contamination mean triplet accuracy >= {P['h1']}", cl["mean_acc"], cl["mean_acc"] >= P["h1"], "hypothesis"),
         chk("H2", f"contamination ({P['cont_leaves']} leaves, {P['cont_frac']:.0%} of positions) lowers mean triplet accuracy by >= {P['h2']}", cl["mean_acc"] - out["contaminated"]["mean_acc"],
             cl["mean_acc"] - out["contaminated"]["mean_acc"] >= P["h2"], "hypothesis"),
         chk("R1", "accuracy per replicate", {k2: v["acc"] for k2, v in out.items()}, True, "reporting")]
    return out, c


KINDS = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_') and k != 'chk' and getattr(v, '__module__', None) == '__main__'}

if __name__ == "__main__":
    P, H, t0 = R.start(sys.argv[1]); rng = np.random.default_rng(P["seed"])
    res, checks = KINDS[P["kind"]](P, rng); R.finish(H, P, res, checks, t0)
