"""SIM-<PH>-NAT: Natural-Sciences simulations (Phases track). Usage: python sim_nat.py iter-<k> (from Natural-Sciences/simulation/)."""
import os, sys, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
import track_runner as R
chk = R.chk

def wf_divergence(P, rng):
    """Two-deme Wright-Fisher model, L independent biallelic neutral loci, 2N gene copies per deme, symmetric migration m
    per generation (gene copies replaced by migrants before drift). Returns Fst = (HT - HS)/HT averaged over loci, and
    within-deme heterozygosity decay. A toy population-genetic model; it does not model Heliconius genomes (P01)."""
    N2 = 2 * P["N"]; L = P["loci"]; T = P["generations"]; out = {}
    for lab, m in (("no_migration", 0.0), ("migration", P["m"])):
        p0 = rng.uniform(0.2, 0.8, L); p = np.vstack([p0, p0]).astype(float); H0 = 2 * p0 * (1 - p0); traj = []
        for t in range(1, T + 1):
            pm = (1 - m) * p + m * p[::-1]
            p = rng.binomial(N2, pm) / N2
            if t in P["checkpoints"]:
                hs = (2 * p * (1 - p)).mean(0); pb = p.mean(0); ht = 2 * pb * (1 - pb); ok = ht > 0
                traj.append(dict(t=t, fst=float(np.mean((ht[ok] - hs[ok]) / ht[ok])) if ok.any() else None,
                                 het_ratio=float((2 * p * (1 - p)).mean() / H0.mean())))
        out[lab] = traj
    t_end = P["checkpoints"][-1]; exp_ratio = (1 - 1 / N2) ** t_end
    obs_ratio = out["no_migration"][-1]["het_ratio"]; fst0 = out["no_migration"][-1]["fst"]; fstm = out["migration"][-1]["fst"]
    Nm = P["N"] * P["m"]
    c = [chk("V1", f"m = 0: within-deme heterozygosity ratio at t={t_end} within 10% (relative) of (1-1/2N)^t = {exp_ratio:.4f}", obs_ratio, abs(obs_ratio / exp_ratio - 1) <= 0.10),
         chk("H1", f"without gene flow the demes diverge: Fst at t={t_end} > {P['h1']}", fst0, fst0 > P["h1"], "hypothesis"),
         chk("H2", f"with gene flow Nm = {Nm:g}: Fst at t={t_end} < {P['h2']} (divergence held back by migration)", fstm, fstm < P["h2"], "hypothesis"),
         chk("R1", "island-model reference 1/(1+4Nm) (infinite-island formula; two demes differ)", 1 / (1 + 4 * Nm), True, "reporting")]
    return out, c

def wf_selection(P, rng):
    """Two-deme Wright-Fisher model (2N gene copies per deme, symmetric migration m) with one locus under divergent selection
    (allele A has relative fitness 1+s in deme 1 and 1/(1+s)... implemented as genic selection: p' = p(1+s)/(1+s p) in deme 1 and
    p' = p/(1+s(1-p)) in deme 2) plus neutral loci, all unlinked. Replicates of the selected locus are independent runs.
    Toy model of a 'genomic island of divergence': it does not model linkage, recombination or any real genome (P01)."""
    N2 = 2 * P["N"]; T = P["generations"]; out = {}
    def fst(p):
        hs = (2 * p * (1 - p)).mean(0); pb = p.mean(0); ht = 2 * pb * (1 - pb); ok = ht > 0
        return float(np.mean((ht[ok] - hs[ok]) / ht[ok])) if ok.any() else 0.0, (ht - hs)[ok] / ht[ok] if ok.any() else np.array([0.0])
    for s in P["s_values"]:
        R = P["reps"]; p0 = rng.uniform(0.2, 0.8, R); ps = np.vstack([p0, p0]).astype(float)
        q0 = rng.uniform(0.2, 0.8, P["loci"]); pn = np.vstack([q0, q0]).astype(float); m = P["m"]
        for t in range(T):
            ps = (1 - m) * ps + m * ps[::-1]; pn = (1 - m) * pn + m * pn[::-1]
            a = ps[0] * (1 + s) / (1 + s * ps[0]); b = ps[1] / (1 + s * (1 - ps[1])); ps = np.vstack([a, b])
            ps = rng.binomial(N2, ps) / N2; pn = rng.binomial(N2, pn) / N2
        f_sel, per_sel = fst(ps); f_neu, per_neu = fst(pn)
        out[str(s)] = dict(fst_selected=f_sel, fst_selected_se=float(per_sel.std(ddof=1) / np.sqrt(len(per_sel))) if len(per_sel) > 1 else 0.0,
                          fst_neutral=f_neu, fst_neutral_se=float(per_neu.std(ddof=1) / np.sqrt(len(per_neu))) if len(per_neu) > 1 else 0.0)
    z = out[str(P["s_values"][0])]; hi = out[str(P["s_values"][-1])]
    diff0 = abs(z["fst_selected"] - z["fst_neutral"]); se0 = (z["fst_selected_se"] ** 2 + z["fst_neutral_se"] ** 2) ** 0.5; k = P["tol_se"]
    sel = [out[str(s)]["fst_selected"] for s in P["s_values"]]
    c = [chk("V1", f"s = {P['s_values'][0]}: selected-locus Fst equals neutral Fst within {k} combined standard errors (code check: selection switched off)", [diff0, k * se0], diff0 <= k * se0),
         chk("H1", f"s = {P['s_values'][-1]}, Nm = {P['N']*P['m']:g}: selected-locus Fst > {P['h1']} while neutral Fst < {P['h2']} (an island of divergence)", [hi["fst_selected"], hi["fst_neutral"]],
             hi["fst_selected"] > P["h1"] and hi["fst_neutral"] < P["h2"], "hypothesis"),
         chk("H2", "selected-locus Fst is non-decreasing in s across the grid (tolerance 0.02)", sel, all(sel[i + 1] >= sel[i] - 0.02 for i in range(len(sel) - 1)), "hypothesis"),
         chk("R1", "Fst by s (selected, neutral) and m", {k2: [v["fst_selected"], v["fst_neutral"]] for k2, v in out.items()}, True, "reporting")]
    return out, c

def pitchfork_landscape(P, rng):
    """Waddington-style landscape as a formal toy (cf. P10's 'marble rolling down a rugged hillside'): cells follow
    dx = (a(t) x - x^3 + bias) dt + sigma dW, with a(t) ramping from a0 < 0 (one valley) to a1 > 0 (two valleys: a pitchfork
    bifurcation). Records the fraction of cells ending in the right-hand valley. No biological gene network is modelled."""
    n = P["cells"]; dt = P["dt"]; steps = int(P["T"] / dt); out = {}
    for bias in P["biases"]:
        x = np.zeros(n)
        for k in range(steps):
            a = P["a0"] + (P["a1"] - P["a0"]) * k / steps
            x = x + (a * x - x ** 3 + bias) * dt + P["sigma"] * np.sqrt(dt) * rng.normal(size=n)
        fr = float((x > 0).mean()); out[str(bias)] = dict(frac_right=fr, se=float(np.sqrt(fr * (1 - fr) / n)), mean_abs_x=float(np.abs(x).mean()))
    z = out["0.0"]; k = P["tol_se"]; seb = np.sqrt(0.25 / n); hb = out[str(P["biases"][-1])]
    c = [chk("V1", f"bias 0 (symmetric landscape): fraction in the right valley within {k} binomial standard errors of 0.5", [z["frac_right"], 0.5, k * seb], abs(z["frac_right"] - 0.5) <= k * seb),
         chk("V2", f"after the bifurcation cells sit near the valley floors: mean |x| within 10% of sqrt(a1) = {np.sqrt(P['a1']):.4f}", z["mean_abs_x"], abs(z["mean_abs_x"] / np.sqrt(P["a1"]) - 1) <= 0.10),
         chk("H1", f"a small bias {P['biases'][-1]} applied during the ramp sends > {P['h1']} of cells into one valley (sensitivity near the bifurcation)", hb["frac_right"], hb["frac_right"] > P["h1"], "hypothesis"),
         chk("R1", "fraction right by bias", {k2: v["frac_right"] for k2, v in out.items()}, True, "reporting")]
    return out, c


