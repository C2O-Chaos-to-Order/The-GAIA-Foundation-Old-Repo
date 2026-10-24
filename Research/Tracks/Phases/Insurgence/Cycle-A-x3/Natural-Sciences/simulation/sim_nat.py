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

KINDS = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_') and k != 'chk' and getattr(v, '__module__', None) == '__main__'}

if __name__ == "__main__":
    P, H, t0 = R.start(sys.argv[1]); rng = np.random.default_rng(P["seed"])
    res, checks = KINDS[P["kind"]](P, rng); R.finish(H, P, res, checks, t0)
