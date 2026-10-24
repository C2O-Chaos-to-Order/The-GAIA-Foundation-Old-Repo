"""SIM-R6-C2: adaptive Daisyworld - does planetary regulation survive when daisies adapt their optimum temperature?
Replicates the DESIGN contrast of Robertson & Robinson 1998 (W02, abstract: unconstrained adaptation) and Lenton & Lovelock 2000/2001
(W03 abstract, W01 full text: adaptation bounded and growth limited near the bounds -> 'temperature regulation is recovered').
Our own re-implementation from the published verbal descriptions; NOT a reproduction of their code or exact equations.
Daisyworld is a parable model (Watson & Lovelock 1983, S21b). Results say nothing about the real Earth by themselves."""
import sys, os, json, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools")); import runner as R
SB = 5.670374419e-8
def daisy(d, Ls, life=True, adapt=0.0, bound=None, cost=0.0):
    """Two-daisy world identical to SIM-R6-C1 when cost=0. bound: max |Topt - T_opt| (None = unbounded).
    cost: peak growth multiplier 1 - cost*(shift/bound)^2 (growth limited as bounds are approached; needs a bound)."""
    ab = aw = d["seed_area"] if life else 0.0; Tob = Tow = d["T_opt"]; rows = []
    for L in Ls:
        for _ in range(d["steps"]):
            ag = d["P"]-ab-aw; A = ag*d["Ag"]+ab*d["Ab"]+aw*d["Aw"]+(1-d["P"])*d["Ag"]
            Te = (d["S"]*L*(1-A)/SB)**0.25-273; Tb = d["q"]*(A-d["Ab"])+Te; Tw = d["q"]*(A-d["Aw"])+Te
            pb = pw = 1.0
            if cost and bound: pb = 1-cost*((Tob-d["T_opt"])/bound)**2; pw = 1-cost*((Tow-d["T_opt"])/bound)**2
            bb = max(0.0, pb*(1-0.003265*(Tob-Tb)**2)); bw = max(0.0, pw*(1-0.003265*(Tow-Tw)**2))
            ab += d["dt"]*ab*(ag*bb-d["gamma"]); aw += d["dt"]*aw*(ag*bw-d["gamma"])
            if life: ab = max(ab, d["seed_area"]); aw = max(aw, d["seed_area"])
            if adapt:
                Tob += d["dt"]*adapt*(Tb-Tob); Tow += d["dt"]*adapt*(Tw-Tow)
                if bound is not None:
                    Tob = min(max(Tob, d["T_opt"]-bound), d["T_opt"]+bound); Tow = min(max(Tow, d["T_opt"]-bound), d["T_opt"]+bound)
        ag = d["P"]-ab-aw; A = ag*d["Ag"]+ab*d["Ab"]+aw*d["Aw"]+(1-d["P"])*d["Ag"]; Te = (d["S"]*L*(1-A)/SB)**0.25-273
        rows.append((float(L), float(Te), float(ab), float(aw), float(Tob), float(Tow)))
    return rows
def multi(d, Ls, albedos, mu):
    """k daisy types with fixed albedos; 'mutation' = fraction mu of each type's growth flows to its albedo neighbours."""
    k = len(albedos); a = np.full(k, d["seed_area"]); Al = np.array(albedos); rows = []
    for L in Ls:
        for _ in range(d["steps"]):
            ag = d["P"]-a.sum(); A = ag*d["Ag"]+(a*Al).sum()+(1-d["P"])*d["Ag"]
            Te = (d["S"]*L*(1-A)/SB)**0.25-273; Ti = d["q"]*(A-Al)+Te
            b = np.maximum(0.0, 1-0.003265*(d["T_opt"]-Ti)**2); g = a*ag*b
            gm = (1-mu)*g; gm[1:] += mu/2*g[:-1]; gm[:-1] += mu/2*g[1:]; gm[0] += mu/2*g[0]; gm[-1] += mu/2*g[-1]
            a = np.maximum(a+d["dt"]*(gm-d["gamma"]*a), d["seed_area"])
        ag = d["P"]-a.sum(); A = ag*d["Ag"]+(a*Al).sum()+(1-d["P"])*d["Ag"]; Te = (d["S"]*L*(1-A)/SB)**0.25-273
        rows.append((float(L), float(Te)))
    return rows
