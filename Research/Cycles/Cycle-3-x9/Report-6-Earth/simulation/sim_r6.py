"""SIM-R6-C3: Daisyworld from the PUBLISHED equations of Lenton & Lovelock 2001 (W01, eqs 1-6 and 15; constants S/sigma = 1.68e10 K^4,
q = 2.06425e9 K^4, c = 0.3, albedos 0.25/0.75/0.5, L from 0.5 to 1.7 in steps of 0.004 with 100 Euler iterations of 1 generation per step,
then reversed) - carried item 'R6 Lenton & Lovelock 2000 published equations'. W03 (Lenton & Lovelock 2000), which holds the constrained-
adaptation equations, is not open access (abstract only), so the constrained variant below follows W01's verbal description and its
general growth function (eq. 15) with our own cost form; it is NOT the W03 model. Daisyworld is a parable: model results say nothing
about whether Earth is regulated, and nothing about any 'soul' of the Earth (Philosophical/Spiritual framing is kept separate)."""
import sys, os, json, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "tools")); import runner as R
def growth(T, Topt=22.5, r=17.5, m=1.0): return max(0.0, m*(1-((Topt-T)/r)**2))
def run(M, adapt=None, dt=1.0):
    """adapt: None | dict(k=rate, bound=None or (lo, hi), R=None or cost half-width). Returns forward and reverse records."""
    alb = M["albedo"]; n = len(alb); a = np.full(n, M["seed"]); Topt = np.full(n, 22.5); out = {}
    Ls = np.round(np.arange(M["L0"], M["L1"]+1e-9, M["dL"]), 6)
    for direction, seq in (("forward", Ls), ("reverse", Ls[::-1])):
        rec = []
        for L in seq:
            for _ in range(int(M["iters"]/dt)):
                x = 1-a.sum(); Ap = x*M["Ag"] + (a*alb).sum(); Te4 = M["S_over_sigma"]*L*(1-Ap); Te = Te4**0.25-273
                Ti = (M["q"]*(Ap-alb) + Te4)**0.25 - 273
                m = np.ones(n)
                if adapt and adapt.get("R"): m = np.array([max(0.0, 1-((t-22.5)/adapt["R"])**2) for t in Topt])
                b = np.array([growth(Ti[i], Topt[i], M["r"], m[i]) for i in range(n)])
                a = np.maximum(a + dt*a*(x*b - M["c"]), M["seed"])
                if adapt:
                    Topt = Topt + dt*adapt["k"]*(Ti-Topt)
                    if adapt.get("bound"): Topt = np.clip(Topt, *adapt["bound"])
            x = 1-a.sum(); Ap = x*M["Ag"] + (a*alb).sum(); Te = (M["S_over_sigma"]*L*(1-Ap))**0.25-273; Td = (M["S_over_sigma"]*L*(1-M["Ag"]))**0.25-273
            rec.append(dict(L=float(L), Te=float(Te), Tdead=float(Td), cover=float(a.sum()-n*M["seed"]), covers=a.tolist()))
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
    return dict(L_establish=L0, L_max=L1, width=L1-L0, total_life=tl, slope_ratio=sr, frac_within_5C=band)
