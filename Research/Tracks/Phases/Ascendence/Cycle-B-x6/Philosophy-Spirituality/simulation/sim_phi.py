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
    if P["mode"] == "ramp":
        a = P["a"]; x = P["x0"]; t = 0.0; T1 = P["T_ramp"]; u0, u1 = P["u0"], P["u1"]; x_peak = None
        while t < 2 * T1 + P["T_hold"]:
            uu = u0 + (u1 - u0) * (t / T1) if t < T1 else (u1 - (u1 - u0) * ((t - T1) / T1) if t < 2 * T1 else u0)
            x = min(max(x + h * ((1 - x) * c * x ** a * uu - x * c * (1 - x) ** a * (1 - uu)), 0.0), 1.0); t += h
            if x_peak is None and t >= T1: x_peak = x
            if abs(t - 2 * T1) < h / 2: x_back = x
        res = dict(a=a, x_at_peak_utility=x_peak, x_when_utility_restored=x_back, x_after_hold=x)
        return res, [chk("V1", "x stays in [0, 1]", res, 0 <= x <= 1, "validation"),
                     chk("H1", P["h1_text"], res, bool(eval(P["h1_expr"], {}, dict(res=res))), "hypothesis"), chk("R1", "values", res, True, "reporting")]
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

def exit_voice(P, rng):
    """Agent's formalization (Hypothetical) of Hirschman's exit-voice-loyalty account as reported in P51 (SEP 'Loyalty'): institutions
    have an 'endemic tendency to decline' (rate d); loyalty lets members persist while voice brings the institution 'back on track'.
    Quality Q in [0, 1]; members i with loyalty lam_i ~ U(0, lam_max) stay while Q >= theta - lam_i and voice while Q < theta;
    dQ/dt = -d + v V (1 - Q) + noise, V = share of members present and voicing. Exit is permanent."""
    th, d, v, dt, T, sig = P["theta"], P["d"], P["v"], P["dt"], P["T"], P["noise"]; out = {}
    for lm in P["lam_max"]:
        reps = []
        for _ in range(P["reps"]):
            lam = rng.uniform(0, lm, P["N"]) if lm > 0 else np.zeros(P["N"]); present = np.ones(P["N"], bool); Q = th; t_last = None
            for st in range(int(T / dt)):
                present &= Q >= th - lam
                V = present.mean() if Q < th else 0.0
                Q = min(1.0, max(0.0, Q + dt * (-d + v * V * (1 - Q)) + sig * np.sqrt(dt) * rng.normal()))
                if t_last is None and not present.any(): t_last = st * dt
            reps.append((Q, present.mean(), t_last))
        out[str(lm)] = dict(Q_end=float(np.mean([r[0] for r in reps])), members_end=float(np.mean([r[1] for r in reps])), t_all_exit=(float(np.mean([r[2] for r in reps])) if all(r[2] is not None for r in reps) else None))
    res = dict(d=d, v=v, recoverable=bool(v * (1 - th) > d), by_lam=out)
    return res, [chk("V1", "quality and membership in [0, 1]", out, all(0 <= o["Q_end"] <= 1 and 0 <= o["members_end"] <= 1 for o in out.values())),
                 chk("H1", P["h1_text"], out, bool(eval(P["h1_expr"], dict(o=out))), "hypothesis"),
                 chk("R1", "values", res, True, "reporting")]

def _hyps(P, res):
    return [chk(f"H{i}", t, res, bool(eval(e, dict(o=res, abs=abs, all=all, any=any, min=min, max=max, len=len))), "hypothesis") for i, (t, e) in enumerate(P["hyps"], 1)]