def band(rows, centre, half):
    ok = [abs(r[1]-centre) <= half for r in rows]; best = cur = 0; step = rows[1][0]-rows[0][0]
    for o in ok: cur = cur+1 if o else 0; best = max(best, cur)
    return round(max(best-1, 0)*step, 4)
def damping(rows_life, rows_dead, centre, half):
    """mean |dTe/dL| lifeless / with life, over L where the living planet is inside the band (higher = stronger damping)."""
    L = np.array([r[0] for r in rows_life]); Tl = np.array([r[1] for r in rows_life]); Td = np.array([r[1] for r in rows_dead])
    m = np.abs(Tl-centre) <= half; m = m[1:] & m[:-1]
    if m.sum() < 2: return None
    sl = np.abs(np.diff(Tl)/np.diff(L))[m].mean(); sd = np.abs(np.diff(Td)/np.diff(L))[m].mean()
    return float(sd/sl) if sl > 0 else None
def main():
    P, prev, H = R.start(sys.argv[1]); t0 = R.now(); X = P["experiments"]; res = {}; chk = []
    base = P["daisy"]; Ls = np.round(np.arange(*base["L"]), 4); c, h = base["T_opt"], base["band_half"]
    w0 = band(daisy(base, Ls), c, h); res["no_adaptation_width"] = w0
    wd = band(daisy(base, Ls, life=False), c, h); res["lifeless_width"] = wd
    if prev: res["carried_from_prev"] = {k: prev[k] for k in P.get("carry", []) if k in prev}
    if "replicate_c1" in X:
        e = X["replicate_c1"]; wu = band(daisy(base, Ls, adapt=e["rate"]), c, h)
        res["replicate_c1"] = dict(no_adaptation=w0, unbounded=wu)
        chk.append(R.chk("R0", f"re-implementation reproduces the Cycle-1 widths exactly ({e['c1_expected']} from {e['c1_ref']})", [w0, wu], [w0, wu] == e["c1_expected"]))
        rates = e["rates"]; out = [(r, band(daisy(base, Ls, adapt=r), c, h)) for r in rates]; res["unbounded_by_rate"] = out
        chk.append(R.chk("U1", "W02 design (unconstrained adaptation): regulation band shrinks below 0.8x non-adapting for every positive rate tested",
                         out, all(w < 0.8*w0 for r, w in out if r > 0), kind="hypothesis"))
        res["worst_rate"] = min((x for x in out if x[0] > 0), key=lambda x: x[1])[0]
    if "constrained" in X:
        e = X["constrained"]; rate = prev["worst_rate"] if prev and "worst_rate" in prev and e.get("use_prev_worst_rate") else e["rate"]
        out = []
        for b in e["bounds"]:
            for k in e["costs"]:
                if b is None and k: continue
                out.append(dict(bound=b, cost=k, rate=rate, width=band(daisy(base, Ls, adapt=rate, bound=b, cost=k), c, h)))
        res["constrained"] = out; res["constrained_rate"] = rate
        ok = [o for o in out if o["bound"] is not None and o["cost"] > 0]
        chk.append(R.chk("LL1", "W03/W01 design (bounded adaptation + growth limited near bounds): band >= 0.8x non-adapting for every bounded, costed setting",
                         [(o["bound"], o["cost"], o["width"]) for o in ok], all(o["width"] >= 0.8*w0 for o in ok), kind="hypothesis"))
        nb = [o["width"] for o in out if o["bound"] is not None]
        chk.append(R.chk("LL2", "wider bounds give narrower bands (Spearman rho(bound, width) < 0 over bounded settings)",
                         float(spearman([o["bound"] for o in out if o["bound"] is not None], nb)), spearman([o["bound"] for o in out if o["bound"] is not None], nb) < 0, kind="hypothesis"))
    if "rate_ratio" in X:
        e = X["rate_ratio"]; out = []
        for st in e["steps"]:
            for r in e["rates"]:
                d = dict(base, steps=st); out.append(dict(steps=st, rate=r, adapt_per_forcing_step=r*st*base["dt"], width=band(daisy(d, Ls, adapt=r), c, h)))
        res["rate_ratio"] = out; xs = [o["adapt_per_forcing_step"] for o in out]; ys = [o["width"] for o in out]
        rho = spearman(xs, ys); res["rate_ratio_spearman"] = rho
        chk.append(R.chk("RR1", "W03 verbal argument: the faster adaptation is relative to forcing, the weaker the regulation (Spearman rho(adapt per forcing step, width) <= -0.8)", rho, rho <= -0.8, kind="hypothesis"))
    if "damping" in X:
        e = X["damping"]; dead = daisy(base, Ls, life=False); out = {}
        for name, kw in e["cases"].items():
            out[name] = damping(daisy(base, Ls, **kw), dead, c, h)
        res["damping"] = out
        chk.append(R.chk("DM0", "no-adaptation damping ratio > 1 (life reduces |dTe/dL| inside the band)", out.get("none"), (out.get("none") or 0) > 1))
        chk.append(R.chk("DM1", "report damping ratios per case (cf. W01 Table 1 'mean damping' - different metric; not comparable numerically)", out, True, kind="reporting"))
    if "mutating_albedo" in X:
        e = X["mutating_albedo"]; out = []
        two = band(multi(base, Ls, [base["Ab"], base["Aw"]], 0.0), c, h)
        chk.append(R.chk("M0", "2-type multi() without mutation equals the two-daisy model width", [two, w0], abs(two-w0) <= 0.02))
        for k in e["k"]:
            for mu in e["mu"]:
                al = list(np.linspace(e["albedo_min"], e["albedo_max"], k)); out.append(dict(k=k, mu=mu, width=band(multi(base, Ls, al, mu), c, h)))
        res["mutating_albedo"] = dict(two_type_width=two, rows=out)
        best_many = max(o["width"] for o in out if o["k"] > 2)
        chk.append(R.chk("M1", "W01 citing Stocker 1995: more albedo types with mutation extend the regulated range (max width for k>2 >= 1.1x two-type)", [best_many, two], best_many >= 1.1*two, kind="hypothesis"))
    if "robustness" in X:
        e = X["robustness"]; rows = []
        for g in e["gamma"]:
            for q in e["q"]:
                d = dict(base, gamma=g, q=q); wn = band(daisy(d, Ls), c, h)
                wc = band(daisy(d, Ls, adapt=e["rate"], bound=e["bound"], cost=e["cost"]), c, h)
                wu = band(daisy(d, Ls, adapt=e["rate"]), c, h)
                rows.append(dict(gamma=g, q=q, none=wn, constrained=wc, unbounded=wu))
        res["robustness"] = rows
        fc = float(np.mean([r["constrained"] >= 0.8*r["none"] for r in rows if r["none"] > 0])); fu = float(np.mean([r["unbounded"] >= 0.8*r["none"] for r in rows if r["none"] > 0]))
        res["robustness_summary"] = dict(frac_constrained_ok=fc, frac_unbounded_ok=fu, n=len(rows))
        chk.append(R.chk("RB1", "constrained adaptation keeps >= 0.8x the non-adapting band in >= 80% of (gamma, q) settings", fc, fc >= 0.8, kind="hypothesis"))
        chk.append(R.chk("RB2", "unbounded adaptation keeps >= 0.8x band in <= 20% of settings (the W02 erosion generalises)", fu, fu <= 0.2, kind="hypothesis"))
    R.finish(H, P, res, chk, t0)
def spearman(x, y):
    from scipy.stats import spearmanr
    r = spearmanr(x, y).correlation; return float(r) if r == r else 0.0
if __name__ == "__main__": main()