def wf_linked(P, rng):
    """Two haploid demes of N with symmetric migration m. Locus A is under divergent selection (allele 1 has fitness 1+s in
    deme 0, allele 0 has fitness 1+s in deme 1). Neutral loci B_j recombine with A at rate c_j (each B_j independently of the
    others: a star of two-locus systems, so each marginal A-B_j dynamic is exact). Fst at B_j vs c_j shows whether divergence
    around a selected locus decays with recombination distance (the 'island' shape of P01, as a toy)."""
    N = P["N"]; R = P["reps"]; cs = np.array([c for c in P["c_values"] for _ in range(P["per_c"])]); L = len(cs)
    H = (rng.random((R, 2, N, 1 + L)) < 0.5).astype(np.int8)
    for g in range(P["generations"]):
        k = int(round(P["m"] * N))
        if k:
            i0 = np.argsort(rng.random((R, N)), 1)[:, :k]; i1 = np.argsort(rng.random((R, N)), 1)[:, :k]; rr = np.arange(R)[:, None]
            a = H[rr, 0, i0].copy(); H[rr, 0, i0] = H[rr, 1, i1]; H[rr, 1, i1] = a
        new = np.empty_like(H)
        for d in range(2):
            w = 1 + P["s"] * (H[:, d, :, 0] == (1 - d)); cw = np.cumsum(w, 1); cw = cw / cw[:, -1:]
            for r in range(R):
                new[r, d] = H[r, d, np.minimum(np.searchsorted(cw[r], rng.random(N)), N - 1)]
        perm = np.argsort(rng.random((R, 2, N)), 2); new = np.take_along_axis(new, perm[..., None], 2)
        a = new[:, :, 0::2, 1:]; b = new[:, :, 1::2, 1:]; sw = rng.random(a.shape) < cs
        a2 = np.where(sw, b, a); b2 = np.where(sw, a, b); new[:, :, 0::2, 1:] = a2; new[:, :, 1::2, 1:] = b2; H = new
    p = H.mean(2)  # R x 2 x (1+L)
    num = ((p[:, 0] - p[:, 1]) / 2) ** 2; pb = p.mean(1); den = pb * (1 - pb)
    fst = {}; se = {}
    for c in P["c_values"]:
        j = 1 + np.where(cs == c)[0]; per_rep = num[:, j].sum(1) / np.maximum(den[:, j].sum(1), 1e-12)
        fst[str(c)] = float(num[:, j].sum() / den[:, j].sum()); se[str(c)] = float(per_rep.std(ddof=1) / np.sqrt(R))
    fA = float(num[:, 0].sum() / max(den[:, 0].sum(), 1e-12)); pn = p[:, :, 1:].mean(); pn_se = float(p[:, :, 1:].mean((1, 2)).std(ddof=1) / np.sqrt(R))
    k = P["tol_se"]; c0 = str(P["c_values"][0]); cl = str(P["c_values"][-1]); cm = str(P["c_mid"])
    vals = [fst[str(c)] for c in P["c_values"]]; mono = all(vals[i + 1] <= vals[i] + P["mono_tol"] for i in range(len(vals) - 1))
    res = dict(fst_by_c=fst, se_by_c=se, fst_selected=fA, neutral_mean_freq=float(pn), neutral_mean_freq_se=pn_se)
    c = [chk("V1", f"neutral allele frequency unbiased: mean within {k} SE of 0.5", [float(pn), pn_se], abs(pn - 0.5) <= k * pn_se + 1e-12),
         chk("H1", f"Fst at c = {c0} exceeds Fst at c = {cl} by more than {k} SE (combined)", [fst[c0], fst[cl]], fst[c0] - fst[cl] > k * np.hypot(se[c0], se[cl]), "hypothesis"),
         chk("H2", f"Fst non-increasing in c (tolerance {P['mono_tol']})", vals, mono, "hypothesis"),
         chk("H3", f"Fst at c = {cm} is below the midpoint of Fst(c={c0}) and Fst(c={cl}) (decay within short map distance)", [fst[cm], (fst[c0] + fst[cl]) / 2], fst[cm] < (fst[c0] + fst[cl]) / 2, "hypothesis"),
         chk("R1", "Fst by c and at the selected locus", res, True, "reporting")]
    return res, c

def hysteresis_sweep(P, rng):
    """P22 (Sayama 8.2) Eq. 8.14: dx/dt = r + x - x^3. Ramp r slowly from -1 to 1 and back (rate P['rate'] per unit time),
    Euler-Maruyama with step dt and noise sigma. Record r at the up-jump (x crosses 0 upward) and down-jump. Exact saddle-node
    thresholds are r* = +/- 2/(3 sqrt 3) = +/- 0.3849. Also checks the analytic root count of r + x - x^3 on a grid (deterministic)."""
    rs = 2 / (3 * np.sqrt(3)); dt = P["dt"]; R_ = P["reps"]; ups = []; downs = []
    grid = np.linspace(-1, 1, 201); nroots = [int(np.sum(np.abs(np.roots([-1, 0, 1, r]).imag) < 1e-9)) for r in grid]
    exp_roots = [3 if abs(r) < rs - 1e-9 else (1 if abs(r) > rs + 1e-9 else 2) for r in grid]
    root_ok = all(a == b for a, b, r in zip(nroots, exp_roots, grid) if abs(abs(r) - rs) > 1e-6)
    n = int(round(2 / P["rate"] / dt))
    for _ in range(R_):
        x = -1.3247; up = None
        r_path = np.linspace(-1, 1, n)
        noise = rng.standard_normal(n) * P["sigma"] * np.sqrt(dt)
        for i in range(n):
            r = r_path[i]; x += (r + x - x ** 3) * dt + noise[i]
            if up is None and x > 0: up = r
        down = None; noise = rng.standard_normal(n) * P["sigma"] * np.sqrt(dt)
        for i in range(n):
            r = r_path[n - 1 - i]; x += (r + x - x ** 3) * dt + noise[i]
            if down is None and x < 0: down = r
        ups.append(up if up is not None else np.nan); downs.append(down if down is not None else np.nan)
    ups = np.array(ups); downs = np.array(downs); mu = float(np.nanmean(ups)); md = float(np.nanmean(downs))
    res = dict(exact_threshold=float(rs), mean_up_jump_r=mu, mean_down_jump_r=md, sd_up=float(np.nanstd(ups)), n_missing=int(np.isnan(ups).sum() + np.isnan(downs).sum()),
               hysteresis_width=mu - md, source_stated_threshold=0.4)
    c = [chk("V1", "analytic root count of r + x - x^3 is 3 for |r| < 2/(3 sqrt 3), 1 beyond (201-point grid; deterministic)", [sum(nroots)], root_ok),
         chk("V2", "every replicate jumps up and back down (no missing jumps)", res["n_missing"], res["n_missing"] == 0),
         chk("H1", f"mean up-jump r within {P['h1']} of the exact threshold 0.3849", [mu, float(rs)], abs(mu - rs) <= P["h1"], "hypothesis"),
         chk("H2", f"hysteresis loop width (up minus down jump) > {P['h2']}", res["hysteresis_width"], res["hysteresis_width"] > P["h2"], "hypothesis"),
         chk("R1", "jump points", res, True, "reporting")]
    return res, c

def pitchfork_types(P, rng):
    """P22 Eqs. 8.10 and 8.12: supercritical dx/dt = r x - x^3 settles at +/- sqrt(r) for r > 0; subcritical dx/dt = r x + x^3
    escapes (|x| exceeds a cap) for r > 0 from a small start. Deterministic RK4 from x0 = +/- eps."""
    def rk(f, x, dt, n, cap):
        for i in range(n):
            k1 = f(x); k2 = f(x + dt / 2 * k1); k3 = f(x + dt / 2 * k2); k4 = f(x + dt * k3); x = x + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            if abs(x) > cap: return x, i * dt
        return x, None
    out = {}; ok_sup = True; esc = True; neg_ok = True
    for r in P["r_values"]:
        xs, _ = rk(lambda x: r * x - x ** 3, P["eps"], P["dt"], P["steps"], 1e6)
        xb, tb = rk(lambda x: r * x + x ** 3, P["eps"], P["dt"], P["steps"], P["cap"])
        out[str(r)] = dict(super_final=float(xs), sub_escape_time=tb)
        if r > 0: ok_sup &= abs(xs - np.sqrt(r)) <= P["tol"]; esc &= tb is not None
        else: neg_ok &= abs(xs) <= P["tol"] and tb is None
    c = [chk("V1", f"supercritical: final x within {P['tol']} of sqrt(r) for every r > 0", out, bool(ok_sup)),
         chk("V2", "r <= 0: both forms decay to 0 (no escape)", out, bool(neg_ok)),
         chk("H1", f"subcritical form escapes |x| > {P['cap']} within the run for every r > 0 (no stable branch near 0)", out, bool(esc), "hypothesis"),
         chk("R1", "finals and escape times", out, True, "reporting")]
    return out, c

