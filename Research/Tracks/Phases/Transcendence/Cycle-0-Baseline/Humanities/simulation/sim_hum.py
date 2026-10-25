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


def geo_tree_mantel(P, rng):
    """Power of a tree-vs-geography correlation test with few languages (cf. P06's six classifications of Andic compared with
    geography). Balanced binary tree of 2^depth tips; at each split daughters move in random directions by step L0 / 2^level,
    plus tip noise sd. Statistic: Pearson correlation of patristic vs Euclidean distances; one-sided permutation p (perms).
    Null control: tip coordinates iid normal, independent of the tree."""
    n = 2 ** P["depth"]; iu = np.triu_indices(n, 1)
    lab = np.arange(n); T = np.zeros((n, n))
    for a in range(n):
        for b in range(n):
            if a != b: T[a, b] = 2 * (int(a ^ b).bit_length())
    tv = T[iu]; PM = np.array([rng.permutation(n) for _ in range(P["perms"])])
    def pval(X):
        G = np.sqrt(((X[:, None, :] - X[None, :, :]) ** 2).sum(-1)); g = G[iu]; r0 = np.corrcoef(tv, g)[0, 1]
        Gp = G[PM[:, :, None], PM[:, None, :]][:, iu[0], iu[1]]
        gc = Gp - Gp.mean(1, keepdims=True); tc = tv - tv.mean(); rp = (gc @ tc) / (np.sqrt((gc ** 2).sum(1)) * np.sqrt((tc ** 2).sum()))
        return (1 + (rp >= r0 - 1e-12).sum()) / (1 + len(rp)), r0
    def tips():
        X = np.zeros((1, 2))
        for lev in range(P["depth"]):
            ang = rng.uniform(0, 2 * np.pi, len(X)); d = np.c_[np.cos(ang), np.sin(ang)] * P["L0"] / 2 ** lev
            X = np.repeat(X, 2, 0); X[0::2] += d; X[1::2] -= d
        return X + rng.normal(0, P["noise"], X.shape)
    pn = []; pa = []; ra = []
    for _ in range(P["reps"]):
        pn.append(pval(rng.normal(0, 1, (n, 2)))[0]); p, r = pval(tips()); pa.append(p); ra.append(r)
    pn = np.array(pn); pa = np.array(pa); a = P["alpha"]; k = P["tol_se"]
    null_rate = float((pn < a).mean()); null_se = float(np.sqrt(a * (1 - a) / P["reps"])); power = float((pa < a).mean())
    res = dict(tips=n, null_rejection=null_rate, null_se=null_se, power=power, median_p=float(np.median(pa)), mean_r=float(np.mean(ra)))
    c = [chk("V1", f"null control: rejection rate at alpha {a} within {k} binomial SE of {a} (permutation p is at most nominal; discreteness may make it conservative)", [null_rate, null_se], null_rate <= a + k * null_se),
         chk("H1", f"power at alpha {a} >= {P['h1']} with {n} tips, noise sd {P['noise']}", power, power >= P["h1"], "hypothesis"),
         chk("R1", "power, null rate, median p", res, True, "reporting")]
    return res, c

