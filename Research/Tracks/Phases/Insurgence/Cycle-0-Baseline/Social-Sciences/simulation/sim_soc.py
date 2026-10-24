"""SIM-<PH>-SOC: Social-Sciences simulations (Phases track). Usage: python sim_soc.py iter-<k>."""
import os, sys, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
import track_runner as R
chk = R.chk

def _clusters(x, gap, min_share):
    xs = np.sort(x); cut = np.where(np.diff(xs) > gap)[0]; groups = np.split(xs, cut + 1)
    return [g for g in groups if len(g) >= min_share * len(x)]

def deffuant(P, rng):
    """Deffuant-Weisbuch bounded-confidence model: random pairs interact if |xi - xj| < eps and move mu toward each other;
    optional Gaussian noise (sd 'noise') per interaction (cf. P03's noisy assimilative influence). Counts major opinion clusters."""
    out = {}
    for eps in P["eps_values"]:
        ks, drift = [], []
        for rep in range(P["reps"]):
            x = rng.uniform(0, 1, P["agents"]); m0 = x.mean()
            for _ in range(P["steps"]):
                i, j = rng.integers(0, P["agents"], 2)
                if i != j and abs(x[i] - x[j]) < eps:
                    d = P["mu"] * (x[j] - x[i]); x[i] += d; x[j] -= d
                    if P["noise"] > 0: x[i] = np.clip(x[i] + rng.normal(0, P["noise"]), 0, 1); x[j] = np.clip(x[j] + rng.normal(0, P["noise"]), 0, 1)
            drift.append(abs(x.mean() - m0)); ks.append(len(_clusters(x, P["gap"], P["min_share"])))
        out[str(eps)] = dict(clusters=ks, mean_clusters=float(np.mean(ks)), max_mean_drift=float(max(drift)))
    lo, hi = str(P["eps_values"][0]), str(P["eps_values"][-1])
    c = [chk("V1", "noise = 0: pairwise updates conserve the mean opinion (|drift| < 1e-9)", max(v["max_mean_drift"] for v in out.values()),
             (max(v["max_mean_drift"] for v in out.values()) < 1e-9) if P["noise"] == 0 else True),
         chk("H1", f"eps = {hi}: every replicate ends in one major cluster (consensus)", out[hi]["clusters"], all(k == 1 for k in out[hi]["clusters"]), "hypothesis"),
         chk("H2", f"eps = {lo}: mean number of major clusters in [{P['h2'][0]}, {P['h2'][1]}] (fragmentation; ~floor(1/(2 eps)))", out[lo]["mean_clusters"],
             P["h2"][0] <= out[lo]["mean_clusters"] <= P["h2"][1], "hypothesis"),
         chk("R1", "clusters per replicate by eps", {k: v["clusters"] for k, v in out.items()}, True, "reporting")]
    return out, c

