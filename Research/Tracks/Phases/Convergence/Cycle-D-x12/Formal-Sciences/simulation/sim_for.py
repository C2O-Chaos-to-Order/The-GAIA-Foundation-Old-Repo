"""SIM-<PH>-FOR: Formal-Sciences simulations (Phases track). Usage: python sim_for.py iter-<k>."""
import os, sys, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
import track_runner as R
chk = R.chk

def logistic_lyapunov(P, rng):
    """Logistic map x -> r x (1-x). Global Lyapunov exponent lambda = mean ln|r(1-2x)| along an orbit (after burn-in),
    and separation growth of two orbits started delta0 apart (sensitive dependence, P09 Chaos_lambda definition)."""
    lam = {}
    for r in P["r_values"]:
        x = rng.uniform(0.1, 0.9); s = 0.0
        for _ in range(P["burn"]): x = r * x * (1 - x)
        for _ in range(P["n"]):
            x = r * x * (1 - x); s += np.log(max(abs(r * (1 - 2 * x)), 1e-300))
        lam[str(r)] = s / P["n"]
    steps = []
    for k in range(P["pairs"]):
        x = rng.uniform(0.1, 0.9); y = x + P["delta0"]; t = 0
        while abs(x - y) < P["sep"] and t < 1000:
            x = 4 * x * (1 - x); y = 4 * y * (1 - y); t += 1
        steps.append(t)
    pred = np.log(P["sep"] / P["delta0"]) / np.log(2)
    res = dict(lyapunov=lam, steps_to_sep=dict(median=float(np.median(steps)), min=int(min(steps)), max=int(max(steps))), predicted_steps_ln2=float(pred))
    c = [chk("V1", "r = 4: lambda within 0.01 of ln 2 = 0.693147 (analytic)", lam["4.0"], abs(lam["4.0"] - np.log(2)) <= 0.01),
         chk("V2", "r = 3.2 (stable 2-cycle): lambda < 0 (analytic)", lam["3.2"], lam["3.2"] < 0),
         chk("H1", f"r = 4: median steps for a {P['delta0']:g} separation to exceed {P['sep']} within 25% of ln(sep/delta0)/ln 2", res["steps_to_sep"]["median"], abs(res["steps_to_sep"]["median"] / pred - 1) <= 0.25, "hypothesis"),
         chk("R1", "lambda by r", lam, True, "reporting")]
    return res, c

def kl_divergence(P, rng):
    """Kullback-Leibler divergence D(p||q) = sum p ln(p/q) between random discrete distributions (Dirichlet(1) on K points):
    exact values, a Monte Carlo estimate from samples of p, and the asymmetry D(p||q) - D(q||p). Formal sense of 'divergence'
    as an asymmetric dissimilarity, not a distance."""
    K = P["K"]; pairs = P["pairs"]; D = []; Dr = []; mc_ok = 0; mc_rows = []
    for i in range(pairs):
        p = rng.dirichlet(np.ones(K)); q = rng.dirichlet(np.ones(K))
        d = float((p * np.log(p / q)).sum()); dr = float((q * np.log(q / p)).sum()); D.append(d); Dr.append(dr)
        if i < P["mc_pairs"]:
            x = rng.choice(K, size=P["mc_n"], p=p); v = np.log(p[x] / q[x]); est = v.mean(); se = v.std(ddof=1) / np.sqrt(len(v))
            ok = abs(est - d) <= P["tol_se"] * se; mc_ok += ok; mc_rows.append([d, float(est), float(se)])
    D = np.array(D); Dr = np.array(Dr); self0 = max(abs(float((p * np.log(p / p)).sum())) for p in [rng.dirichlet(np.ones(K)) for _ in range(20)])
    asym = np.abs(D - Dr) / ((D + Dr) / 2)
    res = dict(min_D=float(D.min()), self_D_max=self0, mean_D=float(D.mean()), median_rel_asymmetry=float(np.median(asym)), mc_within=int(mc_ok), mc_pairs=P["mc_pairs"], mc_examples=mc_rows[:5])
    c = [chk("V1", "D(p||q) >= 0 for every pair (Gibbs' inequality; code check)", res["min_D"], res["min_D"] >= 0),
         chk("V2", "D(p||p) = 0 (|value| < 1e-12)", self0, self0 < 1e-12),
         chk("V3", f"Monte Carlo estimate within {P['tol_se']} standard errors of the exact value in at least {P['mc_min']} of {P['mc_pairs']} pairs", mc_ok, mc_ok >= P["mc_min"]),
         chk("H1", f"divergence is asymmetric: median relative asymmetry |D(p||q)-D(q||p)| / mean > {P['h1']}", res["median_rel_asymmetry"], res["median_rel_asymmetry"] > P["h1"], "hypothesis"),
         chk("R1", "mean D and examples", [res["mean_D"], mc_rows[:3]], True, "reporting")]
    return res, c

def series_divergence(P, rng):
    """Divergent vs convergent series (deterministic): harmonic partial sums H_n against ln n + gamma, the p = 2 series against
    pi^2/6, the alternating harmonic series against ln 2, and the n at which H_n first exceeds a target."""
    g = 0.5772156649015329; out = {}; ok1 = True; ok2 = True; ok3 = True
    for n in P["n_values"]:
        k = np.arange(1, n + 1, dtype=float); H = float(np.sum(1 / k)); S2 = float(np.sum(1 / k ** 2)); A = float(np.sum(((-1) ** (k + 1)) / k))
        e1 = abs(H - np.log(n) - g); e2 = abs(np.pi ** 2 / 6 - S2); e3 = abs(A - np.log(2))
        ok1 &= e1 <= 1 / (2 * n); ok2 &= e2 <= 1 / n; ok3 &= e3 <= 1 / (n + 1)
        out[str(n)] = dict(H=H, err_H=float(e1), S2=S2, err_S2=float(e2), alt=A, err_alt=float(e3))
    s = 0.0; n = 0
    while s <= P["target"]: n += 1; s += 1 / n
    res = dict(by_n=out, first_n_H_exceeds_target=n, target=P["target"])
    c = [chk("V1", "|H_n - ln n - gamma| <= 1/(2n) for every n (harmonic series diverges like ln n)", {k2: v["err_H"] for k2, v in out.items()}, bool(ok1)),
         chk("V2", "|pi^2/6 - sum_{k<=n} 1/k^2| <= 1/n (p = 2 series converges)", {k2: v["err_S2"] for k2, v in out.items()}, bool(ok2)),
         chk("V3", "|alternating harmonic partial sum - ln 2| <= 1/(n+1) (alternating-series bound)", {k2: v["err_alt"] for k2, v in out.items()}, bool(ok3)),
         chk("H1", f"the harmonic series needs more than {P['h1']} terms to exceed {P['target']} (divergence can be extremely slow)", n, n > P["h1"], "hypothesis"),
         chk("R1", "first n with H_n > target", n, True, "reporting")]
    return res, c