def foote_novelty(P, rng):
    """P21 (Mauch et al. 2015) method skeleton: T time slices, d-dim feature means follow a slow random walk plus abrupt shifts at
    known change points; per-slice observations are noisy means of n songs. Euclidean distance matrix -> checkerboard-kernel
    Foote novelty (half-width w); significance by permuting slice order (P21: random permutation of the distance matrix).
    A change point counts as detected if a significant local novelty peak lies within +/- tol slices."""
    T, d, w = P["T"], P["d"], P["w"]; cps = P["change_points"]; R_ = P["reps"]; hits = []; fps = []
    K = np.ones((2 * w, 2 * w)); K[:w, w:] = -1; K[w:, :w] = -1
    def nov(D):
        out = np.zeros(T)
        for i in range(w, T - w): out[i] = -np.sum(K * D[i - w:i + w, i - w:i + w])
        return out
    for _ in range(R_):
        m = np.cumsum(rng.normal(0, P["drift"], (T, d)), 0)
        for cp in cps: m[cp:] += rng.normal(0, P["jump"], d)
        X = m + rng.normal(0, P["noise"] / np.sqrt(P["n_per"]), (T, d))
        D = np.sqrt(((X[:, None, :] - X[None, :, :]) ** 2).sum(-1)); N0 = nov(D)
        mx = []
        for _p in range(P["perms"]):
            pi = rng.permutation(T); mx.append(nov(D[np.ix_(pi, pi)])[w:T - w].max())
        thr = np.quantile(mx, 1 - P["alpha"])
        peaks = [i for i in range(w, T - w) if N0[i] >= thr and N0[i] == N0[max(w, i - w):min(T - w, i + w + 1)].max()]
        hits.append(np.mean([any(abs(p - cp) <= P["tol"] for p in peaks) for cp in cps]) if cps else np.nan)
        fps.append(sum(all(abs(p - cp) > P["tol"] for cp in cps) for p in peaks))
    hits = np.array(hits, dtype=float); fps = np.array(fps, dtype=float)
    res = dict(detection_rate=float(np.nanmean(hits)) if cps else None, mean_false_peaks=float(fps.mean()), reps=R_)
    if cps:
        c = [chk("V1", "detection rates in [0, 1] and computed for every replicate", res, bool(np.all((hits >= 0) & (hits <= 1)))),
             chk("H1", f"mean detection rate of true change points >= {P['h1']}", res["detection_rate"], res["detection_rate"] >= P["h1"], "hypothesis"),
             chk("H2", f"mean number of significant peaks away from true change points <= {P['h2']}", res["mean_false_peaks"], res["mean_false_peaks"] <= P["h2"], "hypothesis")]
    else:
        any_fp = float((fps > 0).mean()); se = np.sqrt(P["alpha"] * (1 - P["alpha"]) / R_); res["share_reps_with_peak"] = any_fp
        c = [chk("V1", f"null (no change points, no drift): share of replicates with any significant peak within {P['tol_se']} binomial SE of alpha = {P['alpha']}", [any_fp, P["alpha"], se], abs(any_fp - P["alpha"]) <= P["tol_se"] * se + 1e-12)]
    c.append(chk("R1", "rates", res, True, "reporting"))
    return res, c

def insurgent_style(P, rng):
    """Agent's toy for P21's rare-then-dominant style (style 2): Wright-Fisher population of N songs; a new style with selective
    advantage s enters at one copy. Kimura establishment probability (1 - e^{-2s})/(1 - e^{-2Ns}); among successful runs the
    deterministic logistic time from 10% to 90% is 2 ln 9 / ln(1+s) generations."""
    k = P["tol_se"]; N, s = P["N"], P["s"]; fix = 0; t1090 = []
    for _ in range(P["reps"]):
        x = 1; t = 0; t10 = None; done = False
        while 0 < x < N and t < P["tmax"]:
            f = x * (1 + s) / (x * (1 + s) + N - x); x = rng.binomial(N, f); t += 1
            if t10 is None and x >= 0.1 * N: t10 = t
            if t10 is not None and not done and x >= 0.9 * N: t1090.append(t - t10); done = True
        if x == N: fix += 1
    ph = fix / P["reps"]; se = np.sqrt(max(ph * (1 - ph), 1e-12) / P["reps"]); an = (1 - np.exp(-2 * s)) / (1 - np.exp(-2 * N * s))
    tl = 2 * np.log(9) / np.log(1 + s); tm = float(np.mean(t1090)) if t1090 else None
    res = dict(p_fix=ph, se=se, kimura=an, t10_90_mean=tm, t10_90_logistic=tl, n_fixed=fix)
    return res, [chk("V1", f"fixation share within {k} SE of Kimura", [ph, se, an], abs(ph - an) <= k * se, "validation"),
                 chk("H1", f"most new styles are lost: fixation share < {P['h1']}", ph, ph < P["h1"], "hypothesis"),
                 chk("H2", f"successful takeovers are S-shaped and fast: mean 10%-90% time within {P['h2']*100:.0f}% of the logistic value", [tm, tl], tm is not None and abs(tm - tl) <= P["h2"] * tl, "hypothesis"),
                 chk("R1", "values", res, True, "reporting")]