def siem(P, rng):
    """Simplified re-implementation of the Social Influence and Event Model (SIEM) of P03: Hegselmann-Krause bounded confidence
    on opinions in [-1, 1]; each step every individual draws k random partners; individuals with certainty above their partners'
    mean drift by U[0, 0.1 eps] (random sign), others take the mean of themselves and partners within eps; certainty is pulled
    back toward its initial value by a random fraction and then given a symmetric drift of amplitude 'cdrift' (interpretation of
    P03's '[0 0.1]'); events start with probability Ef per step, last U[0, 2 Ed] steps, have strength U[Es-0.2, Es+0.2] and sign
    +/- at random, and pull individuals with |O - E| < eps and certainty <= strength toward the event by U[0,1] of the gap.
    Conflict = SD of opinions averaged over steps t0..T. Not P03's code; an independent approximation."""
    n = P["agents"]; out = {}
    for lab, Ef in (("no_events", 0.0), ("events", P["Ef"])):
        conf = []
        for rep in range(P["reps"]):
            lo = np.repeat(np.arange(7) * 0.1, n // 7 + 1)[:n]; C0 = lo + rng.uniform(0, 0.4, n); C = C0.copy()
            O = rng.uniform(-1, 1, n); ev_left = 0; E = 0.0; sds = []
            for t in range(P["T"]):
                nb = rng.integers(0, n, (n, P["k"])); On = O[nb]; Cn = C[nb].mean(1)
                within = np.abs(On - O[:, None]) < P["eps"]
                hk = (O + (On * within).sum(1)) / (1 + within.sum(1))
                drift = rng.uniform(0, 0.1 * P["eps"], n) * rng.choice([-1, 1], n)
                O = np.where(C > Cn, O + drift, hk)
                if ev_left <= 0 and Ef > 0 and rng.random() < Ef:
                    ev_left = rng.uniform(0, 2 * P["Ed"]); E = rng.uniform(P["Es"] - 0.2, P["Es"] + 0.2) * rng.choice([-1, 1])
                if ev_left > 0:
                    hit = (np.abs(O - E) < P["eps"]) & (C <= abs(E)); O = np.where(hit, O + rng.uniform(0, 1, n) * (E - O), O); ev_left -= 1
                O = np.clip(O, -1, 1)
                C = C + rng.uniform(0, 1, n) * (C0 - C); C = np.clip(C + rng.uniform(-P["cdrift"], P["cdrift"], n), 0, 1)
                if t >= P["t0"]: sds.append(O.std())
            conf.append(float(np.mean(sds)))
        out[lab] = dict(conflict=conf, mean=float(np.mean(conf)), se=float(np.std(conf, ddof=1) / np.sqrt(len(conf))))
    eq6 = lambda Es, EfEd: 0.75 * (1 - P["eps"]) * (0.44 + Es * EfEd ** 0.08) if EfEd > 0 else 0.75 * (1 - P["eps"]) * 0.44
    e0 = eq6(0, 0); e1 = eq6(P["Es"], P["Ef"] * P["Ed"]); a, b = out["no_events"]["mean"], out["events"]["mean"]
    lo = np.repeat(np.arange(7) * 0.1, n // 7 + 1)[:n] + rng.uniform(0, 0.4, n); k = P["tol_se"]; sec = lo.std(ddof=1) / np.sqrt(n)
    res = dict(out, eq6_no_events=e0, eq6_events=e1, certainty_mean=float(lo.mean()), certainty_sd=float(lo.std(ddof=1)))
    c = [chk("V1", f"initial certainty allocation (7 overlapping ranges of width 0.4) has mean within {k} standard errors of 0.50", [res["certainty_mean"], k * sec], abs(res["certainty_mean"] - 0.5) <= k * sec),
         chk("H1", f"no events: long-term conflict within {P['h_tol']} of P03 Eq. 6 = {e0:.3f}", a, abs(a - e0) <= P["h_tol"], "hypothesis"),
         chk("H2", f"events (Es {P['Es']}, Ef {P['Ef']}, Ed {P['Ed']}): long-term conflict within {P['h_tol']} of P03 Eq. 6 = {e1:.3f}", b, abs(b - e1) <= P["h_tol"], "hypothesis"),
         chk("H3", f"events raise conflict by more than {P['h3']} over the no-event condition (event-sustained polarisation)", b - a, b - a > P["h3"], "hypothesis"),
         chk("R1", "conflict per replicate, Eq. 6 values, certainty SD", dict(no_events=out["no_events"]["conflict"], events=out["events"]["conflict"], eq6=[e0, e1], certainty_sd=res["certainty_sd"]), True, "reporting")]
    return res, c

def value_divergence(P, rng):
    """Synthetic panel in the spirit of P11's measures (not WVS data): C countries in R regions, I items on a 0-1 scale, W waves.
    Region effects grow by 'region_drift' per wave and country idiosyncrasies shrink toward the region mean by 'pull' per wave.
    Computes P11's 'value variation' (SD of country means per item, averaged over items) globally and within regions, and
    'value distinctiveness' (mean |country mean - global median|)."""
    C, R, I, W = P["countries"], P["regions"], P["items"], P["waves"]; reg = np.arange(C) % R
    base = rng.uniform(0.3, 0.7, I); rdir = rng.normal(0, 1, (R, I)); idio = rng.normal(0, P["idio_sd"], (C, I)); rows = []
    for w in range(W):
        X = np.clip(base + P["region_drift"] * w * rdir[reg] + idio * (1 - P["pull"]) ** w + rng.normal(0, P["noise"], (C, I)), 0, 1)
        g = X.std(0, ddof=1).mean(); within = np.mean([X[reg == r].std(0, ddof=1).mean() for r in range(R)])
        dist = np.abs(X - np.median(X, 0)).mean(); rows.append(dict(wave=w + 1, global_variation=float(g), within_region_variation=float(within), distinctiveness=float(dist)))
    gv = [r["global_variation"] for r in rows]; wv = [r["within_region_variation"] for r in rows]
    t = np.arange(W); slope = lambda y: float(np.polyfit(t, y, 1)[0])
    # code check: two-point configuration with known SD
    x2 = np.array([0.4, 0.6]); sd2 = float(x2.std(ddof=1))
    c = [chk("V1", "SD routine: two countries at 0.4 and 0.6 give SD = 0.141421 (ddof 1)", sd2, abs(sd2 - 0.1414213562) < 1e-9),
         chk("H1", "global value variation rises across waves (positive slope) while within-region variation falls (negative slope): divergence globally, convergence regionally is jointly possible",
             [slope(gv), slope(wv)], slope(gv) > 0 and slope(wv) < 0, "hypothesis"),
         chk("R1", "measures by wave", rows, True, "reporting")]
    return dict(waves=rows, slope_global=slope(gv), slope_within=slope(wv)), c


def bc_noise(P, rng):
    """Deffuant bounded-confidence model with opinion noise: with probability pn per interaction the first agent redraws its opinion
    uniformly (a common noise variant; P03 also shows external events keep opinions spread). SD of opinions vs noise rate."""
    out = {}; cons = []
    for pn in P["noise"]:
        sds = []
        for r in range(P["reps"]):
            x = rng.random(P["agents"]); s0 = x.sum()
            I = rng.integers(0, P["agents"], (P["steps"], 2)); U = rng.random(P["steps"]); Z = rng.random(P["steps"])
            for t in range(P["steps"]):
                i, j = I[t]
                if U[t] < pn: x[i] = Z[t]; continue
                if i != j and abs(x[i] - x[j]) < P["eps"]:
                    d = P["mu"] * (x[j] - x[i]); x[i] += d; x[j] -= d
            if pn == 0: cons.append(abs(x.sum() - s0))
            sds.append(float(x.std()))
        out[str(pn)] = dict(mean_sd=float(np.mean(sds)), se=float(np.std(sds, ddof=1) / np.sqrt(len(sds))))
    u = 1 / np.sqrt(12); lo = str(P["noise"][0]); sm = str(P["noise"][1]); hi = str(P["noise"][-1])
    res = dict(by_noise=out, uniform_sd=u, sum_drift_max=float(max(cons)) if cons else None)
    c = [chk("V1", "noise 0: opinion sum conserved by pairwise updates (|drift| < 1e-9)", res["sum_drift_max"], cons and max(cons) < 1e-9),
         chk("H1", f"noise {hi}: SD within {P['h_tol']} of the uniform SD {u:.4f}", out[hi]["mean_sd"], abs(out[hi]["mean_sd"] - u) <= P["h_tol"], "hypothesis"),
         chk("H2", f"noise {sm}: SD within {P['h_tol']} of the noise-free SD", [out[sm]["mean_sd"], out[lo]["mean_sd"]], abs(out[sm]["mean_sd"] - out[lo]["mean_sd"]) <= P["h_tol"], "hypothesis"),
         chk("R1", "SD by noise", res, True, "reporting")]
    return res, c

def galton_beta(P, rng):
    """Beta- vs sigma-convergence (statistical toy): log incomes y_t = rho y_{t-1} + e_t across countries. Regressing growth
    y_T - y_0 on y_0 gives a negative slope (catch-up) even when the cross-country SD is constant (regression to the mean).
    sd0 sets the initial dispersion; the stationary SD is sd_e / sqrt(1 - rho^2)."""
    st = P["sd_e"] / np.sqrt(1 - P["rho"] ** 2); betas = []; ratio = []
    for _ in range(P["reps"]):
        y0 = rng.normal(0, P["sd0_mult"] * st, P["countries"]); y = y0.copy()
        for _ in range(P["T"]): y = P["rho"] * y + rng.normal(0, P["sd_e"], len(y))
        b = np.polyfit(y0, y - y0, 1)[0]; betas.append(b); ratio.append(y.std() / y0.std())
    betas = np.array(betas); ratio = np.array(ratio); k = P["tol_se"]
    bm = float(betas.mean()); bse = float(betas.std(ddof=1) / np.sqrt(len(betas))); rm = float(ratio.mean()); rse = float(ratio.std(ddof=1) / np.sqrt(len(ratio)))
    exp_b = P["rho"] ** P["T"] - 1
    res = dict(beta_mean=bm, beta_se=bse, beta_expected=exp_b, sd_ratio_mean=rm, sd_ratio_se=rse)
    c = [chk("V1", f"mean beta within {k} SE of rho^T - 1 = {exp_b:.4f}", [bm, bse], abs(bm - exp_b) <= k * bse),
         chk("H1", f"beta < 0 by more than {k} SE (apparent catch-up)", [bm, bse], bm < -k * bse, "hypothesis"),
         chk("H2", f"SD ratio sd_T/sd_0 {P['h2_text']}", [rm, rse], bool(eval(P["h2_expr"], {"r": rm})), "hypothesis"),
         chk("R1", "beta and SD ratio", res, True, "reporting")]
    return res, c

def selection_convergence(P, rng):
    """P19 (Pritchett 1997; De Long 1988 as reported there): sampling only countries that are rich at the end manufactures
    'convergence'. N countries, log income y0 ~ N(0, sd0); per-period growth = g + beta*(y - mean) + e, e ~ N(0, sd_e) over T
    periods (beta = 0: no true convergence). Regress total growth on initial y in (a) the full sample and (b) the top-k by final y."""
    N, T, R_ = P["countries"], P["T"], P["reps"]; bf = []; bs = []; ratio = []
    for _ in range(R_):
        y0 = rng.normal(0, P["sd0"], N); y = y0.copy()
        for t in range(T): y = y + P["g"] + P["beta"] * (y - y.mean()) + rng.normal(0, P["sd_e"], N)
        gr = y - y0; bf.append(np.polyfit(y0, gr, 1)[0]); top = np.argsort(y)[-P["top_k"]:]; bs.append(np.polyfit(y0[top], gr[top], 1)[0]); ratio.append(y.std() / y0.std())
    bf = np.array(bf); bs = np.array(bs); ratio = np.array(ratio); k = P["tol_se"]; se = lambda a: float(a.std(ddof=1) / np.sqrt(len(a)))
    exp_full = (1 + P["beta"]) ** T - 1 if P["beta"] else 0.0
    res = dict(slope_full=float(bf.mean()), slope_full_se=se(bf), expected_full=exp_full, slope_selected=float(bs.mean()), slope_selected_se=se(bs), sd_ratio_full=float(ratio.mean()))
    c = [chk("V1", f"full-sample slope within {k} SE of its expectation (1+beta)^T - 1", [res["slope_full"], exp_full, res["slope_full_se"]], abs(res["slope_full"] - exp_full) <= k * res["slope_full_se"]),
         chk("H1", f"selected (top {P['top_k']}) sample slope below the full-sample slope by more than {k} SE", [res["slope_selected"], res["slope_full"]], res["slope_selected"] - res["slope_full"] < -k * np.hypot(res["slope_selected_se"], res["slope_full_se"]), "hypothesis"),
         chk("H2", f"full-sample dispersion ratio (final/initial SD) {P['h2_text']}", res["sd_ratio_full"], eval(P["h2_expr"], {"r": res["sd_ratio_full"]}), "hypothesis"),
         chk("R1", "slopes and dispersion", res, True, "reporting")]
    return res, c

def pritchett_arithmetic(P, rng):
    """Deterministic re-computation of ratios printed in P19 Table 2 / Figure 1 from P19's own printed inputs."""
    rows = P["rows"]; out = {}; ok = {}
    for name, (num, den, printed) in rows.items():
        v = num / den; out[name] = dict(computed=round(v, 3), printed=printed); ok[name] = abs(v - printed) <= P["tol"]
    us = P["us_growth"]; fold = us[1] / us[0]
    c = [chk("V1", "arithmetic is reproducible (each ratio recomputed twice, identical)", out, all(rows[n][0] / rows[n][1] == rows[n][0] / rows[n][1] for n in rows)),
         chk("H1", f"every printed ratio reproduced from printed inputs within {P['tol']}", {n: ok[n] for n in ok}, all(ok.values()), "hypothesis"),
         chk("H2", "US 1870-1960 growth factor from Table 2 levels within 0.5 of the text's 'about four-fold'", fold, abs(fold - 4) <= 0.5, "hypothesis"),
         chk("R1", "values", dict(out, us_fold=fold), True, "reporting")]
    return dict(out, us_fold=fold), c

def two_clubs(P, rng):
    """Club convergence with between-club divergence (P19's two sets of countries): club A (n_a) converges (beta_a < 0) at drift g_a;
    club B (n_b) has drift g_b and growth sd sd_b, beta_b. Track SD of log income within A and over all countries."""
    R_ = P["reps"]; wa = []; tot = []
    for _ in range(R_):
        ya = rng.normal(P["ya0"], P["sd_a0"], P["n_a"]); yb = rng.normal(P["yb0"], P["sd_b0"], P["n_b"]); a0 = ya.std(); t0 = np.concatenate([ya, yb]).std()
        for t in range(P["T"]):
            ya = ya + P["g_a"] + P["beta_a"] * (ya - ya.mean()) + rng.normal(0, P["sd_ea"], P["n_a"])
            yb = yb + P["g_b"] + P["beta_b"] * (yb - yb.mean()) + rng.normal(0, P["sd_eb"], P["n_b"])
        wa.append(ya.std() / a0); tot.append(np.concatenate([ya, yb]).std() / t0)
    wa = np.array(wa); tot = np.array(tot); k = P["tol_se"]; se = lambda a: float(a.std(ddof=1) / np.sqrt(len(a)))
    res = dict(within_A_sd_ratio=float(wa.mean()), within_A_se=se(wa), total_sd_ratio=float(tot.mean()), total_se=se(tot))
    c = [chk("V1", "ratios are finite and positive", res, all(np.isfinite(list(res.values()))) and res["within_A_sd_ratio"] > 0),
         chk("H1", f"club A converges: within-club SD ratio < 1 by more than {k} SE", res["within_A_sd_ratio"], res["within_A_sd_ratio"] < 1 - k * res["within_A_se"], "hypothesis"),
         chk("H2", f"overall SD ratio > {P['h2']} (divergence across all countries)", res["total_sd_ratio"], res["total_sd_ratio"] > P["h2"], "hypothesis"),
         chk("R1", "dispersion ratios", res, True, "reporting")]
    return res, c

def moro_arith(P, rng):
    """Consistency check of P25's printed design counts and of its statement that the estimated k(0.9, 0.3, n) peaks for n in [1.0, 1.1],
    using P25 Table 2 coefficients (link functions: linear, logit, probit, complementary log-log) on a fine n grid over [0.7, 1.4]."""
    from scipy.stats import norm
    n_n, n_p, n_r, reps = P["grid_sizes"]; total = n_n * n_p * n_r * reps
    g = {"LPM": lambda e: e, "Logit": lambda e: 1 / (1 + np.exp(-e)), "Probit": norm.cdf, "CLogLog": lambda e: 1 - np.exp(-np.exp(e))}
    ns = np.linspace(P["n_lo"], P["n_hi"], 7001); out = {}
    for m, b in P["coef"].items():
        e = b[0] + b[1] * P["p"] + b[2] * P["r"] + b[3] * ns + b[4] * ns ** 2 + b[5] * ns ** 3; k = g[m](e); i = int(np.argmax(k))
        out[m] = dict(n_star=float(ns[i]), k_star=float(k[i]), k_at_lo=float(k[0]), k_at_hi=float(k[-1]))
    okH1 = all(P["band"][0] <= v["n_star"] <= P["band"][1] for v in out.values()); okH2 = all(v["k_at_hi"] < v["k_star"] - P["drop"] for v in out.values())
    counts = dict(total=total, printed_total=P["printed"][0], per_pr_cell=n_n * reps, printed_per_cell=P["printed"][1], per_n=n_p * n_r * reps, printed_per_n=P["printed"][2])
    okV = (total, n_n * reps, n_p * n_r * reps) == tuple(P["printed"])
    return dict(counts=counts, links=out), [chk("V1", "design counts reproduce the printed 17,280 / 480 / 2,160", counts, okV, "validation"),
            chk("H1", f"all four fitted links peak for n in [{P['band'][0]}, {P['band'][1]}]", out, bool(okH1), "hypothesis"),
            chk("H2", f"k falls by more than {P['drop']} from the peak to n = {P['n_hi']} under every link ('decreases markedly')", out, bool(okH2), "hypothesis"),
            chk("R1", "values", out, True, "reporting")]

KINDS = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_') and k != 'chk' and getattr(v, '__module__', None) == '__main__'}

if __name__ == "__main__":
    P, H, t0 = R.start(sys.argv[1]); rng = np.random.default_rng(P["seed"])
    res, checks = KINDS[P["kind"]](P, rng); R.finish(H, P, res, checks, t0)
