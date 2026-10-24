"""SIM-R2-C4: robustness and design power of the delay design that separates Pearce-Hall-type (PH) and Kalman-filter (KF) accounts of
latent inhibition (LI). SUBSTITUTE for the carried item 'R2 faithful Mackintosh (1975) rule', which is BLOCKED: no open-access text giving
the rule's specification was found in Cycle-4 searches (Y05 Esber & Haselgrove 2011 abstract only; Y07, Y08 read, no specification), and we
will not implement Mackintosh from memory. This is therefore a smaller, honest simulation about the PH-vs-KF design only.
run(), li(), design_curve(), grid_points() and recover() are copied from SIM-R2-C3 (Mackintosh branch removed) and extended with ONE new
option: 'rho' = per-empty-step recovery of PH associability toward its initial value (a possible time-based process that would give PH a
delay effect too; rho = 0 reproduces Cycle 3 exactly). No animal data are fitted."""
import sys, os, json, itertools, numpy as np
from scipy import stats
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "tools")); import runner as R
C3IT4 = os.path.join(HERE, "..", "..", "..", "Cycle-3-x9", "Report-2-Mind", "simulation", "iter-4", "outputs", "results.json")
def run(model, p, trials, n_cues=3):
    V = np.zeros(n_cues); a0 = p.get("alpha0", p.get("alpha", 0.3)); al = np.full(n_cues, a0); S = np.eye(n_cues)*p.get("s0", 1.0); preds = []
    for tr in trials:
        if tr is None:
            if model == "KF": S = S + np.eye(n_cues)*p["tau2"]
            if model == "PH" and p.get("rho", 0.0): al = al + p["rho"]*(a0 - al)
            continue
        x, us = tr; x = np.asarray(x, float); v = float(V @ x); preds.append(v); d = us - v
        if model == "RW": V = V + p["alpha"]*p["beta"]*d*x
        elif model == "PH":
            V = V + p["S"]*al*d*x; al = np.where(x > 0, p["gamma"]*abs(d) + (1-p["gamma"])*al, al)
        elif model == "KF":
            S = S + np.eye(n_cues)*p["tau2"]; k = S @ x / (x @ S @ x + p["sigma2"]); V = V + k*d; S = S - np.outer(k, x @ S)
        else: raise ValueError(model)
    return np.array(preds), V
AC1, AC2 = [1, 0, 1], [1, 0, 0]
def li(model, p, n_pre, n_acq, delay=0, ctx_change=False):
    pre_c = AC1; acq_c = AC2 if ctx_change else AC1
    pr, _ = run(model, p, [(pre_c, 0.0)]*n_pre + [None]*delay + [(acq_c, 1.0)]*n_acq); ct, _ = run(model, p, [None]*delay + [(acq_c, 1.0)]*n_acq)
    return float(1 - pr[-1]/ct[-1]) if ct[-1] > 0 else None
def design_curve(model, p, D):
    y = [li(model, p, n, D["n_acq"]) for n in D["n_pre"]] + [li(model, p, D["n_pre_fixed"], D["n_acq"], delay=dl) for dl in D["delays"]]
    return np.array([v if v is not None else 0.0 for v in y])
def grid_points(G): keys = list(G); return [dict(zip(keys, v)) for v in itertools.product(*[G[k] for k in keys])]
def recover(D, grids, truths_fn, noise, reps, rng, fixed=None):
    fixed = fixed or {}
    C = {m: np.array([design_curve(m, dict(fixed.get(m, {}), **p), D) for p in grid_points(G)]) for m, G in grids.items()}; models = list(grids); hit = 0
    for r in range(reps):
        gen = models[r % len(models)]; y = design_curve(gen, truths_fn(gen, rng), D); y = y + noise*rng.standard_normal(len(y))
        best = min(models, key=lambda m: ((C[m]-y)**2).mean(1).min()); hit += int(best == gen)
    return hit/reps
