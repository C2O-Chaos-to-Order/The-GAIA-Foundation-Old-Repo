"""SIM-R1 (Cycle 1+): homeostatic feedback/feedforward toy models. Toy only - no physiological parameter values are claimed."""
import sys, os, json, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools")); import runner as R
def sim(kp, ki, delay=0.0, ff=0.0, kl=0.1, D=1.0, td=10.0, T=60.0, dt=0.01, sigma=0.0, umax=1e9, seed=0, ffhat=1.0):
    rng = np.random.default_rng(seed); n = int(T/dt); lag = int(round(delay/dt)); x = 0.0; I = 0.0; xs = np.empty(n); hist = np.zeros(n)
    for k in range(n):
        t = k*dt; xd = x if lag == 0 else (hist[k-lag] if k-lag >= 0 else 0.0); I += xd*dt; d = D if t >= td else 0.0
        u = np.clip(-kp*xd - ki*I - ff*ffhat*d, -umax, umax)
        x += (-kl*x + u + d)*dt + sigma*np.sqrt(dt)*rng.standard_normal(); xs[k] = x; hist[k] = x
        if abs(x) > 1e6: xs[k:] = np.sign(x)*1e6; break
    return xs
def metrics(xs, dt=0.01, td=10.0):
    a = xs[int(td/dt):]; n = len(a); w = n//5
    amp_last = float(a[-w:].max()-a[-w:].min()); amp_prev = float(a[-2*w:-w].max()-a[-2*w:-w].min())
    return dict(peak=float(np.abs(a).max()), tail_mean=float(a[-w:].mean()), amp_last=amp_last, amp_prev=amp_prev,
                stable=bool(np.isfinite(a).all() and abs(a).max() < 1e5 and (amp_last < 1e-3 or amp_last < 0.9*amp_prev)))
def tau_c(a, k):  # analytic critical delay for x' = -a x(t) - k x(t-tau); stable for all tau if k <= a
    return None if k <= a else float(np.arccos(-a/k)/np.sqrt(k*k-a*a))
def crit_delay(kp, ki, dmax, tol, kl, T):
    lo, hi = 0.0, dmax
    if metrics(sim(kp, ki, hi, kl=kl, T=T))["stable"]: return None
    while hi-lo > tol:
        mid = (lo+hi)/2
        if metrics(sim(kp, ki, mid, kl=kl, T=T))["stable"]: lo = mid
        else: hi = mid
    return (lo+hi)/2
def two_comp(p, ff_gain, rng=None, pert=None):
    # core temperature c, shell s (deviations from set point, arbitrary units); environment step E at t_e acts on the shell.
    q = dict(p); 
    if pert: q.update(pert)
    n = int(q["T"]/q["dt"]); c = s = I = 0.0; pk = 0.0
    for k in range(n):
        t = k*q["dt"]; E = q["E"] if t >= q["t_e"] else 0.0
        u = -q["kp"]*c - q["ki"]*I - ff_gain*q["ff_skin"]*s   # anticipatory use of shell (skin) signal
        I += c*q["dt"]
        c += (q["k_cs"]*(s-c) + u)*q["dt"]; s += (q["k_cs"]*(c-s) + q["k_se"]*(E-s))*q["dt"]
        pk = max(pk, abs(c))
    return dict(peak_core=pk, final_core=c, final_shell=s)