def betrayal_echo(P, rng):
    """Agent's toy of betrayal and repair in an iterated prisoner's dilemma (R 3, S 0, T 5, P 1): two players with the same strategy,
    one unprovoked defection by player 1 at round t0, optional execution errors e. Strategies: TFT (retaliation without forgiveness),
    GTFT (forgives a defection with probability q), CTFT (contrite: the betrayer accepts one round of punishment without retaliating,
    standing-based). Measures rounds until mutual cooperation is restored and the mean payoff per round. Hypothetical analogy to
    Royce's treason and atonement (P63)."""
    PAY = {(1, 1): 3, (1, 0): 0, (0, 1): 5, (0, 0): 1}
    def play(strat, q, e, T, t0, betray):
        last = [1, 1]; good = [True, True]; pay = 0.0; t_rest = None; broken = False
        for t in range(T):
            mv = []
            for i in (0, 1):
                j = 1 - i
                if strat == "TFT": m = last[j]
                elif strat == "GTFT": m = 1 if last[j] == 1 else int(rng.random() < q)
                else: m = 0 if (good[i] and not good[j]) else 1
                mv.append(m)
            if betray and t == t0: mv[0] = 0
            mv = [m if rng.random() >= e else 1 - m for m in mv]
            if strat == "CTFT":
                ng = [True, True]
                for i in (0, 1):
                    j = 1 - i; ng[i] = True if mv[i] == 1 else (good[i] and not good[j])
                good = ng
            pay += PAY[(mv[0], mv[1])]
            if t >= t0 and mv != [1, 1]: broken = True
            if broken and t_rest is None and t > t0 and mv == [1, 1]: t_rest = t - t0
            last = mv
        return pay / T, t_rest
    out = {}
    for lab, st in P["strategies"].items():
        r = [play(st["kind"], st.get("q", 0.0), P["e"], P["T"], P["t0"], True) for _ in range(P["reps"])]
        rest = [x[1] for x in r]; ok = [x for x in rest if x is not None]
        out[lab] = dict(mean_payoff=float(np.mean([x[0] for x in r])), frac_restored=len(ok) / len(rest), mean_rounds_to_restore=float(np.mean(ok)) if ok else None)
    base = {k: play(k, 0.1, 0.0, 50, 10, False)[0] for k in ("TFT", "GTFT", "CTFT")}
    return out, [chk("V1", "without betrayal or errors every strategy cooperates throughout (payoff 3)", base, all(abs(v - 3) < 1e-12 for v in base.values()))] + _hyps(P, out) + [chk("R1", "values", out, True, "reporting")]

def bayes_merge(P, rng):
    """Agent's toy of Peirce's convergence of inquiry (P72): Bayesian inquirers with different priors observe the same Bernoulli
    data. Beta-prior agents (full support) merge on the truth; a dogmatic agent whose prior excludes the truth converges to the
    nearest supported value, not the truth; for two observationally equivalent hypotheses (Peirce's 'buried secrets') posterior
    odds equal prior odds forever, so disagreement never shrinks."""
    th, Nn, cps = P["theta"], P["n_obs"], P["checkpoints"]; x = (rng.random(Nn) < th).astype(int); k = np.cumsum(x)
    beta = {}
    for name, (a, b) in P["beta_priors"].items():
        beta[name] = {str(c): round(float((a + k[c - 1]) / (a + b + c)), 6) for c in cps}
    spread = {str(c): round(max(v[str(c)] for v in beta.values()) - min(v[str(c)] for v in beta.values()), 6) for c in cps}
    sup = np.array(P["dogmatic_support"], float); lp = np.log(np.ones_like(sup) / len(sup))
    lk = k[-1] * np.log(sup) + (Nn - k[-1]) * np.log(1 - sup); post = np.exp(lp + lk - (lp + lk).max()); post /= post.sum()
    dog = dict(mean_end=round(float((post * sup).sum()), 6), mode=float(sup[int(np.argmax(post))]))
    odds = {name: round(float(o), 6) for name, o in P["equivalent_prior_odds"].items()}   # identical likelihoods: posterior odds = prior odds
    buried = dict(posterior_odds=odds, spread=round(max(odds.values()) - min(odds.values()), 6))
    grid = np.linspace(1e-6, 1 - 1e-6, 200001); a, b = list(P["beta_priors"].values())[0]; c = cps[-1]
    lpg = (a - 1 + k[c - 1]) * np.log(grid) + (b - 1 + c - k[c - 1]) * np.log(1 - grid); wgt = np.exp(lpg - lpg.max()); gm = float((grid * wgt).sum() / wgt.sum())
    res = dict(beta_means=beta, spread=spread, dogmatic=dog, buried=buried, freq_end=round(float(k[-1] / Nn), 6))
    ok = abs(gm - beta[list(beta)[0]][str(c)]) < 1e-5
    return res, [chk("V1", "conjugate Beta posterior mean equals a numerical grid posterior mean within 1e-5", [gm, beta[list(beta)[0]][str(c)]], ok)] + _hyps(P, res) + [chk("R1", "values", res, True, "reporting")]

