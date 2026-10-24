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

KINDS = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_') and k != 'chk' and getattr(v, '__module__', None) == '__main__'}

if __name__ == "__main__":
    P, H, t0 = R.start(sys.argv[1]); rng = np.random.default_rng(P["seed"])
    res, checks = KINDS[P["kind"]](P, rng); R.finish(H, P, res, checks, t0)