def divergence_operator(P, rng):
    """Divergence operator of vector calculus: for F = (x^3 + y, x y^2, z x^2) on the unit cube compare (a) a central-difference
    div F with the analytic 3x^2 + 2xy + x^2, (b) a Monte Carlo volume integral of div F with the analytic outward flux
    (divergence theorem). Formal sense: net outflow per unit volume."""
    def F(x, y, z): return np.stack([x ** 3 + y, x * y ** 2, z * x ** 2])
    def divA(x, y, z): return 3 * x ** 2 + 2 * x * y + x ** 2
    pts = rng.uniform(0, 1, (3, P["fd_points"])); h = P["h"]; e = np.eye(3)
    num = sum((F(*(pts + h * e[i][:, None]))[i] - F(*(pts - h * e[i][:, None]))[i]) / (2 * h) for i in range(3))
    fd_err = float(np.max(np.abs(num - divA(*pts))))
    u = rng.uniform(0, 1, (3, P["mc_n"])); v = divA(*u); est = float(v.mean()); se = float(v.std(ddof=1) / np.sqrt(len(v)))
    # analytic outward flux by face: x=1 face: Fx = 1 + y -> 3/2 ; x=0 face: -(y) -> -1/2 ; y=1: Fy = x -> 1/2 ; y=0: 0 ; z=1: Fz = x^2 -> 1/3 ; z=0: 0
    flux = 1.5 - 0.5 + 0.5 + 1 / 3
    res = dict(fd_max_err=fd_err, mc_integral=est, mc_se=se, analytic_flux=flux)
    c = [chk("V1", f"central-difference divergence within {P['fd_tol']} of the analytic divergence at all points", fd_err, fd_err <= P["fd_tol"]),
         chk("V2", f"Monte Carlo volume integral of div F within {P['tol_se']} standard errors of the analytic outward flux {flux:.6f} (divergence theorem)", [est, se], abs(est - flux) <= P["tol_se"] * se),
         chk("R1", "values", res, True, "reporting")]
    return res, c


def kl_likelihood(P, rng):
    """P16 (Shlens 2014) relation: for counts c drawn from p, -(1/n) log L(c|q) -> D(p||q) (Eq. A2, multinomial likelihood with
    its coefficient; Stirling). Also the log-likelihood ratio rate (1/n)[log L(c|p) - log L(c|q)], whose expectation is exactly D."""
    from math import lgamma
    K = P["K"]; p = rng.dirichlet(np.ones(K) * P["conc"]); q = rng.dirichlet(np.ones(K) * P["conc"]); D = float((p * np.log(p / q)).sum())
    lg = np.vectorize(lgamma)
    def logL(c, r): return lgamma(c.sum() + 1) - float(lg(c + 1).sum()) + float((c * np.log(r)).sum())
    rows = {}
    for n in P["n_values"]:
        a = []; lr = []
        for _ in range(P["reps"]):
            c = rng.multinomial(n, p); a.append(-logL(c, q) / n); lr.append((logL(c, p) - logL(c, q)) / n)
        a = np.array(a); lr = np.array(lr)
        rows[str(n)] = dict(eqA2_mean=float(a.mean()), eqA2_abs_err=float(abs(a.mean() - D)), lr_mean=float(lr.mean()), lr_se=float(lr.std(ddof=1) / np.sqrt(len(lr))))
    nl = str(P["n_values"][-1]); k = P["tol_se"]; errs = [rows[str(n)]["eqA2_abs_err"] for n in P["n_values"]]
    lr_ok = all(abs(rows[str(n)]["lr_mean"] - D) <= k * rows[str(n)]["lr_se"] for n in P["n_values"])
    res = dict(D=D, by_n=rows)
    c = [chk("V1", f"likelihood-ratio rate (expectation exactly D) within {k} SE of D at every n", [[rows[str(n)]["lr_mean"], rows[str(n)]["lr_se"]] for n in P["n_values"]] + [D], lr_ok),
         chk("H1", f"P16 Eq. A2 estimate -(1/n) log L(c|q) within {P['h1']} nats of D at n = {nl}", rows[nl]["eqA2_abs_err"], rows[nl]["eqA2_abs_err"] <= P["h1"], "hypothesis"),
         chk("H2", "Eq. A2 absolute error decreases with every increase in n", errs, all(errs[i + 1] < errs[i] for i in range(len(errs) - 1)), "hypothesis"),
         chk("R1", "D and estimates by n", res, True, "reporting")]
    return res, c

