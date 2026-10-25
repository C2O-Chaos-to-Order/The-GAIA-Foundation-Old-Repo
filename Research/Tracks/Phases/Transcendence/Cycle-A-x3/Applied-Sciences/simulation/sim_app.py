"""SIM-<PH>-APP: Applied-Sciences simulations (Phases track). Usage: python sim_app.py iter-<k>."""
import os, sys, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
import track_runner as R
chk = R.chk

def clonal_branching(P, rng):
    """Neutral (or selective) birth-death growth from one cell to N cells; each daughter gains Poisson(u) new mutations
    (infinite sites). Mutation tree kept as nodes; cell fraction of each mutation = descendant cells / N.
    Tests the neutral-growth prediction M(f) ~ a (1/f - 1/fmax) for subclonal mutations (cf. P05's neutral-evolution simulation)."""
    parent = [-1]; nmut = [0]; cells = [0]; fit = [1.0]; total = 0
    while 0 < len(cells) < P["N"]:
        k = rng.integers(len(cells)); f = fit[cells[k]]
        b = P["birth"] * f; d = P["death"]
        if rng.random() < b / (b + d):
            node = cells[k]; new = []
            for _ in range(2):
                km = rng.poisson(P["u"])
                if km:
                    parent.append(node); nmut.append(km); total += km
                    fit.append(fit[node] * (1 + P["s"]) if rng.random() < P["p_driver"] else fit[node]); new.append(len(parent) - 1)
                else: new.append(node)
            cells[k] = new[0]; cells.append(new[1])
        else:
            cells[k] = cells[-1]; cells.pop()
    n = len(cells); cnt = np.bincount(cells, minlength=len(parent)).astype(float)
    for i in range(len(parent) - 1, 0, -1): cnt[parent[i]] += cnt[i]
    freq = cnt / max(n, 1); fr = np.repeat(freq[1:], nmut[1:])
    fgrid = np.linspace(P["fmin"], P["fmax"], 12); M = np.array([(fr >= f).sum() for f in fgrid]); X = 1 / fgrid - 1 / P["fmax"]
    a, b0 = np.polyfit(X, M, 1); pred = a * X + b0; r2 = 1 - ((M - pred) ** 2).sum() / max(((M - M.mean()) ** 2).sum(), 1e-12)
    res = dict(final_cells=n, total_mutations=int(total), bookkeeping=int(sum(nmut)), clonal=int((fr >= 0.99).sum()),
               subclonal_in_window=int(((fr >= P["fmin"]) & (fr < P["fmax"])).sum()), M=M.tolist(), r2=float(r2), slope=float(a), mean_mut_per_cell=float(np.repeat(freq[1:], nmut[1:]).sum()))
    c = [chk("V1", "population reached N (no extinction) and mutation bookkeeping is exact", [n, int(total), int(sum(nmut))], n == P["N"] and total == sum(nmut)),
         chk("H1", f"cumulative subclonal mutations M(f) is linear in 1/f on [{P['fmin']}, {P['fmax']}] with R^2 >= {P['h1']}", float(r2), r2 >= P["h1"], "hypothesis"),
         chk("R1", "slope a (estimates mutation rate / effective division ratio) and clonal count", [float(a), res["clonal"]], True, "reporting")]
    return res, c

def _clonal_once(P, rng):
    parent = [-1]; nmut = [0]; cells = [0]; total = 0
    while 0 < len(cells) < P["N"]:
        k = rng.integers(len(cells))
        if rng.random() < P["birth"] / (P["birth"] + P["death"]):
            node = cells[k]; new = []
            for _ in range(2):
                km = rng.poisson(P["u"])
                if km: parent.append(node); nmut.append(km); total += km; new.append(len(parent) - 1)
                else: new.append(node)
            cells[k] = new[0]; cells.append(new[1])
        else:
            cells[k] = cells[-1]; cells.pop()
    n = len(cells)
    if n == 0: return None
    cnt = np.bincount(cells, minlength=len(parent)).astype(float)
    for i in range(len(parent) - 1, 0, -1): cnt[parent[i]] += cnt[i]
    fr = np.repeat(cnt[1:] / n, nmut[1:])
    fgrid = np.linspace(P["fmin"], P["fmax"], 12); M = np.array([(fr >= f).sum() for f in fgrid]); X = 1 / fgrid - 1 / P["fmax"]
    a, b0 = np.polyfit(X, M, 1); pred = a * X + b0; r2 = 1 - ((M - pred) ** 2).sum() / max(((M - M.mean()) ** 2).sum(), 1e-12)
    return dict(n=n, total=int(total), book=int(sum(nmut)), r2=float(r2), slope=float(a))

def clonal_branching_reps(P, rng):
    """Replicates of the neutral clonal_branching model of DV0 (birth-death growth from one cell to N cells, Poisson(u) new
    mutations per daughter, infinite sites; cf. P05's neutral-evolution simulation). Reports the distribution of R^2 of the
    M(f) ~ 1/f fit across replicates (extinct runs are restarted and counted)."""
    runs = []; extinct = 0
    while len(runs) < P["reps"]:
        r = _clonal_once(P, rng)
        if r is None: extinct += 1; continue
        runs.append(r)
    r2 = np.array([r["r2"] for r in runs]); ok = all(r["n"] == P["N"] and r["total"] == r["book"] for r in runs)
    res = dict(r2=r2.tolist(), median_r2=float(np.median(r2)), min_r2=float(r2.min()), frac_ge_h1=float((r2 >= P["h1"]).mean()), slopes=[r["slope"] for r in runs], extinct_restarts=extinct)
    c = [chk("V1", "every replicate reached N cells and mutation bookkeeping is exact", ok, ok),
         chk("H1", f"median R^2 of the M(f) ~ 1/f fit across {P['reps']} replicates >= {P['h1']}", res["median_r2"], res["median_r2"] >= P["h1"], "hypothesis"),
         chk("R1", "R^2 per replicate, slopes, extinct restarts", [res["r2"], res["slopes"], extinct], True, "reporting")]
    return res, c

def euler_stability(P, rng):
    """Numerical divergence of an iterative solver: explicit Euler on y' = -lam y, y(0) = 1, step h. The iteration
    y_{n+1} = (1 - h lam) y_n converges to 0 iff |1 - h lam| < 1 (0 < h lam < 2) and diverges if h lam > 2. Deterministic."""
    out = {}
    for hl in P["hlam"]:
        y = 1.0; traj = []
        for k in range(P["steps"]): y = (1 - hl) * y; traj.append(abs(y))
        out[str(hl)] = dict(final_abs=float(abs(y)), factor=float(abs(1 - hl)), max_abs=float(max(traj)))
    s = [str(x) for x in P["hlam"]]; conv = [k for k in s if float(k) < 2]; div = [k for k in s if float(k) > 2]
    exact = all(abs(out[k]["final_abs"] - abs(1 - float(k)) ** P["steps"]) <= 1e-9 * max(1.0, abs(1 - float(k)) ** P["steps"]) for k in s)
    c = [chk("V1", "final |y| equals |1 - h lam|^steps for every h lam (relative error <= 1e-9)", exact, exact),
         chk("V2", "h lam < 2: |y| -> 0 (final < 1e-6); h lam > 2: |y| grows (final > 1e6)", {k: out[k]["final_abs"] for k in s},
             all(out[k]["final_abs"] < 1e-6 for k in conv) and all(out[k]["final_abs"] > 1e6 for k in div)),
         chk("R1", "amplification factor by h lam", {k: out[k]["factor"] for k in s}, True, "reporting")]
    return out, c