def peirce_methods(P, rng):
    """Agent's toy of P75's velocity-of-light passage (Peirce 1878): m investigators use different methods with initial
    systematic biases b_i; 'as each perfects his method' bias and noise shrink by factors rho_i per round. Reports the spread of
    the investigators' estimates and the error of their mean over rounds. Variants: one method that never improves (rho = 1), and
    a bias shared by every method (c), which never shows up as disagreement."""
    th, R, cps = P["truth"], P["rounds"], P["checkpoints"]; b = np.array(P["biases"], float); rho = np.array(P.get("rho", [P.get("rho_all", 0.9)] * len(b)), float)
    s0, c = P.get("noise", 0.01), P.get("common_bias", 0.0); out = {}
    for t in range(R + 1):
        if t in cps:
            est = th * (1 + c + b * rho ** t + s0 * rho ** t * rng.standard_normal(len(b)))
            out[str(t)] = dict(spread_rel=round(float((est.max() - est.min()) / th), 6), mean_err_rel=round(float(abs(est.mean() - th) / th), 6))
    res = dict(rounds=out, common_bias=c)
    e0 = th * (1 + c + b); ok = abs(float((e0.max() - e0.min()) / th) - float(b.max() - b.min())) < 1e-12
    return res, [chk("V1", "noise-free spread at round 0 equals max(b) - min(b)", float((e0.max() - e0.min()) / th), ok)] + _hyps(P, res) + [chk("R1", "values", res, True, "reporting")]

def common_core(P, rng):
    """Agent's toy of P81's perennialist inference (Wikipedia 'Perennial philosophy'): perennialists argue that themes which
    developed independently of contact between cultures likely point to deeper truths; critics say similarities are
    overemphasised and the thesis is unfalsifiable. T traditions on a ring (contact network), F binary features.
    (a) Common core: every tradition copies each feature of one shared core with fidelity p_core, else draws it at random.
    (b) Diffusion: traditions start independent and random; for 'rounds' rounds, a random tradition copies one random feature
    from a ring neighbour (prob 1 - long) or from any tradition (prob long). Reports mean pairwise similarity (share of equal
    features) and its correlation with ring distance, for each model; matched means indicate that similarity alone does not
    discriminate the two histories, while a distance gradient does."""
    T, F, reps = P["T"], P["F"], P["reps"]
    dist = np.array([[min(abs(i - j), T - abs(i - j)) for j in range(T)] for i in range(T)]); iu = np.triu_indices(T, 1)
    def stats(X):
        S = (X[:, None, :] == X[None, :, :]).mean(2)[iu]; d = dist[iu]
        return float(S.mean()), float(np.corrcoef(S, d)[0, 1]) if S.std() > 0 else 0.0
    def core():
        c = rng.integers(0, 2, F); keep = rng.random((T, F)) < P["p_core"]; return np.where(keep, c, rng.integers(0, 2, (T, F)))
    def diff():
        X = rng.integers(0, 2, (T, F))
        for _ in range(P["rounds"]):
            i = rng.integers(T); f = rng.integers(F)
            j = rng.integers(T) if rng.random() < P.get("long", 0.0) else (i + rng.choice([-1, 1])) % T
            X[i, f] = X[j, f]
        return X
    out = {}
    for name, gen in [("core", core), ("diffusion", diff)]:
        ss = [stats(gen()) for _ in range(reps)]
        out[name] = dict(mean_sim=round(float(np.mean([s[0] for s in ss])), 5), sd_sim=round(float(np.std([s[0] for s in ss])), 5), corr_sim_dist=round(float(np.mean([s[1] for s in ss])), 4))
    res = dict(models=out, analytic_core_mean=round(float(P["p_core"] ** 2 + (1 - P["p_core"] ** 2) / 2), 5))
    return res, [chk("V1", "core model mean similarity within 0.01 of the analytic p^2 + (1 - p^2)/2", [out["core"]["mean_sim"], res["analytic_core_mean"]], abs(out["core"]["mean_sim"] - res["analytic_core_mean"]) < 0.01)] + _hyps(P, res) + [chk("R1", "values", res, True, "reporting")]