def linear_vs_chaotic(P, rng):
    """P09 (Kellert counterexample): x -> c x with c > 1 has positive Lyapunov exponent ln c but is unbounded and never folds;
    the logistic map at r = 4 has exponent ln 2, stays bounded, and nearby separations sometimes shrink (stretching and folding)."""
    cc = P["c"]; lam_lin = []; shrink_lin = 0; tot = 0
    x = 1.0; s = 0.0
    for _ in range(P["n"]): s += np.log(abs(cc))
    lam_lin = s / P["n"]
    xs = rng.uniform(0.1, 0.9, P["pairs"]); ys = xs + P["d0"]; dl = []; shrink = 0; steps = 0; xmax = 0.0
    lx = rng.uniform(0.1, 0.9); ss = 0.0
    for _ in range(P["n"]): lx = 4 * lx * (1 - lx); ss += np.log(max(abs(4 * (1 - 2 * lx)), 1e-300)); xmax = max(xmax, lx)
    lam_log = ss / P["n"]
    for t in range(P["steps"]):
        d_old = np.abs(xs - ys); xs = 4 * xs * (1 - xs); ys = 4 * ys * (1 - ys); d_new = np.abs(xs - ys)
        shrink += int((d_new < d_old).sum()); steps += len(xs)
        far = d_new > 1e-3; ys[far] = xs[far] + P["d0"] * np.sign(ys[far] - xs[far] + 1e-300)  # renormalise so pairs stay local
    lin_x = P["d0"] * cc ** P["steps"]; lin_shrink = 0.0
    res = dict(lyap_linear=float(lam_lin), lyap_logistic=float(lam_log), logistic_max=float(xmax), shrink_frac_logistic=shrink / steps, shrink_frac_linear=lin_shrink, linear_sep_after_steps=float(lin_x))
    c = [chk("V1", f"linear map exponent equals ln {cc} within 1e-12", lam_lin, abs(lam_lin - np.log(cc)) <= 1e-12),
         chk("V2", "logistic r = 4 exponent within 0.01 of ln 2", lam_log, abs(lam_log - np.log(2)) <= 0.01),
         chk("V3", "logistic orbit stays in [0, 1]", xmax, 0 <= xmax <= 1),
         chk("H1", f"logistic: share of local steps where the separation shrinks > {P['h1']} (folding), linear map share = 0", [res["shrink_frac_logistic"], 0.0], res["shrink_frac_logistic"] > P["h1"], "hypothesis"),
         chk("R1", "exponents, shrink shares, linear separation", res, True, "reporting")]
    return res, c

def local_shrink(P, rng):
    """Logistic map r = 4: local stretching factor |f'(x)| = |4(1-2x)| is < 1 for x in (3/8, 5/8). Share of time an orbit spends
    there vs the analytic invariant-measure share (density 1/(pi sqrt(x(1-x)))). P09: local uncertainty can shrink in a chaotic system."""
    an = (2 / np.pi) * (np.arcsin(np.sqrt(5 / 8)) - np.arcsin(np.sqrt(3 / 8))); sh = []; fl = []
    for _ in range(P["orbits"]):
        x = rng.uniform(0.01, 0.99)
        for _ in range(P["burn"]): x = 4 * x * (1 - x)
        cnt = 0; lsum = 0.0
        for _ in range(P["n"]):
            x = 4 * x * (1 - x); cnt += (3 / 8 < x < 5 / 8); lsum += np.log(max(abs(4 * (1 - 2 * x)), 1e-300))
        sh.append(cnt / P["n"]); fl.append(lsum / P["n"])
    sh = np.array(sh); fl = np.array(fl); m = float(sh.mean()); se = float(sh.std(ddof=1) / np.sqrt(len(sh))); k = P["tol_se"]
    res = dict(analytic_share=float(an), orbit_share=m, se=se, finite_time_lyap_mean=float(fl.mean()), finite_time_lyap_min=float(fl.min()))
    c = [chk("V1", f"orbit share in the shrinking region within {k} SE of the analytic share {an:.5f}", [m, se], abs(m - an) <= k * se),
         chk("H1", f"share of time with local contraction > {P['h1']}", m, m > P["h1"], "hypothesis"),
         chk("H2", f"every finite-time exponent over {P['n']} steps is still positive", float(fl.min()), fl.min() > 0, "hypothesis"),
         chk("R1", "shares and finite-time exponents", res, True, "reporting")]
    return res, c

def lorenz_div(P, rng):
    """Lorenz system (sigma, rho, beta): the vector-field divergence is the constant -(sigma + 1 + beta) (phase-space volumes
    contract), while the largest Lyapunov exponent (Benettin two-trajectory method, RK4) measures trajectory divergence.
    Connects the operator sense (div F) and the dynamical sense of divergence."""
    sg, rh, bt = P["sigma"], P["rho"], P["beta"]
    def F(v): return np.array([sg * (v[1] - v[0]), v[0] * (rh - v[2]) - v[1], v[0] * v[1] - bt * v[2]])
    def rk4(v, h): k1 = F(v); k2 = F(v + h / 2 * k1); k3 = F(v + h / 2 * k2); k4 = F(v + h * k3); return v + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    pts = rng.uniform(-20, 20, (P["fd_points"], 3)); e = P["fd_h"]; errs = []
    for v in pts:
        dv = sum((F(v + e * np.eye(3)[i])[i] - F(v - e * np.eye(3)[i])[i]) / (2 * e) for i in range(3)); errs.append(abs(dv + (sg + 1 + bt)))
    v = np.array([1.0, 1.0, 1.0]) + rng.normal(0, 0.1, 3); h = P["dt"]
    for _ in range(int(P["burn"] / h)): v = rk4(v, h)
    w = v + np.array([P["d0"], 0, 0]); s = 0.0; n = int(P["T"] / h)
    for _ in range(n):
        v = rk4(v, h); w = rk4(w, h); d = np.linalg.norm(w - v); s += np.log(d / P["d0"]); w = v + (w - v) * (P["d0"] / d)
    lam = s / (n * h)
    res = dict(div_F=-(sg + 1 + bt), max_fd_err=float(max(errs)), lyap_max=float(lam))
    hyp = (lam > P["h1"]) if P["h1_dir"] == "gt" else (lam < P["h1"])
    c = [chk("V1", f"finite-difference divergence equals -(sigma+1+beta) = {-(sg + 1 + bt):.6f} within {P['fd_tol']} at {P['fd_points']} random points", float(max(errs)), max(errs) <= P["fd_tol"]),
         chk("H1", f"largest Lyapunov exponent {'>' if P['h1_dir'] == 'gt' else '<'} {P['h1']}", float(lam), bool(hyp), "hypothesis"),
         chk("R1", "div F and lambda_max", res, True, "reporting")]
    return res, c