def bep_drivers(P, rng):
    """Clone-based branching growth (a toy in the spirit of P05's branching-evolution model, not its code): each birth adds
    Poisson(u) new mutations; each new mutation is a driver with probability q, multiplying birth probability by (1 + sd).
    At size N, every mutation's cancer-cell fraction (CCF) is computed. Driver share among high-CCF vs low-CCF mutations."""
    hi = [0, 0]; lo = [0, 0]; mut_tot = 0; births_tot = 0; reps = 0
    while reps < P["reps"]:
        cnt = [1]; par = [-1]; kd = [0]; nm = [0]; nd = [0]
        while 0 < sum(cnt) < P["N"]:
            C = np.array(cnt); pb = np.minimum(P["b0"] * (1 + P["sd"]) ** np.array(kd), 0.95); B = rng.binomial(C, pb); Dd = rng.binomial(C - B, P["d0"]); newc = C + B - Dd
            idx = np.repeat(np.arange(len(C)), B); M = rng.poisson(P["u"], len(idx)); births_tot += len(idx); mut_tot += int(M.sum())
            for j, m in zip(idx[M > 0], M[M > 0]):
                newc[j] -= 1; d = rng.binomial(m, P["q"]); cnt.append(1); par.append(int(j)); kd.append(kd[j] + d); nm.append(int(m)); nd.append(int(d))
            cnt[:len(newc)] = [int(v) for v in newc]
        if sum(cnt) == 0: continue
        reps += 1; tot = np.array(cnt, float)
        for i in range(len(cnt) - 1, 0, -1): tot[par[i]] += tot[i]
        ccf = tot / sum(cnt)
        for i in range(1, len(cnt)):
            if ccf[i] >= P["hi"]: hi[0] += nd[i]; hi[1] += nm[i]
            elif P["lo_min"] <= ccf[i] < P["lo_max"]: lo[0] += nd[i]; lo[1] += nm[i]
    sh = hi[0] / max(hi[1], 1); sl = lo[0] / max(lo[1], 1); urate = mut_tot / births_tot; use = np.sqrt(P["u"] / births_tot); k = P["tol_se"]
    se_diff = np.sqrt(sh * (1 - sh) / max(hi[1], 1) + sl * (1 - sl) / max(lo[1], 1))
    res = dict(high_ccf=dict(drivers=hi[0], mutations=hi[1], share=sh), low_ccf=dict(drivers=lo[0], mutations=lo[1], share=sl), mutations_per_birth=urate, births=births_tot)
    if P["h1_mode"] == "enrich":
        h1 = chk("H1", f"driver share among CCF >= {P['hi']} mutations at least {P['h1']}x the share among {P['lo_min']} <= CCF < {P['lo_max']}", [sh, sl], sh >= P["h1"] * sl and hi[1] > 0, "hypothesis")
    else:
        h1 = chk("H1", f"no enrichment: |share_high - share_low| <= {k} SE (binomial)", [sh, sl, float(se_diff)], abs(sh - sl) <= k * se_diff, "hypothesis")
    c = [chk("V1", f"mean new mutations per birth within {k} SE of u = {P['u']}", [urate, float(use)], abs(urate - P["u"]) <= k * use), h1,
         chk("R1", "driver shares by CCF class", res, True, "reporting")]
    return res, c

def euler_sho(P, rng):
    """P17: forward Euler on the simple harmonic oscillator multiplies the amplitude by |1 + i h w| = sqrt(1 + h^2 w^2) per step,
    so the numerical solution always grows. Compared with semi-implicit (symplectic) Euler, which stays bounded."""
    w = P["omega"]; out = {}
    for h in P["h_values"]:
        n = int(round(P["periods"] * 2 * np.pi / (w * h))); u, v = 0.0, 1.0; us, vs = 0.0, 1.0; amax = 0.0
        for _ in range(n):
            u, v = u - h * w * w * v, v + h * u
            us = us - h * w * w * vs; vs = vs + h * us; amax = max(amax, abs(np.hypot(us / w, vs) - 1))
        amp = float(np.hypot(u / w, v)); pred = (1 + h * h * w * w) ** (n / 2)
        out[str(h)] = dict(steps=n, amp_forward=amp, amp_predicted=float(pred), rel_err=float(abs(amp / pred - 1)), symplectic_max_dev=float(amax))
    hs = str(P["h_values"][-1]); hl = str(P["h_values"][0])
    c = [chk("V1", "forward Euler amplitude equals (1 + h^2 w^2)^(n/2) within relative 1e-9 at every h", [out[k]["rel_err"] for k in out], all(out[k]["rel_err"] <= 1e-9 for k in out)),
         chk("H1", f"forward Euler grows by more than {P['h1']:.0%} over {P['periods']} periods even at the smallest h = {hs}", out[hs]["amp_forward"] - 1, out[hs]["amp_forward"] - 1 > P["h1"], "hypothesis"),
         chk("H2", f"symplectic Euler amplitude stays within {P['h2']:.0%} of 1 at h = {hl}", out[hl]["symplectic_max_dev"], out[hl]["symplectic_max_dev"] <= P["h2"], "hypothesis"),
         chk("R1", "amplitudes by h", out, True, "reporting")]
    return out, c

def euler_order(P, rng):
    """P17: forward Euler RMS (global) error on dy/dt = a y scales as O(h): slope one on a log-log plot."""
    a = P["a"]; errs = []; exact_ok = True
    for h in P["h_values"]:
        n = int(round(P["T"] / h)); t = h * np.arange(n + 1); y = P["y0"] * (1 + a * h) ** np.arange(n + 1)
        yy = [P["y0"]]
        for _ in range(n): yy.append(yy[-1] + h * a * yy[-1])
        exact_ok &= bool(np.allclose(yy, y, rtol=1e-10, atol=0))
        errs.append(float(np.sqrt(np.mean((P["y0"] * np.exp(a * t) - y) ** 2))))
    slope = float(np.polyfit(np.log(P["h_values"]), np.log(errs), 1)[0])
    res = dict(rms_errors=dict(zip(map(str, P["h_values"]), errs)), loglog_slope=slope)
    c = [chk("V1", "iterated forward Euler equals the closed form y0 (1 + a h)^n (rtol 1e-10)", exact_ok, exact_ok),
         chk("H1", f"log-log slope of RMS error vs h within {P['h1']} of 1 (P17 fig. 2.4)", slope, abs(slope - 1) <= P["h1"], "hypothesis"),
         chk("R1", "errors and slope", res, True, "reporting")]
    return res, c

def bep_drivers_pooled(P, rng):
    """Same model as bep_drivers; the no-enrichment control test uses a pooled two-proportion SE, which stays positive when one
    observed share is zero (fixes the DVB iter-2 test-design flaw, decided before this run)."""
    res, c = bep_drivers(dict(P, h1_mode="enrich"), rng)
    hi, lo = res["high_ccf"], res["low_ccf"]; k = P["tol_se"]; n1, n2 = max(hi["mutations"], 1), max(lo["mutations"], 1)
    pp = (hi["drivers"] + lo["drivers"]) / (n1 + n2); se = float(np.sqrt(pp * (1 - pp) * (1 / n1 + 1 / n2))); res["pooled_se"] = se
    if P["h1_mode"] == "null":
        h1 = chk("H1", f"no enrichment: |share_high - share_low| <= {k} pooled SE", [hi["share"], lo["share"], se], abs(hi["share"] - lo["share"]) <= k * se, "hypothesis")
    else:
        h1 = chk("H1", f"enrichment: share_high - share_low > {k} pooled SE", [hi["share"], lo["share"], se], hi["share"] - lo["share"] > k * se, "hypothesis")
    return res, [c[0], h1, chk("R1", "driver shares by CCF class", res, True, "reporting")]