def stats_audit(P, rng):
    """Agent's recomputation of reported statistics from a paper's printed summaries (CVD: P83, Perry, Polito & Thompson 2021).
    Item types: t_pooled (two-sample t and Cohen's d from means, SDs, group sizes), t_welch (Welch t and df), p_F (p of an F
    statistic), p_chi2 (p of a chi-square), coef (t = B/SE and the 95% CI B +- t_crit SE), sum (sum of printed percentages),
    df_check (error df of a design versus the printed df), power_anova (power of a one-way ANOVA with k groups and N subjects
    for Cohen's f, and the f detectable with 80% power). Each item reports the recomputed value next to the printed one."""
    from scipy import stats
    from scipy.optimize import brentq
    out = {}
    for it in P["items"]:
        t = it["type"]; r = dict(type=t)
        if t == "t_pooled":
            n1, n2, m1, m2, s1, s2 = it["n1"], it["n2"], it["m1"], it["m2"], it["s1"], it["s2"]
            sp = np.sqrt(((n1 - 1) * s1 ** 2 + (n2 - 1) * s2 ** 2) / (n1 + n2 - 2)); tv = (m1 - m2) / (sp * np.sqrt(1 / n1 + 1 / n2))
            r.update(t=round(float(tv), 3), d=round(float((m1 - m2) / sp), 3), df=n1 + n2 - 2)
        elif t == "t_welch":
            n1, n2, m1, m2, s1, s2 = it["n1"], it["n2"], it["m1"], it["m2"], it["s1"], it["s2"]
            v1, v2 = s1 ** 2 / n1, s2 ** 2 / n2; tv = (m1 - m2) / np.sqrt(v1 + v2); df = (v1 + v2) ** 2 / (v1 ** 2 / (n1 - 1) + v2 ** 2 / (n2 - 1))
            r.update(t=round(float(tv), 3), df=round(float(df), 1))
        elif t == "p_F": r.update(p=round(float(stats.f.sf(it["F"], it["df1"], it["df2"])), 4))
        elif t == "p_chi2": r.update(p=round(float(stats.chi2.sf(it["chi2"], it["df"])), 4))
        elif t == "coef":
            tc = stats.t.ppf(0.975, it["df"]); r.update(t=round(it["B"] / it["SE"], 3), lo=round(it["B"] - tc * it["SE"], 3), hi=round(it["B"] + tc * it["SE"], 3))
        elif t == "sum": r.update(sum=round(float(sum(it["values"])), 3))
        elif t == "df_check": r.update(df_expected=int(it["N"] - it["cells"]))
        elif t == "power_anova":
            k, N, a = it["k"], it["N"], it.get("alpha", 0.05); fc = stats.f.ppf(1 - a, k - 1, N - k)
            pw = lambda f: float(stats.ncf.sf(fc, k - 1, N - k, f * f * N))
            r.update(power={str(f): round(pw(f), 4) for f in it.get("f_values", [0.1, 0.25])}, f80=round(float(brentq(lambda f: pw(f) - 0.8, 1e-4, 2.0)), 4))
        r["printed"] = it.get("printed"); out[it["name"]] = r
    from scipy import stats as _s
    v = float(_s.t.sf(1.96, 1e7) * 2)
    return dict(items=out), [chk("V1", "two-sided normal-limit p at t = 1.96 equals 0.05 within 1e-4", v, abs(v - 0.05) < 1e-4)] + _hyps(P, dict(items=out)) + [chk("R1", "values", dict(items=out), True, "reporting")]

def instrument_core(P, rng):
    """Agent's toy for P84's critique of P83-type evidence: T traditions, each subject's experience has D dimensions; the
    instrument measures only the first m ('core') dimensions, on which traditions share one mean; the other D - m dimensions
    have tradition-specific means (spread 'delta'). Reports one-way ANOVA p-values across traditions for the instrument total
    and for the unmeasured dimensions, over reps replicate studies with n subjects per tradition."""
    from scipy import stats
    T, D, m, n, reps, dl = P["T"], P["D"], P["m"], P["n"], P["reps"], P["delta"]
    sig_in, sig_out = 0, 0
    for _ in range(reps):
        mu = np.zeros((T, D)); mu[:, m:] = rng.normal(0, dl, (T, D - m))
        X = mu[:, None, :] + rng.standard_normal((T, n, D))
        tot = X[:, :, :m].sum(2); other = X[:, :, m:].sum(2)
        sig_in += stats.f_oneway(*tot).pvalue < 0.05; sig_out += stats.f_oneway(*other).pvalue < 0.05 if D > m else 0
    res = dict(frac_sig_instrument=round(sig_in / reps, 4), frac_sig_unmeasured=round(sig_out / reps, 4) if D > m else None)
    return res, [chk("V1", "with no tradition differences on the measured dimensions the instrument's false-positive rate is within 0.03 of 0.05", res["frac_sig_instrument"], abs(res["frac_sig_instrument"] - 0.05) < 0.03 + 3 * np.sqrt(0.0475 / reps))] + _hyps(P, res) + [chk("R1", "values", res, True, "reporting")]

