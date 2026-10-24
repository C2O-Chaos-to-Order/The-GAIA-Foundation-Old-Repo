"""SIM-R1-C3: two-timescale acclimation memory in the Cycle-2 toy thermoregulation loop (carried item 'R1 two-timescale acclimation memory').
The session model day() is copied unchanged from SIM-R1-C2 (Cycle-2-x6/Report-1-Body/simulation/sim_r1.py). The learned anticipatory gain is
split into a fast and a slow state following the two-state form of Smith, Ghazizadeh & Shadmehr 2006 (X22): x_f <- A_f x_f + B_f e,
x_s <- A_s x_s + B_s e, w = x_f + x_s, where e is the day's mean work error (0 on days without heat). Anchors are qualitative only:
W05 (1 day of HA lost per 2 days of decay; re-induction 8-12x faster than decay for HR and Tc). Nothing is fitted to human data."""
import sys, os, json, itertools, numpy as np
from scipy.stats import spearmanr
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools")); import runner as R
C2IT2 = os.path.join(HERE, "..", "..", "..", "Cycle-2-x6", "Report-1-Body", "simulation", "iter-2", "outputs", "results.json")
def day(m, w, Tset, load=True, cue=True, load_scale=1.0):
    T = m["T0"]; pk = 0.0; mn = 0.0; errs = []; s = m["session"]
    for t in range(s["n"]):
        working = s["work_on"] <= t < s["work_off"]; cueing = cue and s["cue_on"] <= t < s["work_off"]
        d = m["d"]*load_scale if (working and load) else 0.0
        u = min(max(m["Kp"]*(T-Tset), 0.0), m["Umax"]) + (w if cueing else 0.0)
        u = min(max(u, 0.0), m["Umax_total"])
        T += m["dt"]*(-m["a"]*(T-m["T0"]) + d - u)
        pk = max(pk, T-m["T0"]); mn = min(mn, T-m["T0"])
        if working: errs.append(T-Tset)
    return pk, mn, float(np.mean(errs)), Tset
def single(m, eta, lam, days, w=0.0, exposure=None):
    """Cycle-2 single-state learner (no forgetting on exposed days)."""
    traj = []
    for k in range(days):
        if exposure is None or exposure[k]: w = max(w + eta*day(m, w, m["Tset"])[2], 0.0)
        else: w = w*(1-lam)
        traj.append(w)
    return traj, w
def two(m, th, days, st=(0.0, 0.0), exposure=None, rng=None, noise=0.0, retain_on_exposed=True):
    Af, As, Bf, Bs = th; xf, xs = st; traj = []
    for k in range(days):
        ex = exposure is None or exposure[k]
        e = day(m, xf+xs, m["Tset"], load_scale=(max(0.0, 1+noise*rng.standard_normal()) if rng is not None else 1.0))[2] if ex else 0.0
        if ex and not retain_on_exposed: xf, xs = xf + Bf*e, xs + Bs*e
        else: xf, xs = Af*xf + Bf*e, As*xs + Bs*e
        xf, xs = max(xf, 0.0), max(xs, 0.0); traj.append((xf, xs))
    return traj, (xf, xs)
def metrics(m, th, ha=14, had=14, re_days=60, rng=None, noise=0.0, cycles=1):
    """Same metric definitions as SIM-R1-C2 iteration 2: days lost, decay %/day, re-induction %/day to 95% of acclimated w, ratio."""
    out = []; st = (0.0, 0.0); wref = None
    for c in range(cycles):
        tr, st = two(m, th, ha, st, rng=rng, noise=noise); wtraj = [a+b for a, b in tr]; wA = sum(st)
        if wA <= 0: return None
        wref = wA if wref is None else wref  # re-induction target: the first cycle's acclimated gain
        _, sD = two(m, th, had, st, exposure=[False]*had); wD = sum(sD)
        eq = int(np.argmin([abs(x-wD) for x in wtraj]))+1; lost = ha-eq
        pctD = 100*(wA-wD)/wA; rd = pctD/had
        tr2, _ = two(m, th, re_days, sD, rng=rng, noise=noise); ws = [a+b for a, b in tr2]
        need = next((i+1 for i, x in enumerate(ws) if x >= 0.95*wref), None)
        rr = (100*(min(ws[need-1], wref)-wD)/wref)/need if need else None
        out.append(dict(cycle=c+1, w_acclimated=wA, w_after_decay=wD, ha_days_lost=lost, decay_pct_per_day=rd, reinduction_days_to_95pct=need,
                        reinduction_pct_per_day=rr, ratio=(rr/rd if (rr and rd > 0) else None), slow_share_after_decay=(sD[1]/wD if wD > 0 else None)))
        st = sD  # the next cycle's acclimation starts from the decayed state
    return out
