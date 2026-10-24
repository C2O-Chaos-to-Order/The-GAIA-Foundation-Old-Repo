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


KINDS = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_') and k != 'chk' and getattr(v, '__module__', None) == '__main__'}

if __name__ == "__main__":
    P, H, t0 = R.start(sys.argv[1]); rng = np.random.default_rng(P["seed"])
    res, checks = KINDS[P["kind"]](P, rng); R.finish(H, P, res, checks, t0)