def fluency_arith(P, rng):
    """Consistency check of P24's printed conversions between response time and fluency in a 10-min task (600 s),
    assuming a constant response rate as P24 states. rows: label -> [seconds per response, printed responses per 600 s]."""
    out = {}; ok = True
    for k, (s, printed) in P["rows"].items():
        f = P["window"] / s; out[k] = dict(sec=s, computed=round(f, 3), printed=printed, diff=round(f - printed, 3)); ok &= abs(f - printed) <= P["tol"]
    back = P["window"] / P["reverse"][0]; out["reverse"] = dict(responses=P["reverse"][0], computed_sec=back, printed_sec=P["reverse"][1])
    ex = {k: dict(total=v[0], exploration=v[1], rest=v[0] - v[1]) for k, v in P["phases"].items()}; out["phases"] = ex
    faster_expl = min(ex, key=lambda k: ex[k]["exploration"]); faster_total = min(ex, key=lambda k: ex[k]["total"])
    return out, [chk("V1", "arithmetic computed for every printed row", out, True, "validation"),
                 chk("H1", f"every printed fluency within {P['tol']} of 600/s", out, bool(ok), "hypothesis"),
                 chk("H2", "reverse conversion exact (600/responses = printed seconds)", out["reverse"], abs(back - P["reverse"][1]) < 1e-9, "hypothesis"),
                 chk("H3", "fluency ranking reverses when only Exploration time is used", [faster_total, faster_expl], faster_total != faster_expl, "hypothesis"),
                 chk("R1", "values", out, True, "reporting")]

def fluency_confound(P, rng):
    """Agent's toy of P24's fluency-dependency: person i has fluency F_i ~ Poisson(lambda_i) (lambda_i lognormal) and
    true originality mu_i; each response's uncommonness u = logistic(mu_i + N(0, sd_item)). Summative score = sum u;
    average score = mean u. corr(log lambda, mu) = rho."""
    k = P["tol_se"]; R_ = []
    for _ in range(P["reps"]):
        z1 = rng.standard_normal(P["n"]); z2 = P["rho"] * z1 + np.sqrt(1 - P["rho"] ** 2) * rng.standard_normal(P["n"])
        lam = P["lam_mean"] * np.exp(P["sdlog"] * z1 - P["sdlog"] ** 2 / 2); mu = P["sd_mu"] * z2
        F = np.maximum(rng.poisson(lam), 1)
        s = np.array([(1 / (1 + np.exp(-(mu[i] + P["sd_item"] * rng.standard_normal(F[i]))))).sum() for i in range(P["n"])])
        a = s / F; lo = F <= np.median(F); hi = ~lo
        R_.append([np.corrcoef(s, F)[0, 1], np.corrcoef(a, F)[0, 1], np.corrcoef(a, mu)[0, 1], np.corrcoef(a[lo], mu[lo])[0, 1], np.corrcoef(a[hi], mu[hi])[0, 1], np.corrcoef(mu, F)[0, 1]])
    R_ = np.array(R_); m = R_.mean(0); se = R_.std(0, ddof=1) / np.sqrt(len(R_))
    res = dict(corr_sum_fluency=m[0], corr_avg_fluency=m[1], corr_avg_mu=m[2], corr_avg_mu_lowF=m[3], corr_avg_mu_highF=m[4], corr_mu_fluency=m[5], se=se.tolist())
    d = R_[:, 4] - R_[:, 3]; dse = d.std(ddof=1) / np.sqrt(len(d))
    return res, [chk("V1", f"corr(average, fluency) within {k} SE of corr(mu, fluency)", [m[1], m[5], se[1]], abs(m[1] - m[5]) <= k * max(se[1], 1e-9) + 0.02, "validation"),
                 chk("H1", f"corr(summative, fluency) > {P['h1']}", m[0], m[0] > P["h1"], "hypothesis"),
                 chk("H2", f"average score tracks true originality worse in the low-fluency half (difference > {k} SE)", [m[3], m[4], dse], d.mean() > k * dse, "hypothesis"),
                 chk("R1", "correlations", res, True, "reporting")]

def serial_order(P, rng):
    """Agent's mechanism toy for the serial-order effect P24 reports (response rate falls, originality rises across responses):
    ideas k = 1..K have accessibility w_k = k^-a; a person retrieves ideas without replacement, each next idea chosen with
    probability proportional to w among those left, waiting time Exp(rate = c * remaining w). Uncommonness of idea k = k/K."""
    k_ = P["tol_se"]; K = P["K"]; w0 = np.arange(1, K + 1) ** (-P["a"]); n = P["responses"]
    O = np.zeros((P["persons"], n)); W = np.zeros((P["persons"], n))
    for p in range(P["persons"]):
        w = w0.copy()
        for j in range(n):
            tot = w.sum(); W[p, j] = rng.exponential(1 / (P["c"] * tot)); i = rng.choice(K, p=w / tot); O[p, j] = (i + 1) / K; w[i] = 0
    order = np.arange(1, n + 1); so = np.array([np.polyfit(order, O[p], 1)[0] for p in range(P["persons"])])
    h = n // 2; dw = W[:, h:].mean(1) - W[:, :h].mean(1)
    res = dict(mean_uncommonness_first=O[:, 0].mean(), mean_uncommonness_last=O[:, -1].mean(), slope=so.mean(), slope_se=so.std(ddof=1) / np.sqrt(len(so)),
               wait_first_half=W[:, :h].mean(), wait_second_half=W[:, h:].mean(), wait_diff_se=dw.std(ddof=1) / np.sqrt(len(dw)))
    return res, [chk("V1", "uncommonness in (0, 1] and waits positive", res, bool((O > 0).all() and (O <= 1).all() and (W > 0).all()), "validation"),
                 chk("H1", f"uncommonness rises with response order (mean slope > {k_} SE)", [res["slope"], res["slope_se"]], res["slope"] > k_ * res["slope_se"], "hypothesis"),
                 chk("H2", f"waits longer in the second half (difference > {k_} SE)", [dw.mean(), res["wait_diff_se"]], dw.mean() > k_ * res["wait_diff_se"], "hypothesis"),
                 chk("R1", "values", res, True, "reporting")]

def mtci_growth(P, rng):
    """Agent's toy of P24's MTCI 'originality cost': person exploration time on trial t = b0_i + b1_i*t + c_i*u_t + noise,
    u_t = uncommonness of the trial's response in [0, 1]. OLS per person recovers c_i (P24 proposes the model; no data in P24)."""
    k = P["tol_se"]; T = P["trials"]; t = np.arange(T)
    b0 = P["b0"] + P["sd_b0"] * rng.standard_normal(P["persons"]); b1 = P["b1"] + P["sd_b1"] * rng.standard_normal(P["persons"]); c = P["c"] + P["sd_c"] * rng.standard_normal(P["persons"])
    est = []
    for i in range(P["persons"]):
        u = rng.uniform(0, 1, T); y = b0[i] + b1[i] * t + c[i] * u + P["noise"] * rng.standard_normal(T)
        X = np.column_stack([np.ones(T), t, u]); est.append(np.linalg.lstsq(X, y, rcond=None)[0][2])
    est = np.array(est); bias = est.mean() - c.mean(); se = (est - c).std(ddof=1) / np.sqrt(len(est)); r = np.corrcoef(est, c)[0, 1]
    res = dict(mean_true_c=c.mean(), mean_est_c=est.mean(), bias=bias, se=se, corr_est_true=r)
    return res, [chk("V1", f"mean estimate unbiased within {k} SE", [bias, se], abs(bias) <= k * se, "validation"),
                 chk("H1", f"per-person estimates correlate with true cost > {P['h1']}", r, r > P["h1"], "hypothesis"),
                 chk("R1", "values", res, True, "reporting")]

