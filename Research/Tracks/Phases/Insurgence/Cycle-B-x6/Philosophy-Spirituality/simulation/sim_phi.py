"""SIM-<PH>-PHI: Philosophy-Spirituality simulations (Phases track): formal models of conceptual structure only. Usage: python sim_phi.py iter-<k>."""
import os, sys, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
import track_runner as R
chk = R.chk

def crp_one_many(P, rng):
    """Chinese restaurant process (concentration alpha): a formal 'one -> many' branching process starting from a single group.
    It models no tradition: it only tests formal properties a 'divergence from a single source' reading would need
    (unbounded but slow growth of the number of branches; persistence of a dominant branch)."""
    Ks, top, H = [], [], []
    for _ in range(P["reps"]):
        sizes = [1]
        for i in range(1, P["n"]):
            if rng.random() < P["alpha"] / (P["alpha"] + i): sizes.append(1)
            else:
                s = np.array(sizes, float); sizes[rng.choice(len(sizes), p=s / s.sum())] += 1
        s = np.array(sizes, float) / P["n"]; Ks.append(len(sizes)); top.append(s.max()); H.append(float(-(s * np.log(s)).sum()))
    EK = sum(P["alpha"] / (P["alpha"] + i) for i in range(P["n"]))
    res = dict(mean_K=float(np.mean(Ks)), expected_K=float(EK), alpha_ln_n=float(P["alpha"] * np.log(P["n"])), mean_top_share=float(np.mean(top)), mean_entropy=float(np.mean(H)))
    c = [chk("V1", "mean number of branches within 5% of the analytic sum alpha/(alpha+i)", res["mean_K"], abs(res["mean_K"] / EK - 1) <= 0.05),
         chk("H1", f"a dominant branch persists: mean largest-branch share > {P['h1']}", res["mean_top_share"], res["mean_top_share"] > P["h1"], "hypothesis"),
         chk("R1", "entropy of the final partition and alpha ln n reference", [res["mean_entropy"], res["alpha_ln_n"]], True, "reporting")]
    return res, c

def crp_one_many_se(P, rng):
    """Chinese restaurant process (concentration alpha) as in DV0's crp_one_many, with the validation tolerance sized as a
    multiple of the Monte Carlo standard error (the lesson of DV0's V1 Fail, where a fixed 5% band ignored sampling error).
    Formal 'one -> many' structure only; models no tradition."""
    res = {}
    for a in P["alphas"]:
        Ks, top = [], []
        for _ in range(P["reps"]):
            sizes = [1]
            for i in range(1, P["n"]):
                if rng.random() < a / (a + i): sizes.append(1)
                else:
                    s = np.array(sizes, float); sizes[rng.choice(len(sizes), p=s / s.sum())] += 1
            Ks.append(len(sizes)); top.append(max(sizes) / P["n"])
        EK = sum(a / (a + i) for i in range(P["n"]))
        res[str(a)] = dict(mean_K=float(np.mean(Ks)), se_K=float(np.std(Ks, ddof=1) / np.sqrt(len(Ks))), expected_K=float(EK), mean_top_share=float(np.mean(top)))
    k = P["tol_se"]; ok = all(abs(v["mean_K"] - v["expected_K"]) <= k * v["se_K"] for v in res.values()); lo = res[str(P["alphas"][0])]
    c = [chk("V1", f"for every alpha, mean number of branches within {k} Monte Carlo standard errors of the analytic sum alpha/(alpha+i)",
             {kk: [v["mean_K"], v["expected_K"], v["se_K"]] for kk, v in res.items()}, ok),
         chk("H1", f"alpha {P['alphas'][0]}: mean largest-branch share > {P['h1']} (one source stays dominant)", lo["mean_top_share"], lo["mean_top_share"] > P["h1"], "hypothesis"),
         chk("R1", "results by alpha", res, True, "reporting")]
    return res, c

