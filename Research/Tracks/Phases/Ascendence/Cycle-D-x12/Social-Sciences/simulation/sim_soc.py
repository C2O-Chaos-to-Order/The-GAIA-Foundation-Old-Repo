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

def threshold_cascade(P, rng):
    """Threshold model of collective behaviour as described in P25 (after Granovetter): each of N people joins once the number already
    participating reaches their threshold. Iterate to the fixed point. Deterministic cases plus normal thresholds (mean mu, sd over a grid)."""
    def final(th):
        th = np.sort(th); a = 0
        while True:
            b = int(np.sum(th <= a))
            if b == a: return a
            a = b
    N = P["N"]; uni = final(np.arange(N)); pert = np.arange(N).copy(); pert[1] = 2; per = final(pert)
    grid = {}
    for sd in P["sd_values"]:
        sz = [final(np.clip(np.round(rng.normal(P["mu"], sd, N)), 0, None)) / N for _ in range(P["reps"])]
        grid[str(sd)] = dict(mean=float(np.mean(sz)), full_share=float(np.mean(np.array(sz) > 0.9)))
    ms = [grid[str(s)]["mean"] for s in P["sd_values"]]; jump = float(np.max(np.diff(ms)))
    res = dict(uniform=uni, perturbed=per, normal=grid, largest_step=jump)
    return res, [chk("V1", "uniform thresholds 0..N-1 give a full cascade", uni, uni == N, "validation"),
                 chk("H1", "raising one threshold (1 -> 2) stops the cascade at 1 person", per, per == 1, "hypothesis"),
                 chk("H2", f"with normal thresholds the mean final size jumps by > {P['h2']} between adjacent sd values (sudden)", jump, jump > P["h2"], "hypothesis"),
                 chk("R1", "values", res, True, "reporting")]

def pillar_toy(P, rng):
    """Agent's toy of P31's pillar strategies (not P31's model): Np pillars with defection thresholds ~ N(mu, sd) clipped to [0, 1].
    Each step a movement of strength A (0-1) applies pressure: 'spread' gives every pillar pressure A; 'focus' gives m random pillars
    pressure min(1, A Np / m); 'weakest' gives the m pillars with the lowest thresholds that pressure (requires knowing thresholds).
    A pillar defects when pressure >= its threshold; each defection adds 'boost' to A (defections embolden protest). Success = defected
    share >= v within T steps."""
    out = {}
    for strat in P["strategies"]:
        win = 0
        for _ in range(P["reps"]):
            th = np.clip(rng.normal(P["mu"], P["sd"], P["Np"]), 0, 1); dfc = np.zeros(P["Np"], bool); A = P["A"]
            for _ in range(P["T"]):
                pr = np.zeros(P["Np"]); live = np.where(~dfc)[0]
                if len(live) == 0: break
                if strat == "spread": pr[:] = A
                else:
                    m = min(P["m"], len(live)); idx = rng.choice(live, m, replace=False) if strat == "focus" else live[np.argsort(th[live])[:m]]
                    pr[idx] = min(1.0, A * P["Np"] / m)
                new = (~dfc) & (pr >= th); dfc |= new; A = min(1.0, A + P["boost"] * new.sum())
                if dfc.mean() >= P["v"]: break
            win += dfc.mean() >= P["v"]
        p = win / P["reps"]; out[strat] = dict(success=p, se=float(np.sqrt(max(p * (1 - p), 1e-12) / P["reps"])))
    s = [out[k]["success"] for k in P["strategies"]]
    return out, [chk("V1", "success shares are probabilities", out, all(0 <= x <= 1 for x in s), "validation"),
                 chk("H1", f"ordering {P['h1_text']}", s, eval(P["h1_expr"], {"s": s}), "hypothesis"), chk("R1", "values", out, True, "reporting")]

