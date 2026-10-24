"""SIM-R1-C4: continuous re-induction metric for the two-state acclimation memory (carried item 'R1 continuous re-induction metric').
Imports the Cycle-3 model unchanged (Cycle-3-x9/Report-1-Body/simulation/sim_r1.py: day(), single(), two(), metrics()). Cycle 3 found the
re-induction/decay ratio quantised by whole days (re-induction took 1-2 days). Here the day on which 95% of the acclimated gain is regained,
and the day equivalent to the decayed state, are found by linear interpolation between days. Anchors as in Cycle 3: W05 (about 1 HA day
lost per 2 decay days; re-induction 8-12x faster than decay; decay about 2.5% per day of decay for HR and Tc). Toy; nothing fitted."""
import sys, os, json, itertools, importlib.util, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "tools")); import runner as R
C3P = os.path.join(HERE, "..", "..", "..", "Cycle-3-x9", "Report-1-Body", "simulation")
spec = importlib.util.spec_from_file_location("c3r1", os.path.join(C3P, "sim_r1.py")); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
def cross(seq, target, start):
    prev = start
    for i, x in enumerate(seq):
        if x >= target: return i + (target - prev) / (x - prev) if x != prev else i + 1.0
        prev = x
    return None
def cmet(m, th, ha=14, had=14, thr=0.95, rng=None, noise=0.0, re_days=60, single=None):
    if single: tr, wA = M.single(m, single[0], single[1], ha); wt = tr; _, wD = M.single(m, single[0], single[1], had, w=wA, exposure=[False] * had); ws, _ = M.single(m, single[0], single[1], re_days, w=wD)
    else:
        tr, st = M.two(m, th, ha, (0.0, 0.0), rng=rng, noise=noise); wt = [a + b for a, b in tr]; wA = sum(st)
        if wA <= 0: return None
        _, sD = M.two(m, th, had, st, exposure=[False] * had); wD = sum(sD); tr2, _ = M.two(m, th, re_days, sD, rng=rng, noise=noise); ws = [a + b for a, b in tr2]
    if wA <= 0: return None
    eq = cross(wt, wD, 0.0); tre = cross(ws, thr * wA, wD)
    if eq is None or tre is None or tre <= 0: return None
    rd = 100 * (wA - wD) / wA / had; rr = 100 * (thr * wA - wD) / wA / tre
    return dict(lost=ha - eq, decay_pct_day=rd, t_re=tre, ratio=(rr / rd if rd > 0 else None))
def ok(r): return r is not None and r["ratio"] is not None and 8 <= r["ratio"] <= 12 and abs(r["lost"] - 7) <= 1
def grid(g): return [tuple(float(v) for v in t) for t in itertools.product(g["Af"], g["As"], g["Bf"], g["Bs"])]
def scan(m, g):
    rows = [(th, cmet(m, th)) for th in grid(g)]; hits = [(th, r) for th, r in rows if ok(r)]
    return rows, hits