def cfst_scale(P, rng):
    """Cultural fixation index CFst = var_between / (var_between + var_within) (P15's Eq. 1) on synthetic data: G groups of n
    people, latent trait = group effect (SD sb) + individual effect (SD sw). Compares CFst on the latent continuous trait with
    CFst on a dichotomised version (above/below the overall latent median), as survey items on different scales would be."""
    out = {"continuous": [], "binary": []}
    def cf(y, g):
        mu = np.array([y[g == j].mean() for j in range(P["groups"])]); vb = mu.var(ddof=0); vw = np.mean([y[g == j].var(ddof=0) for j in range(P["groups"])]); return vb / (vb + vw)
    for _ in range(P["reps"]):
        g = np.repeat(np.arange(P["groups"]), P["n"]); y = rng.normal(0, P["sb"], P["groups"])[g] + rng.normal(0, P["sw"], len(g))
        out["continuous"].append(cf(y, g)); out["binary"].append(cf((y > np.median(y)).astype(float), g))
    an = P["sb"] ** 2 / (P["sb"] ** 2 + P["sw"] ** 2); m = {k: float(np.mean(v)) for k, v in out.items()}; se = {k: float(np.std(v, ddof=1) / np.sqrt(len(v))) for k, v in out.items()}
    # finite-sample expectation of the between-group variance of group means adds sw^2/n (approximately)
    an_fs = (P["sb"] ** 2 * (1 - 1 / P["groups"]) + P["sw"] ** 2 / P["n"]) / (P["sb"] ** 2 * (1 - 1 / P["groups"]) + P["sw"] ** 2 / P["n"] + P["sw"] ** 2 * (1 - 1 / P["n"]))
    k = P["tol_se"]; tol = max(k * se["continuous"], P["bias_allow"])
    c = [chk("V1", f"continuous trait: mean CFst within max({k} SE, {P['bias_allow']}) of the finite-sample approximation (population value sb^2/(sb^2+sw^2) = {an:.4f} reported)",
             [m["continuous"], an_fs, tol], abs(m["continuous"] - an_fs) <= tol),
         chk("H1", f"dichotomising the same trait lowers CFst by at least {P['h1']:.0%} relative to the continuous value", 1 - m["binary"] / m["continuous"], 1 - m["binary"] / m["continuous"] >= P["h1"], "hypothesis"),
         chk("R1", "mean CFst by scale, population and finite-sample values", dict(mean=m, se=se, population=an, finite_sample=an_fs), True, "reporting")]
    return dict(mean=m, se=se, population=an, finite_sample=an_fs), c

def schism_yule(P, rng):
    """Nested schisms as a pure-birth (Yule) splitting process (cf. P14: world religions may show tree-like nested schisms).
    Each group splits at rate lam per unit time; optionally the daughter inherits a rate multiplied by exp(N(0, het)) (heritable
    rate variation). Records group counts at time T (constant-rate Yule) and, for trees grown to a fixed number of groups, imbalance (Colless index normalised by its maximum)."""
    def grow(het, T=None, ntips=None):
        groups = [(P["lam"], "")]; t = 0.0
        while True:
            tot = sum(r for r, _ in groups); t += rng.exponential(1 / tot)
            if (T is not None and t > T) or (ntips is not None and len(groups) >= ntips) or len(groups) >= P["cap"]: break
            i = rng.choice(len(groups), p=np.array([r for r, _ in groups]) / tot); r, path = groups.pop(i)
            for b in "01": groups.append((r * float(np.exp(rng.normal(0, het))) if het > 0 else r, path + b))
        return [p for _, p in groups]
    def colless(ps):
        if len(ps) <= 1: return 0
        l = [p[1:] for p in ps if p[0] == "0"]; r_ = [p[1:] for p in ps if p[0] == "1"]
        return abs(len(l) - len(r_)) + colless(l) + colless(r_)
    n = P["tips"]; mx = (n - 1) * (n - 2) / 2
    ns = np.array([len(grow(0.0, T=P["T"])) for _ in range(P["reps"])])
    out = dict(yule_time=dict(mean_n=float(ns.mean()), se_n=float(ns.std(ddof=1) / np.sqrt(len(ns))), capped=int((ns >= P["cap"]).sum())))
    for lab, het in (("yule", 0.0), ("heritable_rates", P["het"])):
        cs = np.array([colless(grow(het, ntips=n)) / mx for _ in range(P["reps"])])
        out[lab] = dict(mean_colless=float(cs.mean()), se_colless=float(cs.std(ddof=1) / np.sqrt(len(cs))))
    yt = out["yule_time"]; y = out["yule"]; En = float(np.exp(P["lam"] * P["T"])); k = P["tol_se"]; h = out["heritable_rates"]
    c = [chk("V1", f"Yule: mean number of groups at T within {k} standard errors of exp(lam T) = {En:.3f} (no run reached the cap)", [yt["mean_n"], En, k * yt["se_n"], yt["capped"]],
             abs(yt["mean_n"] - En) <= k * yt["se_n"] and yt["capped"] == 0),
         chk("H1", f"at {P['tips']} groups, heritable rate variation (SD {P['het']}) makes schism trees more imbalanced: normalised Colless higher than Yule by more than {k} combined SE",
             [h["mean_colless"], y["mean_colless"]], h["mean_colless"] - y["mean_colless"] > k * (h["se_colless"] ** 2 + y["se_colless"] ** 2) ** 0.5, "hypothesis"),
         chk("R1", "results", out, True, "reporting")]
    return out, c