def _feltgen_P(x, beta, gamma):
    f = (x + gamma) / (1 + gamma); f = np.clip(f, 1e-12, 1 - 1e-12)
    return 0.5 * (1 + np.tanh(beta * (2 * f - 1) / (f * (1 - f))))
def _feltgen_gc(beta):
    xs = np.linspace(1e-4, 1 - 1e-4, 20001); lo, hi = 0.0, 1.0
    for _ in range(60):
        g = (lo + hi) / 2
        if np.all(_feltgen_P(xs, beta, g) - xs > 0): hi = g
        else: lo = g
    return hi
def feltgen_semantic(P, rng):
    """P28's model (Eqs. 3.1-3.2, implemented from the effective-frequency definition f = (x + gamma)/(1 + gamma) and
    P(f) = (1 + tanh(beta (2f - 1)/(f(1 - f))))/2). mode 'det': deterministic dx/dt = P(x) - x, transmission time 0 -> 0.99 vs
    delta = (gamma - gamma_c)/gamma_c. mode 'stoch': P28's random walk (M exemplars, one replacement per step), many runs in parallel;
    latency = time from x_c - w to x_c + w, growth = time from x_c + w to 0.99 (agent's operational definition)."""
    beta = P["beta"]; gc = _feltgen_gc(beta); xs = np.linspace(1e-4, 1 - 1e-4, 20001)
    if P["mode"] == "det":
        out = {}
        for d in P["deltas"]:
            g = gc * (1 + d); x = 0.0; t = 0.0; h = P["dt"]
            while x < 0.99 and t < P["tmax"]: x += h * (_feltgen_P(x, beta, g) - x); t += h
            out[str(d)] = dict(T=t if x >= 0.99 else None, stuck_at=None if x >= 0.99 else x)
        below = [d for d in P["deltas"] if d < 0]; above = sorted(d for d in P["deltas"] if d > 0)
        sl = float(np.polyfit(np.log(above), np.log([out[str(d)]["T"] for d in above]), 1)[0])
        xc = float(xs[np.argmin(_feltgen_P(xs, beta, gc) - xs)])
        return dict(gamma_c=gc, x_c=xc, runs=out, slope=sl), [chk("V1", "below threshold the deterministic system is stuck; above it reaches 0.99", out, all(out[str(d)]["T"] is None for d in below) and all(out[str(d)]["T"] is not None for d in above), "validation"),
                chk("H1", f"transmission time diverges as delta -> 0+: log-log slope within {P['h1']} of -1/2 (saddle-node bottleneck)", sl, abs(sl + 0.5) <= P["h1"], "hypothesis"),
                chk("R1", "values", out, True, "reporting")]
    g = gc * (1 + P["delta"]); M = P["M"]; R = P["runs"]; xc = float(xs[np.argmin(_feltgen_P(xs, beta, gc) - xs)]); w = P["w"]
    n = np.zeros(R, dtype=np.int64); t_in = np.full(R, np.nan); t_out = np.full(R, np.nan); t_end = np.full(R, np.nan); step = 0
    while step < P["max_steps"] and np.isnan(t_end).any():
        x = n / M; prod = rng.random(R) < _feltgen_P(x, beta, g); erase = rng.random(R) < x
        n = n + (prod & ~erase) - (~prod & erase); n = np.clip(n, 0, M); step += 1; x = n / M; tt = step / M
        t_in = np.where(np.isnan(t_in) & (x >= xc - w), tt, t_in); t_out = np.where(np.isnan(t_out) & (x >= xc + w), tt, t_out); t_end = np.where(np.isnan(t_end) & (x >= 0.99), tt, t_end)
    done = ~np.isnan(t_end); lat = (t_out - t_in)[done]; gro = (t_end - t_out)[done]
    res = dict(gamma_c=gc, x_c=xc, delta=P["delta"], share_completed=float(done.mean()), mean_latency=float(lat.mean()) if done.any() else None, mean_growth=float(gro.mean()) if done.any() else None,
               cv_latency=float(lat.std() / lat.mean()) if done.sum() > 1 else None)
    ok = done.any() and lat.mean() > gro.mean()
    return res, [chk("V1", "frequencies stay in [0, 1] and some runs complete", res, bool(done.any()), "validation"),
                 chk("H1", f"share of runs completing the change within the step budget {P['h1_text']}", res["share_completed"], eval(P["h1_expr"], {"s": res["share_completed"]}), "hypothesis"),
                 chk("H2", "mean latency (time in the trap) exceeds mean growth time", [res["mean_latency"], res["mean_growth"]], bool(ok), "hypothesis"),
                 chk("R1", "values", res, True, "reporting")]