def ascent_ladder(P, rng):
    """Agent's Hypothetical toy of the ascent in Diotima's speech as reported by P90 (Reeve, SEP 'Plato on Friendship and Eros'):
    incoherence 'encountered at lower stages in the ascent ... leads the correct lover ... to climb to the next stage'. Rungs
    k = 0..K-1 each cover a share c_k of the beautiful things met (c increasing to 1 at the top). Each encounter draws a thing;
    if the current rung does not cover it (an inconsistency), the lover climbs one rung with probability q (the 'rational desire
    for truth and consistency'); otherwise nothing changes. Reports the share reaching the top within n_max encounters and the
    mean encounters needed, against the analytic mean sum_k 1/(q (1 - c_k)) over the non-top rungs. Also reports the weight on
    the first beloved at the top under two readings P90 contrasts: 'kick the ladder away' (weight only on the top rung) and
    'valuing appropriately is still valuing' (weight spread over everything loved, first beloved = 1/n_total)."""
    c, reps, nmax = P["cover"], P["reps"], P["n_max"]; out = {}
    for q in P["q_values"]:
        steps = np.full(reps, -1)
        for r in range(reps):
            k, t = 0, 0
            while k < len(c) - 1 and t < nmax:
                t += 1
                if rng.random() > c[k] and rng.random() < q: k += 1
            if k == len(c) - 1: steps[r] = t
        done = steps >= 0
        an = float(sum(1 / (q * (1 - ck)) for ck in c[:-1])) if q > 0 else None
        out[str(q)] = dict(frac_top=round(float(done.mean()), 4), mean_steps=(round(float(steps[done].mean()), 3) if done.any() else None),
                           se=(round(float(steps[done].std(ddof=1) / np.sqrt(done.sum())), 3) if done.sum() > 1 else None), analytic_mean=(round(an, 3) if an else None))
    nt = P["n_total_loved"]; out_w = dict(kick=0.0, inclusive=round(1 / nt, 6))
    res = dict(by_q=out, first_beloved_weight=out_w)
    q1 = out[str(P["q_values"][0])]
    v = q1["mean_steps"] is not None and abs(q1["mean_steps"] - q1["analytic_mean"]) < 4 * q1["se"]
    return res, [chk("V1", "for the first q the simulated mean number of encounters to the top is within 4 SE of the analytic sum 1/(q(1 - c_k))", q1, bool(v))] + _hyps(P, res) + [chk("R1", "values", res, True, "reporting")]


def ascent_ladder2(P, rng):
    """ASA extension of ascent_ladder: a population of lovers whose disposition q is drawn from Beta(a, b) (q_dist) or fixed
    (q_fixed), with an optional fall-back probability r per encounter (moving down one rung when the current rung covers the case,
    a stand-in for P90's Alcibiades 'regressively' returning to the crowd). Reports the share reaching the top within n_max
    encounters, the mean rung reached, and the share still on the first rung."""
    c, reps, nmax, r = P["cover"], P["reps"], P["n_max"], P.get("r", 0.0)
    qs = rng.beta(*P["q_dist"], reps) if "q_dist" in P else np.full(reps, P["q_fixed"])
    top = len(c) - 1; k = np.zeros(reps, int); done = np.zeros(reps, bool)
    for t in range(nmax):
        act = ~done
        if not act.any(): break
        u = rng.random(reps); cov = u <= np.array(c)[k]
        up = act & ~cov & (rng.random(reps) < qs); dn = act & cov & (k > 0) & (rng.random(reps) < r)
        k = k + up - dn; done |= k == top
    res = dict(frac_top=round(float(done.mean()), 4), mean_rung=round(float(k.mean()), 3), frac_first_rung=round(float((k == 0).mean()), 4),
               mean_q_reached=(round(float(qs[done].mean()), 4) if done.any() else None), mean_q_not=(round(float(qs[~done].mean()), 4) if (~done).any() else None), se=round(float(np.sqrt(max(done.mean() * (1 - done.mean()), 1e-12) / reps)), 4))
    v = 0 <= res["frac_top"] <= 1 and (r > 0 or "q_dist" in P or True)
    return res, [chk("V1", "shares lie in [0, 1] and every lover's rung is between 0 and the top", [res["frac_top"], int(k.min()), int(k.max())], bool(v and k.min() >= 0 and k.max() <= top))] + _hyps(P, res) + [chk("R1", "values", res, True, "reporting")]


KINDS = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_') and k != 'chk' and getattr(v, '__module__', None) == '__main__'}

if __name__ == "__main__":
    P, H, t0 = R.start(sys.argv[1]); rng = np.random.default_rng(P["seed"])
    res, checks = KINDS[P["kind"]](P, rng); R.finish(H, P, res, checks, t0)