def ok12(r, lo=8, hi=12): return r is not None and r["ratio"] is not None and lo <= r["ratio"] <= hi and abs(r["ha_days_lost"]-7) <= 1
def grid(g): return [tuple(float(v) for v in t) for t in itertools.product(g["Af"], g["As"], g["Bf"], g["Bs"])]
def main():
    P, prev, H = R.start(sys.argv[1]); t0 = R.now(); X = P["experiments"]; m = P["model"]; res = {}; chk = []
    sel = tuple(prev["selected_theta"]) if prev and prev.get("selected_theta") else None
    if prev: res["carried_from_prev"] = {k: prev[k] for k in P.get("carry", []) if k in prev}
    if "equivalence" in X:
        e = X["equivalence"]; c2 = json.load(open(C2IT2))
        _, wA = single(m, e["eta"], 0.0, 14); trA, _ = single(m, e["eta"], 0.0, 14)
        _, wD = single(m, e["eta"], c2["lam_fitted"], 14, w=wA, exposure=[False]*14)
        tr, _ = single(m, e["eta"], c2["lam_fitted"], 60, w=wD); need = next(i+1 for i, x in enumerate(tr) if x >= 0.95*wA)
        ratio = ((100*(min(tr[need-1], wA)-wD)/wA)/need)/(100*(wA-wD)/wA/14)
        chk.append(R.chk("V1", "copied day()/single-state code reproduces the Cycle-2 iteration-2 ratio (|diff| < 1e-9)", [ratio, c2["decay_reinduction"]["ratio"]], abs(ratio-c2["decay_reinduction"]["ratio"]) < 1e-9))
        lam = c2["lam_fitted"]; trS, _ = single(m, e["eta"], lam, 30, exposure=[k < 14 for k in range(30)])
        trT, _ = two(m, (1-lam, 1.0, e["eta"], 0.0), 30, exposure=[k < 14 for k in range(30)], retain_on_exposed=False)
        # two-state with B_s = 0 and retention only on unexposed days must equal the single-state learner
        dif = max(abs(a-(b[0]+b[1])) for a, b in zip(trS, trT))
        chk.append(R.chk("V2", "two-state code with B_s = 0 (fast state = Cycle-2 learner) reproduces the single-state trajectory (max |diff| < 1e-12)", dif, dif < 1e-12))
        res["single_state_ratio"] = ratio
    if "grid" in X:
        e = X["grid"]; rows = []
        for th in grid(e):
            r = metrics(m, th); rows.append(dict(theta=th, **(r[0] if r else dict(ratio=None))))
        good = [r for r in rows if r.get("ratio") is not None and 8 <= r["ratio"] <= 12 and abs(r["ha_days_lost"]-7) <= 1]
        res["grid"] = rows; res["n_settings"] = len(rows); res["n_meeting_both"] = len(good)
        val = [r for r in rows if r.get("ratio") is not None]
        best = min(val, key=lambda r: (0 if abs(r["ha_days_lost"]-7) <= 1 else 1, abs(r["ratio"]-10)))
        res["selected_theta"] = best["theta"]; res["selected"] = best
        chk.append(R.chk("H2", "some two-state setting meets BOTH W05 anchors: ~7 of 14 HA days lost (+-1) AND re-induction 8-12x faster than decay", [len(good), len(rows)], len(good) > 0, kind="hypothesis"))
        chk.append(R.chk("H2r", "report the selected setting (meets the 1:2 anchor if possible; ratio closest to 10) and the range of ratios", [best["theta"], best["ratio"], best["ha_days_lost"], min(r["ratio"] for r in val), max(r["ratio"] for r in val)], True, kind="reporting"))
    if "slow_retention" in X:
        e = X["slow_retention"]; out = []
        for As in e["As"]:
            th = (sel[0], float(As), sel[2], sel[3]); r = metrics(m, th); out.append(dict(As=As, **(r[0] if r else {})))
        res["slow_retention"] = out; xs = [o["As"] for o in out if o.get("ratio")]; ys = [o["ratio"] for o in out if o.get("ratio")]
        rho = float(spearmanr(xs, ys)[0]) if len(xs) > 2 else None
        chk.append(R.chk("H3", "re-induction/decay ratio rises monotonically as the slow state's retention A_s approaches 1 (Spearman >= 0.9)", rho, rho is not None and rho >= 0.9, kind="hypothesis"))
    if "decay_length" in X:
        e = X["decay_length"]; out = {}
        for name, th in (("two_state", sel), ("single_state", (1-e["lam_single"], 1.0, e["eta_single"], 0.0))):
            rows = []
            for had in e["had"]:
                r = metrics(m, th, had=had) if name == "two_state" else None
                if name == "single_state":
                    _, wA = single(m, e["eta_single"], 0.0, 14); _, wD = single(m, e["eta_single"], e["lam_single"], had, w=wA, exposure=[False]*had)
                    r = [dict(decay_pct_per_day=100*(wA-wD)/wA/had)]
                rows.append(dict(had=had, decay_pct_per_day=r[0]["decay_pct_per_day"]))
            out[name] = rows
        dec = {k: v[-1]["decay_pct_per_day"]/v[0]["decay_pct_per_day"] for k, v in out.items()}
        res["decay_length"] = out; res["deceleration_ratio_longest_vs_shortest"] = dec
        chk.append(R.chk("H4", "decay decelerates more with longer absence in the two-state model than in the single-state model (ratio of %/day at longest vs shortest absence lower by >= 0.1)", dec, dec["two_state"] <= dec["single_state"]-0.1, kind="hypothesis"))
    if "identifiability" in X:
        e = X["identifiability"]; rng = np.random.default_rng(e["seed"])
        def curve(th):  # observed w-proxy: peak on test days of HA, after decay, during re-induction
            tr, st = two(m, th, 14); _, sD = two(m, th, e["had"], st, exposure=[False]*e["had"]); tr2, _ = two(m, th, 5, sD)
            ws = [sum(tr[i]) for i in (0, 6, 13)] + [sum(sD)] + [sum(x) for x in tr2]
            return np.array([day(m, w, m["Tset"])[0] for w in ws])
        G2 = grid(e["two_grid"]); G1 = [(1-l, 1.0, eta, 0.0) for l in e["single_grid"]["lam"] for eta in e["single_grid"]["eta"]]
        C2c = np.array([curve(t) for t in G2]); C1c = np.array([curve(t) for t in G1]); truth = {"two": sel, "single": tuple(e["single_truth"])}
        out = {}
        for sd in e["noise"]:
            correct = 0
            for rep in range(e["reps"]):
                gen = "two" if rep % 2 == 0 else "single"; y = curve(truth[gen]); y = y*(1+sd*rng.standard_normal(len(y)))
                s2 = ((C2c-y)**2).sum(1).min(); s1 = ((C1c-y)**2).sum(1).min()
                k2, k1 = 4, 2; n = len(y)  # BIC with Gaussian errors
                b2 = n*np.log(s2/n+1e-300)+k2*np.log(n); b1 = n*np.log(s1/n+1e-300)+k1*np.log(n)
                correct += int(("two" if b2 < b1 else "single") == gen)
            out[str(sd)] = correct/e["reps"]
        res["recovery"] = out
        chk.append(R.chk("H5", f"BIC model selection on a realistic sampling scheme (3 HA test days, 1 post-decay, 5 re-induction days) recovers the generating model in >= 80% of datasets at {e['noise'][0]:.0%} noise", out, out[str(e["noise"][0])] >= 0.8, kind="hypothesis"))
        chk.append(R.chk("H5r", "report recovery at higher noise", out, True, kind="reporting"))
    if "noise_seeds" in X:
        e = X["noise_seeds"]; out = []
        for s in e["seeds"]:
            r = metrics(m, sel, rng=np.random.default_rng(s), noise=e["load_noise"]); out.append(r[0]["ratio"] if r else None)
        frac = float(np.mean([o is not None and 8 <= o <= 12 for o in out])); res["noise_seeds"] = dict(ratios=out, frac_in_8_12=frac)
        chk.append(R.chk("H6", "with 20% day-to-day load noise the selected setting keeps the ratio in [8, 12] in >= 80% of 20 seeds", frac, frac >= 0.8, kind="hypothesis"))
    if "oat" in X:
        e = X["oat"]; base = metrics(m, sel)[0]["ratio"]; out = []
        names = ["Af", "As", "Bf", "Bs"]
        for i, nm in enumerate(names):
            for f in e["factors"]:
                th = list(sel); th[i] = min(th[i]*f, 1.0) if nm in ("Af", "As") else th[i]*f
                r = metrics(m, tuple(th)); out.append(dict(param=nm, factor=f, ratio=(r[0]["ratio"] if r else None), lost=(r[0]["ha_days_lost"] if r else None)))
        for nm in ("Kp", "Umax"):
            for f in e["factors"]:
                mm = dict(m); mm[nm] = m[nm]*f; r = metrics(mm, sel); out.append(dict(param=nm, factor=f, ratio=(r[0]["ratio"] if r else None), lost=(r[0]["ha_days_lost"] if r else None)))
        res["oat"] = dict(base_ratio=base, rows=out); inside = all(o["ratio"] is not None and 6 <= o["ratio"] <= 14 for o in out)
        chk.append(R.chk("H7", "one-at-a-time +-20% perturbation of each of A_f, A_s, B_f, B_s, Kp, Umax keeps the ratio within [6, 14]", [[o["param"], o["factor"], o["ratio"]] for o in out], inside, kind="hypothesis"))
    if "cycles" in X:
        e = X["cycles"]; r2 = metrics(m, sel, cycles=e["n"]); r1 = []
        res["cycles_two_state"] = r2; need = [c["reinduction_days_to_95pct"] for c in r2]
        chk.append(R.chk("H8", "savings accumulate: in the two-state model, days to 95% re-induction fall across 3 acclimation/decay cycles (last < first)", need, None not in need and need[-1] < need[0], kind="hypothesis"))
        slow = [c["slow_share_after_decay"] for c in r2]
        chk.append(R.chk("H8r", "report slow-state share of the remaining gain after each decay", slow, True, kind="reporting"))
    if "fine_grid" in X:
        e = X["fine_grid"]; rows = []
        for th in grid(e):
            r = metrics(m, th)
            if r: rows.append(dict(theta=th, ratio=r[0]["ratio"], lost=r[0]["ha_days_lost"]))
        good = [r for r in rows if r["ratio"] is not None and 8 <= r["ratio"] <= 12 and abs(r["lost"]-7) <= 1]
        res["fine_grid"] = dict(n=len(rows), n_meeting_both=len(good), examples=good[:10])
        prevgood = (prev or {}).get("carried_from_prev", {}).get("n_meeting_both")
        chk.append(R.chk("H9", "a finer, independent grid also contains settings meeting both W05 anchors (replicates the iteration-2 answer)", [len(good), len(rows)], len(good) > 0, kind="hypothesis"))
    if sel and "selected_theta" not in res: res["selected_theta"] = list(sel)
    R.finish(H, P, res, chk, t0)
if __name__ == "__main__": main()