def bass_factors(P, rng):
    """P29's Bass model dρ/dt = (a + bρ)(1 - ρ) simulated with N agents (well mixed, small time step): each adoption is attributed to the
    exogenous factor with probability a/(a + bρ) (P29 Eq. 3); the share G of exogenous adoptions is compared with P29 Eq. 6,
    G = (a/b) ln((a + b)/a)."""
    out = {}; ok = True
    for a, b in P["ab"]:
        Gs = []
        for _ in range(P["reps"]):
            N = P["N"]; n = 0; ex = 0; dt = P["dt"]
            while n < N:
                rho = n / N; k = rng.binomial(N - n, min(1.0, (a + b * rho) * dt))
                if k: ex += rng.binomial(k, a / (a + b * rho)); n += k
            Gs.append(ex / N)
        g = float(np.mean(Gs)); se = float(np.std(Gs, ddof=1) / np.sqrt(len(Gs))); th = a / b * np.log((a + b) / a)
        out[f"{a},{b}"] = dict(G=g, se=se, eq6=float(th)); ok &= abs(g - th) <= P["tol_se"] * se + P["bias"]
    return out, [chk("V1", "G in [0, 1]", out, all(0 <= v["G"] <= 1 for v in out.values()), "validation"),
                 chk("H1", f"simulated G within {P['tol_se']} SE (+{P['bias']}) of Eq. 6 for every (a, b)", out, bool(ok), "hypothesis"),
                 chk("H2", f"{P['h2_text']}", out, eval(P["h2_expr"], {"o": out}), "hypothesis"), chk("R1", "values", out, True, "reporting")]

def kramers_switch(P, rng):
    """Noise-induced switching in P41's drift h = r + x - x^3 (P41 Eq. 3; P41 also names Kramers' escape rate), read here as an
    'apparently spontaneous' transformation without any parameter change (interpretive mapping to P43's transformative experiences).
    mode 'kramers': r = 0, start at x = -1, mean first time x > 0.5 for several noise levels sigma (Euler-Maruyama dt 0.01, vectorised over
    replicates); Kramers' law ln T ~ 2 dV / sigma^2 with dV = 1/4 (standard result, agent's; not derived in P41).
    mode 'gradual': quasi-static sweep of r for h = r + a x - x^3: a < 0 has one equilibrium (gradual change), a > 0 folds (sudden jump);
    largest change of the tracked equilibrium between successive r steps (James's 'volitional' vs 'self-surrender' types, P43; mapping is the agent's)."""
    if P["mode"] == "kramers":
        dt = 0.01; out = {}
        for s_ in P["sigmas"]:
            n = P["reps"]; x = -np.ones(n); T = np.full(n, np.nan); t = 0.0; act = np.ones(n, bool); steps = 0
            while act.any() and steps < P["max_steps"]:
                x[act] += (x[act] - x[act] ** 3) * dt + s_ * np.sqrt(dt) * rng.standard_normal(act.sum()); t += dt; steps += 1
                hit = act & (x > 0.5); T[hit] = t; act &= ~hit
            out[str(s_)] = dict(mean_T=float(np.nanmean(T)), censored=int(np.isnan(T).sum()))
        inv = 1 / np.array(P["sigmas"]) ** 2; lt = np.log([out[str(s_)]["mean_T"] for s_ in P["sigmas"]]); fit = np.polyfit(inv, lt, 1); r2 = float(np.corrcoef(inv, lt)[0, 1] ** 2)
        res = dict(by_sigma=out, slope=float(fit[0]), r2=r2, kramers_slope=0.5)
        return res, [chk("V1", "no censored replicates", sum(v["censored"] for v in out.values()), all(v["censored"] == 0 for v in out.values())),
                     chk("H1", "ln mean switching time linear in 1/sigma^2 (r^2 > 0.95)", r2, r2 > 0.95, "hypothesis"),
                     chk("H2", f"slope within {P['h2']} of Kramers' 2 dV = 0.5", fit[0], abs(fit[0] - 0.5) <= P["h2"], "hypothesis"), chk("R1", "values", res, True, "reporting")]
    out = {}
    for a in P["a_values"]:
        rs = np.linspace(P["r0"], P["r1"], P["n_r"]); x = float(np.max(np.real([z for z in np.roots([-1, 0, a, rs[0]]) if abs(z.imag) < 1e-9]))) if a > 0 else float(np.real([z for z in np.roots([-1, 0, a, rs[0]]) if abs(z.imag) < 1e-9][0]))
        xs = []
        for r in rs:
            for _ in range(P["relax"]): x += 0.01 * (r + a * x - x ** 3)
            xs.append(x)
        out[str(a)] = dict(max_step_change=float(np.max(np.abs(np.diff(xs)))), total_change=float(abs(xs[-1] - xs[0])))
    res = dict(by_a=out, r_step=float((P["r1"] - P["r0"]) / (P["n_r"] - 1)))
    return res, [chk("V1", "both sweeps cover a total change > 1", out, all(v["total_change"] > 1 for v in out.values())),
                 chk("H1", P["h1_text"], out, bool(eval(P["h1_expr"], {}, dict(o=out))), "hypothesis"), chk("R1", "values", res, True, "reporting")]