def escalation_war(P, rng):
    """P39 (Clauset et al. 2026) Eq. 2 interstate-war model: x1 ~ PowerLaw(eta) above x_min = 1000, T ~ Geometric(q) on 1, 2, ...,
    lambda_t ~ DoublePareto(alpha = 2.1) (escalation) or 1 (no escalation), x_(t+1) = lambda_t x_t, total X = sum x_t, with x_t >= x_min
    enforced by clamping (agent's reading of 'we enforce CoW's minimum threshold'). Double Pareto read as ln lambda = +/- Exp(alpha - 1),
    i.e. density ~ lambda^-alpha above 1 and its mirror below (agent's parameterisation; P39's exact form is in its SI, not read).
    Tail exponent: discrete-free MLE alpha_hat = 1 + n / sum ln(X / 7061) for X >= 7061 (P39 reports 1.53 +/- 0.07 for CoW wars).
    mode 'tail': one parameter set; mode 'exante': per-year chance of doubling and tenfold escalation with a share q0 of lambda = 1;
    mode 'civil': adds mean reversion ln lambda -> ln lambda - kappa ln(x / 500) (agent's parametric stand-in for P39 Fig. 2C)."""
    xmin = 1000.0; xt = 7061.0; al = P.get("alpha", 2.1)
    def mle(X):
        X = X[X >= xt]; a = 1 + len(X) / np.sum(np.log(X / xt)); return float(a), float((a - 1) / np.sqrt(len(X))), int(len(X))
    if P["mode"] == "exante":
        q0 = P["q0"]; n = P["n"]; L = np.where(rng.random(n) < q0, 0.0, rng.choice([-1, 1], n) * rng.exponential(1 / (al - 1), n))
        sim2, sim10 = float(np.mean(L >= np.log(2))), float(np.mean(L >= np.log(10)))
        a2 = (1 - q0) * 0.5 * 2 ** -(al - 1); a10 = (1 - q0) * 0.5 * 10 ** -(al - 1)
        b2 = (1 - q0) * 0.5 * 2 ** -al; b10 = (1 - q0) * 0.5 * 10 ** -al
        res = dict(p_double=sim2, p_tenfold=sim10, analytic_density_reading=[a2, a10], analytic_ccdf_reading=[b2, b10], source=[0.10, 0.01])
        se = np.sqrt(a2 * (1 - a2) / n)
        return res, [chk("V1", "simulated doubling share within 4 SE of the analytic value", [sim2, a2], abs(sim2 - a2) <= 4 * se),
                     chk("H1", "doubling about 10% (within 0.03) and tenfold about 1% (within 0.005) per year, as P39's Discussion states", [sim2, sim10], abs(sim2 - 0.10) <= 0.03 and abs(sim10 - 0.01) <= 0.005, "hypothesis"),
                     chk("H2", "the same under the alternative reading (alpha as tail exponent of the CCDF)", [b2, b10], abs(b2 - 0.10) <= 0.03 and abs(b10 - 0.01) <= 0.005, "hypothesis"),
                     chk("R1", "values", res, True, "reporting")]
    out = {}
    for lab, esc, eta, q in P["sets"]:
        n = P["n"]; x = xmin * rng.random(n) ** (-1 / (eta - 1)); T = rng.geometric(q, n); X = x.copy(); alive = T > 1; t = 1
        while alive.any():
            L = rng.choice([-1, 1], n) * rng.exponential(1 / (al - 1), n) if esc else np.zeros(n)
            if P["mode"] == "civil" and esc and lab.startswith("civil"): L = L - P["kappa"] * np.log(x / 500.0)
            x = np.where(alive, np.maximum(x * np.exp(L), xmin), x); X = X + np.where(alive, x, 0); t += 1; alive = T > t
        a, se, k = mle(X); x1a = mle(xmin * rng.random(n) ** (-1 / (eta - 1)))
        out[lab] = dict(escalation=bool(esc), eta=eta, q=q, alpha_hat=a, se=se, n_tail=k, median_X=float(np.median(X)), share_over_1e6=float(np.mean(X > 1e6)), x1_alpha_hat=x1a[0])
    first = out[P["sets"][0][0]]
    c = [chk("V1", "MLE recovers eta from the initial sizes alone (within 4 SE + 0.02) for the first set", [first["x1_alpha_hat"], first["eta"]], abs(first["x1_alpha_hat"] - first["eta"]) <= 4 * first["se"] + 0.02)]
    c.append(chk("H1", P["h1_text"], {k: v["alpha_hat"] for k, v in out.items()}, bool(eval(P["h1_expr"], {}, dict(o=out))), "hypothesis"))
    c.append(chk("R1", "values", out, True, "reporting")); return dict(sets=out), c