def main():
    P, prev, H = R.start(sys.argv[1]); t0 = R.now(); X = P["experiments"]; m = P["model"]; k = P["iteration"]; C = []; res = {}
    sel = tuple(prev["selected_theta"]) if prev and prev.get("selected_theta") else None
    if k == 1:
        th = tuple(X["c3_selected"]); r3 = M.metrics(m, th)[0]; r4 = cmet(m, th)
        res.update(c3_integer=r3, c4_continuous=r4)
        C += [R.chk("V1", "imported Cycle-3 code reproduces C3 iteration-2's selected-setting ratio 7.0", r3["ratio"], abs(r3["ratio"] - 7.0) < 1e-9),
              R.chk("V2", "continuous crossing time lies within the whole-day interval (need-1, need]", [r4["t_re"], r3["reinduction_days_to_95pct"]], r3["reinduction_days_to_95pct"] - 1 < r4["t_re"] <= r3["reinduction_days_to_95pct"])]
    elif k in (2, 3, 10):
        rows, hits = scan(m, X["grid"]); best = min(hits, key=lambda h: abs(h[1]["ratio"] - 10)) if hits else None
        res.update(n=len(rows), n_meeting_both=len(hits), examples=[dict(theta=t, **r) for t, r in hits[:6]], ratio_range=[min(r["ratio"] for _, r in rows if r and r["ratio"]), max(r["ratio"] for _, r in rows if r and r["ratio"])])
        if k == 2: res["selected_theta"] = list(best[0]) if best else X["fallback"]
        if k != 2 and sel: res["selected_theta"] = list(sel)
        exp = {2: ("H2", "continuous metric, C3 coarse grid (144): >= 1 setting meets both anchors (C3 integer metric: 0)", len(hits) >= 1),
               3: ("H3", "continuous metric, C3 fine grid (180): more than C3's 2 settings meet both anchors", len(hits) > 2),
               10: ("H10", "continuous metric, a third grid with new points: >= 1 setting meets both anchors", len(hits) >= 1)}[k]
        C += [R.chk(exp[0], exp[1], [len(hits), len(rows)], exp[2], "hypothesis")]
    elif k in (4, 11):
        rs = [cmet(m, sel, rng=np.random.default_rng(s), noise=X["load_noise"]) for s in X["seeds"]]; f = float(np.mean([r is not None and r["ratio"] is not None and 8 <= r["ratio"] <= 12 for r in rs]))
        res.update(ratios=[r["ratio"] if r else None for r in rs], share=f, selected_theta=list(sel))
        C += [R.chk(f"H{k}", "selected setting keeps ratio in [8,12] in >= 80% of load-noise seeds" + (" (new seeds)" if k == 11 else ""), f, f >= 0.8, "hypothesis")]
    elif k == 5:
        out = []
        for i, f in itertools.product(range(4), X["factors"]):
            th = list(sel); th[i] = min(th[i] * f, 1.0); r = cmet(m, tuple(th)); out.append(dict(param=i, factor=f, ratio=r["ratio"] if r else None))
        for key, f in itertools.product(["a", "Kp"], X["factors"]):
            mm = dict(m); mm[key] = m[key] * f; r = cmet(mm, sel); out.append(dict(param=key, factor=f, ratio=r["ratio"] if r else None))
        good = all(o["ratio"] is not None and 6 <= o["ratio"] <= 14 for o in out); res.update(oat=out, selected_theta=list(sel))
        C += [R.chk("H5", "+-20% one-at-a-time: ratio stays in [6,14]", [o["ratio"] for o in out], good, "hypothesis")]
    elif k == 6:
        out = {str(t): cmet(m, sel, thr=t) for t in X["thr"]}; res.update(by_threshold=out, selected_theta=list(sel))
        C += [R.chk("H6", "selected setting meets both anchors at 90%, 95% and 98% re-induction thresholds", {t: (r["ratio"], r["lost"]) for t, r in out.items()}, all(ok(r) for r in out.values()), "hypothesis")]
    elif k == 7:
        r = cmet(m, sel); res.update(r=r, selected_theta=list(sel))
        C += [R.chk("H7", "decay of the learned gain is 1.5-3.5% per day (W05: about 2.5% per decay day for HR and Tc)", r["decay_pct_day"], 1.5 <= r["decay_pct_day"] <= 3.5, "hypothesis")]
    elif k == 8:
        rows = [(e, l, cmet(m, None, single=(e, l))) for e, l in itertools.product(X["eta"], X["lam"])]; hits = [(e, l) for e, l, r in rows if ok(r)]
        res.update(n=len(rows), hits=hits, ratios=[(e, l, r["ratio"] if r else None, r["lost"] if r else None) for e, l, r in rows], selected_theta=list(sel))
        C += [R.chk("H8", "negative control: no single-state (Cycle-2) setting meets both anchors under the continuous metric", [len(hits), len(rows)], len(hits) == 0, "hypothesis")]
    elif k == 9:
        def perday(th, had, single=None):
            r = cmet(m, th, had=had, single=single); return r["decay_pct_day"] if r else None
        two_r = perday(sel, 40) / perday(sel, 7); one_r = perday(None, 40, single=tuple(X["single"])) / perday(None, 7, single=tuple(X["single"]))
        res.update(two_state=two_r, single_state=one_r, selected_theta=list(sel))
        C += [R.chk("H9", "decay decelerates more for the two-state memory (per-day loss 40 d / 7 d lower by >= 0.1 than single exponential)", [two_r, one_r], one_r - two_r >= 0.1, "hypothesis")]
    elif k == 12:
        allrows = []
        for g in X["grids"]: allrows += scan(m, g)[0]
        n = len(allrows); h = sum(ok(r) for _, r in allrows); res.update(n=n, n_meeting_both=h, share=h / n, selected_theta=list(sel))
        C += [R.chk("H12", "across all three grids >= 5% of settings meet both anchors under the continuous metric", [h, n], h / n >= 0.05, "hypothesis")]
    R.finish(H, P, res, C, t0)
if __name__ == "__main__": main()