def main():
    P, prev, H = R.start(sys.argv[1]); t0 = R.now(); X = P["experiments"]; M = P["model"]; T1 = P["W01_table1"]; res = {}; chk = []
    if "checks" in X:
        Td = (M["S_over_sigma"]*1.0*(1-M["Ag"]))**0.25-273; an = (1.68e10*0.5)**0.25-273
        chk.append(R.chk("V1", "dead-planet temperature at L=1 equals the analytic energy balance (|diff| < 1e-9)", [Td, an], abs(Td-an) < 1e-9))
        g = [growth(22.5), growth(5.0), growth(40.0)]
        chk.append(R.chk("V2", "W01 eq. 3: growth 1 at 22.5 C and 0 at 5 C and 40 C", g, abs(g[0]-1) < 1e-12 and abs(g[1]) < 1e-12 and abs(g[2]) < 1e-12))
    if "original" in X:
        s = summary(run(M)); res["original"] = s; t = T1["original"]
        chk.append(R.chk("H2", "re-implementation from W01's published equations reproduces Table 1 'Original Daisyworld': establishment L 0.68 and maximum L 1.50 (each within +-0.02)", [s["L_establish"], s["L_max"], t], abs(s["L_establish"]-t["L_establish"]) <= 0.02 and abs(s["L_max"]-t["L_max"]) <= 0.02, kind="hypothesis"))
    if "neutral" in X:
        o = summary(run(dict(M, albedo=[0.5, 0.5]))); s = summary(run(M)); res["neutral"] = o; res["original"] = s; t = T1["neutral"]
        chk.append(R.chk("H3", "neutral-daisy control reproduces Table 1: range 0.74-1.11 (each within +-0.02)", [o["L_establish"], o["L_max"], t], abs(o["L_establish"]-t["L_establish"]) <= 0.02 and abs(o["L_max"]-t["L_max"]) <= 0.02, kind="hypothesis"))
        ok = all(abs(x["total_life"]-T1[k]["total_life"])/T1[k]["total_life"] <= 0.1 for x, k in ((s, "original"), (o, "neutral")))
        chk.append(R.chk("H3b", "our reading of 'total life' (integral of daisy cover over luminosity) reproduces Table 1's 0.556 and 0.204 within 10%", [s["total_life"], o["total_life"]], ok, kind="hypothesis"))
    if "seed_floor" in X:
        out = {str(f): summary(run(dict(M, seed=f))) for f in X["seed_floor"]["floors"]}; res["seed_floor"] = out
        Le = [v["L_establish"] for v in out.values()]
        chk.append(R.chk("H4", "establishment luminosity changes by <= 0.02 across seed floors 1e-4 to 1e-2 (the floor is not given in W01)", Le, max(Le)-min(Le) <= 0.02, kind="hypothesis"))
    if "unbounded" in X:
        e = X["unbounded"]; s0 = summary(run(M)); out = [dict(k=k, **summary(run(M, adapt=dict(k=k)))) for k in e["k"]]; res["original"] = s0; res["unbounded"] = out
        worse = [o for o in out if o["slope_ratio"] is not None and o["slope_ratio"] >= s0["slope_ratio"] + e["min_increase"]]
        chk.append(R.chk("H5", "unbounded adaptation of growth optima toward local temperature (R&R 1998 in W01's equations) weakens regulation at every rate: slope ratio rises by >= 0.3", [s0["slope_ratio"], [(o["k"], o["slope_ratio"], o["width"]) for o in out]], len(worse) == len(out), kind="hypothesis"))
    if "constrained" in X:
        e = X["constrained"]; s0 = summary(run(M)); u = summary(run(M, adapt=dict(k=e["k"]))); c = summary(run(M, adapt=dict(k=e["k"], bound=tuple(e["bound"]), R=e["R"])))
        res["constrained"] = dict(original=s0, unbounded=u, constrained=c)
        chk.append(R.chk("H6", "bounded, costed adaptation recovers regulation (slope ratio within 0.2 of the original) while extending the life range beyond the original", [s0["slope_ratio"], u["slope_ratio"], c["slope_ratio"], s0["width"], c["width"]], c["slope_ratio"] is not None and abs(c["slope_ratio"]-s0["slope_ratio"]) <= 0.2 and c["width"] > s0["width"], kind="hypothesis"))
    if "vs_published" in X:
        e = X["vs_published"]; c = summary(run(M, adapt=dict(k=e["k"], bound=tuple(e["bound"]), R=e["R"]))); t = T1["constrained_LL2000"]; res["constrained"] = c
        chk.append(R.chk("H7", "our constrained variant matches the published Table 1 'Constrained adaptation' row (L 0.51-2.32) within +-0.1 at both ends (W03 equations unavailable)", [c["L_establish"], c["L_max"], t], c["L_establish"] is not None and abs(c["L_establish"]-t["L_establish"]) <= 0.1 and abs(c["L_max"]-t["L_max"]) <= 0.1, kind="hypothesis"))
    if "grid" in X:
        e = X["grid"]; s0 = summary(run(M)); rows = []
        for k in e["k"]:
            for Rr in e["R"]:
                c = summary(run(M, adapt=dict(k=k, bound=tuple(e["bound"]), R=Rr))); rows.append(dict(k=k, R=Rr, slope_ratio=c["slope_ratio"], width=c["width"]))
            u = summary(run(M, adapt=dict(k=k))); rows.append(dict(k=k, R=None, slope_ratio=u["slope_ratio"], width=u["width"]))
        ok = lambda r: r["slope_ratio"] is not None and abs(r["slope_ratio"]-s0["slope_ratio"]) <= 0.2
        fc = float(np.mean([ok(r) for r in rows if r["R"] is not None])); fu = float(np.mean([ok(r) for r in rows if r["R"] is None])); res["grid"] = dict(rows=rows, frac_constrained=fc, frac_unbounded=fu)
        chk.append(R.chk("H8", "regulation recovered in >= 70% of constrained settings and <= 30% of unbounded ones", [fc, fu], fc >= 0.7 and fu <= 0.3, kind="hypothesis"))
    if "timestep" in X:
        s1 = summary(run(M)); s2 = summary(run(M, dt=X["timestep"]["dt"])); res["timestep"] = dict(dt1=s1, dt_half=s2)
        chk.append(R.chk("H9", "halving the Euler time step changes establishment and maximum luminosity by <= 0.01 (numerical robustness)", [s1["L_establish"], s2["L_establish"], s1["L_max"], s2["L_max"]], abs(s1["L_establish"]-s2["L_establish"]) <= 0.01 and abs(s1["L_max"]-s2["L_max"]) <= 0.01, kind="hypothesis"))
    R.finish(H, P, res, chk, t0)
if __name__ == "__main__": main()