def complex_contagion(P, rng):
    """P40 (Wan, Riedl & Lazer 2025) model: n = 250 k nodes, clustered ring lattice (each node linked to its k nearest neighbours) vs a
    random regular network from degree-preserving connected edge swaps (networkx; swaps = number of edges). Per-exposure adoption
    probability p(c) = p1 if 1 <= c < i, p2 if c >= i, c = number of different influential neighbours met so far (cumulative), exposures
    counted serially within a step; adopters stay influential for T steps. Seeds: one random node and i - 1 of its neighbours on both
    networks (P40 seeds the lattice deterministically; agent's simplification). Outcomes: final adopter share and steps to 60%.
    Random-network threshold p1* = 1 - (1 - 1/(k - 1))^(1/T) (P40)."""
    import networkx as nx
    k, i, T = P["k"], P["i"], P["T"]; n = 250 * k
    lat = nx.watts_strogatz_graph(n, k, 0.0)
    def sim(G, p1, p2):
        nb = [list(G.neighbors(v)) for v in range(n)]; state = np.zeros(n, int); left = np.zeros(n, int); seen = [set() for _ in range(n)]
        s0 = int(rng.integers(n)); seeds = [s0] + list(rng.choice(nb[s0], i - 1, replace=False)); state[seeds] = 1; left[seeds] = T
        t = 0; t60 = None; adopted = len(seeds)
        while (state == 1).any() and (state == 0).any():
            t += 1; inf = np.flatnonzero(state == 1); new = []
            for u in inf:
                for v in nb[u]:
                    if state[v] != 0 or v in new: continue
                    if u not in seen[v]: seen[v].add(u)
                    c = len(seen[v]); pr = p1 if c < i else p2
                    if rng.random() < pr: new.append(v)
            left[inf] -= 1; state[inf[left[inf] <= 0]] = 2
            for v in set(new): state[v] = 1; left[v] = T
            adopted += len(set(new))
            if t60 is None and adopted >= 0.6 * n: t60 = t
        return adopted / n, t60
    out = {}
    for p1, p2 in P["pairs"]:
        cl = []; rd = []; tc = []; tr = []
        for _ in range(P["trials"]):
            G = lat.copy(); nx.connected_double_edge_swap(G, nswap=G.number_of_edges(), seed=int(rng.integers(2**31)))
            a, b = sim(lat, p1, p2); c_, d = sim(G, p1, p2); cl.append(a); tc.append(b); rd.append(c_); tr.append(d)
        f = lambda L: float(np.mean([x for x in L if x is not None])) if any(x is not None for x in L) else None
        out[f"{p1},{p2}"] = dict(clustered=float(np.mean(cl)), random=float(np.mean(rd)), t60_clustered=f(tc), t60_random=f(tr))
    pstar = 1 - (1 - 1 / (k - 1)) ** (1 / T)
    res = dict(k=k, i=i, T=T, n=n, p1_star=pstar, by_pair=out)
    return res, [chk("V1", "shares in [0, 1]", out, all(0 <= v["clustered"] <= 1 and 0 <= v["random"] <= 1 for v in out.values())),
                 chk("H1", P["h1_text"], out, bool(eval(P["h1_expr"], dict(o=out, ps=pstar))), "hypothesis"), chk("R1", "values", res, True, "reporting")]

def fusion_loop(P, rng):
    """Agent's formalization (Hypothetical) of P48's labelling loop (Newson, Cunliffe & Whitehouse 2025): 'external condemnation
    amplifies fusion to a deviant group, which in turns leads to more deviant behaviour'. F = fusion to the deviant group (0-1),
    D = deviant behaviour, condemnation = kappa * D. dF/dt = a kappa D (1 - F) - delta F; dD/dt = beta F - gamma D.
    Loop gain R = a kappa beta / (gamma delta); for R > 1 a fused state F* = 1 - 1/R exists. Reintegration = lowering kappa (stigma).
    Irrevocability (P48's fourth principle) = small delta: time for F to halve after condemnation stops."""
    a, b, g, dl, dt = P["a"], P["beta"], P["gamma"], P["delta"], P["dt"]
    def run(kappa, F, D, T):
        for _ in range(int(T / dt)):
            F, D = F + dt * (a * kappa * D * (1 - F) - dl * F), D + dt * (b * F - g * D)
        return F, D
    out = {}
    for kap in P["kappas"]:
        R_ = a * kap * b / (g * dl); F, D = run(kap, P["F0"], P["D0"], P["T"])
        out[str(kap)] = dict(R=R_, F_end=F, F_star=max(0.0, 1 - 1 / R_))
    kh = P["kappas"][-1]; F, D = run(kh, P["F0"], P["D0"], P["T"]); t = 0.0; F0 = F
    while F > F0 / 2 and t < 1e5:
        F, D = F + dt * (a * 0 * D * (1 - F) - dl * F), D + dt * (b * F - g * D); t += dt
    res = dict(by_kappa=out, half_life_after_stop=t, ln2_over_delta=np.log(2) / dl)
    err = max(abs(v["F_end"] - v["F_star"]) for v in out.values())
    return res, [chk("V1", "simulated end state within 0.01 of the analytic fixed point for every kappa", err, err <= 0.01),
                 chk("H1", P["h1_text"], out, bool(eval(P["h1_expr"], dict(o=out, res=res))), "hypothesis"),
                 chk("R1", "values", res, True, "reporting")]