def language_markov(P, rng):
    """P50 (Yang et al. 2025, Proc R Soc B, CC BY): Eq. 4.4 two-group unequal-prestige model, here with constant population (growth
    term 0): dM1'/dt = s1 r21 M2' - s2 r12 M1'. Constant per-capita rates give a coexistence equilibrium M1'* = s1 r21/(s1 r21 + s2 r12)
    (agent's computation). Comparator: P30's group-competition form (Abrams et al., read in INA) dx/dt = y x^a u_x - x y^a u_y; a = 0 is
    the constant-rate case, a >= 1 makes the weaker group vanish. Illustrative inputs: P50's reported s1, s2, r12, r21 (from the model
    with bilinguals, Eq. 4.3) plugged into Eq. 4.4 (agent's simplification, disclosed)."""
    dt, T = P["dt"], P["T"]; cases = {}
    for lab, (s1, s2, r12, r21) in P["cases"].items():
        x = 0.5
        for _ in range(int(T / dt)): x += dt * (s1 * r21 * (1 - x) - s2 * r12 * x)
        cases[lab] = dict(M1_end=x, M1_star=s1 * r21 / (s1 * r21 + s2 * r12), eff_min_to_maj=s2 * r12, eff_maj_to_min=s1 * r21)
    ux = P["u_x"]; ex = {}
    for a in P["a_values"]:
        x = 0.5
        for _ in range(int(P["T2"] / dt)):
            y = 1 - x; x += dt * (y * x ** a * ux - x * y ** a * (1 - ux)); x = min(max(x, 0.0), 1.0)
        ex[str(a)] = x
    res = dict(cases=cases, exponent=ex, u_x=ux)
    err = max(abs(v["M1_end"] - v["M1_star"]) for v in cases.values())
    return res, [chk("V1", "Eq. 4.4 end state within 1e-3 of the analytic equilibrium for every case", err, err <= 1e-3),
                 chk("H1", "with P50's constant rates the minority keeps a positive equilibrium share (> 0.01) in every case", {k: v["M1_star"] for k, v in cases.items()}, all(v["M1_star"] > 0.01 for v in cases.values()), "hypothesis"),
                 chk("H2", "effective (prestige-weighted) minority-to-majority rate exceeds the reverse in every case", {k: [v["eff_min_to_maj"], v["eff_maj_to_min"]] for k, v in cases.items()}, all(v["eff_min_to_maj"] > v["eff_maj_to_min"] for v in cases.values()), "hypothesis"),
                 chk("H3", "P30 form: weaker group keeps > 0.05 for a < 1 and falls below 0.01 for a >= 1", ex, all((ex[str(a)] > 0.05) if a < 1 else (ex[str(a)] < 0.01) for a in P["a_values"]), "hypothesis"),
                 chk("R1", "values", res, True, "reporting")]