def transcritical_onset(P, rng):
    """P22 Eq. 8.8, dx/dt = r x - x^2 (transcritical: equilibria 0 and r exchange stability at r = 0). From a small seed x0 the
    new state 'rises up' only for r > 0. RK4; the logistic solution gives the time to reach r/2: ln((r - x0)/x0)/r."""
    out = {}; okV = True; okH = True
    for r in P["r_values"]:
        x = P["x0"]; t = 0.0; th = None; f = lambda x: r * x - x * x; h = P["dt"]
        for k in range(P["steps"]):
            k1 = f(x); k2 = f(x + h * k1 / 2); k3 = f(x + h * k2 / 2); k4 = f(x + h * k3); x += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6; t += h
            if th is None and r > 0 and x >= r / 2: th = t
        exact = max(r, 0.0); an = (np.log((r - P["x0"]) / P["x0"]) / r) if r > 0 else None
        out[str(r)] = dict(final=x, expected=exact, t_half=th, t_half_exact=an)
        okV &= abs(x - exact) <= P["tol"] if r > 0 else x <= P["x0"]
        if r > 0: okH &= th is not None and abs(th - an) <= P["h1"] * an
    rs = [r for r in P["r_values"] if r > 0]; ratio = out[str(min(rs))]["t_half"] / out[str(max(rs))]["t_half"]
    return out, [chk("V1", f"final state = max(r, 0) (r > 0 within {P['tol']}; r <= 0 decays below x0)", out, bool(okV), "validation"),
                 chk("H1", f"time to r/2 within {P['h1']*100:.0f}% of ln((r-x0)/x0)/r", out, bool(okH), "hypothesis"),
                 chk("H2", f"onset slows near the threshold: t_half(smallest r) / t_half(largest r) > {P['h2']}", ratio, ratio > P["h2"], "hypothesis"),
                 chk("R1", "values", out, True, "reporting")]

def saddle_bottleneck(P, rng):
    """Saddle-node normal form dx/dt = r + x^2 (cf. P22's saddle-node bifurcation) just past the bifurcation (r > 0): passage time
    from -L to +L; exact 2 arctan(L/sqrt r)/sqrt r, i.e. ~ pi r^(-1/2) as r -> 0 (the 'bottleneck' behind slow onsets)."""
    out = {}; ok = True
    for r in P["r_values"]:
        x = -P["L"]; t = 0.0; h = P["dt"]; f = lambda x: r + x * x
        while x < P["L"]:
            k1 = f(x); k2 = f(x + h * k1 / 2); k3 = f(x + h * k2 / 2); k4 = f(x + h * k3); x += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6; t += h
        ex = 2 * np.arctan(P["L"] / np.sqrt(r)) / np.sqrt(r); out[str(r)] = dict(T=t, exact=ex); ok &= abs(t - ex) <= P["tol"] * ex
    lr = np.log(P["r_values"]); lt = np.log([out[str(r)]["T"] for r in P["r_values"]]); sl = float(np.polyfit(lr, lt, 1)[0])
    return dict(times=out, slope=sl), [chk("V1", f"passage time within {P['tol']*100:.1f}% of 2 arctan(L/sqrt r)/sqrt r", out, bool(ok), "validation"),
            chk("H1", f"log-log slope of passage time on r within {P['h1']} of -1/2", sl, abs(sl + 0.5) <= P["h1"], "hypothesis"),
            chk("R1", "values", out, True, "reporting")]

def transcritical_noise(P, rng):
    """P22 Eq. 8.8 with additive noise (Euler-Maruyama, reflecting at 0): dx = (r x - x^2) dt + sigma dW from x0. Onset time = first
    time x >= r/2. Compared with the deterministic logistic time ln((r - x0)/x0)/r."""
    k = P["tol_se"]; r = P["r"]; T = []
    for _ in range(P["reps"]):
        x = P["x0"]; t = 0.0; sq = P["sigma"] * np.sqrt(P["dt"])
        while x < r / 2 and t < P["tmax"]:
            x = abs(x + (r * x - x * x) * P["dt"] + sq * rng.standard_normal()); t += P["dt"]
        T.append(t)
    T = np.array(T); m = float(T.mean()); se = float(T.std(ddof=1) / np.sqrt(len(T))); det = float(np.log((r - P["x0"]) / P["x0"]) / r); cv = float(T.std(ddof=1) / m)
    res = dict(mean_onset=m, se=se, deterministic=det, cv=cv, min=float(T.min()), max=float(T.max()), censored=int((T >= P["tmax"]).sum()))
    return res, [chk("V1", "no run censored at tmax", res["censored"], res["censored"] == 0, "validation"),
                 chk("H1", f"noise advances onset from a tiny seed: mean below deterministic by > {k} SE", [m, se, det], det - m > k * se, "hypothesis"),
                 chk("H2", f"onset timing varies: coefficient of variation > {P['h2']}", cv, cv > P["h2"], "hypothesis"),
                 chk("R1", "values", res, True, "reporting")]

def nucleation(P, rng):
    """Cluster-size random walk for classical nucleation (P37): free energy dG_n = A n^(2/3) - B n (units of kT). Attachment rate 1,
    detachment rate exp(dG_n - dG_(n-1)) (detailed balance; agent's kinetic choice, not P37's). n* = (2A/(3B))^3 and
    G* = 4A^3/(27 B^2) (P37). mode 'mfpt': simulated mean first-passage time from n = 1 to N_end vs the exact birth-death sum;
    mode 'scaling': exact MFPT for several B vs exp(G*); mode 'commit': share of walks started at round(n*) that reach N_end before 1."""
    A = P["A"]
    def G(n, B): return A * n ** (2 / 3) - B * n
    def rates(B, N):
        n = np.arange(1, N + 1, dtype=float); up = np.ones(N); dn = np.exp(G(n, B) - G(np.maximum(n - 1, 1), B)); dn[0] = 0.0; return up, dn
    def exact(B, N):
        up, dn = rates(B, N)
        w = np.cumprod(np.r_[1.0, up[:-1] / np.where(dn[1:] > 0, dn[1:], 1)])   # stationary weights pi_n (relative)
        return float(sum(np.sum(w[: k + 1]) / (up[k] * w[k]) for k in range(N - 1)))
    if P["mode"] == "mfpt":
        B = P["B"]; N = P["N_end"]; up, dn = rates(B, N); T = []
        for _ in range(P["reps"]):
            n, t = 1, 0.0
            while n < N:
                tot = up[n - 1] + dn[n - 1]; t += rng.exponential(1 / tot); n += 1 if rng.random() < up[n - 1] / tot else -1
            T.append(t)
        T = np.array(T); m = float(T.mean()); se = float(T.std(ddof=1) / np.sqrt(len(T))); ex = exact(B, N); ns = (2 * A / (3 * B)) ** 3; gs = 4 * A ** 3 / (27 * B ** 2)
        nn = np.arange(1, N + 1); num_ns = int(nn[np.argmax(G(nn, B))])
        res = dict(n_star=ns, n_star_grid=num_ns, G_star=gs, mean_T=m, se=se, exact=ex)
        return res, [chk("V1", "grid maximum of dG_n within 1 of n* = (2A/3B)^3", [ns, num_ns], abs(num_ns - ns) <= 1, "validation"),
                     chk("H1", f"simulated MFPT within {P['tol_se']} SE of the exact birth-death value", [m, se, ex], abs(m - ex) <= P["tol_se"] * se, "hypothesis"),
                     chk("R1", "values", res, True, "reporting")]
    if P["mode"] == "scaling":
        out = {}
        for B in P["B_values"]:
            ns = (2 * A / (3 * B)) ** 3; N = int(np.ceil(P["end_factor"] * ns)); out[str(B)] = dict(G_star=4 * A ** 3 / (27 * B ** 2), T=exact(B, N), N_end=N)
        g = [out[str(B)]["G_star"] for B in P["B_values"]]; lt = [np.log(out[str(B)]["T"]) for B in P["B_values"]]; sl = float(np.polyfit(g, lt, 1)[0])
        return dict(by_B=out, slope=sl), [chk("V1", "MFPT increases with the barrier", lt, all(np.diff(lt) * np.sign(np.diff(g)) > 0), "validation"),
                chk("H1", f"slope of ln MFPT on G* within {P['h1']} of 1 (Arrhenius-like exp(G*))", sl, abs(sl - 1) <= P["h1"], "hypothesis"), chk("R1", "values", out, True, "reporting")]
    B = P["B"]; N = P["N_end"]; up, dn = rates(B, N); n0 = int(round((2 * A / (3 * B)) ** 3)); hit = 0
    for _ in range(P["reps"]):
        n = n0
        while 1 < n < N: n += 1 if rng.random() < up[n - 1] / (up[n - 1] + dn[n - 1]) else -1
        hit += n >= N
    ph = hit / P["reps"]; se = float(np.sqrt(ph * (1 - ph) / P["reps"]))
    return dict(n0=n0, share_growing=ph, se=se), [chk("V1", "share is a probability", ph, 0 <= ph <= 1, "validation"),
            chk("H1", f"a cluster at the critical size grows with probability within {P['h1']} of 1/2", ph, abs(ph - 0.5) <= P["h1"], "hypothesis"), chk("R1", "values", ph, True, "reporting")]