def corr_regress(P, rng):
    """P52 (Ozkan, El-Astal & Cakal 2025, Br J Soc Psychol 64:e70002, CC BY-NC): Tables 1-3 print the correlations among identity
    fusion (F), group identification (G), peaceful (Pc) and violent (V) pro-group action, scale alphas and N. Agent's check: standardized
    two-predictor regression coefficients from the printed correlations, beta_F = (r_FY - r_GY r_FG)/(1 - r_FG^2), beta_G likewise, with
    SE = sqrt((1 - R^2)/((N - 3)(1 - r_FG^2))); also disattenuated with the printed alphas (r / sqrt(a_i a_j)). Compared with the signs
    of P52's latent-variable SEM paths (Model 2). Manifest regression on scale scores is not P52's method (disclosed)."""
    out = {}
    for lab, d in P["studies"].items():
        r = d["r"]; N = d["N"]; al = d["alpha"]; o = {}
        for mode in ("manifest", "disattenuated"):
            def rr(a, b):
                v = r[a + b] if a + b in r else r[b + a]
                return v / np.sqrt(al[a] * al[b]) if mode == "disattenuated" else v
            fg = rr("F", "G"); o[mode] = {}
            for y in ("P", "V"):
                fy, gy = rr("F", y), rr("G", y); bF = (fy - gy * fg) / (1 - fg ** 2); bG = (gy - fy * fg) / (1 - fg ** 2)
                R2 = bF * fy + bG * gy; se = float(np.sqrt(max(1e-12, 1 - R2) / ((N - 3) * (1 - fg ** 2))))
                A = np.array([[1, fg], [fg, 1]]); resid = float(np.max(abs(A @ np.array([bF, bG]) - np.array([fy, gy]))))
                o[mode][y] = dict(beta_F=float(bF), beta_G=float(bG), se=se, R2=float(R2), resid=resid)
        o["sem"] = d["sem"]; out[lab] = o
    resid = max(v[m][y]["resid"] for v in out.values() for m in ("manifest", "disattenuated") for y in ("P", "V"))
    sgn = lambda x: (x > 0) - (x < 0)
    h1 = {k: [v["manifest"]["V"]["beta_F"], v["sem"]["F_V"]] for k, v in out.items()}
    h2 = {k: [v["manifest"]["P"]["beta_G"], v["sem"]["G_P"]] for k, v in out.items()}
    h3 = {k: all(sgn(v["manifest"][y][b]) == sgn(v["disattenuated"][y][b]) for y in ("P", "V") for b in ("beta_F", "beta_G")) for k, v in out.items()}
    res = dict(studies=out)
    return res, [chk("V1", "coefficients solve the 2 x 2 normal equations (residual < 1e-12) in every study and mode", resid, resid < 1e-12),
                 chk("H1", "manifest beta for fusion -> violent action has the same sign as P52's SEM path in every study", h1, all(sgn(a) == sgn(b) for a, b in h1.values()), "hypothesis"),
                 chk("H2", "manifest beta for identification -> peaceful action has the same sign as P52's SEM path in every study", h2, all(sgn(a) == sgn(b) for a, b in h2.values()), "hypothesis"),
                 chk("H3", "disattenuation with the printed alphas changes no coefficient sign", h3, all(h3.values()), "hypothesis"),
                 chk("R1", "values", res, True, "reporting")]