def split_merge(P, rng):
    """Branching paired with merging ('procession' with 'reversion' as a formal skeleton only; P07, P18; also P14's
    reticulation): K groups, each splits at rate lam, each pair merges at rate mu. The stationary law is exactly a zero-truncated
    Poisson with x = 2 lam / mu (birth-death chain: pi_K proportional to x^(K-1)/K!), mean x / (1 - e^-x); mean-field gives 1 + x.
    Control: mu = 0 is a Yule process with E K(T) = e^(lam T)."""
    lam, mu = P["lam"], P["mu"]
    def run(T, mu_):
        K = 1; t = 0.0
        while True:
            rate = lam * K + mu_ * K * (K - 1) / 2; t += rng.exponential(1 / rate)
            if t > T: return K
            if rng.random() < lam * K / rate: K += 1
            else: K -= 1
    y = np.array([run(P["Ty"], 0.0) for _ in range(P["reps_y"])]); ym = float(y.mean()); yse = float(y.std(ddof=1) / np.sqrt(len(y))); yex = float(np.exp(lam * P["Ty"]))
    s = np.array([run(P["T"], mu) for _ in range(P["reps"])]); sm = float(s.mean()); sse = float(s.std(ddof=1) / np.sqrt(len(s)))
    x = 2 * lam / mu; ex = x / (1 - np.exp(-x)); mf = 1 + x; k = P["tol_se"]
    res = dict(yule_mean=ym, yule_se=yse, yule_expected=yex, stationary_mean=sm, stationary_se=sse, exact_mean=float(ex), mean_field=float(mf), max_K=int(s.max()))
    c = [chk("V1", f"mu = 0 control: mean K(T={P['Ty']}) within {k} SE of e^(lam T) = {yex:.4f}", [ym, yse], abs(ym - yex) <= k * yse),
         chk("V2", f"mean K at T = {P['T']} within {k} SE of the exact stationary mean x/(1-e^-x) = {ex:.4f}", [sm, sse], abs(sm - ex) <= k * sse),
         chk("H1", f"mean-field 1 + 2 lam/mu = {mf:.3f} within 10% of the simulated stationary mean", [mf, sm], abs(mf / sm - 1) <= 0.10, "hypothesis"),
         chk("R1", "means", res, True, "reporting")]
    return res, c