def thermal_explosion(P, rng):
    """P38 (Novozhilov 2016) Eq. 1 with m = 0 (planar slab) and Eq. 2: d theta/d tau = (1/delta) theta_xixi + exp(theta/(1 + Ar theta)),
    theta_xi(0) = 0, theta(1, tau) = A0 sin(omega tau), theta(xi, 0) = 0 (initial condition is the agent's; not stated in the text read).
    Semi-implicit finite differences (diffusion implicit, source explicit; agent's scheme, P38 used Crank-Nicolson). Runaway = max theta
    exceeds P['thr'] before tau_max (agent's criterion; P38 used an inflection-point criterion). Modes: 'static' bisects delta at A0 = 0 and
    compares with the exact steady critical value (theta(0) = m, delta = 2 e^-m arccosh(e^(m/2))^2 maximised over m; standard result, P38
    states 0.88); 'acrit' bisects the critical amplitude A0 for each omega (or delta, or Ar) in a list; 'history' runs one amplitude and
    counts the oscillation maxima of theta(0) before runaway."""
    from scipy.linalg import solve_banded
    M = P.get("M", 40); h = 1.0 / M; dt = P.get("dt", 0.002); thr = P.get("thr", 15.0)
    def run(delta, Ar, A0, om, tmax, record=False):
        a = dt / (delta * h * h); n = M
        ab = np.zeros((3, n)); ab[1, :] = 1 + 2 * a; ab[0, 1:] = -a; ab[2, :-1] = -a; ab[0, 1] = -2 * a
        th = np.zeros(M + 1); t = 0.0; hist = []
        while t < tmax:
            t += dt; bnd = A0 * np.sin(om * t)
            src = np.exp(th[:-1] / (1 + Ar * th[:-1])) if Ar > 0 else np.exp(np.minimum(th[:-1], 50))
            rhs = th[:-1] + dt * src; rhs[-1] += a * bnd
            th[:-1] = solve_banded((1, 1), ab, rhs); th[-1] = bnd
            if record: hist.append(th[0])
            if th.max() > thr: return True, t, hist
        return False, t, hist
    def bisect(f, lo, hi, it):
        for _ in range(it):
            mid = 0.5 * (lo + hi)
            if f(mid): hi = mid
            else: lo = mid
        return 0.5 * (lo + hi)
    mm = np.linspace(0.01, 6, 60000); dd = 2 * np.exp(-mm) * np.arccosh(np.exp(mm / 2)) ** 2; dcr = float(dd.max())
    if P["mode"] == "static":
        d = bisect(lambda x: run(x, P["Ar"], 0.0, 1.0, P["tmax"])[0], 0.5, 1.2, P["iters"])
        res = dict(delta_cr_exact=dcr, delta_cr_sim=d, source_value=0.88)
        return res, [chk("V1", "exact steady critical delta (planar) within 0.005 of P38's stated 0.88", [dcr, 0.88], abs(dcr - 0.88) <= 0.005),
                     chk("H1", f"simulated critical delta within {P['tol']} of the exact value", [d, dcr], abs(d - dcr) <= P["tol"], "hypothesis"),
                     chk("R1", "values", res, True, "reporting")]
    if P["mode"] == "acrit":
        var = P["vary"]; out = {}
        for v in P["values"]:
            q = dict(delta=P.get("delta"), Ar=P.get("Ar"), om=P.get("omega")); q[var] = v
            tmax = max(P["tmax"], 2 * 2 * np.pi / q["om"])
            out[str(v)] = bisect(lambda A: run(q["delta"], q["Ar"], A, q["om"], tmax)[0], P["lo"], P["hi"], P["iters"])
        vals = [out[str(v)] for v in P["values"]]
        res = dict(vary=var, critical_A0=out)
        c = [chk("V1", "critical amplitudes inside the search bracket", vals, all(P["lo"] + 1e-3 < x < P["hi"] - 1e-3 for x in vals))]
        o = dict(v=list(P["values"]), a=vals, np=np)
        c.append(chk("H1", P["h1_text"], vals, bool(eval(P["h1_expr"], {}, o)), "hypothesis"))
        if var == "om" and len(vals) > 2:
            r = np.corrcoef(P["values"], vals)[0, 1] ** 2; res["r2_linear"] = float(r)
        c.append(chk("R1", "values", res, True, "reporting")); return res, c
    boom, t, hist = run(P["delta"], P["Ar"], P["A0"], P["omega"], P["tmax"], record=True)
    hh = np.array(hist); peaks = int(np.sum((hh[1:-1] > hh[:-2]) & (hh[1:-1] >= hh[2:]))) if len(hh) > 2 else 0
    res = dict(runaway=boom, t_runaway=t, maxima_before=peaks, period=2 * np.pi / P["omega"])
    return res, [chk("V1", "simulation ran", t, t > 0), chk("H1", P["h1_text"], [boom, peaks], bool(eval(P["h1_expr"], {}, dict(boom=boom, peaks=peaks, t=t))), "hypothesis"),
                 chk("R1", "values", res, True, "reporting")]

def hill_binding(P, rng):
    """P46 (Jakubowski, LibreTexts C3 'Hill Plot'): Hill equation Y = L^n/(Kd + L^n), Kd = P50^n; Hill plot log(Y/(1-Y)) vs log L.
    Agent's comparator: a 4-site Adair (stepwise) binding polynomial with agent-chosen stepwise association constants K1..K4
    (increasing affinity) and an independent-sites control (statistical factors 4, 3/2, 2/3, 1/4 times one site constant).
    Hill slope n_H = d log(Y/(1-Y)) / d log L computed by finite differences on a log grid."""
    def Y(L, K):
        p = np.cumprod(K)[None, :] * L[:, None] ** np.arange(1, 5)[None, :]
        return (p * np.arange(1, 5)).sum(1) / (4 * (1 + p.sum(1)))
    def slopes(K):
        lg = np.linspace(-8, 8, 16001); L = 10 ** lg; y = Y(L, np.array(K, float)); h = np.log10(y / (1 - y))
        s = np.gradient(h, lg); i50 = np.argmin(abs(y - 0.5)); p50 = lg[i50]
        lo = s[np.argmin(abs(lg - (p50 - 4)))]; hi = s[np.argmin(abs(lg - (p50 + 4)))]; im = np.argmax(s)
        return dict(log10_P50=float(p50), slope_low=float(lo), slope_high=float(hi), slope_max=float(s[im]), log10_L_at_max=float(lg[im]), monotone=bool(np.all(np.diff(y) >= -1e-15)))
    coop = slopes(P["K_coop"]); k = P["k_site"]; ind = slopes([4 * k, 1.5 * k, k * 2 / 3, k / 4])
    n = P["n_hill"]; p50 = P["P50"]; yh = p50 ** n / (p50 ** n + p50 ** n)
    res = dict(cooperative=coop, independent=ind, hill_check=dict(n=n, P50=p50, Kd=p50 ** n, Y_at_P50=yh))
    return res, [chk("V1", "binding curves monotone and the Hill equation with Kd = P50^n gives Y(P50) = 0.5 (P46 Eq. 4)", [coop["monotone"], ind["monotone"], yh], coop["monotone"] and ind["monotone"] and abs(yh - 0.5) < 1e-12),
                 chk("H1", "cooperative Hill plot: end slopes within 0.05 of 1 (P46: ends approach slopes of 1)", [coop["slope_low"], coop["slope_high"]], abs(coop["slope_low"] - 1) <= 0.05 and abs(coop["slope_high"] - 1) <= 0.05, "hypothesis"),
                 chk("H2", "maximum slope between 1 and 4 and within 0.5 log units of P50 (P46: maximal cooperativity in the middle)", [coop["slope_max"], coop["log10_L_at_max"], coop["log10_P50"]], 1 < coop["slope_max"] < 4 and abs(coop["log10_L_at_max"] - coop["log10_P50"]) <= 0.5, "hypothesis"),
                 chk("H3", "independent identical sites: slope within 0.01 of 1 everywhere (P46: n = 1 when affinity does not change)", [ind["slope_max"], ind["slope_low"]], abs(ind["slope_max"] - 1) < 0.01 and abs(ind["slope_low"] - 1) < 0.01, "hypothesis"),
                 chk("R1", "values", res, True, "reporting")]


