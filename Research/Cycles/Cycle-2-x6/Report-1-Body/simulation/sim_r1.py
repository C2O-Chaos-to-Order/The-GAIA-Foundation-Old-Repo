"""SIM-R1-C2: bounded, learning feedforward in a toy thermoregulation loop (heat acclimation as slow learning).
Toy model of our own: core temperature T (deg C deviation units), passive loss a, work heat load d, bounded feedback effector
(sweating-like) plus a learned anticipatory (feedforward) term w*cue that is updated once per day and forgets without exposure.
Qualitative anchors only: W04 (Lim 2020: up to 14 days of daily heat exposure lowers Tb), W05 (Daanen et al. 2018: '1 day of HA is lost
following 2 days of HAD'; 'HRA was 8-12 times faster than HAD' for HR and Tc). Not a physiological model; no parameter is fitted to human data."""
import sys, os, json, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools")); import runner as R
def day(m, w, Tset, load=True, cue=True, load_scale=1.0, setpoint_adapt=None):
    """One session; returns (peak deviation above T0, min deviation, mean error during work, final Tset)."""
    T = m["T0"]; pk = 0.0; mn = 0.0; errs = []; s = m["session"]; Ts = Tset
    for t in range(s["n"]):
        working = s["work_on"] <= t < s["work_off"]; cueing = cue and s["cue_on"] <= t < s["work_off"]
        d = m["d"]*load_scale if (working and load) else 0.0
        u = min(max(m["Kp"]*(T-Ts), 0.0), m["Umax"]) + (w if cueing else 0.0)
        u = min(max(u, 0.0), m["Umax_total"])
        T += m["dt"]*(-m["a"]*(T-m["T0"]) + d - u)
        if setpoint_adapt:
            r, b = setpoint_adapt; Ts += m["dt"]*r*(T-Ts)
            if b is not None: Ts = min(max(Ts, m["T0"]-b), m["T0"]+b)
        pk = max(pk, T-m["T0"]); mn = min(mn, T-m["T0"])
        if working: errs.append(T-Ts)
    return pk, mn, float(np.mean(errs)), Ts
def train(m, L, days, w=0.0, exposure=None, rng=None):
    """Daily LMS update w += eta*mean work error (exposed days); w *= (1-lam) on unexposed days; w clipped to [0, w_max]."""
    out = []
    for k in range(days):
        exp_ = True if exposure is None else exposure[k]
        sc = 1.0 if rng is None else float(max(0.0, 1+L.get("load_noise", 0)*rng.standard_normal()))
        if exp_:
            pk, mn, e, _ = day(m, w, m["Tset"], load_scale=sc); w = w+L["eta"]*e
        else:
            pk, mn, e = None, None, None; w = w*(1-L["lam"])
        w = min(max(w, 0.0), L["w_max"] if L.get("w_max") is not None else np.inf)
        out.append(dict(day=k+1, exposed=exp_, peak=pk, w=w))
    return out, w