def series_suite(P, rng):
    """Deterministic partial-sum checks for the series sense of divergence (P23, Active Calculus 8.3). mode:
    'source_values' : S_1000 of 1/k vs P23's 7.485470861 and S_10 of 1/k^2 vs 1.549767731; H1 S_n - ln n -> gamma.
    'slow_p'        : p-series with p = P['p']: S_n at n = 10^3..10^6 vs zeta(p) (p > 1) or vs the integral bound (p < 1).
    'ratio'         : a_k = 2^k/(3^k - k): ratio a_{k+1}/a_k at k = 25 vs 2/3; partial sum converges.
    'sum_of_divergent': a_n = 1 + 2^-n, b_n = -1 (P23 exercise 7): partial sums of a and b diverge, of a+b converge to 2."""
    from scipy.special import zeta
    m = P["mode"]; res = {}; c = []
    if m == "source_values":
        k = np.arange(1, 1001, dtype=np.float64); S1000 = float(np.sum(1 / k[::-1])); S10 = float(np.sum(1 / np.arange(1, 11.0) ** 2))
        n = 10 ** 6; Hn = float(np.sum(1 / np.arange(n, 0, -1, dtype=np.float64))); g = Hn - np.log(n)
        res = dict(S1000_harmonic=S1000, S10_inverse_squares=S10, H_1e6_minus_ln=g, euler_gamma=0.5772156649)
        c = [chk("V1", "harmonic S_1000 equals P23's 7.485470861 within 1e-9", [S1000, 7.485470861], abs(S1000 - 7.485470861) < 1e-9),
             chk("V2", "S_10 of 1/k^2 equals P23's 1.549767731 within 1e-9", [S10, 1.549767731], abs(S10 - 1.549767731) < 1e-9),
             chk("H1", f"H_n - ln n at n = 1e6 within {P['h1']} of Euler's gamma (divergence is logarithmic)", [g], abs(g - 0.5772156649) < P["h1"], "hypothesis")]
    elif m == "slow_p":
        p = P["p"]; ns = [10 ** e for e in range(3, 7)]; k = np.arange(1, ns[-1] + 1, dtype=np.float64); terms = 1 / k ** p; cs = np.cumsum(terms)
        S = {str(n): float(cs[n - 1]) for n in ns}
        if p > 1:
            z = float(zeta(p)); lo = z - (ns[-1] + 1) ** (1 - p) / (p - 1); res = dict(p=p, S=S, zeta=z, share_of_limit_at_1e6=S[str(ns[-1])] / z)
            c = [chk("V1", "S_1e6 within the integral-test bracket zeta(p) - int_{n+1}^inf <= S_n <= zeta(p) (1e-6 slack)", [S[str(ns[-1])], lo, z], lo - 1e-6 <= S[str(ns[-1])] <= z + 1e-6),
                 chk("H1", f"a convergent p-series looks divergent: S_1e6 below {P['h1']} of its limit", res["share_of_limit_at_1e6"], res["share_of_limit_at_1e6"] < P["h1"], "hypothesis")]
        else:
            n = ns[-1]; lower = ((n + 1) ** (1 - p) - 1) / (1 - p); upper = 1 + (n ** (1 - p) - 1) / (1 - p); res = dict(p=p, S=S, integral_lower=lower, integral_upper=upper)
            inc = all(S[str(ns[i + 1])] - S[str(ns[i])] > 0 for i in range(len(ns) - 1))
            c = [chk("V1", "S_1e6 inside the integral bounds int_1^{n+1} x^-p dx <= S_n <= 1 + int_1^n x^-p dx", [S[str(n)], lower, upper], lower - 1e-6 <= S[str(n)] <= upper + 1e-6),
                 chk("H1", f"a divergent series looks tame: S_1e6 below {P['h1']}", S[str(n)], S[str(n)] < P["h1"], "hypothesis")]
    elif m == "ratio":
        kk = np.arange(1, 60, dtype=np.float64); a = 2 ** kk / (3 ** kk - kk); r25 = float(a[25] / a[24]); s = np.cumsum(a)
        res = dict(ratio_k25=r25, S20=float(s[19]), S59=float(s[-1]))
        c = [chk("V1", "ratio a_26/a_25 within 1e-3 of 2/3", r25, abs(r25 - 2 / 3) < 1e-3),
             chk("H1", "partial sums settle: |S_59 - S_20| < 1e-3", [res["S20"], res["S59"]], abs(res["S59"] - res["S20"]) < 1e-3, "hypothesis")]
    elif m == "sum_of_divergent":
        n = np.arange(0, P["n"]); a = 1 + 2.0 ** -n; b = -np.ones_like(a); SA = float(a.sum()); SB = float(b.sum()); SAB = float((a + b).sum())
        res = dict(S_a=SA, S_b=SB, S_a_plus_b=SAB)
        c = [chk("V1", "sum of (a+b) partial sum within 1e-9 of 2 - 2^-(n-1)", SAB, abs(SAB - (2 - 2.0 ** -(P['n'] - 1))) < 1e-9),
             chk("H1", "both component partial sums exceed n/2 in magnitude while their sum stays below 2", [SA, SB, SAB], abs(SA) > P["n"] / 2 and abs(SB) > P["n"] / 2 and SAB < 2, "hypothesis")]
    c.append(chk("R1", "values", res, True, "reporting"))
    return res, c