def mwc_binding(P, rng):
    """P53 (Eaton 2022, J Chem Phys 157:184104, CC BY): MWC partition function for 4 equivalent subunits, Eq. (4):
    Xi = L (1 + K_T p)^4 + (1 + K_R p)^4, and the tertiary two-state (TTS) model, Eq. (13), read by the agent as
    Xi = (L / l_T^4) [(1 + K_r p) + l_T (1 + K_t p)]^4 + [(1 + K_r p) + l_R (1 + K_t p)]^4 (the fraction layout is lost in the
    extracted text; agent's reading, consistent with P53's definition of L as the all-t T / all-r R population ratio).
    Saturation y = (1/4) d ln Xi / d ln p (P53 Eq. 5); Hill slope d log(y/(1-y)) / d log p by finite differences."""
    def lnXi(lp, prm, L, part="both"):
        p = 10.0 ** lp
        if P["model"] == "MWC":
            T = np.log(L) + 4 * np.log1p(prm["K_T"] * p); R = 4 * np.log1p(prm["K_R"] * p)
        else:
            lT, lR, Kt, Kr = prm["l_T"], prm["l_R"], prm["K_t"], prm["K_r"]
            T = np.log(L) - 4 * np.log(lT) + 4 * np.log((1 + Kr * p) + lT * (1 + Kt * p)); R = 4 * np.log((1 + Kr * p) + lR * (1 + Kt * p))
        if part == "T": return T
        if part == "R": return R
        return np.logaddexp(T, R)
    lg = np.linspace(-6, 8, 14001)
    def curve(L, part="both"):
        ln = lnXi(lg, P["params"], L, part); y = np.gradient(ln, lg * np.log(10)) / 4
        y = np.clip(y, 1e-300, 1 - 1e-16); h = np.log10(y / (1 - y)); s = np.gradient(h, lg)
        i50 = int(np.argmin(abs(y - 0.5))); p50 = lg[i50]; inner = slice(50, -50)
        lo = s[np.argmin(abs(lg - (p50 - 4)))]; hi = s[np.argmin(abs(lg - (p50 + 4)))]; im = int(np.argmax(s[inner])) + 50
        ok = (y > 1e-6) & (y < 1 - 1e-6); ok[:50] = False; ok[-50:] = False
        return dict(log10_P50=float(p50), P50=float(10 ** p50), slope_low=float(lo), slope_high=float(hi), slope_max=float(s[im]), log10_p_at_max=float(lg[im]),
                    monotone=bool(np.all(np.diff(y[inner]) >= -1e-12)), y_min=float(y[inner].min()), y_max=float(y[inner].max())), s[ok]
    main, _ = curve(P["L"]); byL = {str(L): curve(L)[0] for L in P["L_values"]}
    _, sT = curve(P["L"], "T"); _, sR = curve(P["L"], "R"); dT = float(np.max(abs(sT - 1))); dR = float(np.max(abs(sR - 1)))
    spread = max(v["slope_max"] for v in byL.values()) - min(v["slope_max"] for v in byL.values())
    res = dict(model=P["model"], main=main, by_L=byL, T_only_max_dev=dT, R_only_max_dev=dR, nmax_spread_over_L=spread, n_ref=P["n_ref"])
    return res, [chk("V1", "saturation monotone within (0, 1); T-only and R-only partition functions give Hill slope 1 within 0.01 where 1e-6 < y < 1 - 1e-6 (non-cooperative within each quaternary state, P53)", [main["monotone"], main["y_min"], main["y_max"], dT, dR], main["monotone"] and 0 <= main["y_min"] and main["y_max"] <= 1 and dT < 0.01 and dR < 0.01),
                 chk("H1", "end slopes of the Hill plot within 0.05 of 1", [main["slope_low"], main["slope_high"]], abs(main["slope_low"] - 1) <= 0.05 and abs(main["slope_high"] - 1) <= 0.05, "hypothesis"),
                 chk("H2", f"maximum Hill slope within {P['tol_n']} of n = {P['n_ref']} (P46's fitted value for haemoglobin)", [main["slope_max"], P["n_ref"]], abs(main["slope_max"] - P["n_ref"]) <= P["tol_n"], "hypothesis"),
                 chk("H3", "changing only L (as heterotropic effectors do in MWC) changes the maximum Hill slope by more than 0.1 across the L values (P53: n is not independent of conditions)", byL, spread > 0.1, "hypothesis"),
                 ] + (_hyps(P, res, 4) if P.get("hyps") else []) + [chk("R1", "values", res, True, "reporting")]


def adair_identify(P, rng):
    """P55 (Benndorf & Schulz 2023, J Gen Physiol 155:e202313423, CC BY-NC-SA): identifiability of equilibrium constants from noisy
    concentration-response data; noise n = A * R * y * (1 - y), R ~ U(-1, 1) (P55 Eq. 9, A = 0.25); seven concentrations equally spaced
    on a log scale between y = 0.01 and 0.99, five points each (P55 'Simulation of data points'). Agent's application: one 4-site Adair
    binding curve (stepwise constants K1..K4), refitted by least squares in log K from the true start (as P55's first analysis), reps times.
    Imprecision of each constant = SD of fitted log10 K (agent's measure; P55 uses relative SD). Also P55's counting rules
    n_p = 2^n - 1 + 2n and n_CAR = 2^n for n = 2..5 (P55 Eqs. 20-21)."""
    from scipy.optimize import least_squares, brentq
    K = np.array(P["K_true"], float)
    def Y(L, lk):
        k = 10.0 ** lk; c = np.cumprod(k); p = c[None, :] * L[:, None] ** np.arange(1, 5)[None, :]
        return (p * np.arange(1, 5)).sum(1) / (4 * (1 + p.sum(1)))
    lk0 = np.log10(K)
    f = lambda lx, y: Y(np.array([10 ** lx]), lk0)[0] - y
    lo, hi = brentq(f, -10, 10, args=(0.01,)), brentq(f, -10, 10, args=(0.99,))
    Lc = 10 ** np.linspace(lo, hi, P["n_conc"]); Lr = np.repeat(Lc, P["n_rep"]); y0 = Y(Lr, lk0)
    fit0 = least_squares(lambda lk: Y(Lr, lk) - y0, lk0 + 0.3, method="lm").x
    v_err = float(np.max(abs(fit0 - lk0)))
    def nmax(lk):
        lg = np.linspace(lo - 3, hi + 3, 3001); y = Y(10 ** lg, lk); h = np.log10(y / (1 - y)); return float(np.max(np.gradient(h, lg)))
    fits = []; nm = []; fail = 0
    for _ in range(P["reps"]):
        y = y0 + P["A"] * rng.uniform(-1, 1, len(y0)) * y0 * (1 - y0)
        r = least_squares(lambda lk: Y(Lr, lk) - y, lk0, method="trf", bounds=(lk0 - 8, lk0 + 8))
        if not r.success: fail += 1; continue
        fits.append(r.x); nm.append(nmax(r.x))
    F = np.array(fits); sd = F.std(0); bias = F.mean(0) - lk0
    counts = {n: [2 ** n - 1 + 2 * n, 2 ** n] for n in range(2, 6)}
    nm = np.array(nm); n_true = nmax(lk0)
    res = dict(log10_K_true=lk0.tolist(), sd_log10K=sd.tolist(), bias_log10K=bias.tolist(), n_fits=len(fits), n_fail=fail, nmax_true=n_true,
               nmax_mean=float(nm.mean()), nmax_cv=float(nm.std() / nm.mean()), counts=counts, noise_free_max_err=v_err)
    return res, [chk("V1", "noise-free refit recovers the true log K within 1e-4 and P55's counts n_p = 7, 13, 23, 41 and n_CAR = 4, 8, 16, 32", [v_err, counts], v_err < 1e-4 and [c[0] for c in counts.values()] == [7, 13, 23, 41] and [c[1] for c in counts.values()] == [4, 8, 16, 32]),
                 chk("H1", "the first and last constants are less precise than the middle ones: min(sd K1, sd K4) > max(sd K2, sd K3) (P55: Z1 and Zmax more uncertain)", sd.tolist(), min(sd[0], sd[3]) > max(sd[1], sd[2]), "hypothesis"),
                 chk("H2", "the maximal Hill slope is well determined (CV < 0.1) even when individual constants are not", [float(nm.std() / nm.mean()), float(sd.max())], nm.std() / nm.mean() < 0.1, "hypothesis"),
                 chk("R1", "values", res, True, "reporting")]