def main():
    P, prev, H = R.start(sys.argv[1]); t0 = R.now(); X = P["experiments"]; m = P["model"]; res = {}; chk = []
    if prev: res["carried_from_prev"] = {k: prev[k] for k in P.get("carry", []) if k in prev}
    L = dict(P["learning"]); [L.update({k: prev[k]}) for k in P.get("carry", []) if prev and k in prev and k in L]
    res["learning_used"] = L
    if "acquisition" in X:
        e = X["acquisition"]
        pk0, mn0, _, _ = day(m, 0.0, m["Tset"], load=False, cue=False)
        chk.append(R.chk("V1", "no load, no cue: temperature stays at T0 (|dev| < 1e-12)", [pk0, mn0], abs(pk0) < 1e-12 and abs(mn0) < 1e-12))
        mm = dict(m, Umax=1e9, Umax_total=1e9, session=dict(m["session"], n=4000, work_on=0, work_off=4000, cue_on=4000))
        pk, _, _, _ = day(mm, 0.0, m["Tset"]); ss = m["d"]/(m["a"]+m["Kp"])
        chk.append(R.chk("V2", "unsaturated P-control steady state equals analytic d/(a+Kp) (rel. error < 1e-6)", [pk, ss], abs(pk-ss) < 1e-6*ss))
        tr, w = train(m, L, e["days"]); p1, pN = tr[0]["peak"], tr[-1]["peak"]; red = (p1-pN)/p1
        res["acquisition"] = dict(daily=tr, peak_day1=p1, peak_last=pN, reduction=red, w_final=w); res["w_acclimated"] = w
        chk.append(R.chk("H1", f"daily exposure for {e['days']} days lowers peak core deviation by >= {e['min_reduction']:.0%} (direction per W04)", red, red >= e["min_reduction"], kind="hypothesis"))
        d50 = next((r["day"] for r in tr if (p1-r["peak"]) >= 0.5*(p1-pN)), None); res["days_to_half_adaptation"] = d50
        chk.append(R.chk("H1b", "report days to reach half of the final adaptation", d50, True, kind="reporting"))
    if "decay_reinduction" in X:
        e = X["decay_reinduction"]; base_tr, wA = train(m, dict(L, lam=0.0), e["ha_days"]); traj = [r["w"] for r in base_tr]
        best = None
        for lam in np.round(np.arange(*e["lam_grid"]), 5):
            _, wD = train(m, dict(L, lam=float(lam)), e["had_days"], w=wA, exposure=[False]*e["had_days"])
            eq = int(np.argmin([abs(x-wD) for x in traj]))+1  # HA day with the same w
            lost = e["ha_days"]-eq; err = abs(lost - e["had_days"]/2)
            if best is None or err < best[0]: best = (err, float(lam), lost, wD)
        lam = best[1]; res["lam_fitted"] = lam; res["ha_days_lost"] = best[2]
        chk.append(R.chk("C1cal", f"calibration: forgetting rate chosen so {e['had_days']} decay days lose ~{e['had_days']//2} HA days (W05 heuristic 1:2)", [lam, best[2]], True, kind="reporting"))
        pctD = 100*(wA-best[3])/wA; rate_decay = pctD/e["had_days"]
        tr, _ = train(m, dict(L, lam=lam), 60, w=best[3]); need = next((r["day"] for r in tr if r["w"] >= 0.95*wA), None)
        rate_re = (100*(min(tr[need-1]["w"], wA)-best[3])/wA)/need if need else None
        ratio = rate_re/rate_decay if rate_re else None
        res["decay_reinduction"] = dict(w_acclimated=wA, w_after_decay=best[3], pct_decay=pctD, decay_rate_pct_per_day=rate_decay, reinduction_days_to_95pct=need, reinduction_rate_pct_per_day=rate_re, ratio=ratio)
        chk.append(R.chk("H2", "with the 1:2 calibration, re-induction is 8-12x faster than decay (W05 HR/Tc finding)", ratio, ratio is not None and 8 <= ratio <= 12, kind="hypothesis"))
    if "false_cue" in X:
        e = X["false_cue"]; out = []
        for wm in e["w_max"]:
            Lb = dict(L, w_max=wm); _, w = train(m, Lb, e["days"])
            pk, _, _, _ = day(m, w, m["Tset"]); _, mn, _, _ = day(m, w, m["Tset"], load=False, cue=True)
            out.append(dict(w_max=wm, w=w, peak_with_load=pk, undershoot_cue_no_load=-mn))
        res["false_cue"] = out; unb = [o for o in out if o["w_max"] is None][0]; p0 = day(m, 0.0, m["Tset"])[0]
        ok = [o for o in out if o["w_max"] is not None and o["undershoot_cue_no_load"] <= e["max_undershoot"]]
        keep = [(o["w_max"], (p0-o["peak_with_load"])/(p0-unb["peak_with_load"])) for o in ok] if p0 > unb["peak_with_load"] else []
        res["benefit_retained_by_safe_bounds"] = keep
        good = [wm for wm, k in keep if k >= 0.7]; res["safe_w_max"] = max(good) if good else (max(o["w_max"] for o in ok) if ok else None)
        chk.append(R.chk("H3", f"some bound keeps false-cue undershoot <= {e['max_undershoot']} while retaining >= 70% of the unbounded peak reduction", keep, any(k >= 0.7 for _, k in keep), kind="hypothesis"))
        chk.append(R.chk("H3r", "report unbounded false-cue undershoot", unb["undershoot_cue_no_load"], True, kind="reporting"))
    if "setpoint_adaptation" in X:
        e = X["setpoint_adaptation"]; out = []
        mm = dict(m, session=dict(m["session"], n=e["n"], work_on=0, work_off=e["n"], cue_on=e["n"]))
        for r in e["rates"]:
            for b in e["bounds"]:
                pk, _, _, Ts = day(mm, 0.0, m["Tset"], setpoint_adapt=(r, b) if r else None); out.append(dict(rate=r, bound=b, peak=pk, final_Tset=Ts))
        res["setpoint_adaptation"] = out; p0 = [o["peak"] for o in out if o["rate"] == 0][0]
        unb = [o["peak"] for o in out if o["rate"] > 0 and o["bound"] is None]; bd = [o["peak"] for o in out if o["rate"] > 0 and o["bound"] is not None and o["bound"] <= e["tight"]]
        chk.append(R.chk("H4", "R6 analogue: unbounded set-point adaptation raises the sustained-load peak by >= 50% over a fixed set point", [p0, unb], min(unb) >= 1.5*p0, kind="hypothesis"))
        chk.append(R.chk("H4b", f"bounded (<= {e['tight']}) set-point adaptation keeps the peak within 20% of fixed", [p0, bd], max(bd) <= 1.2*p0, kind="hypothesis"))
    if "robustness" in X:
        e = dict(X["robustness"]); rng = np.random.default_rng(e["seed"]); rows = []
        if e["w_max"] == "from_prev": e["w_max"] = (prev or {}).get("safe_w_max") or (prev or {}).get("carried_from_prev", {}).get("safe_w_max")
        res["w_max_used"] = e["w_max"]
        for eta in e["eta"]:
            for kp in e["Kp"]:
                for um in e["Umax"]:
                    mm = dict(m, Kp=kp, Umax=um); Lr = dict(L, eta=eta, w_max=e["w_max"], load_noise=e["load_noise"])
                    tr, w = train(mm, Lr, e["days"], rng=rng); p0 = day(mm, 0.0, m["Tset"])[0]; p1 = day(mm, w, m["Tset"])[0]; un = -day(mm, w, m["Tset"], load=False)[1]
                    rows.append(dict(eta=eta, Kp=kp, Umax=um, reduction=(p0-p1)/p0, undershoot=un))
        res["robustness"] = rows; f = float(np.mean([r["reduction"] >= 0.2 and r["undershoot"] <= e["max_undershoot"] for r in rows]))
        res["robustness_frac_ok"] = f
        chk.append(R.chk("H5", "bounded learning feedforward gives >= 20% peak reduction with acceptable false-cue undershoot in >= 80% of settings (noisy loads)", f, f >= 0.8, kind="hypothesis"))
    if prev and "safe_w_max" not in res: res["safe_w_max"] = prev.get("safe_w_max") or prev.get("carried_from_prev", {}).get("safe_w_max")
    if "replication" in X:
        e = X["replication"]; reds = []
        for s in e["seeds"]:
            rng = np.random.default_rng(s); _, w = train(m, dict(L, load_noise=e["load_noise"]), e["days"], rng=rng); p0 = day(m, 0.0, m["Tset"])[0]; reds.append((p0-day(m, w, m["Tset"])[0])/p0)
        res["replication"] = dict(reductions=reds, mean=float(np.mean(reds)), sd=float(np.std(reds, ddof=1)))
        chk.append(R.chk("H6", f"H1 replicates under {e['load_noise']:.0%} day-to-day load noise: reduction >= 30% in every seed", [min(reds), max(reds)], min(reds) >= 0.3, kind="hypothesis"))
    R.finish(H, P, res, chk, t0)
if __name__ == "__main__": main()