def branching_outbreak(P, rng):
    """Galton-Watson outbreak from one case with Poisson(R0) secondary cases (agent's model of P26's threshold statement). A 'major'
    outbreak reaches K cumulative cases. Analytic major-outbreak probability = 1 - q, q = exp(R0 (q - 1)). Generation time Tg sets
    calendar speed only: time to K cases is recorded for two Tg values with the same R0 (P26: R0 is not a rate)."""
    k = P["tol_se"]; out = {}; okV = True; okH1 = True
    for R0 in P["R0"]:
        q = 0.0; m_ = R0 * (1 - P.get("v", 0.0))
        for _ in range(5000): q = np.exp(m_ * (q - 1)) if P.get("k") is None else (1 + m_ * (1 - q) / P["k"]) ** (-P["k"])
        maj = 0; gens = []
        for _ in range(P["reps"]):
            z, tot, g = 1, 1, 0
            while 0 < z and tot < P["K"]:
                m = R0 * (1 - P.get("v", 0.0))
                z = int(rng.poisson(m * z)) if P.get("k") is None else int(rng.poisson(rng.gamma(P["k"], m / P["k"], z)).sum()); tot += z; g += 1
            if tot >= P["K"]: maj += 1; gens.append(g)
        ph = maj / P["reps"]; se = np.sqrt(max(ph * (1 - ph), 1e-12) / P["reps"]); an = 1 - q if R0 * (1 - P.get("v", 0.0)) > 1 else 0.0
        out[str(R0)] = dict(p_major=ph, se=se, analytic=an, mean_generations_to_K=float(np.mean(gens)) if gens else None,
                            days_to_K={str(T): (float(np.mean(gens)) * T if gens else None) for T in P["Tg"]})
        okV &= abs(ph - an) <= k * se + 0.002
        if R0 * (1 - P.get("v", 0.0)) < 1: okH1 &= ph == 0.0
    sup = [r for r in P["R0"] if r * (1 - P.get("v", 0.0)) > 1] or list(P["R0"]); d = out[str(sup[0])]["days_to_K"]; T0, T1 = [str(t) for t in P["Tg"]]
    return out, [chk("V1", f"major-outbreak share within {k} SE (+0.002) of 1 - q", out, bool(okV), "validation"),
                 chk("H1", "no major outbreak when the reproduction number R0 (1 - v) < 1", {r: out[str(r)]["p_major"] for r in P["R0"] if r * (1 - P.get("v", 0.0)) < 1}, bool(okH1), "hypothesis"),
                 chk("H2", f"same R0, different generation time: same outbreak probability, calendar time scales by {P['Tg'][1]}/{P['Tg'][0]}", d, (d[T0] is not None and abs(d[T1] / d[T0] - P["Tg"][1] / P["Tg"][0]) < 1e-9), "hypothesis"),
                 chk("R1", "values", out, True, "reporting")]

def offspring_profile(P, rng):
    """Negative-binomial offspring (mean m, dispersion k; P32's fit m = 0.88, k = 0.27): share with zero secondary cases, share with > 5,
    and the smallest share of index cases producing 80% of secondary cases, over samples of n index cases (P32: 67%, 3%, 17%)."""
    z0, z5, t80 = [], [], []
    for _ in range(P["reps"]):
        x = rng.poisson(rng.gamma(P["k"], P["m"] / P["k"], P["n"])); s = np.sort(x)[::-1]; c = np.cumsum(s)
        z0.append(np.mean(x == 0)); z5.append(np.mean(x > 5)); t80.append((np.searchsorted(c, 0.8 * c[-1]) + 1) / P["n"])
    f = lambda v: (float(np.mean(v)), float(np.std(v, ddof=1)))
    a0 = (1 + P["m"] / P["k"]) ** (-P["k"]); res = dict(zero=f(z0), gt5=f(z5), top_for_80=f(t80), analytic_zero=a0)
    tol = P["tol"]
    return res, [chk("V1", "simulated zero share within 0.005 of (1 + m/k)^(-k)", [res["zero"][0], a0], abs(res["zero"][0] - a0) <= 0.005, "validation"),
                 chk("H1", f"zero share within {tol} of P32's {P['p_zero']}", res["zero"][0], abs(res["zero"][0] - P["p_zero"]) <= tol, "hypothesis"),
                 chk("H2", f"share > 5 within {tol} of P32's {P['p_gt5']}", res["gt5"][0], abs(res["gt5"][0] - P["p_gt5"]) <= tol, "hypothesis"),
                 chk("H3", f"share producing 80% within {tol} of P32's {P['p_top80']}", res["top_for_80"][0], abs(res["top_for_80"][0] - P["p_top80"]) <= tol, "hypothesis"),
                 chk("R1", "values", res, True, "reporting")]