def main():
    P, prev, H = R.start(sys.argv[1]); t0 = R.now(); X = P["experiments"]; dfl = P["defaults"]; G = P["grids"]; D = P["design"]; res = {}; chk = []; k = P["iteration"]
    def off(gen, rng, wide=1.0, rho=None):
        q = {kk: float(rng.uniform(*v)) for kk, v in P["off_grid"][gen].items()}
        if gen == "KF" and wide != 1.0: q["tau2"] = float(np.exp(rng.uniform(np.log(P["off_grid"]["KF"]["tau2"][0]/wide), np.log(P["off_grid"]["KF"]["tau2"][1]*wide))))
        if gen == "PH" and rho: q["rho"] = float(rng.uniform(*rho))
        return q
    if k == 1:
        c3 = json.load(open(C3IT4))["li_by_delay"]; e = X["reproduce"]
        mine = {m: [li(m, dfl[m], e["n_pre"], e["n_acq"], delay=d) for d in c3["delays"]] for m in ("PH", "KF")}
        chk.append(R.chk("V1", "copied run() (Mackintosh branch removed, rho = 0) reproduces the Cycle-3 iteration-4 LI-by-delay values for PH and KF (|diff| < 1e-9)", [mine, {m: c3[m] for m in mine}], all(abs(a-b) < 1e-9 for m in mine for a, b in zip(mine[m], c3[m]))))
        _, Vp = run("PH", dict(dfl["PH"], rho=0.05), [None]*5)
        chk.append(R.chk("V2", "with the new rho option, empty delay steps still change no associative weight", Vp.tolist(), not Vp.any()))
        res["li_by_delay"] = mine
    elif k == 2:
        e = X["power"]; rng = np.random.default_rng(e["seed"]); d0 = {m: li(m, dfl[m], 30, 5) for m in ("PH", "KF")}; d1 = {m: li(m, dfl[m], 30, 5, delay=e["delay"]) for m in ("PH", "KF")}
        out = {}
        for sd in e["sd"]:
            for n in e["n"]:
                hits = {m: 0 for m in ("PH", "KF")}
                for _ in range(e["reps"]):
                    for m in ("PH", "KF"):
                        a = d0[m] + sd*rng.standard_normal(n); b = d1[m] + sd*rng.standard_normal(n); hits[m] += int(stats.ttest_ind(a, b).pvalue < 0.05)
                out[f"sd{sd}_n{n}"] = {m: hits[m]/e["reps"] for m in hits}
        n80 = next((n for n in e["n"] if out[f"sd{e['sd'][-1]}_n{n}"]["KF"] >= 0.8), None); res.update(li_no_delay=d0, li_delay=d1, power=out, n80_at_max_sd=n80)
        fp = [out[kk]["PH"] for kk in out]
        chk.append(R.chk("H2", f"80% power to detect the KF delay effect (two groups, t-test) is reached at <= 20 subjects per group with between-subject SD {e['sd'][-1]} in LI", n80, n80 is not None and n80 <= 20, "hypothesis"))
        chk.append(R.chk("V3", "PH has no delay effect, so its 'detection' rate is the false-positive rate: every cell within 2-9% (nominal 5%)", fp, all(.02 <= f <= .09 for f in fp)))
    elif k in (3, 4, 5):
        e = X["recovery"]; rng = np.random.default_rng(e["seed"]); Dk = dict(D, **e.get("design_override", {})); out = {}
        for nz in e["noise"]: out[str(nz)] = recover(Dk, {m: G[m] for m in ("PH", "KF")}, off, nz, e["reps"], rng)
        res["recovery"] = out; res["design_used"] = Dk
        thr = e["threshold"]; chk.append(R.chk(f"H{k}", e["label"], out, out[str(e["at"])] >= thr, "hypothesis"))
    elif k == 6:
        e = X["recovery"]; rng = np.random.default_rng(e["seed"]); out = {}
        for nz in e["noise"]: out[str(nz)] = recover(D, {m: G[m] for m in ("PH", "KF")}, lambda g, r: off(g, r, wide=e["wide"]), nz, e["reps"], rng)
        res["recovery_wide_tau2"] = out
        chk.append(R.chk("H6", f"recovery stays >= 70% at noise 0.1 when KF tau2 generators range {e['wide']}x beyond the fitting grid on each side (mis-specified range)", out, out["0.1"] >= 0.7, "hypothesis"))
    elif k == 7:
        e = X["hybrid"]; rng = np.random.default_rng(e["seed"]); Cg = {m: np.array([design_curve(m, p, D) for p in grid_points(G[m])]) for m in ("PH", "KF")}; out = {}
        for w in e["w_kf"]:
            pick = []
            for _ in range(e["reps"]):
                y = w*design_curve("KF", off("KF", rng), D) + (1-w)*design_curve("PH", off("PH", rng), D) + 0.1*rng.standard_normal(len(D["n_pre"]) + len(D["delays"]))
                pick.append(min(("PH", "KF"), key=lambda m: ((Cg[m]-y)**2).mean(1).min()) == "KF")
            out[str(w)] = float(np.mean(pick))
        res["share_classified_KF"] = out
        chk.append(R.chk("H7r", "share of 50/50 and other mixtures classified as KF (a two-model comparison forces a choice)", out, True, "reporting"))
        chk.append(R.chk("H7", "a 50/50 PH-KF mixture is NOT confidently assigned to either model (share classified KF between 0.2 and 0.8)", out["0.5"], .2 <= out["0.5"] <= .8, "hypothesis"))
    elif k == 8:
        e = X["delay_scan"]; out = {str(d): li("KF", dfl["KF"], 30, 5, delay=d) for d in e["delays"]}; base0 = out["0"]
        half = next((d for d in e["delays"] if out[str(d)] <= base0/2), None); res.update(kf_li_by_delay=out, delay_half=half)
        rows = []
        for t2 in e["tau2"]:
            p = dict(dfl["KF"], tau2=t2); a = li("KF", p, 30, 5); rows.append(dict(tau2=t2, half=next((d for d in e["delays"] if li("KF", p, 30, 5, delay=d) <= a/2), None)))
        res["half_by_tau2"] = rows
        chk.append(R.chk("H8", "at KF defaults, a delay of <= 20 empty steps halves LI", half, half is not None and half <= 20, "hypothesis"))
        chk.append(R.chk("H8r", "delay needed to halve LI, by tau2", rows, True, "reporting"))
    elif k == 9:
        e = X["ph_recovery"]; out = {}
        for rho in e["rho"]:
            p = dict(dfl["PH"], rho=rho); a = li("PH", p, 30, 5); b = li("PH", p, 30, 5, delay=e["delay"]); out[str(rho)] = dict(li0=a, li_delay=b, drop=(1-b/a) if a else None)
        kf = 1 - li("KF", dfl["KF"], 30, 5, delay=e["delay"])/li("KF", dfl["KF"], 30, 5); res.update(ph=out, kf_drop=kf)
        chk.append(R.chk("H9", f"if PH associability recovers during the delay at rho = {e['rho'][1]} per step, the PH delay drop stays < 50% (the signature still separates the models)", out[str(e["rho"][1])], out[str(e["rho"][1])]["drop"] < 0.5, "hypothesis"))
        chk.append(R.chk("H9r", "PH delay drop by rho, and KF drop", [{kk: v["drop"] for kk, v in out.items()}, kf], True, "reporting"))
    elif k == 10:
        e = X["recovery_rho"]; rng = np.random.default_rng(e["seed"]); out = {}
        grids = {"PH": dict(G["PH"], rho=e["rho_grid"]), "KF": G["KF"]}
        for nz in e["noise"]: out[str(nz)] = recover(D, grids, lambda g, r: off(g, r, rho=e["rho_gen"]), nz, e["reps"], rng)
        res["recovery_with_ph_recovery"] = out
        chk.append(R.chk("H10", "when PH associability may recover during the delay (generators rho in [0, 0.05], fitted with a rho grid), recovery is still >= 70% at noise 0.1", out, out["0.1"] >= 0.7, "hypothesis"))
    elif k == 11:
        e = X["replicate"]; rng = np.random.default_rng(e["seed"]); Dk = dict(D, **e["design_override"]); a = recover(Dk, {m: G[m] for m in ("PH", "KF")}, off, 0.1, e["reps"], rng)
        p3 = json.load(open(os.path.join(H, "..", "iter-3", "outputs", "results.json")))["recovery"]["0.1"]; res["replicate"] = dict(new_seed=a, iter3=p3)
        chk.append(R.chk("H11", "iteration-3 (delay-only design) recovery at noise 0.1 replicates with a new seed and 2x replicates (|diff| <= 0.05)", [a, p3], abs(a-p3) <= 0.05, "hypothesis"))
    elif k == 12:
        tab = {}
        for kk in range(3, 12):
            r = json.load(open(os.path.join(H, "..", f"iter-{kk}", "outputs", "results.json"))); tab[f"iter-{kk}"] = r
        rec = {kk: tab[kk]["recovery"]["0.1"] for kk in ("iter-3", "iter-4", "iter-5")}
        res.update(recovery_by_design_at_0_1=rec, summary=dict(wide=tab["iter-6"]["recovery_wide_tau2"]["0.1"], rho=tab["iter-10"]["recovery_with_ph_recovery"]["0.1"], replicate=tab["iter-11"]["replicate"]))
        chk.append(R.chk("H12", "consolidation: the delay arms carry the discrimination - the delay-only design (iter-3) recovers at least as well as the pre-exposure-curve-only design (iter-4) at noise 0.1", rec, rec["iter-3"] >= rec["iter-4"], "hypothesis"))
    R.finish(H, P, res, chk, t0)
if __name__ == "__main__": main()