def _hyps(P, res, start=1):
    return [chk(f"H{i}", t, res, bool(eval(e, dict(o=res, abs=abs, all=all, any=any, min=min, max=max, len=len))), "hypothesis") for i, (t, e) in enumerate(P["hyps"], start)]

def mixture_hill(P, rng):
    """Hill plot of a sum of independent non-cooperative components, y(p) = sum_i f_i p / (p + K_i) (P62's two-component analysis of
    gel-trapped anion-free T-state haemoglobin), compared with alternative component sets (e.g. the TTS prediction quoted in P62).
    Agent's computation; slopes are d log(y/(1-y)) / d log p on a fine grid."""
    lp = np.linspace(np.log10(P.get("p_lo", 1e-3)), np.log10(P.get("p_hi", 1e5)), 8001); p = 10 ** lp
    def curve(comp):
        f = np.array([c[0] for c in comp], float); K = np.array([c[1] for c in comp], float); f = f / f.sum()
        y = (f[None, :] * p[:, None] / (p[:, None] + K[None, :])).sum(1); ok = (y > 1e-9) & (y < 1 - 1e-9)
        h = np.log(y / (1 - y)); n = np.gradient(h, np.log(p)); n = n[ok]
        i50 = int(np.argmin(abs(y - 0.5)))
        return dict(P50=float(p[i50]), n_min=float(n.min()), n_max=float(n.max()), n_at_P50=float(n[np.argmin(abs(y[ok] - 0.5))]), n_low=float(n[0]), n_high=float(n[-1]))
    res = {k: curve(v) for k, v in P["sets"].items()}
    single = curve([[1.0, 7.0]])
    return res, [chk("V1", "a single non-cooperative component has slope 1 everywhere (within 1e-3) and P50 = K (within 1%)", single, abs(single["n_min"] - 1) < 1e-3 and abs(single["n_max"] - 1) < 1e-3 and abs(single["P50"] / 7.0 - 1) < 0.01)] + _hyps(P, res) + [chk("R1", "values", res, True, "reporting")]

def sync_cheaters(P, rng):
    """Sakaguchi-Kuramoto two-group model of P68 (Amichay, Gong & Abrams 2026), Eq. 1 with identical frequencies (omega = 0):
    cooperators (lag 0) and cheaters (lag alpha). From the two-cluster state (cooperators at 0, cheaters at alpha, plus noise) the
    N-oscillator system is integrated (RK4, mean-field sums) and the cluster gap and order parameter R recorded; P68's bound
    n_ch < 1/(1 - cos alpha) is compared. Optional replicator part: P68 Eq. 8 with P68's closed-form payoffs g(R) = R,
    f = 1 - cos(dtheta)."""
    N, K, T, dt, eps = P["N"], P.get("K", 1.0), P["T"], P["dt"], P.get("eps", 0.05)
    wf = 0.0   # CVB extension: optional non-identical natural frequencies (freq_sd, centred Gaussian quantiles) for the lag grid only
    def run(alpha, nch, th0=None, al=None):
        m = int(round(nch * N)); a = np.zeros(N) if al is None else al.copy()
        if al is None: a[:m] = alpha
        th = (np.where(np.arange(N) < m, alpha, 0.0) + eps * rng.standard_normal(N)) if th0 is None else th0.copy()
        def f(t):
            z = np.exp(1j * t).mean(); return wf + K * np.imag(np.exp(1j * (a - t)) * z)
        for _ in range(int(T / dt)):
            k1 = f(th); k2 = f(th + dt / 2 * k1); k3 = f(th + dt / 2 * k2); k4 = f(th + dt * k3); th = th + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        z = np.exp(1j * th); R = float(abs(z.mean()))
        if m == 0 or m == N: return dict(R=R)
        zc, zh = z[m:].mean(), z[:m].mean(); gap = float(np.angle(zh / zc))
        return dict(R=round(R, 6), gap=round(gap, 6), spread_co=round(float(1 - abs(zc)), 6), spread_ch=round(float(1 - abs(zh)), 6),
                    two_cluster=bool(abs(gap - alpha) < 0.05 and abs(zc) > 0.99 and abs(zh) > 0.99))
    grid = {}
    if P.get("freq_sd"):
        from scipy.stats import norm as _n; wf = _n.ppf((np.arange(N) + 0.5) / N) * P["freq_sd"]; wf = wf[rng.permutation(N)]
    for alpha in P["alphas"]:
        b = 1 / (1 - np.cos(alpha))
        for nch in P["n_ch_values"]:
            r = run(alpha, nch); r["bound"] = round(float(b), 6); r["below_bound"] = bool(nch < b); grid[f"a{alpha:.4f}_n{nch}"] = r
    res = dict(grid=grid)
    wf = 0.0
    def repl(rp):
        al, n, k, Tg, dtg = rp["alpha"], rp["n0"], rp.get("k", 1.0), rp["T"], rp.get("dt", 0.01)
        for _ in range(int(Tg / dtg)):
            Z = (1 - n) + n * np.exp(1j * al); R, ph = abs(Z), np.angle(Z)
            pco, pch = R * (1 - np.cos(ph)), R * (1 - np.cos(al - ph)); pb = (1 - n) * pco + n * pch
            n = n + dtg * k * n * (pch - pb)
        return dict(alpha=al, n0=rp["n0"], n_end=round(float(n), 6))
    if P.get("replicator"): res["replicator"] = repl(P["replicator"])
    if P.get("replicators"): res["replicators"] = [repl(rp) for rp in P["replicators"]]   # CVA extension: several (alpha, n0)
    th0 = rng.uniform(0, 2 * np.pi, N); v = run(0.0, 0.0, th0=th0, al=np.zeros(N))
    res["V1_R_classical"] = round(v["R"], 6)
    return res, [chk("V1", "classical Kuramoto (all lags 0, identical frequencies, K > 0) synchronises from random phases: R > 0.99 at T", v["R"], v["R"] > 0.99)] + _hyps(P, res, 1) + [chk("R1", "values", res, True, "reporting")]