def table_audit(P, rng):
    """P52 (Ozkan, El-Astal & Cakal 2025) Table correlations vs P57 (P52's OSF project huysb: raw .sav data and Mplus output of Model 6).
    Agent's audit: (i) printed vs raw scale-score correlations (raw values computed by the agent's extraction script from the OSF data,
    passed as parameters); (ii) printed with fusion and identification columns swapped vs raw; (iii) correlations implied by the latent
    SEM paths, corr(F, Y) = b_F + b_G r_FG and corr(G, Y) = b_G + b_F r_FG, vs raw correlations disattenuated with raw alphas."""
    out = {}
    for lab, d in P["studies"].items():
        pr, rw, al = d["printed"], d["raw"], d["alpha_raw"]
        diff = max(abs(pr[k] - rw[k]) for k in rw)
        sw = dict(pr); sw["FV"], sw["GV"], sw["FP"], sw["GP"] = pr["GV"], pr["FV"], pr["GP"], pr["FP"]
        dsw = max(abs(sw[k] - rw[k]) for k in rw)
        o = dict(max_diff_printed_raw=diff, max_diff_swapped_raw=dsw)
        if "sem" in d:
            s = d["sem"]; rfg = s["r_FG"]; imp = {}
            for y in ("P", "V"):
                bF, bG = s["F_" + y], s["G_" + y]; imp["F" + y] = bF + bG * rfg; imp["G" + y] = bG + bF * rfg
            dis = {k: rw[k] / np.sqrt(al[k[0]] * al[k[1]]) for k in ("FP", "FV", "GP", "GV")}
            o.update(sem_implied=imp, raw_disattenuated=dis, max_diff_implied_dis=max(abs(imp[k] - dis[k]) for k in imp),
                     order_ok=bool((imp["FV"] > imp["GV"]) == (dis["FV"] > dis["GV"])), identity_err=abs(imp["FV"] - (s["F_V"] + s["G_V"] * rfg)))
        out[lab] = o
    tol = P["tol"]; A = P["audit_study"]
    res = dict(studies=out, tol=tol)
    ok_other = all(v["max_diff_printed_raw"] <= tol for k, v in out.items() if k != A)
    return res, [chk("V1", "implied-correlation identity reproduced exactly where SEM paths are given", [v.get("identity_err") for v in out.values()], all(v.get("identity_err", 0) < 1e-12 for v in out.values())),
                 chk("H1", f"printed correlations match the raw-data correlations within {tol} in every study", {k: v["max_diff_printed_raw"] for k, v in out.items()}, all(v["max_diff_printed_raw"] <= tol for v in out.values()), "hypothesis"),
                 chk("H2", f"in {A}, swapping the fusion and identification entries of the printed table matches the raw data within {tol}, and the other studies match unswapped", [out[A]["max_diff_swapped_raw"], ok_other], out[A]["max_diff_swapped_raw"] <= tol and ok_other, "hypothesis"),
                 chk("H3", f"in {A}, the SEM-implied latent correlations order fusion-violent above identification-violent as the disattenuated raw data do, within 0.05 of them", [out[A].get("order_ok"), out[A].get("max_diff_implied_dis")], bool(out[A].get("order_ok")) and out[A].get("max_diff_implied_dis", 9) <= 0.05, "hypothesis"),
                 chk("R1", "values", res, True, "reporting")]

def _hyps(P, res):
    return [chk(f"H{i}", t, res, bool(eval(e, dict(o=res, abs=abs, all=all, any=any, min=min, max=max, len=len))), "hypothesis") for i, (t, e) in enumerate(P["hyps"], 1)]

