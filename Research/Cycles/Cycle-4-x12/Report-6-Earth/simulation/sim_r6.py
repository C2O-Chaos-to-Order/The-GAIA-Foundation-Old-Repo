"""SIM-R6-C4: constrained-adaptation Daisyworld over an EXTENDED luminosity range. Cycle 3 (SIM-R6-C3) integrated only up to L = 1.7, so its
constrained variant hit the edge of the range (L_max 1.70) and could not be compared with W01 Table 1's published 'Constrained adaptation'
row (L 0.51-2.32, total life 1.223, citing Lenton & Lovelock 2000 = W03). W03 remains closed (abstract only), so the cost form is still OURS
(peak growth limited as optima approach bounds, following W01 section 6.3's verbal description); it is NOT the W03 model, and any agreement
with the published row is calibration, not reproduction. Equations and constants otherwise from W01 (eqs 1-6, 15), as in Cycle 3.
run() and summary() are copied from SIM-R6-C3 with growth vectorised (identical arithmetic; checked in iteration 1) and a 'cost' option
('quadratic' = Cycle 3; 'linear' = our alternative). Daisyworld is a parable: nothing here says Earth is regulated or has a soul."""
import sys, os, json, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "tools")); import runner as R
C3 = os.path.join(HERE, "..", "..", "..", "Cycle-3-x9", "Report-6-Earth", "simulation")
def growth_v(T, Topt, r, m): return np.maximum(0.0, m*(1-((Topt-T)/r)**2))
def run(M, adapt=None, dt=1.0):
    alb = np.array(M["albedo"]); n = len(alb); a = np.full(n, M["seed"]); Topt = np.full(n, 22.5); out = {}
    Ls = np.round(np.arange(M["L0"], M["L1"]+1e-9, M["dL"]), 6)
    for direction, seq in (("forward", Ls), ("reverse", Ls[::-1])):
        rec = []
        for L in seq:
            for _ in range(int(M["iters"]/dt)):
                x = 1-a.sum(); Ap = x*M["Ag"] + (a*alb).sum(); Te4 = M["S_over_sigma"]*L*(1-Ap)
                Ti = (M["q"]*(Ap-alb) + Te4)**0.25 - 273
                m = np.ones(n)
                if adapt and adapt.get("R"):
                    d = np.abs(Topt-22.5)/adapt["R"]; m = np.maximum(0.0, 1-d) if adapt.get("cost") == "linear" else np.maximum(0.0, 1-d**2)
                b = growth_v(Ti, Topt, M["r"], m)
                a = np.maximum(a + dt*a*(x*b - M["c"]), M["seed"])
                if adapt:
                    Topt = Topt + dt*adapt["k"]*(Ti-Topt)
                    if adapt.get("bound"): Topt = np.clip(Topt, *adapt["bound"])
            x = 1-a.sum(); Ap = x*M["Ag"] + (a*alb).sum(); Te = (M["S_over_sigma"]*L*(1-Ap))**0.25-273; Td = (M["S_over_sigma"]*L*(1-M["Ag"]))**0.25-273
            rec.append(dict(L=float(L), Te=float(Te), Tdead=float(Td), cover=float(a.sum()-n*M["seed"])))
        out[direction] = rec
    return out
def summary(o, live=0.01):
    f = o["forward"]; alive = [r for r in f if r["cover"] > live]
    if not alive: return dict(L_establish=None, L_max=None, width=0.0, total_life=0.0, slope_ratio=None)
    L0, L1 = alive[0]["L"], alive[-1]["L"]; dL = f[1]["L"]-f[0]["L"]
    tl = float(sum(r["cover"] for r in f if L0 <= r["L"] <= L1)*dL)
    Ls = np.array([r["L"] for r in alive]); Te = np.array([r["Te"] for r in alive]); Td = np.array([r["Tdead"] for r in alive])
    sr = float(np.polyfit(Ls, Te, 1)[0]/np.polyfit(Ls, Td, 1)[0]) if len(Ls) > 2 else None
    band = float(np.mean(np.abs(Te-22.5) <= 5)) if len(Te) else 0.0
    return dict(L_establish=L0, L_max=L1, width=L1-L0, total_life=tl, slope_ratio=sr, frac_within_5C=band, at_range_edge=bool(L1 >= f[-1]["L"]-1e-9))