def text_consolidation(P, rng):
    """P18 (Chan, SEP 'Laozi', read in full in DVC): collections of sayings 'overlapping to some extent' expanded and competed,
    then 'the demand for textual uniformity rose' and 'the different textual traditions eventually gave way to the received text'.
    Toy: L lineages of a text of M binary sites copied independently for t1 generations (per-site change mu per generation),
    then for t2 generations each copy, per site with probability u, adopts the majority reading across lineages (standardisation).
    Mean pairwise distance (share of differing sites) is tracked; divergence-phase expectation (1 - (1 - 2 mu)^(2 t1)) / 2."""
    L, M, R_ = P["lineages"], P["M"], P["reps"]; d1 = []; d2 = []
    def mpd(X): return float(np.mean([(X[i] != X[j]).mean() for i in range(L) for j in range(i + 1, L)]))
    for _ in range(R_):
        X = np.zeros((L, M), dtype=np.int8)
        for t in range(P["t1"]): X ^= (rng.random((L, M)) < P["mu"]).astype(np.int8)
        d1.append(mpd(X))
        for t in range(P["t2"]):
            maj = (X.mean(0) > 0.5).astype(np.int8); adopt = rng.random((L, M)) < P["u"]; X = np.where(adopt, maj[None, :], X).astype(np.int8)
            X ^= (rng.random((L, M)) < P["mu"]).astype(np.int8)
        d2.append(mpd(X))
    d1 = np.array(d1); d2 = np.array(d2); k = P["tol_se"]; se = lambda a: float(a.std(ddof=1) / np.sqrt(len(a)))
    e1 = (1 - (1 - 2 * P["mu"]) ** (2 * P["t1"])) / 2
    res = dict(div_phase_distance=float(d1.mean()), div_phase_se=se(d1), expected=e1, after_consolidation=float(d2.mean()), after_se=se(d2))
    c = [chk("V1", f"divergence-phase mean pairwise distance within {k} SE of (1-(1-2mu)^(2 t1))/2", [res["div_phase_distance"], e1, res["div_phase_se"]], abs(res["div_phase_distance"] - e1) <= k * res["div_phase_se"] + 1e-12),
         chk("H1", f"standardisation lowers distance by more than {P['h1']} (relative)", [res["div_phase_distance"], res["after_consolidation"]], res["after_consolidation"] < (1 - P["h1"]) * res["div_phase_distance"], "hypothesis"),
         chk("R1", "distances", res, True, "reporting")]
    return res, c

def novelty_stream(P, rng):
    """Agent's toy for the continuing emergence of new forms (Bergson's creation of the new, P08, interpretive): a Chinese-restaurant
    process with concentration alpha; expected number of distinct forms after n draws is sum_{i<n} alpha/(alpha+i)."""
    k = P["tol_se"]; res = {}
    for n in P["n_values"]:
        K = []
        for _ in range(P["reps"]):
            u = rng.random(n); K.append(int(np.sum(u < P["alpha"] / (P["alpha"] + np.arange(n)))))
        an = float(np.sum(P["alpha"] / (P["alpha"] + np.arange(n)))); res[str(n)] = dict(mean=float(np.mean(K)), se=float(np.std(K, ddof=1) / np.sqrt(len(K))), analytic=an)
    a, b = res[str(P["n_values"][0])], res[str(P["n_values"][-1])]
    okV = all(abs(v["mean"] - v["analytic"]) <= k * v["se"] for v in res.values())
    return res, [chk("V1", f"mean number of forms within {k} SE of the analytic sum", res, bool(okV), "validation"),
                 chk("H1", f"novelty does not stop: forms at n = {P['n_values'][-1]} exceed n = {P['n_values'][0]} by > {k} combined SE", [a, b], b["mean"] - a["mean"] > k * np.hypot(a["se"], b["se"]), "hypothesis"),
                 chk("H2", f"but its rate falls: new forms per draw at the end < {P['h2']} of the start", [P["alpha"] / (P["alpha"] + P["n_values"][-1])], P["alpha"] / (P["alpha"] + P["n_values"][-1]) < P["h2"], "hypothesis"),
                 chk("R1", "values", res, True, "reporting")]