def zfel_null(P, rng):
    """P74 (Berger et al. 2026) null model of molecular convergence (Zero-Force Evolutionary Law): each of n loci in each of two
    independently evolving lineages is a two-state Markov chain (0 -> 1 with P_gain, 1 -> 0 with P_loss per step), steady state
    S = P_gain / (P_gain + P_loss) (P74 Eq. 1); the expected chance overlap is the product of the proportions of ones, S^2 at
    equilibrium. Simulated overlap over time is compared with the analytic S(t)^2, S(t) = S + (S0 - S)(1 - P_gain - P_loss)^t.
    Also reports the pair/quartet combinatorics P74 prints."""
    n, S0, S, reps = P["n_loci"], P["S0"], P["S"], P.get("reps", 20)
    from math import comb
    out = {}
    for pl in P["P_loss"]:
        pg = S * pl / (1 - S); lam = 1 - pg - pl; ts = P["t_report"]
        an = {str(t): (S + (S0 - S) * lam ** t) ** 2 for t in ts}; sim = {str(t): [] for t in ts}
        for _ in range(reps):
            x = [(rng.random(n) < S0).astype(np.int8) for _ in range(2)]; t0 = 0
            for t in sorted(ts):
                for _ in range(t - t0):
                    for i in range(2):
                        u = rng.random(n); x[i] = np.where(x[i] == 1, (u >= pl).astype(np.int8), (u < pg).astype(np.int8))
                t0 = t; sim[str(t)].append(float(x[0].mean() * x[1].mean()))
        out[f"Ploss{pl}"] = dict(P_gain=round(pg, 8), analytic={k: round(v, 6) for k, v in an.items()},
                                 sim_mean={k: round(float(np.mean(v)), 6) for k, v in sim.items()}, sim_se={k: round(float(np.std(v, ddof=1) / np.sqrt(len(v))), 6) for k, v in sim.items()})
    res = dict(runs=out, S0_sq=round(S0 ** 2, 6), S_sq=round(S ** 2, 6))
    if P.get("combinatorics"):
        c = P["combinatorics"]; ns = c["n_species"]; out2 = {}
        for m in ns:
            pairs = comb(m, 2); p_overlap = 1 - comb(m - 2, 2) / comb(m, 2)
            out2[str(m)] = dict(pairs=pairs, disjoint_pair_of_pairs=pairs * comb(m - 2, 2) // 2, expected_disjoint_in_sample=round(c["samples"] * comb(c["pairs_per_sample"], 2) * (1 - p_overlap), 1))
        res["combinatorics"] = dict(by_n=out2, sampled_quartets=c["samples"] * comb(c["pairs_per_sample"], 2))
    pg, pl = 0.3, 0.2; T2 = np.array([[1 - pg, pg], [pl, 1 - pl]]); w, v = np.linalg.eig(T2.T); e = np.real(v[:, np.argmin(abs(w - 1))]); e = e / e.sum()
    ok = abs(e[1] - pg / (pg + pl)) < 1e-12
    return res, [chk("V1", "two-state chain: stationary P(1) equals P_gain / (P_gain + P_loss) (P74 Eq. 1) within 1e-12", float(e[1]), ok)] + _hyps(P, res, 1) + [chk("R1", "values", res, True, "reporting")]

def kuramoto_hetero(P, rng):
    """P76 (Wikipedia 'Kuramoto model'): all-to-all Kuramoto model d theta_i/dt = omega_i + (K/N) sum_j sin(theta_j - theta_i) with
    heterogeneous natural frequencies. Frequencies are deterministic quantiles of a Lorentzian (half-width gamma, clipped at
    +-clip*gamma) or Gaussian (sd sigma) g. Reports the time-averaged order parameter r over the second half of [0, T] for each K,
    next to P76's K_c = 2/(pi g(0)), the self-consistency solution r = rK int cos^2 g(Kr sin) and P76's small-mu approximation
    r ~ sqrt(16/(pi K_c^3)) sqrt(mu/(-g''(0))). Optional N = 2 locking test (P76: locked iff K > K_c = 2|omega_1|)."""
    from scipy.stats import norm
    from scipy.optimize import brentq
    N, dist, w, T, dt = P["N"], P["dist"], P["width"], P["T"], P["dt"]
    u = (np.arange(N) + 0.5) / N
    if dist == "lorentz":
        om = w * np.tan(np.pi * (u - 0.5)); om = np.clip(om, -P.get("clip", 50) * w, P.get("clip", 50) * w)
        g = lambda x: w / (np.pi * (x * x + w * w)); g2 = -2 / (np.pi * w ** 3)
    else:
        om = norm.ppf(u) * w; g = lambda x: np.exp(-x * x / (2 * w * w)) / (w * np.sqrt(2 * np.pi)); g2 = -1 / (w ** 3 * np.sqrt(2 * np.pi))
    Kc = 2 / (np.pi * g(0.0))
    def sim(K, om, th):
        f = lambda t: om + K * np.imag(np.exp(1j * t).mean() * np.exp(-1j * t))
        rs = []
        for s in range(int(T / dt)):
            k1 = f(th); k2 = f(th + dt / 2 * k1); k3 = f(th + dt / 2 * k2); k4 = f(th + dt * k3); th = th + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            if s * dt >= T / 2: rs.append(abs(np.exp(1j * th).mean()))
        return float(np.mean(rs)), th
    th = rng.uniform(0, 2 * np.pi, N); xs = np.linspace(-np.pi / 2, np.pi / 2, 4001)
    def sc(K):
        F = lambda r: K * np.trapezoid(np.cos(xs) ** 2 * g(K * r * np.sin(xs)), xs) - 1
        return 0.0 if K <= Kc * (1 + 1e-9) or F(1.0) > 0 else float(brentq(F, 1e-9, 1.0))
    out = {}
    for K in P["K_values"]:
        r, _ = sim(K, om, th.copy()); mu = K / Kc - 1
        out[str(K)] = dict(r_sim=round(r, 5), r_selfconsistent=round(sc(K), 5), r_small_mu=round(float(np.sqrt(16 / (np.pi * Kc ** 3)) * np.sqrt(mu / -g2)), 5) if mu > 0 else 0.0,
                           r_lorentz_exact=round(float(np.sqrt(1 - Kc / K)), 5) if (dist == "lorentz" and K > Kc) else (0.0 if dist == "lorentz" else None))
    res = dict(Kc=round(float(Kc), 6), N=N, dist=dist, width=w, by_K=out)
    if P.get("pair"):
        pr = P["pair"]; lk = {}
        for K in pr["K_values"]:
            o2 = np.array([pr["w"], -pr["w"]]); th2 = np.array([0.0, np.pi / 2]); TT = pr.get("T", 400); d2 = 0.01
            f2 = lambda t: o2 + K / 2 * np.sin(t[::-1] - t)
            for s in range(int(TT / d2)):
                k1 = f2(th2); k2 = f2(th2 + d2 / 2 * k1); k3 = f2(th2 + d2 / 2 * k2); k4 = f2(th2 + d2 * k3); th2 = th2 + d2 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            dv = f2(th2); lk[str(K)] = dict(freq_diff=round(float(abs(dv[0] - dv[1])), 6), locked=bool(abs(dv[0] - dv[1]) < 1e-3), above_Kc=bool(K > 2 * pr["w"]))
        res["pair"] = lk
    r0, _ = sim(1.0, np.zeros(N), th.copy())
    res["V1_r_identical"] = round(r0, 6)
    return res, [chk("V1", "identical frequencies with K = 1 synchronise from random phases: time-averaged r > 0.99 over the second half", r0, r0 > 0.99)] + _hyps(P, res, 1) + [chk("R1", "values", res, True, "reporting")]

def kuramoto_lyap(P, rng):
    """P76 (Wikipedia 'Kuramoto model') states that chaos first occurs at N = 4 (the N = 3 phase-difference flow lives on a
    2-torus and cannot be chaotic). Agent's test: largest Lyapunov exponent of the all-to-all Kuramoto model for small N, by
    the Benettin method (RK4 on phases and tangent vector, tangent kept orthogonal to the neutral direction (1, ..., 1),
    renormalised every 'renorm' time units), for 'settings' random draws of natural frequencies (uniform on [-1, 1], centred)
    at each coupling K. Reports per-N maxima and the fraction of settings with exponent above 'thr'."""
    T, dt, ev, thr = P["T"], P["dt"], P.get("renorm", 1.0), P["thr"]
    def lyap(om, K, N):
        def f(th): d = th[None, :] - th[:, None]; return om + K / N * np.sin(d).sum(1)
        def J(th): d = th[None, :] - th[:, None]; C = K / N * np.cos(d); np.fill_diagonal(C, 0.0); return C - np.diag(C.sum(1))
        th = rng.uniform(0, 2 * np.pi, N); v = rng.standard_normal(N); one = np.ones(N) / np.sqrt(N)
        v -= v.dot(one) * one; v /= np.linalg.norm(v); s = 0.0; tt = 0.0; nre = max(1, int(round(ev / dt))); burn = P.get("burn", 100.0)
        for k in range(int(T / dt)):
            k1 = f(th); j1 = J(th) @ v; t2 = th + dt / 2 * k1; k2 = f(t2); j2 = J(t2) @ (v + dt / 2 * j1); t3 = th + dt / 2 * k2; k3 = f(t3); j3 = J(t3) @ (v + dt / 2 * j2)
            t4 = th + dt * k3; k4 = f(t4); j4 = J(t4) @ (v + dt * j3)
            th = th + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4); v = v + dt / 6 * (j1 + 2 * j2 + 2 * j3 + j4)
            if (k + 1) % nre == 0:
                v -= v.dot(one) * one; nv = np.linalg.norm(v); v /= nv
                if (k + 1) * dt > burn: s += np.log(nv); tt += nre * dt
        return s / tt
    out = {}
    for N in P["N_values"]:
        for K in P["K_values"]:
            ls = []
            for _ in range(P["settings"]):
                om = rng.uniform(-1, 1, N); om -= om.mean(); ls.append(lyap(om, K, N))
            out[f"N{N}_K{K}"] = dict(max_lyap=round(float(max(ls)), 5), frac_above_thr=round(float(np.mean(np.array(ls) > thr)), 4), median=round(float(np.median(ls)), 5))
    res = dict(by_case=out, thr=thr)
    om0 = np.zeros(2); l0 = lyap(om0, 1.0, 2)
    res["V1_pair_identical"] = round(float(l0), 5)
    return res, [chk("V1", "N = 2, identical frequencies, K = 1: the transverse exponent equals the analytic -K = -1 within 0.02", l0, abs(l0 + 1.0) < 0.02)] + _hyps(P, res) + [chk("R1", "values", res, True, "reporting")]