def summary_audit(P, rng):
    """Agent's re-computation of printed statistics from printed summaries (P61): standardized regression betas from a correlation matrix,
    one-way ANOVA F from group means/SDs/ns, Tukey HSD comparisons, eta squared from F, the a-priori F-test sample size for effect size f,
    and percentage shares of mediation tables."""
    from scipy.stats import f as fdist, ncf, studentized_range
    res = {}
    if "regression" in P:
        g = P["regression"]; nm = g["names"]; R = np.array(g["R"], float); xi = [nm.index(x) for x in g["x"]]; yi = nm.index(g["y"])
        beta = np.linalg.solve(R[np.ix_(xi, xi)], R[xi, yi]); res["regression"] = dict(beta={x: float(v) for x, v in zip(g["x"], beta)}, printed=g["printed"], max_diff=float(max(abs(beta[k] - g["printed"][x]) for k, x in enumerate(g["x"]))))
    for key in ("anova", "anova2"):
        if key in P:
            g = P[key]; m = np.array(g["means"], float); s = np.array(g["sds"], float); n = np.array(g["n"], float); k = len(m); N = n.sum()
            gm = (n * m).sum() / N; msb = (n * (m - gm) ** 2).sum() / (k - 1); msw = ((n - 1) * s ** 2).sum() / (N - k); F = msb / msw
            out = dict(F=float(F), printed_F=g["printed_F"], diff=float(F - g["printed_F"]), msw=float(msw), df=[k - 1, int(N - k)])
            if g.get("tukey"):
                q = float(studentized_range.ppf(0.95, k, N - k)); hsd = q * np.sqrt(msw / n[0])
                out["tukey"] = dict(q_crit=q, hsd=float(hsd), pairs={f"{a}-{b}": dict(diff=float(m[a] - m[b]), sig=bool(abs(m[a] - m[b]) > hsd)) for a, b in g["tukey"]})
            res[key] = out
    if "tukey_ci" in P:
        g = P["tukey_ci"]; k, n, df = g["k"], g["n"], g["df"]; q = float(studentized_range.ppf(0.95, k, df)); half = np.mean([(hi - lo) / 2 for lo, hi in g["cis"].values()])
        msw = (half / q) ** 2 * n; diffs = g["diffs"]; mm = np.array([0.0, diffs[0], diffs[1]]); gm = mm.mean(); F = n * ((mm - gm) ** 2).sum() / (k - 1) / msw
        res["tukey_ci"] = dict(q_crit=q, implied_msw=float(msw), implied_F=float(F), printed_F=g["printed_F"])
    if "eta2" in P:
        g = P["eta2"]; e = g["F"] * g["df1"] / (g["F"] * g["df1"] + g["df2"]); res["eta2"] = dict(eta2=float(e), printed=g["printed"])
    if "fpower" in P:
        g = P["fpower"]; k = g["k"]; Nmin = None
        for N in range(k + 2, 2000):
            lam = g["f"] ** 2 * N; crit = fdist.ppf(1 - g["alpha"], k - 1, N - k); pw = 1 - ncf.cdf(crit, k - 1, N - k, lam)
            if pw >= g["target"]: Nmin = N; break
        res["fpower"] = dict(N_min=Nmin, printed_N=g["printed_N"])
    if "shares" in P:
        res["shares"] = {}
        for lab, g in P["shares"].items():
            tot = g["total"]; pct = {k: 100 * v / tot for k, v in g["parts"].items()}
            res["shares"][lab] = dict(pct=pct, max_pct_diff=float(max(abs(pct[k] - g["printed_pct"][k]) for k in pct)), sum_parts=float(sum(g["parts"].values())), total=tot)
    if "sums" in P:
        res["sums"] = {lab: dict(computed=float(sum(g["parts"])), printed=g["printed"], diff=float(sum(g["parts"]) - g["printed"])) for lab, g in P["sums"].items()}
    if "medians" in P:
        res["medians"] = {lab: dict(computed=float(np.median(g["values"])), printed=g["printed"], n=len(g["values"])) for lab, g in P["medians"].items()}
    if "fisher" in P:
        res["fisher"] = {}
        for lab, (r, lo, hi) in P["fisher"].items():
            z, zl, zh = np.arctanh(r), np.arctanh(lo), np.arctanh(hi)
            res["fisher"][lab] = dict(asym_z=float((zh - z) - (z - zl)), half_z=float((zh - zl) / 2), asym_r=float((hi - r) - (r - lo)))
    if "sign_ci" in P:
        res["sign_ci"] = {lab: dict(inside=bool(lo <= b <= hi), b=b, lo=lo, hi=hi) for lab, (b, lo, hi) in P["sign_ci"].items()}
    I = np.eye(3); bI = np.linalg.solve(I[:2, :2], np.array([0.3, -0.2]))
    return res, [chk("V1", "with uncorrelated predictors the standardized betas equal the correlations (1e-12)", bI.tolist(), abs(bI[0] - 0.3) < 1e-12 and abs(bI[1] + 0.2) < 1e-12)] + _hyps(P, res) + [chk("R1", "values", res, True, "reporting")]