def abrams_groups(P, rng):
    """P30's model dx/dt = (1-x) c x^a u - x c (1-x)^a (1-u) (x = unaffiliated share, u = its perceived utility).
    mode 'logistic' (a = 1): compare with the exact logistic x(t) for rate c(2u-1); mode 'bistable' (a > 1): interior unstable fixed point
    acts as a threshold for the rise of a minority with higher utility; mode 'cliques': two clusters (sizes x0, 1-x0) coupled with
    out-group weight p, mean-field version of P30's Eq. 2/4 experiment; delay to reach x = 0.5 vs -ln p / (2u - 1)."""
    c, u = P["c"], P["u"]; h = P["dt"]
    def rhs(x, a): return (1 - x) * c * x ** a * u - x * c * (1 - x) ** a * (1 - u)
    if P["mode"] == "logistic":
        x = P["x0"]; t = 0.0; err = 0.0; rate = c * (2 * u - 1)
        for _ in range(P["steps"]):
            k1 = rhs(x, 1); k2 = rhs(x + h * k1 / 2, 1); k3 = rhs(x + h * k2 / 2, 1); k4 = rhs(x + h * k3, 1); x += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6; t += h
            ex = 1 / (1 + (1 / P["x0"] - 1) * np.exp(-rate * t)); err = max(err, abs(x - ex))
        tq = {str(q): float(np.log((q / (1 - q)) / (P["x0"] / (1 - P["x0"]))) / rate) for q in P["quantiles"]}
        return dict(final=x, max_err=err, times=tq), [chk("V1", "RK4 matches the logistic solution within 1e-6", err, err < 1e-6, "validation"),
                chk("H1", f"from x0 = {P['x0']} the unaffiliated share exceeds 0.5 by t = {P['t_check']}", tq, tq["0.5"] <= P["t_check"], "hypothesis"), chk("R1", "values", tq, True, "reporting")]
    if P["mode"] == "shock":
        x = P["x0"]; t = 0.0; peak = x; tr = []
        while t < P["tmax"]:
            uu = u if t < P["t_shock"] else P["u_after"]; k1 = (1 - x) * c * x * uu - x * c * (1 - x) * (1 - uu); x += h * k1; t += h; peak = max(peak, x)
            if abs(t - P["t_shock"]) < h / 2: x_at = x
        res = dict(x_at_shock=x_at, peak=peak, final=x)
        return res, [chk("V1", "x stays in [0, 1]", res, 0 <= x <= 1, "validation"),
                     chk("H1", f"after the utility drop to {P['u_after']} the stance declines below {P['h1']} by t = {P['tmax']}", res, x < P["h1"], "hypothesis"), chk("R1", "values", res, True, "reporting")]
    if P["mode"] == "bistable":
        a = P["a"]; xs = np.linspace(1e-6, 1 - 1e-6, 200001); fv = rhs(xs, a); roots = xs[1:][np.sign(fv[1:]) != np.sign(fv[:-1])]
        xstar = float(roots[0]) if len(roots) else None; fin = {}
        for x0 in P["x0_values"]:
            x = x0
            for _ in range(P["steps"]): x = min(max(x + h * rhs(x, a), 0.0), 1.0)
            fin[str(x0)] = x
        below = [x0 for x0 in P["x0_values"] if xstar and x0 < xstar]; above = [x0 for x0 in P["x0_values"] if xstar and x0 > xstar]
        return dict(interior_fixed_point=xstar, finals=fin), [chk("V1", "exactly one interior fixed point", [float(r) for r in roots], len(roots) == 1, "validation"),
                chk("H1", "a minority starting below the interior point declines even with the higher utility", fin, all(fin[str(x0)] < 0.01 for x0 in below) and len(below) > 0, "hypothesis"),
                chk("H2", "above it, the minority rises to dominance", fin, all(fin[str(x0)] > 0.99 for x0 in above) and len(above) > 0, "hypothesis"), chk("R1", "values", fin, True, "reporting")]
    out = {}
    for p in P["p_values"]:
        X, Y = 1.0, 0.0; t = 0.0; w1, w2 = P["x0"], 1 - P["x0"]
        while (w1 * X + w2 * Y) < 0.5 and t < P["tmax"]:
            l1 = (w1 * X + p * w2 * Y) / (w1 + p * w2); l2 = (p * w1 * X + w2 * Y) / (p * w1 + w2)
            dX = (1 - X) * c * l1 * u - X * c * (1 - l1) * (1 - u); dY = (1 - Y) * c * l2 * u - Y * c * (1 - l2) * (1 - u)
            X += h * dX; Y += h * dY; t += h
        out[str(p)] = t
    lp = -np.log(P["p_values"]) / (2 * u - 1); tt = np.array([out[str(p)] for p in P["p_values"]]); fit = np.polyfit(lp, tt, 1); r2 = float(np.corrcoef(lp, tt)[0, 1] ** 2)
    return dict(t_half=out, slope=float(fit[0]), intercept=float(fit[1]), r2=r2), [chk("V1", "all runs reach x = 0.5 before tmax", out, all(v < P["tmax"] for v in out.values()), "validation"),
            chk("H1", f"delay grows linearly with -ln p/(2u-1) (r^2 > {P['h1']})", r2, r2 > P["h1"], "hypothesis"), chk("R1", "values", out, True, "reporting")]

KINDS = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_') and k != 'chk' and getattr(v, '__module__', None) == '__main__'}

if __name__ == "__main__":
    P, H, t0 = R.start(sys.argv[1]); rng = np.random.default_rng(P["seed"])
    res, checks = KINDS[P["kind"]](P, rng); R.finish(H, P, res, checks, t0)