def _hyps(P, res):
    return [chk(f"H{i}", t, res, bool(eval(e, dict(o=res, abs=abs, all=all, any=any, min=min, max=max, len=len))), "hypothesis") for i, (t, e) in enumerate(P["hyps"], 1)]

def three_language(P, rng):
    """Agent's three-language extension of the Abrams-Strogatz form (P30): dx_i/dt = sum_j [x_j c s_i x_i^a - x_i c s_j x_j^a], for the
    'three-party game' P60 proposes (a dominant language, an officialised heritage language and a non-officialised heritage language).
    Hypothetical toy; statuses and exponents are the agent's."""
    s = np.array(P["s"], float); x = np.array(P["x0"], float); a = P["a"]; c = P.get("c", 1.0); dt = P["dt"]; T = P["T"]
    ext = [None] * 3; t = 0.0; tot0 = x.sum()
    for k in range(int(T / dt)):
        pull = c * s * x ** a; dx = pull * (x.sum() - x) - x * (pull.sum() - pull); x = np.clip(x + dt * dx, 0, None); t += dt
        for i in range(3):
            if ext[i] is None and x[i] < 1e-3: ext[i] = round(t, 3)
    res = dict(x_end=[float(v) for v in x], t_extinct=ext, conserved=float(abs(x.sum() - tot0)))
    return res, [chk("V1", "total speaker share conserved within 1e-6", res["conserved"], res["conserved"] < 1e-6)] + _hyps(P, res) + [chk("R1", "values", res, True, "reporting")]

def count_audit(P, rng):
    """Arithmetic audit of printed counts in a review (ALD): each entry in 'sums' adds signed parts and compares with the printed total;
    each entry in 'medians' recomputes a median. Deterministic; no inference."""
    res = {}
    res["sums"] = {lab: dict(computed=float(sum(g["parts"])), printed=g["printed"], diff=float(sum(g["parts"]) - g["printed"])) for lab, g in P.get("sums", {}).items()}
    if "medians" in P:
        res["medians"] = {lab: dict(computed=float(np.median(g["values"])), printed=g["printed"], n=len(g["values"])) for lab, g in P["medians"].items()}
    ok = sum([3, -1, 2]) == 4 and float(np.median([5, 1, 3, 9])) == 4.0
    return res, [chk("V1", "identity check: signed sum of [3, -1, 2] is 4 and the median of [5, 1, 3, 9] is 4", ok, ok)] + _hyps(P, res) + [chk("R1", "values", res, True, "reporting")]

def glmm_audit(P, rng):
    """Arithmetic audit of a printed model-selection table and coefficient table (P71): BIC recomputed from AIC and df
    (BIC = AIC + df (ln n - 2)), likelihood-ratio chi-square recomputed from AIC differences (chi2 = AIC_small - AIC_big + 2 ddf)
    and its p value, z = beta / SE and two-sided normal p, and printed percentages."""
    from scipy.stats import chi2, norm
    n = P.get("n_obs", 1); M = {m[0]: dict(df=m[1], AIC=m[2], BIC=m[3]) for m in P.get("models", [])}   # CVA: models/comparisons optional
    bic = {k: dict(printed=v["BIC"], computed=round(v["AIC"] + v["df"] * (np.log(n) - 2), 2)) for k, v in M.items()}
    for v in bic.values(): v["diff"] = round(v["computed"] - v["printed"], 3)
    lr = {}
    for big, small, c2, p in P.get("comparisons", []):
        d = M[big]["df"] - M[small]["df"]; x = M[small]["AIC"] - M[big]["AIC"] + 2 * d
        lr[f"{big}_vs_{small}"] = dict(ddf=d, chi2=round(x, 3), printed_chi2=c2, chi2_diff=round(x - c2, 3), p=round(float(chi2.sf(x, d)), 4), printed_p=p)
    co = {}
    for name, b, se, z, p in P.get("coefs", []):
        zz = b / se; co[name] = dict(z=round(zz, 3), printed_z=z, z_diff=round(zz - z, 3), p_from_printed_z=round(float(2 * norm.sf(abs(z))), 4), printed_p=p)
    pc = {k: dict(computed=round(100 * a / b, 2), printed=c, diff=round(100 * a / b - c, 2)) for k, (a, b, c) in P.get("percents", {}).items()}
    res = dict(bic=bic, lr=lr, coefs=co, percents=pc, sums={k: dict(computed=sum(v[0]), printed=v[1]) for k, v in P.get("sums", {}).items()})
    if P.get("chi2_text"):   # CVA extension: in-text chi-square statistics (stat, df, printed p)
        res["chi2_text"] = {k: dict(p=round(float(chi2.sf(x, d)), 4), printed_p=pp, diff=round(float(chi2.sf(x, d)) - pp, 4)) for k, (x, d, pp) in P["chi2_text"].items()}
    if P.get("mix"):   # CVA extension: weight w implied by an overall percentage that mixes two subgroup percentages
        res["mix"] = {k: dict(implied_w=round((o - b) / (a - b), 4)) for k, (o, a, b) in P["mix"].items()}
    v = float(chi2.sf(3.841459, 1))
    return res, [chk("V1", "chi-square survival function: P(chi2_1 > 3.8415) = 0.05", v, abs(v - 0.05) < 1e-6)] + _hyps(P, res) + [chk("R1", "values", res, True, "reporting")]