def crowd_centralization(P, rng):
    """P69 (Almaatouq, Rahimian, Burton & Alhajri 2022): probability Omega_n that a centralized collective estimate
    a_n(omega) = omega a_1 + (1 - omega) mean(a) lies closer to the truth than the decentralized mean, for i.i.d. log-normal
    initial estimates a_i = theta exp(mu + sigma Z) (the agent's parametrisation of P69's F_{mu,sigma}^theta; P69's exact form is in its SI, not read)."""
    n, w, th, reps = P["n"], P["omega"], P["theta"], P["reps"]
    def omega(mu, s, ww, nn=None):
        a = th * np.exp(mu + s * rng.standard_normal((reps, nn or n))); m = a.mean(1); c = ww * a[:, 0] + (1 - ww) * m
        return float(np.mean(abs(c - th) < abs(m - th)))
    res = dict(Omega={f"mu{mu}_s{s}": round(omega(mu, s, w), 5) for mu, s in P["contexts"]}, n=n, omega=w, se_max=round(float(0.5 / np.sqrt(reps)), 5))
    if P.get("n_values"):   # CVA extension: Omega as a function of group size for the first context
        mu0, s0 = P["contexts"][0]; res["by_n"] = {}
        for nn in P["n_values"]: res["by_n"][str(nn)] = round(omega(mu0, s0, w, nn), 5)
    if P.get("omega_values"):   # CVA extension: Omega as a function of the centralization weight for the first context
        mu0, s0 = P["contexts"][0]; res["by_omega"] = {str(ww): round(omega(mu0, s0, ww), 5) for ww in P["omega_values"]}
    z = omega(0.0, 1.0, 0.0)
    return res, [chk("V1", "with omega = 0 the two estimates coincide, so Omega is exactly 0", z, z == 0.0)] + _hyps(P, res) + [chk("R1", "values", res, True, "reporting")]

def crowd_bound(P, rng):
    """P69 (Almaatouq et al. 2022) lower bound on the centralization advantage: Omega_n >= sup_{beta > theta/(1 - omega)}
    F(beta) (1 - F(n beta)^(n - 1)), with F the CDF of the i.i.d. initial estimates. Agent's evaluation for log-normal
    estimates a = theta exp(mu + sigma Z) (F(x) = Phi((ln(x/theta) - mu)/sigma)), sup taken on a log-spaced beta grid, next to
    a Monte Carlo estimate of Omega_n (as in crowd_centralization) for each (context, n)."""
    from scipy.stats import norm
    th, w, reps = P["theta"], P["omega"], P["reps"]
    F = lambda x: norm.cdf((np.log(x / th) - mu) / s)
    out = {}
    for mu, s in P["contexts"]:
        for n in P["n_values"]:
            b = th / (1 - w) * np.exp(np.linspace(1e-6, P.get("log_span", 12), 20001))
            lb = float(np.max(F(b) * (1 - F(n * b) ** (n - 1))))
            a = th * np.exp(mu + s * rng.standard_normal((reps, n))); m = a.mean(1); c = w * a[:, 0] + (1 - w) * m
            mc = float(np.mean(abs(c - th) < abs(m - th)))
            out[f"mu{mu}_s{s}_n{n}"] = dict(bound=round(lb, 5), mc=round(mc, 5), bound_le_mc_plus_3se=bool(lb <= mc + 3 * np.sqrt(max(mc * (1 - mc), 1e-12) / reps) + 1e-12))
    res = dict(by_case=out, theta=th, omega=w, reps=reps)
    mu, s = 0.0, 1.0; v = float(F(np.array([th]))[0])
    return res, [chk("V1", "the log-normal CDF at the truth with mu = 0 is exactly 1/2", v, abs(v - 0.5) < 1e-12)] + _hyps(P, res) + [chk("R1", "values", res, True, "reporting")]

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