def main():
    P, prev, H = R.start(sys.argv[1]); t0 = R.now(); X = P["experiments"]; res = {}; chk = []
    if "gain_grid" in X:
        g = X["gain_grid"]; cells = []
        for kp in g["kp"]:
            for ki in g["ki"]:
                m = metrics(sim(kp, ki, g.get("delay", 0.0), T=g["T"])); cells.append(dict(kp=kp, ki=ki, **m))
        st = [c for c in cells if c["stable"]]; res["gain_grid"] = dict(cells=cells, frac_stable=len(st)/len(cells),
            best_peak=min(st, key=lambda c: c["peak"]) if st else None)
        p_only = [c for c in cells if c["ki"] == 0 and g.get("delay", 0.0) == 0]
        err = max(abs(c["tail_mean"]-1.0/(0.1+c["kp"]))/(1.0/(0.1+c["kp"])) for c in p_only) if p_only else 0
        chk.append(R.chk("G1", "P-only cells match analytic residual D/(kl+kp) within 1%", err, err < 0.01))
        chk.append(R.chk("G2", "every stable PI cell (ki>0) returns to set point (|tail mean|<0.02)", max([abs(c["tail_mean"]) for c in st if c["ki"] > 0] or [0]), all(abs(c["tail_mean"]) < 0.02 for c in st if c["ki"] > 0)))
    if "delay_scan" in X:
        d = X["delay_scan"]; out = []
        for kp in d["p_only_kp"]:
            num = crit_delay(kp, 0.0, d["dmax"], d["tol"], 0.1, d["T"]); an = tau_c(0.1, kp); out.append(dict(kp=kp, numeric=num, analytic=an))
        res["delay_p_only"] = out
        rel = max(abs(o["numeric"]-o["analytic"])/o["analytic"] for o in out if o["analytic"])
        chk.append(R.chk("D1", "numeric critical delay (P-only) matches analytic arccos(-a/k)/sqrt(k^2-a^2) within 5%", rel, rel < 0.05))
        gains = d.get("pi_gains") or []
        if d.get("pi_from_prev") and prev and prev.get("gain_grid", {}).get("best_peak"):
            b = prev["gain_grid"]["best_peak"]; gains = gains + [[b["kp"], b["ki"]]]
        pi = [dict(kp=a, ki=b, crit=crit_delay(a, b, d["dmax"], d["tol"], 0.1, d["T"])) for a, b in gains]
        res["delay_pi"] = pi
        if len(pi) >= 2:
            chk.append(R.chk("D2", "higher-gain PI tolerates less delay (critical delay decreases with kp at fixed ki ratio) - reported", [p["crit"] for p in pi], True, kind="reporting"))
    if "mc_robust" in X:
        m = X["mc_robust"]; rng = np.random.default_rng(m["seed"]); fb = []; ffb = []; red = []
        for _ in range(m["n"]):
            kl = rng.uniform(*m["kl"]); kp = rng.uniform(*m["kp"]); ki = rng.uniform(*m["ki"]); dl = rng.uniform(*m["delay"]); fh = rng.normal(1.0, m["ffhat_sd"])
            a = metrics(sim(kp, ki, dl, kl=kl, T=m["T"])); b = metrics(sim(kp, ki, dl, ff=m["ff"], ffhat=fh, kl=kl, T=m["T"]))
            fb.append(a["stable"] and abs(a["tail_mean"]) < 0.05); ffb.append(b["stable"] and abs(b["tail_mean"]) < 0.05)
            if a["stable"] and b["stable"]: red.append(b["peak"]/a["peak"])
        res["mc_robust"] = dict(n=m["n"], frac_restored_fb=float(np.mean(fb)), frac_restored_fb_ff=float(np.mean(ffb)),
                                peak_ratio_ff_over_fb=dict(median=float(np.median(red)), q05=float(np.quantile(red, .05)), q95=float(np.quantile(red, .95)), n=len(red)))
        chk.append(R.chk("M1", "with feedback present, adding feedforward does not reduce the fraction of runs that restore the set point", [res["mc_robust"]["frac_restored_fb"], res["mc_robust"]["frac_restored_fb_ff"]], res["mc_robust"]["frac_restored_fb_ff"] >= res["mc_robust"]["frac_restored_fb"]-0.01, kind="hypothesis"))
        chk.append(R.chk("M2", "median peak ratio (FB+FF)/FB < 1 across parameter uncertainty", res["mc_robust"]["peak_ratio_ff_over_fb"]["median"], res["mc_robust"]["peak_ratio_ff_over_fb"]["median"] < 1, kind="hypothesis"))
    if "two_compartment" in X:
        t = X["two_compartment"]; base = two_comp(t, 0.0); ant = two_comp(t, 1.0); noI = two_comp(dict(t, ki=0.0), 0.0)
        res["two_compartment"] = dict(feedback_only=base, with_skin_feedforward=ant, proportional_only=noI)
        chk.append(R.chk("T1", "skin-signal feedforward lowers peak core deviation vs feedback only", [ant["peak_core"], base["peak_core"]], ant["peak_core"] < base["peak_core"], kind="hypothesis"))
        chk.append(R.chk("T2", "integral action returns core to set point (|final|<0.01) while P-only leaves a residual (>0.01)", [base["final_core"], noI["final_core"]], abs(base["final_core"]) < 0.01 and abs(noI["final_core"]) > 0.01))
        if t.get("mc_n"):
            rng = np.random.default_rng(t["seed"]); ratios = []
            for _ in range(t["mc_n"]):
                pert = {k: t[k]*rng.uniform(0.5, 1.5) for k in ("k_cs", "k_se", "kp", "ki")}
                ratios.append(two_comp(t, 1.0, pert=pert)["peak_core"]/two_comp(t, 0.0, pert=pert)["peak_core"])
            res["two_compartment"]["mc_peak_ratio"] = dict(n=t["mc_n"], frac_below_1=float(np.mean(np.array(ratios) < 1)), median=float(np.median(ratios)), max=float(np.max(ratios)))
            chk.append(R.chk("T3", "feedforward benefit robust to +/-50% parameter perturbation (ratio<1 in >=95% of draws)", res["two_compartment"]["mc_peak_ratio"]["frac_below_1"], res["two_compartment"]["mc_peak_ratio"]["frac_below_1"] >= 0.95, kind="hypothesis"))
    R.finish(H, P, res, chk, t0)
if __name__ == "__main__": main()