def rev_summary(o, live=0.01):
    r = [x for x in o["reverse"] if x["cover"] > live]
    return dict(L_first_alive_reverse=(r[0]["L"] if r else None), L_last_alive_reverse=(r[-1]["L"] if r else None))
def main():
    P, prev, H = R.start(sys.argv[1]); t0 = R.now(); X = P["experiments"]; M = P["model"]; ME = dict(M, L1=P["L1_extended"]); T = P["W01_table1_constrained"]; res = {}; chk = []; k = P["iteration"]
    CA = dict(k=P["adapt"]["k"], bound=tuple(P["adapt"]["bound"]), R=P["adapt"]["R"])
    def near(s): return s["L_establish"] is not None and abs(s["L_establish"]-T["L_establish"]) <= 0.1 and abs(s["L_max"]-T["L_max"]) <= 0.1
    if k == 1:
        c3o = json.load(open(os.path.join(C3, "iter-2", "outputs", "results.json")))["original"]; c3c = json.load(open(os.path.join(C3, "iter-6", "outputs", "results.json")))["constrained"]["constrained"]
        s = summary(run(M)); c = summary(run(M, adapt=CA)); keys = ("L_establish", "L_max", "total_life", "slope_ratio")
        chk.append(R.chk("V1", "vectorised copy reproduces Cycle-3 iter-2 (original) and iter-6 (constrained) summaries over L 0.5-1.7 (|diff| < 1e-9)", [[s[x] for x in keys], [c3o[x] for x in keys], [c[x] for x in keys], [c3c[x] for x in keys]], all(abs(s[x]-c3o[x]) < 1e-9 and abs(c[x]-c3c[x]) < 1e-9 for x in keys)))
        se = summary(run(ME)); res.update(original=s, original_extended=se, constrained_c3_range=c)
        chk.append(R.chk("V2", "extending the range to L = 2.6 leaves the original model's summary unchanged (life is gone by L 1.5)", [[s[x] for x in keys], [se[x] for x in keys]], all(abs(s[x]-se[x]) < 1e-9 for x in keys)))
        chk.append(R.chk("C0", "Cycle-3 constrained run ended at the range edge (L_max = L1 = 1.7)", c["at_range_edge"], True, "reporting"))
    elif k == 2:
        c = summary(run(ME, adapt=CA)); res["constrained_extended"] = c
        chk.append(R.chk("H2", "over the extended range, our constrained variant's maximum luminosity is within +-0.1 of the published 2.32", [c["L_max"], T["L_max"], c["at_range_edge"]], c["L_max"] is not None and abs(c["L_max"]-T["L_max"]) <= 0.1, "hypothesis"))
        chk.append(R.chk("H2r", "establishment, total life (published 1.223)", [c["L_establish"], c["total_life"]], True, "reporting"))
    elif k == 3:
        u = summary(run(ME, adapt=dict(k=P["adapt"]["k"]))); res["unbounded_extended"] = u
        chk.append(R.chk("H3", "unbounded adaptation keeps life alive to at least L = 2.0 (it removes regulation but extends survival)", [u["L_max"], u["slope_ratio"], u["at_range_edge"]], u["L_max"] is not None and u["L_max"] >= 2.0, "hypothesis"))
    elif k == 4:
        rows = [dict(R=Rr, **summary(run(ME, adapt=dict(CA, R=Rr)))) for Rr in X["R"]]; res["by_R"] = rows; lm = [r["L_max"] for r in rows]
        chk.append(R.chk("H4", "maximum luminosity rises monotonically with cost half-width R (a cheaper adaptation tolerates more forcing)", [(r["R"], r["L_max"], r["slope_ratio"]) for r in rows], all(b >= a-1e-9 for a, b in zip(lm, lm[1:])), "hypothesis"))
    elif k == 5:
        rows = [dict(bound=b, **summary(run(ME, adapt=dict(CA, bound=tuple(b))))) for b in X["bounds"]]; res["by_bound"] = rows; lm = [r["L_max"] for r in rows]
        chk.append(R.chk("H5", "maximum luminosity is insensitive to the adaptation bounds (range across three bound choices <= 0.1)", [(r["bound"], r["L_max"], r["L_establish"]) for r in rows], max(lm)-min(lm) <= 0.1, "hypothesis"))
    elif k == 6:
        c = summary(run(ME, adapt=CA)); s0 = summary(run(M)); res.update(constrained_extended=c, original=s0)
        chk.append(R.chk("H6", "over the extended range, the constrained variant still regulates: slope ratio within 0.2 of the original model", [c["slope_ratio"], s0["slope_ratio"], c["frac_within_5C"]], c["slope_ratio"] is not None and abs(c["slope_ratio"]-s0["slope_ratio"]) <= 0.2, "hypothesis"))
    elif k == 7:
        q = summary(run(ME, adapt=CA)); l = summary(run(ME, adapt=dict(CA, cost="linear"))); res.update(quadratic=q, linear=l)
        chk.append(R.chk("H7", "the cost SHAPE matters little: linear vs quadratic peak-growth cost changes L_max by <= 0.1", [q["L_max"], l["L_max"]], q["L_max"] is not None and l["L_max"] is not None and abs(q["L_max"]-l["L_max"]) <= 0.1, "hypothesis"))
    elif k == 8:
        o = run(M); f = summary(o); r = rev_summary(o); res.update(forward=f, reverse=r)
        hy = abs(r["L_first_alive_reverse"]-f["L_max"]) >= 0.02 if r["L_first_alive_reverse"] is not None else False
        chk.append(R.chk("H8", "original Daisyworld shows hysteresis: on the reverse sweep life reappears at a luminosity >= 0.02 away from the forward maximum", [f["L_max"], r], hy, "hypothesis"))
    elif k == 9:
        c1 = summary(run(ME, adapt=CA)); c2 = summary(run(ME, adapt=CA, dt=X["dt"])); res.update(dt1=c1, dt_half=c2)
        chk.append(R.chk("H9", "halving the Euler step changes the extended constrained run's L_establish and L_max by <= 0.01", [c1["L_establish"], c2["L_establish"], c1["L_max"], c2["L_max"]], abs(c1["L_establish"]-c2["L_establish"]) <= 0.01 and abs(c1["L_max"]-c2["L_max"]) <= 0.01, "hypothesis"))
    elif k == 10:
        rows = []
        for kk in X["k"]:
            for Rr in X["R"]:
                s = summary(run(ME, adapt=dict(CA, k=kk, R=Rr))); rows.append(dict(k=kk, R=Rr, L_establish=s["L_establish"], L_max=s["L_max"], total_life=s["total_life"], slope_ratio=s["slope_ratio"], err=(None if s["L_max"] is None else max(abs(s["L_establish"]-T["L_establish"]), abs(s["L_max"]-T["L_max"])))))
        ok = [r for r in rows if r["err"] is not None]; best = min(ok, key=lambda r: r["err"]) if ok else None; res.update(calibration=rows, best=best)
        chk.append(R.chk("H10", "CALIBRATION (not reproduction): some setting in the k x R grid matches both ends of the published constrained row within +-0.05", best, best is not None and best["err"] <= 0.05, "hypothesis"))
    elif k == 11:
        e = X["sensitivity"]; base = summary(run(ME, adapt=CA)); out = {}
        for key, vals in e.items():
            out[key] = [dict(v=v, L_max=summary(run(dict(ME, **{key: v}), adapt=CA))["L_max"]) for v in vals]
        res.update(base=base, oat=out); lm = [x["L_max"] for v in out.values() for x in v if x["L_max"] is not None]
        chk.append(R.chk("H11", "one-at-a-time changes of death rate c and growth half-width r (+-10%) move the constrained L_max by <= 0.1", [base["L_max"], out], lm and max(abs(x-base["L_max"]) for x in lm) <= 0.1, "hypothesis"))
    elif k == 12:
        t = {}
        for kk in range(2, 12):
            r = json.load(open(os.path.join(H, "..", f"iter-{kk}", "EXECUTION_RECORD.json"))); t[f"iter-{kk}"] = [(c["id"], c["result"]) for c in r["pre_registered_checks"] if c["kind"] == "hypothesis"]
        c2 = json.load(open(os.path.join(H, "..", "iter-2", "outputs", "results.json")))["constrained_extended"]; res.update(summary=t, constrained_extended=c2)
        chk.append(R.chk("H12", "consolidation: the Cycle-3 mismatch with the published constrained row was (at least in part) a range artefact - with the range extended, L_max is beyond 1.7 and closer to 2.32 than Cycle 3's 1.70", c2["L_max"], c2["L_max"] is not None and c2["L_max"] > 1.7 and abs(c2["L_max"]-T["L_max"]) < abs(1.7-T["L_max"]), "hypothesis"))
    R.finish(H, P, res, chk, t0)
if __name__ == "__main__": main()