def exemplar_shift(P, rng):
    """Agent's exemplar toy of P71's entrenchment account: each word has N stored exemplars of the speaker's baseline variant
    (N_high for high-frequency, N_low for low-frequency words); each heard model token adds weight a (task attention: shadowing
    a_shadow, interaction a_inter) to the alternative variant; each production picks the alternative with probability
    W_alt / (N + W_alt). Reports accommodation rates by task x frequency, the logit-scale task x frequency interaction, and the
    first-half vs second-half rate (order effect). Optional exemplar decay (memory) d per trial. CVB extension: optional
    word-independent accommodation floor per task (floor_shado, floor_inter): p = floor + (1 - floor) W / (N + W)."""
    S, k, reps, d = P["speakers"], P["tokens_per_word"], P.get("reps", 200), P.get("decay", 0.0)
    out = {}
    for task, a in [("shadowing", P["a_shadow"]), ("interaction", P["a_inter"])]:
        for fq, N in [("high", P["N_high"]), ("low", P["N_low"])]:
            prod = np.zeros((reps, S, k))
            for j in range(k):
                W = a * sum((1 - d) ** (j - i) for i in range(j + 1)); p = W / (N + W); fl = P.get(f"floor_{task[:5]}", 0.0); p = fl + (1 - fl) * p; prod[:, :, j] = rng.random((reps, S)) < p
            out[f"{task}_{fq}"] = dict(rate=round(float(prod.mean()), 5), first_half=round(float(prod[:, :, :k // 2].mean()), 5), second_half=round(float(prod[:, :, k // 2:].mean()), 5))
    lg = lambda r: float(np.log(r / (1 - r)))
    inter = (lg(out["shadowing_low"]["rate"]) - lg(out["shadowing_high"]["rate"])) - (lg(out["interaction_low"]["rate"]) - lg(out["interaction_high"]["rate"]))
    res = dict(cells=out, logit_task_x_freq=round(inter, 4), logit_freq_shadowing=round(lg(out["shadowing_low"]["rate"]) - lg(out["shadowing_high"]["rate"]), 4))
    a, N = P["a_shadow"], P["N_low"]; fs = P.get("floor_shado", 0.0); exact = float(np.mean([fs + (1 - fs) * a * (j + 1) / (N + a * (j + 1)) for j in range(k)])) if d == 0 else None
    ok = True if exact is None else abs(out["shadowing_low"]["rate"] - exact) < 4 * np.sqrt(exact * (1 - exact) / (reps * S * k))
    return res, [chk("V1", "without decay the simulated shadowing/low-frequency rate matches its analytic mean within 4 SE", [out["shadowing_low"]["rate"], exact], bool(ok))] + _hyps(P, res) + [chk("R1", "values", res, True, "reporting")]

def levelling_voter(P, rng):
    """Agent's toy of P82's dialect levelling (Wikipedia 'Dialect levelling'): a variant A of one feature has initial share x0
    in a mixed community of N speakers; each generation every new speaker adopts A with probability q(x), x the previous
    generation's share: neutral copying q = x (Wright-Fisher), or conformist (majority-amplifying) copying
    q = x^c / (x^c + (1 - x)^c), c > 1 (a stand-in for Trudgill's 'majority forms win'), optionally shifted toward a standard
    variant by b: q' = q + b (1 - q). Reports P(A fixes), P(A lost), mean generations to fixation or loss, by x0."""
    N, G, reps, c, b = P["N"], P["gens_max"], P["reps"], P.get("c", 1.0), P.get("b", 0.0)
    sel = P.get("bias_mode") == "selection"   # CVD extension: bias as selection, q' = q + b q (1 - q), keeps loss and fixation absorbing
    def q(x): qq = x if c == 1.0 else x ** c / (x ** c + (1 - x) ** c); return qq + b * qq * (1 - qq) if sel else qq + b * (1 - qq)
    out = {}
    for x0 in P["x0_values"]:
        k = np.full(reps, int(round(x0 * N))); t_abs = np.full(reps, -1)
        for g in range(1, G + 1):
            alive = (k > 0) & (k < N)
            if not alive.any(): break
            k[alive] = rng.binomial(N, q(k[alive] / N)); t_abs[alive & ((k == 0) | (k == N))] = g
        fixed, lost = float(np.mean(k == N)), float(np.mean(k == 0)); done = t_abs > 0
        out[str(x0)] = dict(p_fix=round(fixed, 5), p_lost=round(lost, 5), p_unresolved=round(1 - fixed - lost, 5), mean_gens=round(float(t_abs[done].mean()), 3) if done.any() else None)
    res = dict(by_x0=out, N=N, c=c, b=b, se_max=round(0.5 / np.sqrt(reps), 5))
    kk = np.full(20000, N // 4)
    for _ in range(3): kk = rng.binomial(N, kk / N)
    m = float(kk.mean() / N); ok = abs(m - (N // 4) / N) < 4 * np.sqrt(0.25 * 0.75 * 3 / N / 20000) + 1e-9
    return res, [chk("V1", "neutral copying is a martingale: mean share after 3 generations from x0 = 1/4 within 4 SE of 1/4", m, bool(ok))] + _hyps(P, res) + [chk("R1", "values", res, True, "reporting")]

def arith_audit(P, rng):
    """Agent's recomputation of printed numbers from a source's own printed inputs. Each item is a named arithmetic expression
    (written in the SPEC, evaluated with numpy/scipy helpers) next to the value the source prints; 'diff' = computed - printed.
    Helpers: chi2_sf(x, df), t_p2(t, df) two-sided t p-value, logistic(x), exp, log, sqrt, np."""
    from scipy import stats
    ns = dict(np=np, exp=np.exp, log=np.log, sqrt=np.sqrt, abs=abs, sum=sum, min=min, max=max, round=round,
              chi2_sf=lambda x, d: float(stats.chi2.sf(x, d)), t_p2=lambda t, d: float(2 * stats.t.sf(abs(t), d)), logistic=lambda x: float(1 / (1 + np.exp(-x))))
    out = {}
    for it in P["items"]:
        v = float(eval(it["expr"], dict(ns))); pr = it.get("printed")
        out[it["name"]] = dict(value=round(v, 6), printed=pr, diff=(round(v - pr, 6) if isinstance(pr, (int, float)) else None))
    v1 = float(stats.chi2.sf(3.841458820694124, 1))
    return dict(items=out), [chk("V1", "chi-square survival at 3.8415 with 1 df equals 0.05 within 1e-9", v1, abs(v1 - 0.05) < 1e-9)] + _hyps(P, dict(items=out)) + [chk("R1", "values", dict(items=out), True, "reporting")]


KINDS = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_') and k != 'chk' and getattr(v, '__module__', None) == '__main__'}

if __name__ == "__main__":
    P, H, t0 = R.start(sys.argv[1]); rng = np.random.default_rng(P["seed"])
    res, checks = KINDS[P["kind"]](P, rng); R.finish(H, P, res, checks, t0)