def ntipping(P, rng):
    """P41 (Hessler & Kamps 2025) synthetic systems, Euler-Maruyama with dt = 0.05 (4e4 samples over t in [0, 2000], as P41).
    mode 'switch': P41 Eq. 2 pitchfork h = nu x - x^3 (nu = 1), noise 0.05 until t = 500, ramp 2.4e-4 (t - 500) + 0.05 to t = 1750 (P41 prints 2.4e-4 t + 0.05, which would jump
    from 0.17 to 0.47 and contradict its own plateaus 0.05 and 0.35; the offset form joins both and is used),
    then 0.35; start at x = 1; switch = first time x < -0.5 (agent's criterion). mode 'indicators': same system; rolling windows of 2,000
    points shifted by 100 (P41's choice) up to the first switch; lag-1 autocorrelation, standard deviation, and a least-squares linear drift
    slope and noise level (agent's simplified estimator, NOT P41's Bayesian BLE). mode 'fold': P41 Eq. 3 drift h = r + x - x^3 with r
    ramped DOWN from r0 to r1 (agent's B-tipping comparator; P41 ramps r upward to stabilise), start on the upper branch; tipping = x < 0;
    the exact fold is r = -2/(3 sqrt 3) = -0.385 (direct computation)."""
    from scipy.stats import kendalltau
    dt = 0.05
    def sig_n(t):
        t = np.asarray(t, float); return np.where(t < 500, 0.05, np.where(t < 1750, 2.4e-4 * (t - 500) + 0.05, 0.35))
    if P["mode"] in ("switch", "indicators"):
        N = int(2000 / dt); ts = np.arange(N) * dt; sg = sig_n(ts); stats = []; sw = []
        printed_end = float(2.4e-4 * 1750 + 0.05)
        for _ in range(P["reps"]):
            x = np.empty(N); x[0] = 1.0; z = rng.standard_normal(N) * np.sqrt(dt); k = None
            for i in range(1, N):
                x[i] = x[i - 1] + (x[i - 1] - x[i - 1] ** 3) * dt + sg[i - 1] * z[i]
                if k is None and x[i] < -0.5: k = i; break
            sw.append(ts[k] if k is not None else np.nan)
            if P["mode"] == "indicators" and k is not None and k > 4000:
                W = 2000; ar = []; sd = []; zt = []; st = []; tm = []; tru = []
                for e in range(W, k - 100, 100):
                    w = x[e - W:e]; d = w - w.mean(); ar.append(float(np.corrcoef(d[:-1], d[1:])[0, 1])); sd.append(float(d.std()))
                    b = np.polyfit(d[:-1], np.diff(w), 1)[0]; res_ = np.diff(w) - b * d[:-1]
                    zt.append(b / dt); st.append(float(res_.std() / np.sqrt(dt))); tm.append(ts[e - W // 2]); tru.append(float(sig_n(ts[e - W // 2])))
                stats.append(dict(tau_ar1=float(kendalltau(range(len(ar)), ar)[0]), tau_sd=float(kendalltau(range(len(sd)), sd)[0]),
                                  median_zeta=float(np.median(zt)), median_rel_err_sigma=float(np.median(np.abs(np.array(st) / np.array(tru) - 1)))))
        sw = np.array(sw); res = dict(median_switch_t=float(np.nanmedian(sw)), q10_q90=[float(np.nanpercentile(sw, 10)), float(np.nanpercentile(sw, 90))],
                                      share_no_switch=float(np.mean(np.isnan(sw))), noise_printed_at_1750=printed_end, source_single_run=1386.8)
        if P["mode"] == "switch":
            return res, [chk("V1", "internal check of P41 Eq. 2: the printed ramp 2.4e-4 t + 0.05 reaches 0.47 at t = 1750, not the stated plateau 0.35 (the offset form is used)", printed_end, abs(printed_end - 0.47) < 1e-9, "validation"),
                         chk("H1", P["h1_text"], res, bool(eval(P["h1_expr"], {}, dict(r=res))), "hypothesis"), chk("R1", "values", res, True, "reporting")]
        S = {k_: float(np.median([s_[k_] for s_ in stats])) for k_ in stats[0]} if stats else {}
        res["n_used"] = len(stats); res.update(S)
        return res, [chk("V1", "indicator windows available in at least half the replicates", len(stats), len(stats) >= P["reps"] / 2),
                     chk("H1", "standard deviation trends up (median Kendall tau > 0.5): noise growth is visible", S.get("tau_sd"), S.get("tau_sd", 0) > 0.5, "hypothesis"),
                     chk("H2", "lag-1 autocorrelation shows no comparable trend (median |tau| < 0.3): no critical slowing down", S.get("tau_ar1"), abs(S.get("tau_ar1", 1)) < 0.3, "hypothesis"),
                     chk("H3", "least-squares drift slope near the true -2 (within 0.4) and noise level within 10% of truth (medians)", [S.get("median_zeta"), S.get("median_rel_err_sigma")], abs(S.get("median_zeta", 0) + 2) <= 0.4 and S.get("median_rel_err_sigma", 1) <= 0.1, "hypothesis"),
                     chk("R1", "values", res, True, "reporting")]
    rf = -2 / (3 * np.sqrt(3)); N = int((P["r0"] - P["r1"]) / P["rate"] / dt); rp = np.linspace(P["r0"], P["r1"], N); tips = []; taus = []
    for _ in range(P["reps"]):
        x = 1.32; z = rng.standard_normal(N) * np.sqrt(dt) * P["sigma"]; path = np.empty(N); k = None
        for i in range(N):
            x = x + (rp[i] + x - x ** 3) * dt + z[i]; path[i] = x
            if x < 0: k = i; break
        tips.append(rp[k] if k is not None else np.nan)
        if k is not None and k > 6000 and P["sigma"] > 0:
            W = 2000; ar = []
            for e in range(W, k - 500, 100):
                w = path[e - W:e]; d = w - np.convolve(w, np.ones(200) / 200, mode="same"); d = d[100:-100]; ar.append(float(np.corrcoef(d[:-1], d[1:])[0, 1]))
            taus.append(float(kendalltau(range(len(ar)), ar)[0]))
    tips = np.array(tips); res = dict(exact_fold=float(rf), mean_tip_r=float(np.nanmean(tips)), sd_tip_r=float(np.nanstd(tips)), n_missing=int(np.isnan(tips).sum()),
                                      median_tau_ar1=(float(np.median(taus)) if taus else None))
    return res, [chk("V1", "every replicate tips before the ramp ends", res["n_missing"], res["n_missing"] == 0),
                 chk("H1", P["h1_text"], res, bool(eval(P["h1_expr"], {}, dict(r=res, rf=rf))), "hypothesis"), chk("R1", "values", res, True, "reporting")]

def meta_power(P, rng):
    """P49 (Schuenemann et al. 2025, Clin Psychol Eur, CC BY): allegiance as a moderator in random-effects meta-regression; reported
    beta = -0.183, SE 0.125, p = .144 (symptom severity, end of intervention, N = 47). Agent's check: power of a two-sided z-test
    at alpha 0.05 to detect a true moderator of P49's size with P49's SE (normal approximation), and a simulation of K studies with a
    binary moderator (share pi), within-study SEs uniform [s_lo, s_hi], heterogeneity tau, DerSimonian-Laird tau^2 and WLS
    meta-regression (agent's implementation). Also the chance of >= 2 'significant' moderators in 5 independent null tests."""
    from scipy.stats import norm, binom
    z = abs(P["beta_rep"]) / P["se_rep"]; pw = norm.cdf(z - 1.96) + norm.cdf(-z - 1.96); p_rep = 2 * (1 - norm.cdf(z))
    K, pi, tau, bt = P["K"], P["pi"], P["tau"], P["beta_true"]; ests = []; ses = []; sig = 0
    for _ in range(P["reps"]):
        x = (rng.random(K) < pi).astype(float)
        while x.sum() < 2 or x.sum() > K - 2: x = (rng.random(K) < pi).astype(float)
        s = rng.uniform(P["s_lo"], P["s_hi"], K); y = P["b0"] + bt * x + rng.normal(0, tau, K) + rng.normal(0, s)
        X = np.c_[np.ones(K), x]; W = 1 / s ** 2; beta = np.linalg.solve(X.T @ (W[:, None] * X), X.T @ (W * y))
        Q = float((W * (y - X @ beta) ** 2).sum()); Pm = W.sum() - np.trace(np.linalg.solve(X.T @ (W[:, None] * X), X.T @ (W[:, None] ** 2 * X)))
        t2 = max(0.0, (Q - (K - 2)) / Pm); W2 = 1 / (s ** 2 + t2); A = X.T @ (W2[:, None] * X); beta = np.linalg.solve(A, X.T @ (W2 * y)); se = np.sqrt(np.linalg.inv(A)[1, 1])
        ests.append(beta[1]); ses.append(se); sig += abs(beta[1] / se) > 1.96
    m, sd = float(np.mean(ests)), float(np.std(ests)); psim = sig / P["reps"]; mse = float(np.mean(ses))
    p2of5 = float(1 - binom.cdf(1, 5, 0.05))
    res = dict(analytic=dict(z=z, p_two_sided=p_rep, power=pw), sim=dict(mean_beta=m, sd_beta=sd, mean_se=mse, power=psim), p_ge2_of_5_null=p2of5)
    return res, [chk("V1", "reported p reproduced from beta/SE within 0.01 (P49: p = .144) and simulated mean beta within 4 SE of truth", [p_rep, m, sd], abs(p_rep - P["p_rep"]) <= 0.01 and abs(m - bt) <= 4 * sd / np.sqrt(P["reps"])),
                 chk("H1", "power to detect P49's moderator size with P49's SE is below 0.5", pw, pw < 0.5, "hypothesis"),
                 chk("H2", "simulated design gives a mean SE within 20% of 0.125 and power within 0.1 of the analytic value", [mse, psim, pw], abs(mse / P["se_rep"] - 1) <= 0.2 and abs(psim - pw) <= 0.1, "hypothesis"),
                 chk("R1", "values", res, True, "reporting")]


def ci_power(P, rng):
    """Agent's check of reported meta-regression coefficients with 95% CIs (normal approximation): SE = (upper - lower)/(2 * 1.96),
    two-sided p, power at alpha 0.05 to detect each true effect in delta_values, and whether the CI excludes effects larger than
    margin in absolute value (an equivalence reading). Inputs are printed values from P56 (Leijten et al. 2026, Table 1) or P49."""
    from scipy.stats import norm
    out = {}
    for lab, (b, lo, hi) in P["coefs"].items():
        se = (hi - lo) / (2 * 1.959964); z = b / se; p = float(2 * (1 - norm.cdf(abs(z))))
        pw = {str(dl): float(norm.cdf(abs(dl) / se - 1.959964) + norm.cdf(-abs(dl) / se - 1.959964)) for dl in P["delta_values"]}
        mid = (lo + hi) / 2
        out[lab] = dict(beta=b, lo=lo, hi=hi, se=se, z=z, p=p, power=pw, midpoint_offset=b - mid, excludes_margin=bool(lo > -P["margin"] and hi < P["margin"]))
    t = P["target"]; res = dict(coefs=out, margin=P["margin"])
    return res, [chk("V1", "reported estimates lie at the CI midpoint within 0.01 (symmetric normal CIs)", {k: v["midpoint_offset"] for k, v in out.items()}, all(abs(v["midpoint_offset"]) <= 0.01 for v in out.values())),
                 chk("H1", P["h1_text"], out[t], bool(eval(P["h1_expr"], dict(o=out, t=out[t]))), "hypothesis"),
                 chk("H2", P["h2_text"], out[t], bool(eval(P["h2_expr"], dict(o=out, t=out[t]))), "hypothesis"),
                 chk("R1", "values", res, True, "reporting")]

def _hyps(P, res):
    return [chk(f"H{i}", t, res, bool(eval(e, dict(o=res, abs=abs, all=all, any=any, min=min, max=max, len=len))), "hypothesis") for i, (t, e) in enumerate(P["hyps"], 1)]

def t_power(P, rng):
    """Agent's two-sided two-sample t-test power (noncentral t) for printed trial designs, e.g. P54's stated power 0.84 for d = 0.6 with
    100 patients, and the power of the realised design to detect smaller between-group effects."""
    from scipy.stats import t as tdist, nct
    def pw(n1, n2, d, a):
        df = n1 + n2 - 2; nc = d * np.sqrt(n1 * n2 / (n1 + n2)); cr = tdist.ppf(1 - a / 2, df)
        return float(1 - nct.cdf(cr, df, nc) + nct.cdf(-cr, df, nc))
    res = {g["label"]: dict(power={str(d): pw(g["n1"], g["n2"], d, g.get("alpha", 0.05)) for d in g["d_values"]}, printed=g.get("printed")) for g in P["designs"]}
    z = pw(50, 50, 0.0, 0.05)
    return res, [chk("V1", "power at d = 0 equals alpha (within 1e-6)", z, abs(z - 0.05) < 1e-6)] + _hyps(P, res) + [chk("R1", "values", res, True, "reporting")]

def quad_convergence(P, rng):
    """P70 (Asgedom & Kefela 2026): composite trapezoid, Simpson and 2-point Gauss-Legendre errors for int_0^1 exp(-x^2) dx at
    n subintervals, empirical orders, the smallest n (and function evaluations) reaching 1e-8, the asymptotic efficiency index
    eta = |I - G| / |S - G| on one small interval (P70 Lemma 2.6), P70's Algorithm 1 implemented as printed (evaluation count and
    error for tolerance eps), and the percentage reductions implied by P70's Table 2 and Table 3 counts."""
    from math import erf, sqrt, pi
    FUN = dict(f1=lambda x: np.exp(-x ** 2), f2=lambda x: np.sin(20 * x ** 2), f3=lambda x: 1 / (0.01 + (x - 0.5) ** 2), f4=lambda x: x * np.sin(10 * x))
    fk = P.get("func", "f1"); f = FUN[fk]   # CVA extension: P70's test functions f2-f4 (f5 = x^-0.5 is singular at 0 and not used)
    if fk == "f1": I = sqrt(pi) / 2 * erf(1.0)
    elif fk == "f3": I = 2 * 10 * np.arctan(0.5 / 0.1)
    elif fk == "f4": I = (np.sin(10) - 10 * np.cos(10)) / 100
    else:
        from scipy.integrate import quad; I = quad(f, 0, 1, epsabs=1e-15, epsrel=1e-15, limit=500)[0]
    mode = P.get("n_mode", "sub")   # CVA extension: 'sub' = n subintervals; 'points' = n nodes; 'panels' = n Simpson/Gauss panels of 2 subintervals
    def m_of(n): return {"sub": n, "points": n - 1, "panels": 2 * n}[mode]
    def trap(n): m = m_of(n); x = np.linspace(0, 1, m + 1); return (x[1] - x[0]) * (f(x).sum() - (f(0) + f(1)) / 2)
    def simp(n):
        m = m_of(n); m += m % 2; x = np.linspace(0, 1, m + 1); h = 1 / m; y = f(x); return h / 3 * (y[0] + y[-1] + 4 * y[1:-1:2].sum() + 2 * y[2:-1:2].sum())
    g = (1 - 1 / sqrt(3)) / 2
    def gauss(n): m = m_of(n); a = np.arange(m) / m; h = 1 / m; return h / 2 * (f(a + g * h) + f(a + (1 - g) * h)).sum()
    rules = dict(trapezoid=(trap, lambda n: m_of(n) + 1), simpson=(simp, lambda n: m_of(n) + (m_of(n) % 2) + 1), gauss2=(gauss, lambda n: 2 * m_of(n)))
    tab = {}
    for k, (q, ev) in rules.items():
        e = {str(n): abs(q(n) - I) for n in P["n_values"]}; ns = P["n_values"]
        orders = [float(np.log2(e[str(ns[i])] / e[str(ns[i + 1])])) for i in range(len(ns) - 1)]
        n = 2
        while abs(q(n) - I) >= P["target"] and n < P.get("n_cap", 200000): n += 2
        tab[k] = dict(errors=e, orders=[round(o, 4) for o in orders], n_for_target=n, evals_for_target=ev(n))
    h, x0 = P.get("eta_h", 1e-2), P.get("eta_x0", 0.3)
    S = h / 6 * (f(x0) + 4 * f(x0 + h / 2) + f(x0 + h)); G = h / 2 * (f(x0 + g * h) + f(x0 + (1 - g) * h))
    from math import erf as _e
    if fk == "f1": Ik = sqrt(pi) / 2 * (_e(x0 + h) - _e(x0))
    else:
        from scipy.integrate import quad; Ik = quad(f, x0, x0 + h, epsabs=1e-16, epsrel=1e-14)[0]
    eta = abs(Ik - G) / abs(S - G)
    def ahqs(eps, sig=0.8, L=1.0):
        Q = 0.0; ev = 0; st = [(0.0, 1.0, 0)]
        while st:
            a, b, d = st.pop(); hh = b - a
            if hh < 1e-12 or d > 50: Q += hh / 2 * (f(a) + f(b)); ev += 2; continue
            c = (a + b) / 2; IS = hh / 6 * (f(a) + 4 * f(c) + f(b)); IG = hh / 2 * (f(a + g * hh) + f(a + (1 - g) * hh)); ev += 5
            if abs(IS - IG) < sig * eps * hh / L: Q += IG
            else: st += [(a, c, d + 1), (c, b, d + 1)]
        return Q, ev
    Q, ev = ahqs(P["eps"])
    ahqs_by = {str(e): dict(zip(["evals", "error"], [r[1], float(abs(r[0] - I))])) for e in P.get("eps_values", []) for r in [ahqs(e)]}
    red = {}
    for lab, (new, old) in P.get("reductions", {}).items(): red[lab] = round(100 * (1 - new / old), 2)
    res = dict(table=tab, printed=P.get("printed"), eta=round(float(eta), 6), ahqs=dict(evals=ev, error=float(abs(Q - I))), reductions_pct=red, exact=I)
    if ahqs_by: res["ahqs_by_eps"] = ahqs_by
    if fk != "f1" or mode != "sub": res["func"], res["n_mode"] = fk, mode
    cub = lambda x: x ** 3 - 2 * x + 1; ok = abs(1 / 6 * (cub(0) + 4 * cub(.5) + cub(1)) - 0.25) < 1e-14 and abs(0.5 * (cub(g) + cub(1 - g)) - 0.25) < 1e-14
    return res, [chk("V1", "Simpson and 2-point Gauss integrate x^3 - 2x + 1 on [0, 1] exactly (0.25)", ok, ok)] + _hyps(P, res) + [chk("R1", "values", res, True, "reporting")]

def trap_error(P, rng):
    """P79 (Wikipedia 'Trapezoidal rule'): composite trapezoidal rule T_N on [a, b] with N equal subintervals; absolute and
    relative error; P79's error bound (b - a)^3/(12 N^2) max|f''| (max on a 200001-point grid); P79's asymptotic estimate
    E ~ -(b - a)^2/(12 N^2) [f'(b) - f'(a)]; the N guaranteed by the bound and the N predicted by the asymptotic estimate for a
    tolerance, against the smallest N actually reaching it (scan N = 1, 2, ...). f, f', f'' are numpy expressions in x
    supplied in the configuration (agent-derived derivatives)."""
    from math import ceil, sqrt
    ns = dict(np=np, exp=np.exp, sin=np.sin, cos=np.cos, log=np.log)
    a, b = P["a"], P["b"]
    f = lambda x: eval(P["f"], ns, dict(x=x)); d1 = lambda x: eval(P["d1"], ns, dict(x=x)); d2 = lambda x: eval(P["d2"], ns, dict(x=x))
    I = float(eval(P["exact"], ns, {})) if isinstance(P["exact"], str) else float(P["exact"])
    def T(N): x = np.linspace(a, b, N + 1); y = f(x) * np.ones_like(x); return float((b - a) / N * (y.sum() - (y[0] + y[-1]) / 2))
    xx = np.linspace(a, b, 200001); M = float(np.max(np.abs(d2(xx)))); D = float(d1(b) - d1(a))
    rows = {}
    for N in P.get("N_values", []):
        t = T(N); E = I - t
        rows[str(N)] = dict(T=round(t, 10), E=float(E), abs_err=float(abs(E)), rel_pct=round(float(abs(E) / abs(I) * 100), 6), bound=float(M * (b - a) ** 3 / (12 * N * N)),
                            asym=float(-(b - a) ** 2 / (12 * N * N) * D), overestimates=bool(t > I))
    res = dict(exact=I, M2=M, fprime_diff=D, rows=rows)
    if P.get("tol"):
        tol = P["tol"]; Nb = ceil(sqrt(M * (b - a) ** 3 / (12 * tol))); Na = ceil(sqrt((b - a) ** 2 * abs(D) / (12 * tol))) if D != 0 else None
        N = 1
        while abs(T(N) - I) >= tol and N < P.get("N_cap", 100000): N += 1
        res["tol"] = dict(tol=tol, N_bound=Nb, N_asym=Na, N_actual=N, evals_bound=Nb + 1, evals_actual=N + 1)
        if P.get("printed_evals"): res["tol"]["printed_evals"] = P["printed_evals"]
    x = np.linspace(0, 1, 5); ok = abs(0.25 * ((2 * x + 1).sum() - (1 + 3) / 2) - 2.0) < 1e-14
    return res, [chk("V1", "the trapezoidal rule integrates 2x + 1 on [0, 1] exactly (2) with N = 4", 2.0, bool(ok))] + _hyps(P, res) + [chk("R1", "values", res, True, "reporting")]

def trap_simpson(P, rng):
    """P79 (Wikipedia 'Trapezoidal rule'): composite trapezoidal vs composite Simpson rule at equal numbers of function
    evaluations m (Simpson needs m odd), for an integrand f (numpy expression in x) on [a, b] with a known exact value.
    Optional 'gauss' mode for P79's claim about the full Gaussian integral: for m equally spaced nodes x_k = c + k h with the
    offset c chosen symmetric, the rule h sum f(x_k) (trapezoid on a truncated infinite range, end weights negligible) or the
    Simpson weights, minimised over the spacing h on a fine grid; reports the smallest m reaching a relative tolerance."""
    ns = dict(np=np, exp=np.exp, sin=np.sin, cos=np.cos, log=np.log, sqrt=np.sqrt, abs=np.abs, pi=np.pi)
    res = {}
    if P.get("f"):
        a, b = P["a"], P["b"]; f = lambda x: eval(P["f"], ns, dict(x=x)); I = float(eval(P["exact"], ns, {})) if isinstance(P["exact"], str) else float(P["exact"])
        def T(m): x = np.linspace(a, b, m); y = f(x); return float((b - a) / (m - 1) * (y.sum() - (y[0] + y[-1]) / 2))
        def S(m): x = np.linspace(a, b, m); y = f(x); h = (b - a) / (m - 1); return float(h / 3 * (y[0] + y[-1] + 4 * y[1:-1:2].sum() + 2 * y[2:-1:2].sum()))
        rows = {}
        for m in P["m_values"]:
            et = abs(T(m) - I); es = abs(S(m) - I) if m % 2 == 1 else None
            rows[str(m)] = dict(trap_err=float(et), simp_err=None if es is None else float(es))
        ms = [m for m in P["m_values"] if m % 2 == 1]
        def order(key):
            m1, m2 = ms[-2], ms[-1]; e1, e2 = rows[str(m1)][key], rows[str(m2)][key]
            return round(float(-np.log(e2 / e1) / np.log((m2 - 1) / (m1 - 1))), 4) if e1 > 0 and e2 > 0 else None
        res.update(exact=I, rows=rows, order_trap=order("trap_err"), order_simp=order("simp_err"))
    if P.get("gauss"):
        g = P["gauss"]; tol = g["tol"]; hs = np.linspace(0.05, 3.0, 5901); out = {}
        for m in range(2, g["m_max"] + 1):
            k = np.arange(m) - (m - 1) / 2; bt, bs = np.inf, np.inf
            for h in hs:
                y = np.exp(-(k * h) ** 2); bt = min(bt, abs(h * y.sum() - np.sqrt(np.pi)) / np.sqrt(np.pi))
                if m % 2 == 1 and m >= 3:
                    wts = np.ones(m); wts[1:-1:2] = 4; wts[2:-1:2] = 2; bs = min(bs, abs(h / 3 * (wts * y).sum() - np.sqrt(np.pi)) / np.sqrt(np.pi))
            out[str(m)] = dict(trap_best_rel=float(bt), simp_best_rel=None if not np.isfinite(bs) else float(bs))
        mt = next((m for m in range(2, g["m_max"] + 1) if out[str(m)]["trap_best_rel"] < tol), None)
        msimp = next((m for m in range(3, g["m_max"] + 1) if out[str(m)]["simp_best_rel"] is not None and out[str(m)]["simp_best_rel"] < tol), None)
        res["gauss"] = dict(by_m=out, m_trap=mt, m_simp=msimp, ratio=None if not (mt and msimp) else round(msimp / mt, 4))
    x = np.linspace(0, 1, 5); y = x ** 3; ok = abs(0.25 / 3 * (y[0] + y[-1] + 4 * (y[1] + y[3]) + 2 * y[2]) - 0.25) < 1e-14
    return res, [chk("V1", "Simpson's rule integrates x^3 on [0, 1] exactly (1/4) with 5 nodes", 0.25, bool(ok))] + _hyps(P, res) + [chk("R1", "values", res, True, "reporting")]

def arith_audit(P, rng):
    """Agent's recomputation of printed numbers from a source's own printed inputs. Each item is a named arithmetic expression
    (written in the SPEC, evaluated with numpy/scipy helpers) next to the value the source prints; 'diff' = computed - printed.
    Helpers: chi2_sf(x, df), t_p2(t, df) two-sided t p-value, logistic(x), exp, log, sqrt, np."""
    from scipy import stats
    ns = dict(np=np, exp=np.exp, log=np.log, sqrt=np.sqrt, abs=abs, sum=sum, min=min, max=max, round=round,
              chi2_sf=lambda x, d: float(stats.chi2.sf(x, d)), t_p2=lambda t, d: float(2 * stats.t.sf(abs(t), d)), logistic=lambda x: float(1 / (1 + np.exp(-x))))
    ns['chi2_2x2'] = lambda a, b, c, d, yates=False: float(stats.chi2_contingency(np.array([[a, b], [c, d]]), correction=yates)[1])  # ASA: p of a 2x2 Pearson chi-square
    import math; ns['comb'] = math.comb  # TR0: binomial coefficient
    ns['ncf_pow'] = lambda lam, d1, d2, a=0.05: float(stats.ncf.sf(stats.f.ppf(1 - a, d1, d2), d1, d2, lam))  # TRA: noncentral-F power
    ns['nct_pow2'] = lambda delta, df, a=0.05: float(stats.nct.sf(stats.t.ppf(1 - a / 2, df), df, delta) + stats.nct.cdf(-stats.t.ppf(1 - a / 2, df), df, delta))  # TRA: two-sided t power
    ns['nct_pow1'] = lambda delta, df, a=0.05: float(stats.nct.sf(stats.t.ppf(1 - a, df), df, delta))  # TRA: one-sided t power
    ns['t_p1'] = lambda t, d: float(stats.t.sf(t, d))  # TRA: one-sided (upper) t p-value
    out = {}
    for it in P["items"]:
        v = float(eval(it["expr"], dict(ns))); pr = it.get("printed")
        out[it["name"]] = dict(value=round(v, 6), printed=pr, diff=(round(v - pr, 6) if isinstance(pr, (int, float)) else None))
    v1 = float(stats.chi2.sf(3.841458820694124, 1))
    return dict(items=out), [chk("V1", "chi-square survival at 3.8415 with 1 df equals 0.05 within 1e-9", v1, abs(v1 - 0.05) < 1e-9)] + _hyps(P, dict(items=out)) + [chk("R1", "values", dict(items=out), True, "reporting")]


def ordlogit_mc(P, rng):
    """ASA: P88 model-4 counterfactual with coefficient uncertainty. Draws each coefficient independently from N(estimate, SE)
    (agent's approximation: P88's posterior correlations are not printed) and computes P(moderate or severe) = 1 - logistic(c2 - eta)
    for a 1-day and a k-day ascent of gain_km, eta = b_rate * rate + b_peak ln(peak) + b_res ln(res) + b_age; reports the mean and
    quantiles of the risk ratio, the ratio of mean probabilities, and the point-estimate ratio."""
    n = P["draws"]; c = P["coef"]
    def draw(k): return rng.normal(c[k][0], c[k][1], n)
    b = {k: draw(k) for k in c}
    def pr(rate): eta = b["rate"] * rate + b["peak"] * np.log(P["peak_m"]) + b["res"] * np.log(P["res_m"]) + b["age"]; return 1 - 1 / (1 + np.exp(-(b["c2"] - eta)))
    def pr0(rate): eta = c["rate"][0] * rate + c["peak"][0] * np.log(P["peak_m"]) + c["res"][0] * np.log(P["res_m"]) + c["age"][0]; return float(1 - 1 / (1 + np.exp(-(c["c2"][0] - eta))))
    out = {}
    for days in P["days"]:
        p1, pk = pr(P["gain_km"]), pr(P["gain_km"] / days); rr = p1 / pk
        out[str(days)] = dict(mean_rr=round(float(rr.mean()), 4), median_rr=round(float(np.median(rr)), 4), q05=round(float(np.quantile(rr, 0.05)), 4), q95=round(float(np.quantile(rr, 0.95)), 4),
                              ratio_of_means=round(float(p1.mean() / pk.mean()), 4), point_rr=round(pr0(P["gain_km"]) / pr0(P["gain_km"] / days), 4), se_mean_rr=round(float(rr.std(ddof=1) / np.sqrt(n)), 4))
    res = dict(by_days=out)
    v = abs(out[str(P["days"][0])]["point_rr"] - P["v1_point"]) < 1e-3
    return res, [chk("V1", P.get("v1_label", "the point-estimate risk ratio for the first k equals the AS0 audit value within 1e-3"), out[str(P["days"][0])]["point_rr"], v)] + _hyps(P, res) + [chk("R1", "values", res, True, "reporting")]


def cvi_chance_mc(P, rng):
    """Chance agreement for content validity (Polit, Beck & Owen): N experts each rate an item relevant with probability 0.5;
    the probability that exactly A agree is Pc = C(N, A) 0.5^N. Monte Carlo frequencies vs the formula, and the modified
    kappa (I-CVI - Pc)/(1 - Pc) for each A."""
    import math
    N = P["N"]; reps = P["reps"]; x = rng.binomial(N, 0.5, reps); out = {}
    for A in P["A_list"]:
        pc = math.comb(N, A) * 0.5 ** N; fr = float((x == A).mean()); se = math.sqrt(pc * (1 - pc) / reps)
        out[str(A)] = dict(pc=pc, freq=fr, se=se, icvi=A / N, kappa=(A / N - pc) / (1 - pc))
    tot = sum(math.comb(N, a) for a in range(N + 1)) * 0.5 ** N
    res = dict(by_A=out, N=N)
    return res, [chk("V1", "binomial probabilities C(N, a) 0.5^N sum to 1 over a = 0..N", tot, abs(tot - 1) < 1e-12)] + _hyps(P, res) + [chk("R1", "values", res, True, "reporting")]


KINDS = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_') and k != 'chk' and getattr(v, '__module__', None) == '__main__'}

if __name__ == "__main__":
    P, H, t0 = R.start(sys.argv[1]); rng = np.random.default_rng(P["seed"])
    res, checks = KINDS[P["kind"]](P, rng); R.finish(H, P, res, checks, t0)