def er_giant(P, rng):
    """Sparse Erdos-Renyi G(n, p = c/(n-1)) (P27). Edges: Binomial(n(n-1)/2, p) random pairs (duplicates and self-pairs dropped).
    Reports (a) mean size of the component containing a fixed node (P27's subcritical experiment; theory 1/(1-c)) and
    (b) largest-component fraction vs the solution of s = 1 - exp(-c s) (P27 Eq. 2.2)."""
    from scipy.sparse import coo_matrix; from scipy.sparse.csgraph import connected_components
    def graph(n, c):
        m = rng.binomial(n * (n - 1) // 2, c / (n - 1)); a = rng.integers(0, n, m); b = rng.integers(0, n, m); k = a != b
        g = coo_matrix((np.ones(k.sum()), (a[k], b[k])), shape=(n, n)); return connected_components(g, directed=False)[1]
    def s_eq(c):
        s = 0.9
        for _ in range(2000): s = 1 - np.exp(-c * s)
        return s if c > 1 else 0.0
    sub = [np.sum((lab := graph(P["n_sub"], P["c_sub"])) == lab[0]) for _ in range(P["reps_sub"])]
    ms = float(np.mean(sub)); se = float(np.std(sub, ddof=1) / np.sqrt(len(sub))); th = 1 / (1 - P["c_sub"])
    sweep = {}
    for c in P["c_values"]:
        fr = [np.bincount(graph(P["n"], c)).max() / P["n"] for _ in range(P["reps"])]
        sweep[str(c)] = dict(largest=float(np.mean(fr)), se=float(np.std(fr, ddof=1) / np.sqrt(len(fr))), theory=s_eq(c))
    hi = [k for k in sweep if float(k) > 1 + 1e-9]; okH2 = all(abs(sweep[k]["largest"] - sweep[k]["theory"]) <= P["h2"] for k in hi if float(k) >= P["h2_from"])
    lo = max(sweep[k]["largest"] for k in sweep if float(k) <= P["below"]); up = min(sweep[k]["largest"] for k in sweep if float(k) >= P["above"])
    res = dict(subcritical=dict(c=P["c_sub"], n=P["n_sub"], mean=ms, se=se, theory=th, printed=P["printed"]), sweep=sweep)
    return res, [chk("V1", f"subcritical mean component size within {P['tol_se']} SE of 1/(1-c)", [ms, se, th], abs(ms - th) <= P["tol_se"] * se, "validation"),
                 chk("H1", f"P27's printed experiment value ({P['printed']}) within {P['tol_se']} SE of this run's mean", [P["printed"], ms, se], abs(P["printed"] - ms) <= P["tol_se"] * se, "hypothesis"),
                 chk("H2", f"largest-component fraction within {P['h2']} of s = 1 - exp(-cs) for c >= {P['h2_from']}", sweep, bool(okH2), "hypothesis"),
                 chk("H3", f"sudden emergence: largest fraction <= {P['h3_lo']} for c <= {P['below']} and >= {P['h3_hi']} for c >= {P['above']}", [lo, up], lo <= P["h3_lo"] and up >= P["h3_hi"], "hypothesis"),
                 chk("R1", "values", res, True, "reporting")]

def er_critical(P, rng):
    """Largest component of G(n, 1/(n-1)) at the critical point c = 1 for several n; the standard result (not from P27) is size ~ n^(2/3)."""
    from scipy.sparse import coo_matrix; from scipy.sparse.csgraph import connected_components
    out = {}
    for n in P["n_values"]:
        Ls = []
        for _ in range(P["reps"]):
            cc = P["c"] + P.get("lam", 0.0) * n ** (-1 / 3); m = rng.binomial(n * (n - 1) // 2, cc / (n - 1)); a = rng.integers(0, n, m); b = rng.integers(0, n, m); kk = a != b
            lab = connected_components(coo_matrix((np.ones(kk.sum()), (a[kk], b[kk])), shape=(n, n)), directed=False)[1]; Ls.append(np.bincount(lab).max())
        out[str(n)] = dict(mean_largest=float(np.mean(Ls)), se=float(np.std(Ls, ddof=1) / np.sqrt(len(Ls))), fraction=float(np.mean(Ls)) / n, scaled=float(np.mean(Ls)) / n ** (2 / 3))
    sl = float(np.polyfit(np.log(P["n_values"]), np.log([out[str(n)]["mean_largest"] for n in P["n_values"]]), 1)[0])
    return dict(by_n=out, slope=sl), [chk("V1", "largest component fraction falls with n at c = 1", [out[str(n)]["fraction"] for n in P["n_values"]], all(np.diff([out[str(n)]["fraction"] for n in P["n_values"]]) < 0), "validation"),
            chk("H1", f"log-log slope within {P['h1']} of 2/3", sl, abs(sl - 2 / 3) <= P["h1"], "hypothesis"), chk("R1", "values", out, True, "reporting")]

def gw_survival(P, rng):
    """Poisson(c) Galton-Watson process (P27 Definition 2.4) from one individual: share reaching K total individuals vs the survival
    probability s solving s = 1 - exp(-c s) (the same equation as P27 Eq. 2.2 for the giant component)."""
    k = P["tol_se"]; out = {}; ok = True
    for c in P["c_values"]:
        s = 0.9
        for _ in range(5000): s = 1 - np.exp(-c * s)
        hit = 0
        for _ in range(P["reps"]):
            z, tot = 1, 1
            while 0 < z and tot < P["K"]: z = int(rng.poisson(c * z)); tot += z
            hit += tot >= P["K"]
        ph = hit / P["reps"]; se = np.sqrt(max(ph * (1 - ph), 1e-12) / P["reps"]); out[str(c)] = dict(share=ph, se=se, s=s); ok &= abs(ph - s) <= k * se + P["bias"]
    return out, [chk("V1", "share is a probability", out, all(0 <= v["share"] <= 1 for v in out.values()), "validation"),
                 chk("H1", f"share reaching K within {k} SE (+{P['bias']}) of s = 1 - exp(-cs) for every c", out, bool(ok), "hypothesis"),
                 chk("R1", "values", out, True, "reporting")]

def percolation(P, rng):
    """P44/P45 (Downey, Think Complexity 7.3-7.4, LibreTexts): n x n grid, each cell porous with probability q, top row wet, wetness
    spreads to porous von Neumann neighbours; a percolating cluster connects top to bottom. Implemented with connected-component
    labelling (4-connectivity), equivalent to running the CA to its fixed point. mode 'prob': share of percolating arrays at each q;
    mode 'walk': P45's find_critical random walk (start 0.6, step 0.005) averaged over walks, for several n;
    mode 'sharp': slope of the percolation probability between two q values for several n."""
    from scipy import ndimage
    def perc(n, q):
        a = rng.random((n, n)) < q; lab, _ = ndimage.label(a)
        top = set(lab[0][lab[0] > 0]); bot = set(lab[-1][lab[-1] > 0]); return len(top & bot) > 0
    if P["mode"] == "prob":
        out = {str(q): float(np.mean([perc(P["n"], q) for _ in range(P["reps"])])) for q in P["q_values"]}
        o = [out[str(q)] for q in P["q_values"]]
        return dict(n=P["n"], p_perc=out), [chk("V1", "percolation probability non-decreasing in q (within 4 SE)", o, all(o[i + 1] >= o[i] - 4 * np.sqrt(0.25 / P["reps"]) for i in range(len(o) - 1))),
                chk("H1", P["h1_text"], out, bool(eval(P["h1_expr"], {}, dict(o=o))), "hypothesis"), chk("R1", "values", out, True, "reporting")]
    if P["mode"] == "walk":
        out = {}
        for n in P["n_values"]:
            means = []
            for _ in range(P["walks"]):
                q = 0.6; qs = [q]
                for _ in range(P["iters"]):
                    q = q - 0.005 if perc(n, q) else q + 0.005; qs.append(q)
                means.append(np.mean(qs))
            out[str(n)] = dict(mean=float(np.mean(means)), se=float(np.std(means, ddof=1) / np.sqrt(len(means))))
        m = [out[str(n)]["mean"] for n in P["n_values"]]
        return dict(by_n=out), [chk("V1", "walk means inside (0.5, 0.7)", m, all(0.5 < x < 0.7 for x in m)),
                chk("H1", P["h1_text"], m, bool(eval(P["h1_expr"], {}, dict(m=m))), "hypothesis"), chk("R1", "values", out, True, "reporting")]
    out = {}
    for n in P["n_values"]:
        lo = np.mean([perc(n, P["q_lo"]) for _ in range(P["reps"])]); hi = np.mean([perc(n, P["q_hi"]) for _ in range(P["reps"])])
        out[str(n)] = dict(p_lo=float(lo), p_hi=float(hi), slope=float((hi - lo) / (P["q_hi"] - P["q_lo"])))
    sl = [out[str(n)]["slope"] for n in P["n_values"]]
    return dict(by_n=out), [chk("V1", "probabilities in [0, 1]", sl, all(0 <= out[str(n)]["p_lo"] <= 1 for n in P["n_values"])),
            chk("H1", "the transition sharpens with n (slope increases with n)", sl, all(np.diff(sl) > 0), "hypothesis"), chk("R1", "values", out, True, "reporting")]

def coop_rules(P, rng):
    """P47 (Nowak 2006, Science 314:1560, author manuscript PMC3279745): Table 1 payoff matrices (alpha, beta; gamma, delta) for kin
    selection, direct, indirect and network reciprocity and group selection, with ESS (alpha > gamma), RD (alpha + beta > gamma + delta)
    and AD (alpha + 2 beta > gamma + 2 delta) conditions. Thresholds in b/c are found numerically (bisection, c = 1) and compared with
    P47's printed rules. Moran check (agent's, standard theory not in P47): exact fixation probability of one cooperator (tit-for-tat)
    among defectors in a frequency-dependent Moran process, fitness 1 - s + s * payoff, and a stochastic simulation of it."""
    w, q, r, k, n, m = P["w"], P["q"], P["r"], P["k"], P["n"], P["m"]
    def mats(b, c=1.0):
        H = ((b - c) * k - 2 * c) / ((k + 1) * (k - 2))
        return {"kin": ((b - c) * (1 + r), b * r - c, b - r * c, 0.0), "direct": ((b - c) / (1 - w), -c, b, 0.0),
                "indirect": (b - c, -c * (1 - q), b * (1 - q), 0.0), "network": (b - c, H - c, b - H, 0.0),
                "group": ((b - c) * (m + n), (b - c) * m - c * n, b * n, 0.0)}
    conds = {"ESS": lambda a, bb, g, d: a - g, "RD": lambda a, bb, g, d: a + bb - g - d, "AD": lambda a, bb, g, d: a + 2 * bb - g - 2 * d}
    printed = {"kin": [1 / r] * 3, "direct": [1 / w, (2 - w) / w, (3 - 2 * w) / w], "indirect": [1 / q, (2 - q) / q, (3 - 2 * q) / q], "network": [k] * 3, "group": [1 + n / m] * 3}
    num = {}
    for mech in printed:
        num[mech] = []
        for cn, f in conds.items():
            lo, hi = 1.0 + 1e-9, 1e4
            for _ in range(200):
                mid = (lo + hi) / 2
                if f(*mats(mid)[mech]) > 0: hi = mid
                else: lo = mid
            num[mech].append(hi)
    err = max(abs(a - b) / b for mech in printed for a, b in zip(num[mech], printed[mech]))
    N, s = P["N"], P["s_sel"]
    def rho(bc, N=N, s=s):
        a, bb, g, d = mats(bc)["direct"]; prod = 1.0; tot = 1.0
        for i in range(1, N):
            fC = 1 - s + s * (a * (i - 1) + bb * (N - i)) / (N - 1); fD = 1 - s + s * (g * i + d * (N - i - 1)) / (N - 1)
            prod *= fD / fC; tot += prod
        return 1 / tot
    rho_vals = {str(bc): rho(bc) for bc in P["bc_values"]}
    grid = np.linspace(P["bc_values"][0], P["bc_values"][-1], 4001); rv = np.array([rho(x) for x in grid]); cross = float(grid[np.argmax(rv > 1 / N)]) if (rv > 1 / N).any() else None
    Ns, bs = P["N_sim"], P["bc_sim"]; a, bb, g, d = mats(bs)["direct"]; fix = 0
    for _ in range(P["reps"]):
        i = 1
        while 0 < i < Ns:
            fC = 1 - s * 10 + s * 10 * (a * (i - 1) + bb * (Ns - i)) / (Ns - 1); fD = 1 - s * 10 + s * 10 * (g * i + d * (Ns - i - 1)) / (Ns - 1)
            pr = i * fC / (i * fC + (Ns - i) * fD); birthC = rng.random() < pr; deathC = rng.random() < i / Ns
            i += int(birthC) - int(deathC)
        fix += i == Ns
    rex = rho(bs, Ns, 10 * s)
    pf = fix / P["reps"]; se = np.sqrt(pf * (1 - pf) / P["reps"])
    res = dict(numeric=num, printed=printed, max_rel_err=err, rho=rho_vals, inv_N=1 / N, crossing_bc=cross, AD_threshold=(3 - 2 * w) / w, sim=dict(N=Ns, bc=bs, s=10 * s, p_fix=pf, se=se, exact=rex))
    lo_bc, hi_bc = P["bc_values"][0], P["bc_values"][-1]
    return res, [chk("V1", "numerical thresholds equal P47's printed rules (relative error < 1e-6) for all five mechanisms", err, err < 1e-6),
                 chk("V2", "stochastic Moran fixation within 4 SE of the exact formula", [pf, se, rex], abs(pf - rex) <= 4 * max(se, 1e-9)),
                 chk("H1", "1/3 rule: rho < 1/N below and > 1/N above the AD threshold (end points of the b/c range)", [rho_vals[str(lo_bc)], rho_vals[str(hi_bc)], 1 / N], rho_vals[str(lo_bc)] < 1 / N < rho_vals[str(hi_bc)], "hypothesis"),
                 chk("H2", "finite-N crossing within 5% of the AD threshold (3 - 2w)/w", [cross, (3 - 2 * w) / w], cross is not None and abs(cross / ((3 - 2 * w) / w) - 1) <= 0.05, "hypothesis"),
                 chk("R1", "values", res, True, "reporting")]

def _hyps(P, res):
    return [chk(f"H{i}", t, res, bool(eval(e, dict(o=res, abs=abs, all=all, any=any, min=min, max=max, len=len))), "hypothesis") for i, (t, e) in enumerate(P["hyps"], 1)]

def moran_game(P, rng):
    """Exact fixation probability of one A mutant in a Moran process with frequency-dependent fitness f_i = 1 - w + w F_i (P58 Eqs. 2-3, B.1),
    for a coordination game with payoffs a, b, c, d. For each (N, w) the agent finds by bisection the payoff a at which rho_A = 1/N and the
    corresponding unstable equilibrium x* = (d - b)/((d - b) + (a - c)); compares with P58 Eq. 4 (weak selection) and the one-third law."""
    b, c, d = P["b"], P["c"], P["d"]
    def rho(a, N, w):
        i = np.arange(1, N); F = (a * (i - 1) + b * (N - i)) / (N - 1); G = (c * i + d * (N - i - 1)) / (N - 1)
        r = (1 - w + w * G) / (1 - w + w * F); return float(1 / (1 + np.cumprod(r).sum()))
    def xstar(a): return (d - b) / ((d - b) + (a - c))
    out = {}
    for N in P["N_values"]:
        for w in P["w_values"]:
            lo, hi = c + 1e-9, c + 1e4
            for _ in range(200):
                m = 0.5 * (lo + hi)
                if rho(m, N, w) > 1 / N: hi = m
                else: lo = m
            a_eq4 = ((N + 1) * c + (2 * N - 4) * d - (2 * N - 1) * b) / (N - 2)
            out[f"N{N}_w{w}"] = dict(N=N, w=w, Nw=N * w, a_crit=hi, x_crit=xstar(hi), a_eq4=a_eq4, x_eq4=xstar(a_eq4) if a_eq4 > c else None)
    # V1: neutral rho = 1/N, and B.1 equals a direct absorption-probability solve (N = 10)
    N0 = 10; a0 = c + 2.0; w0 = 0.3; i = np.arange(0, N0 + 1)
    F = np.where(i > 0, (a0 * (i - 1) + b * (N0 - i)) / (N0 - 1), 0); G = np.where(i < N0, (c * i + d * (N0 - i - 1)) / (N0 - 1), 0)
    f = 1 - w0 + w0 * F; g = 1 - w0 + w0 * G; A = np.zeros((N0 + 1, N0 + 1)); rhs = np.zeros(N0 + 1); A[0, 0] = 1; A[N0, N0] = 1; rhs[N0] = 1
    for k in range(1, N0):
        tot = k * f[k] + (N0 - k) * g[k]; up = (N0 - k) / N0 * k * f[k] / tot; dn = k / N0 * (N0 - k) * g[k] / tot
        A[k, k] = up + dn; A[k, k + 1] = -up; A[k, k - 1] = -dn
    direct = float(np.linalg.solve(A, rhs)[1]); vals = dict(neutral=rho(a0, N0, 0.0), inv_N=1 / N0, B1=rho(a0, N0, w0), direct=direct)
    return out, [chk("V1", "neutral rho = 1/N (1e-12) and P58 Eq. B.1 equals a direct absorption solve (1e-10) at N = 10", vals, abs(vals["neutral"] - 0.1) < 1e-12 and abs(vals["B1"] - direct) < 1e-10)] + _hyps(P, out) + [chk("R1", "values", out, True, "reporting")]

def markov_converge(P, rng):
    """Regular Markov chains (P73, Sekhon & Bloom, LibreTexts 10.3): iterates V_n = V_0 T^n, the equilibrium E solving ET = E,
    the geometric convergence rate (second eigenvalue modulus), Wielandt's primitivity bound m <= (n - 1)^2 + 1 checked on the
    Wielandt matrix, a periodic chain for which ET = E has a solution but T^n does not converge, and DeGroot averaging
    x_{t+1} = T x_t (consensus) whose limit is the E-weighted mean of initial opinions."""
    T = np.array(P["T"], float); V0 = np.array(P["V0"], float)
    def eq(M):
        w, v = np.linalg.eig(M.T); i = int(np.argmin(abs(w - 1))); e = np.real(v[:, i]); return e / e.sum()
    E = eq(T); Vs = {}; V = V0.copy()
    for n in range(1, P.get("n_max", 30) + 1):
        V = V @ T
        if n in P["report_n"]: Vs[str(n)] = [round(float(x), 10) for x in V]
    lam = sorted(abs(np.linalg.eigvals(T)), reverse=True); l2 = float(lam[1]) if len(lam) > 1 else 0.0
    err20 = float(abs(V0 @ np.linalg.matrix_power(T, 20) - E).max())
    res = dict(E=[round(float(x), 10) for x in E], V=Vs, lambda2=round(l2, 10), err_n20=err20, ET_minus_E=float(abs(E @ T - E).max()))
    def expo(M):
        n = M.shape[0]; B = (M > 0).astype(int); C = B.copy()
        for m in range(1, 3 * n * n):
            if (C > 0).all(): return m
            C = ((C @ B) > 0).astype(int)
        return None
    if "check_regular" in P:
        res["regular"] = {k: dict(exponent=expo(np.array(M, float)), bound=(len(M) - 1) ** 2 + 1) for k, M in P["check_regular"].items()}
        res["powers2"] = {k: np.round(np.linalg.matrix_power(np.array(M, float), 2), 10).tolist() for k, M in P["check_regular"].items()}
    if P.get("wielandt_n"):
        out = {}
        for n in P["wielandt_n"]:
            W = np.zeros((n, n))
            for i in range(n - 1): W[i, i + 1] = 1
            W[n - 1, 0] = 0.5; W[n - 1, 1] = 0.5
            out[str(n)] = dict(exponent=expo(W), bound=(n - 1) ** 2 + 1)
        res["wielandt"] = out
    if P.get("periodic"):
        Pm = np.array(P["periodic"], float); Ep = eq(Pm); x = np.array(P.get("periodic_V0", [1.0] + [0.0] * (len(Pm) - 1)))
        seq = [x @ np.linalg.matrix_power(Pm, k) for k in (50, 51)]
        res["periodic"] = dict(E=[round(float(v), 10) for v in Ep], ET_minus_E=float(abs(Ep @ Pm - Ep).max()), V50=[round(float(v), 6) for v in seq[0]], V51=[round(float(v), 6) for v in seq[1]],
                              converges=bool(abs(seq[0] - seq[1]).max() < 1e-9))
    if P.get("degroot_x0"):
        x0 = np.array(P["degroot_x0"], float); x = x0.copy()
        for _ in range(P.get("degroot_steps", 200)): x = T @ x
        res["degroot"] = dict(x_end=[round(float(v), 10) for v in x], weighted_mean=round(float(E @ x0), 10), spread=float(x.max() - x.min()))
    if P.get("V0_alt"):   # CVA extension: a second initial distribution, to test dependence on the start
        Va = np.array(P["V0_alt"], float) @ np.linalg.matrix_power(T, P.get("n_max", 30)); Vb = V0 @ np.linalg.matrix_power(T, P.get("n_max", 30))
        res["alt"] = dict(V_alt=[round(float(x), 10) for x in Va], V_main=[round(float(x), 10) for x in Vb], max_diff=float(abs(Va - Vb).max()))
    if P.get("random_primitive"):   # CVA extension: exponents of random primitive 0/1 patterns vs the (n - 1)^2 + 1 bound
        rp = P["random_primitive"]; out = {}
        for n in rp["n"]:
            ex = []
            while len(ex) < rp["count"]:
                M = (rng.random((n, n)) < rp["density"]).astype(float); e_ = expo(M)
                if e_ is not None: ex.append(e_)
            out[str(n)] = dict(max_exponent=int(max(ex)), mean_exponent=round(float(np.mean(ex)), 3), bound=(n - 1) ** 2 + 1)
        res["random_primitive"] = out
    ok = res["ET_minus_E"] < 1e-12 and abs(E.sum() - 1) < 1e-12 and np.allclose(T.sum(1), 1)
    return res, [chk("V1", "E T = E within 1e-12, E sums to 1, rows of T sum to 1", [res["ET_minus_E"], float(E.sum())], ok)] + _hyps(P, res) + [chk("R1", "values", res, True, "reporting")]

def mixing_time(P, rng):
    """P78 (Wikipedia 'Markov chain mixing time'): exact total-variation distance d(t) = max_x ||P^t(x, .) - pi||_TV and
    t_mix(eps) = min{t : d(t) <= eps} for (a) explicit transition matrices (lazy random walk on an n-cycle, or a given matrix)
    and (b) the Gilbert-Shannon-Reeds riffle shuffle of an n-card deck, computed exactly from the rising-sequence formula
    (probability of a permutation with r rising sequences after k shuffles = C(2^k + n - r, n) / 2^(kn), Eulerian-number
    multiplicities; agent's implementation of the Bayer-Diaconis result P78 cites, not read)."""
    from fractions import Fraction
    from math import comb, factorial, log2
    res = {}
    def tmix(d, eps): return next((t for t, v in enumerate(d) if v <= eps), None)
    eps_list = P.get("eps_values", [0.25])
    chains = {}
    for name, spec in P.get("chains", {}).items():
        if isinstance(spec, dict) and spec.get("lazy_cycle"):
            n = spec["lazy_cycle"]; M = np.zeros((n, n))
            for i in range(n): M[i, i] += 0.5; M[i, (i + 1) % n] += 0.25; M[i, (i - 1) % n] += 0.25
        else: M = np.array(spec, float)
        w, v = np.linalg.eig(M.T); pi = np.real(v[:, np.argmin(abs(w - 1))]); pi = pi / pi.sum()
        d, Pt = [], np.eye(len(M))
        for t in range(P.get("t_max", 5000) + 1):
            d.append(float(0.5 * np.abs(Pt - pi).sum(axis=1).max())); Pt = Pt @ M
            if d[-1] <= min(eps_list) and t > 0: break
        ev = sorted(abs(np.linalg.eigvals(M)))[::-1]; lam = float(ev[1]) if len(ev) > 1 else 0.0
        chains[name] = dict(n=len(M), tmix={str(e): tmix(d, e) for e in eps_list}, lambda2=round(lam, 10), t_rel=round(1 / (1 - lam), 4) if lam < 1 else None,
                            d_at={str(t): round(d[t], 6) for t in P.get("report_t", []) if t < len(d)})
    if chains: res["chains"] = chains
    if P.get("riffle"):
        rf = P["riffle"]; out = {}
        for n in rf["n_cards"]:
            A = [1]
            for m in range(2, n + 1):   # Eulerian numbers A(m, j), j = 0..m-1
                B = [0] * m
                for j in range(m): B[j] = (j + 1) * (A[j] if j < len(A) else 0) + (m - j) * (A[j - 1] if 0 < j <= len(A) else 0)
                A = B
            assert sum(A) == factorial(n)
            nf = factorial(n); d = [1 - Fraction(1, nf)]
            for k in range(1, rf["k_max"] + 1):
                den = 2 ** (k * n); tv = Fraction(0)
                for j, a in enumerate(A):
                    r = j + 1; p = Fraction(comb(2 ** k + n - r, n), den) if 2 ** k + n - r >= n else Fraction(0)
                    tv += a * abs(p - Fraction(1, nf))
                d.append(tv / 2)
            df = [float(x) for x in d]
            out[str(n)] = dict(d={str(k): round(v, 6) for k, v in enumerate(df)}, tmix={str(e): tmix(df, e) for e in eps_list}, one_point_five_log2n=round(1.5 * log2(n), 4))
        res["riffle"] = out
    M = np.array([[0.5, 0.5], [0.5, 0.5]]); ok = abs(0.5 * np.abs(M - np.array([0.5, 0.5])).sum(axis=1).max()) < 1e-15
    return res, [chk("V1", "a chain whose rows already equal pi has d(1) = 0", 0.0, bool(ok))] + _hyps(P, res) + [chk("R1", "values", res, True, "reporting")]

KINDS = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_') and k != 'chk' and getattr(v, '__module__', None) == '__main__'}

if __name__ == "__main__":
    P, H, t0 = R.start(sys.argv[1]); rng = np.random.default_rng(P["seed"])
    res, checks = KINDS[P["kind"]](P, rng); R.finish(H, P, res, checks, t0)