def kuramoto_fss(P, rng):
    """P76 (Wikipedia 'Kuramoto model'): finite-size behaviour of the order parameter for i.i.d. random natural frequencies
    (Gaussian, sd 'width'). For each N, 'reps' independent frequency draws and initial phases; r time-averaged over the second
    half of [0, T]. Reports mean r and r sqrt(N) by N for each K, next to the self-consistency r_inf. Agent's computation;
    the N^(-1/2) incoherent scaling is standard finite-size theory, not stated in P76 (foreknown)."""
    from scipy.optimize import brentq
    w, T, dt = P["width"], P["T"], P["dt"]; Kc = 2 / (np.pi * (1 / (w * np.sqrt(2 * np.pi)))); xs = np.linspace(-np.pi / 2, np.pi / 2, 4001)
    g = lambda x: np.exp(-x * x / (2 * w * w)) / (w * np.sqrt(2 * np.pi))
    def sc(K):
        F = lambda r: K * np.trapezoid(np.cos(xs) ** 2 * g(K * r * np.sin(xs)), xs) - 1
        return 0.0 if K <= Kc * (1 + 1e-9) or F(1.0) > 0 else float(brentq(F, 1e-9, 1.0))
    out = {}
    for K in P["K_values"]:
        row = {}
        for N in P["N_values"]:
            rr = []
            for _ in range(P["reps"]):
                om = rng.normal(0, w, N); th = rng.uniform(0, 2 * np.pi, N); acc = []
                f = lambda t: om + K * np.imag(np.exp(1j * t).mean() * np.exp(-1j * t))
                for s in range(int(T / dt)):
                    k1 = f(th); k2 = f(th + dt / 2 * k1); k3 = f(th + dt / 2 * k2); k4 = f(th + dt * k3); th = th + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
                    if s * dt >= T / 2: acc.append(abs(np.exp(1j * th).mean()))
                rr.append(np.mean(acc))
            row[str(N)] = dict(r_mean=round(float(np.mean(rr)), 5), r_sqrtN=round(float(np.mean(rr) * np.sqrt(N)), 4), r_sd=round(float(np.std(rr)), 5))
        out[str(K)] = dict(r_inf=round(sc(K), 5), by_N=row)
    res = dict(Kc=round(float(Kc), 6), by_K=out)
    th = rng.uniform(0, 2 * np.pi, 100000); r0 = abs(np.exp(1j * th).mean())
    return res, [chk("V1", "uniform random phases (N = 100000) give r below 0.02 (expected ~ N^-1/2 = 0.003)", float(r0), r0 < 0.02)] + _hyps(P, res) + [chk("R1", "values", res, True, "reporting")]

def adaptive_walk(P, rng):
    """Adaptive walks on small genotype landscapes (AS0: P85, Li & Zhang 2025). Genotypes of L sites with A states; neighbours
    differ at one site. Landscape models as stated in P85's Methods: RMF F(x) = -D(x, x*) + eta_x, eta ~ N(0.5, sigma), x* a
    random reference genotype; HoC F ~ N(0.5, 0.1) truncated to [0, 1]; NK with K random interacting sites, uniform(0, 1)
    contributions, F = mean. A walk moves to a uniformly chosen fitter neighbour until it reaches a peak (no fitter neighbour;
    P85's SSWM rule). One walk from every genotype. High peaks = the top floor(frac * n_peaks) peaks (at least 1). Basin of a
    peak = genotypes with a monotonically increasing path to it (P85's definition), found by downhill search from the peak.
    Agent's implementation at a smaller size than P85 (P85: 9 four-state sites)."""
    L, A = P["L"], P["A"]; G = A ** L; W = A ** np.arange(L); dig = (np.arange(G)[:, None] // W) % A
    nb = np.stack([np.arange(G) + (((dig[:, j] + s) % A) - dig[:, j]) * W[j] for j in range(L) for s in range(1, A)], 1)
    def land(spec):
        m = spec["model"]
        if m == "rmf":
            xs = int(rng.integers(G)); D = (dig != dig[xs]).sum(1); return -D + rng.normal(0.5, spec["sigma"], G)
        if m == "hoc":
            f = rng.normal(0.5, 0.1, G)
            while ((f < 0) | (f > 1)).any(): bad = (f < 0) | (f > 1); f[bad] = rng.normal(0.5, 0.1, bad.sum())
            return f
        if m == "nk":
            K = spec["K"]; inter = [np.concatenate([[i], rng.choice([j for j in range(L) if j != i], K, replace=False)]) if K else np.array([i]) for i in range(L)]
            tabs = [rng.random(A ** (K + 1)) for _ in range(L)]; F = np.zeros(G)
            for i in range(L):
                idx = (dig[:, inter[i]] * (A ** np.arange(K + 1))).sum(1); F += tabs[i][idx]
            return F / L
    def analyse(F):
        fn = F[nb]; peak = F > fn.max(1); peaks = np.flatnonzero(peak)
        cur = np.arange(G)
        for _ in range(10 * G):
            better = F[nb[cur]] > F[cur][:, None]; act = better.any(1)
            if not act.any(): break
            r = rng.random(better.shape) * better; ch = r.argmax(1); cur = np.where(act, nb[cur, ch], cur)
        order = peaks[np.argsort(-F[peaks])]; end = cur
        out = dict(n_peaks=int(len(peaks)), frac_peaks=round(len(peaks) / G, 5))
        for fr in P["fracs"]:
            k = max(1, int(np.floor(fr * len(peaks) - 1e-9))); top = set(order[:k].tolist())
            out[f"P{fr}"] = round(float(np.isin(end, list(top)).mean()), 4)
        out["P_global"] = round(float((end == order[0]).mean()), 4)
        if len(peaks) >= 3 and len(peaks) <= P.get("max_basin_peaks", 400):
            bs = []
            for p in peaks:
                seen = np.zeros(G, bool); seen[p] = True; front = np.array([p])
                while len(front):
                    cand = nb[front]; lower = F[cand] < F[front][:, None]; nxt = np.unique(cand[lower]); nxt = nxt[~seen[nxt]]; seen[nxt] = True; front = nxt
                bs.append(seen.sum() / G)
            out["R_ph_bs"] = round(float(np.corrcoef(F[peaks], bs)[0, 1]), 4)
        else: out["R_ph_bs"] = None
        return out
    res = {}
    for spec in P["landscapes"]:
        rows = [analyse(land(spec)) for _ in range(P["reps"])]
        agg = {k: (round(float(np.mean([r[k] for r in rows if r[k] is not None])), 4) if any(r[k] is not None for r in rows) else None) for k in rows[0]}
        agg["R_ph_bs_min"] = min([r["R_ph_bs"] for r in rows if r["R_ph_bs"] is not None], default=None)
        agg["P0.14_min"] = min(r["P0.14"] for r in rows) if "P0.14" in rows[0] else None
        res[spec["name"]] = agg
    sm = analyse(land(dict(model="rmf", sigma=0.0)))
    res["V1_smooth"] = sm
    return dict(landscapes=res, G=G), [chk("V1", "an RMF landscape with sigma = 0 (additive) has exactly one peak and every walk ends on it", sm, sm["n_peaks"] == 1 and sm["P_global"] == 1.0)] + _hyps(P, dict(landscapes=res)) + [chk("R1", "values", dict(landscapes=res, G=G), True, "reporting")]


def adaptive_walk_sizes(P, rng):
    """ASA extension of adaptive_walk: runs the same analysis for each number of sites in L_list (four states unless A given),
    to compare P14% with P85's printed values at P85's own size (9 four-state sites) or to vary landscape size as P85 does for
    HoC (5-10 sites). Basins are skipped when a landscape has more than max_basin_peaks peaks."""
    out = {}
    for L in P["L_list"]:
        r, _ = adaptive_walk(dict(P, L=L, hyps=[]), rng); out[str(L)] = r["landscapes"]
    v = all(out[k]["V1_smooth"]["n_peaks"] == 1 and out[k]["V1_smooth"]["P_global"] == 1.0 for k in out)
    return dict(by_L=out), [chk("V1", "for every L an additive RMF landscape (sigma 0) has one peak reached by every walk", v, v)] + _hyps(P, dict(by_L=out)) + [chk("R1", "values", dict(by_L=out), True, "reporting")]


KINDS = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_') and k != 'chk' and getattr(v, '__module__', None) == '__main__'}

if __name__ == "__main__":
    P, H, t0 = R.start(sys.argv[1]); rng = np.random.default_rng(P["seed"])
    res, checks = KINDS[P["kind"]](P, rng); R.finish(H, P, res, checks, t0)