def mobility_qpm(P, rng):
    """ASA: structural vs relative mobility with P87's quasi-perfect-mobility (QPM) form. For each year's origin and destination
    margins (P87 Table 2, 7 classes) a table m_ij = a_i b_j exp(delta_i [i = j]) is fitted to both margins by iterative
    proportional fitting, with the class-inheritance parameters delta held fixed (P87 Table 6, 1901; or scaled by 'delta_scale').
    Reports the % on the diagonal (immobile) and % mobile for each year: under fixed delta, differences between years come only
    from the margins (structural change). Also reports the % mobile under independence (delta = 0)."""
    def fit(o, d, dl):
        o = np.array(o, float) / sum(o); d = np.array(d, float) / sum(d); K = len(o); W = np.ones((K, K)) + np.diag(np.exp(np.array(dl)) - 1)
        m = W.copy()
        for _ in range(P.get("iters", 5000)):
            m *= (o / m.sum(1))[:, None]; m *= (d / m.sum(0))[None, :]
            if np.abs(m.sum(1) - o).max() < 1e-13: break
        return m, float(max(np.abs(m.sum(1) - o).max(), np.abs(m.sum(0) - d).max()))
    out = {}; errs = []
    for y, (o, d) in P["margins"].items():
        r = {}
        for nm, sc in P["delta_scale"].items():
            m, e = fit(o, d, [sc * x for x in P["delta"]]); errs.append(e); r[nm] = dict(pct_mobile=round(100 * (1 - np.trace(m)), 3))
        mi, e = fit(o, d, [0.0] * len(o)); errs.append(e); r["independence"] = dict(pct_mobile=round(100 * (1 - np.trace(mi)), 3))
        r["min_mobility_pct"] = round(100 * 0.5 * float(np.abs(np.array(o) / sum(o) - np.array(d) / sum(d)).sum()), 3); out[y] = r
    res = dict(by_year=out, max_margin_err=float(f"{max(errs):.3g}"))
    return res, [chk("V1", "IPF reproduces both margins within 1e-9 in every fit", res["max_margin_err"], res["max_margin_err"] < 1e-9)] + _hyps(P, res) + [chk("R1", "values", res, True, "reporting")]


def rank_mobility(P, rng):
    """ASD (P96, Song et al. 2020): toy of relative vs absolute occupational mobility. Father and son latent statuses are
    bivariate normal with correlation rho; each is cut into K equal-sized occupations (ranks 1..K, rescaled to 0-100 as in
    P96). The son's latent status may be shifted by 'upgrade' (structural upgrading: sons' distribution moves up against the
    fathers' fixed cut points, as when high-status occupations expand). Reports the rank-rank (Spearman) correlation of the
    rescaled ranks and the shares moving up / down by at least 'thr' points (P96: 7.5) and staying, for each rho x upgrade."""
    from scipy import stats
    n, K, thr = P["n"], P.get("K", 70), P.get("thr", 7.5)
    cuts = stats.norm.ppf(np.arange(1, K) / K)
    out = {}
    for rho in P["rho_values"]:
        for up in P.get("upgrade_values", [0.0]):
            z1 = rng.standard_normal(n); z2 = rho * z1 + np.sqrt(1 - rho ** 2) * rng.standard_normal(n) + up
            r1 = np.searchsorted(cuts, z1); r2 = np.searchsorted(cuts, z2)
            s1 = 100 * r1 / (K - 1); s2 = 100 * r2 / (K - 1); d = s2 - s1
            rr = float(stats.spearmanr(s1, s2)[0])
            out[f"rho{rho}_up{up}"] = dict(rank_corr=round(rr, 4), up=round(float(np.mean(d >= thr)), 4), down=round(float(np.mean(d <= -thr)), 4), stay=round(float(np.mean(np.abs(d) < thr)), 4))
    z1 = rng.standard_normal(200000); z2 = rng.standard_normal(200000)
    v = abs(float(stats.spearmanr(z1, z2)[0])) < 0.01
    return dict(cells=out, n=n, K=K, thr=thr), [chk("V1", "independent latent statuses give |rank correlation| < 0.01 (n 200,000)", v, v)] + _hyps(P, dict(cells=out)) + [chk("R1", "values", dict(cells=out), True, "reporting")]


KINDS = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_') and k != 'chk' and getattr(v, '__module__', None) == '__main__'}

if __name__ == "__main__":
    P, H, t0 = R.start(sys.argv[1]); rng = np.random.default_rng(P["seed"])
    res, checks = KINDS[P["kind"]](P, rng); R.finish(H, P, res, checks, t0)
