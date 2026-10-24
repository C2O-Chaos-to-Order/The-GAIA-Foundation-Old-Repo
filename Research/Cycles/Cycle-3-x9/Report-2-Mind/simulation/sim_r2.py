"""SIM-R2-C3: designing experiments that discriminate Pearce-Hall-type and Kalman-filter (Bayesian) accounts of latent inhibition
(carried item 'R2 discriminating LI datasets'). Logged Cycle-3 searches found no open-access parametric latent-inhibition dataset to fit
(see research/pass-1 and pass-5), so this simulation asks which designs WOULD discriminate. run() is copied unchanged from SIM-R2-C2 and
extended with (i) empty 'delay' steps (no trials) and (ii) a Mackintosh-type associability model as a third competitor. No animal data fitted."""
import sys, os, json, itertools, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "tools")); import runner as R
C2IT1 = os.path.join(HERE, "..", "..", "..", "Cycle-2-x6", "Report-2-Mind", "simulation", "iter-1", "outputs", "results.json")
def run(model, p, trials, n_cues=3):
    """trials: (cue_vector, US) or None (= one empty delay step). Returns predictions (before update) and final weights."""
    V = np.zeros(n_cues); al = np.full(n_cues, p.get("alpha0", p.get("alpha", 0.3))); S = np.eye(n_cues)*p.get("s0", 1.0); preds = []
    for tr in trials:
        if tr is None:
            if model == "KF": S = S + np.eye(n_cues)*p["tau2"]
            continue
        x, us = tr; x = np.asarray(x, float); v = float(V @ x); preds.append(v); d = us - v
        if model == "RW": V = V + p["alpha"]*p["beta"]*d*x
        elif model == "PH":
            V = V + p["S"]*al*d*x; al = np.where(x > 0, p["gamma"]*abs(d) + (1-p["gamma"])*al, al)
        elif model == "KF":
            S = S + np.eye(n_cues)*p["tau2"]; k = S @ x / (x @ S @ x + p["sigma2"]); V = V + k*d; S = S - np.outer(k, x @ S)
        elif model == "MK":  # Mackintosh (1975)-type: separate errors; associability rises for the cue that predicts better than the others
            Vn = V.copy()
            for i in np.nonzero(x)[0]:
                oth = float(V @ x - V[i]); al[i] = np.clip(al[i] + p["theta"]*(abs(us-oth) - abs(us-V[i])), p["amin"], 1.0)
                Vn[i] = V[i] + p["S"]*al[i]*(us - V[i])
            if x.sum() == 1:  # single cue: associability declines with non-informative exposure (pre-exposure, US = 0 ~ V)
                i = int(np.nonzero(x)[0][0]); al[i] = max(p["amin"], al[i] - p["theta"]*(1 - abs(us - V[i]))*(us == 0))
            V = Vn
        else: raise ValueError(model)
    return np.array(preds), V
A, X, B = [1, 0, 0], [0, 1, 0], [1, 1, 0]
AC1, AC2 = [1, 0, 1], [1, 0, 0]  # cue A with context cue (C1) present / absent (context change)
def li(model, p, n_pre, n_acq, delay=0, ctx_change=False):
    pre_c = AC1; acq_c = AC2 if ctx_change else AC1
    pr, _ = run(model, p, [(pre_c, 0.0)]*n_pre + [None]*delay + [(acq_c, 1.0)]*n_acq); ct, _ = run(model, p, [None]*delay + [(acq_c, 1.0)]*n_acq)
    return float(1 - pr[-1]/ct[-1]) if ct[-1] > 0 else None
def design_curve(model, p, D):
    y = [li(model, p, n, D["n_acq"]) for n in D["n_pre"]] + [li(model, p, D["n_pre_fixed"], D["n_acq"], delay=dl) for dl in D["delays"]]
    return np.array([v if v is not None else 0.0 for v in y])
def grid_points(G): keys = list(G); return [dict(zip(keys, v)) for v in itertools.product(*[G[k] for k in keys])]
def recover(D, grids, truths_fn, noise, reps, rng):
    C = {m: np.array([design_curve(m, p, D) for p in grid_points(G)]) for m, G in grids.items()}; models = list(grids); hit = 0
    for r in range(reps):
        gen = models[r % len(models)]; y = design_curve(gen, truths_fn(gen, rng), D); y = y + noise*rng.standard_normal(len(y))
        best = min(models, key=lambda m: ((C[m]-y)**2).mean(1).min()); hit += int(best == gen)
    return hit/reps
def main():
    P, prev, H = R.start(sys.argv[1]); t0 = R.now(); X = P["experiments"]; dfl = P["defaults"]; res = {}; chk = []
    if "reproduce" in X:
        c2 = json.load(open(C2IT1)); e = X["reproduce"]; mine = {}
        for mdl in ("PH", "KF"):
            pre, _ = run(mdl, dfl[mdl], [(A, 0.0)]*e["n_pre"] + [(A, 1.0)]*e["n_acq"]); ctl, _ = run(mdl, dfl[mdl], [(A, 1.0)]*e["n_acq"]); mine[mdl] = float(1-pre[-1]/ctl[-1])
        ref = {k: c2["phenomena"][k]["LI"] for k in ("PH", "KF")}
        chk.append(R.chk("V1", "copied run() reproduces the Cycle-2 iteration-1 latent-inhibition indices for PH and KF (|diff| < 1e-9)", [mine, ref], all(abs(mine[k]-ref[k]) < 1e-9 for k in mine)))
        _, Vd = run("KF", dfl["KF"], [None]*5); _, Vp = run("PH", dfl["PH"], [None]*5)
        chk.append(R.chk("V2", "empty delay steps change no associative weight in any model", [Vd.tolist(), Vp.tolist()], not Vd.any() and not Vp.any()))
    if "preexposure_curve" in X:
        e = X["preexposure_curve"]; out = {m: [li(m, dfl[m], n, e["n_acq"]) for n in e["n_pre"]] for m in ("PH", "KF", "MK")}
        res["li_by_preexposure"] = dict(n_pre=e["n_pre"], **out); dif = max(abs(a-b) for a, b in zip(out["PH"], out["KF"]))
        chk.append(R.chk("H2", "LI-by-number-of-pre-exposures curves of PH and KF differ by >= 0.15 somewhere (a parametric design could discriminate)", dif, dif >= 0.15, kind="hypothesis"))
        mono = all(b >= a-1e-12 for a, b in zip(out["MK"], out["MK"][1:]))
        chk.append(R.chk("H2b", "the Mackintosh-type model also yields LI that grows with pre-exposure (monotone)", out["MK"], mono and out["MK"][-1] > 0.05, kind="hypothesis"))
    if "context" in X:
        e = X["context"]; out = {}
        for m in ("PH", "KF", "MK"):
            same = li(m, dfl[m], e["n_pre"], e["n_acq"]); chg = li(m, dfl[m], e["n_pre"], e["n_acq"], ctx_change=True); out[m] = dict(same=same, changed=chg, attenuation=(1-chg/same) if same else None)
        res["context_change"] = out
        chk.append(R.chk("H3", "context change between pre-exposure and conditioning attenuates LI by >= 50% in BOTH PH and KF (LI is context-specific in animals)", out, all(out[m]["attenuation"] is not None and out[m]["attenuation"] >= 0.5 for m in ("PH", "KF")), kind="hypothesis"))
    if "delay" in X:
        e = X["delay"]; out = {m: [li(m, dfl[m], e["n_pre"], e["n_acq"], delay=d) for d in e["delays"]] for m in ("PH", "KF", "MK")}
        res["li_by_delay"] = dict(delays=e["delays"], **out); kf = 1-out["KF"][-1]/out["KF"][0]; ph = abs(1-out["PH"][-1]/out["PH"][0])
        chk.append(R.chk("H4", "a delay between pre-exposure and conditioning attenuates LI by >= 50% in KF (uncertainty grows) but changes PH by < 5% (no trials, no change)", [kf, ph], kf >= 0.5 and ph < 0.05, kind="hypothesis"))
    D = X.get("design")
    truths = lambda gen, rng: dfl[gen]
    def off(gen, rng):
        G = P["off_grid"][gen]; return {k: float(rng.uniform(*v)) for k, v in G.items()}
    if "recovery_on_grid" in X:
        e = X["recovery_on_grid"]; rng = np.random.default_rng(e["seed"]); out = {}
        for nz in e["noise"]:
            out[str(nz)] = recover(D, {k: P["grids"][k] for k in ("PH", "KF")}, truths, nz, e["reps"], rng)
        res["recovery_on_grid"] = out
        chk.append(R.chk("H5", "PH vs KF recovered in >= 80% of datasets at noise 0.1 with the parametric pre-exposure + delay design (defaults as generators)", out, out["0.1"] >= 0.8, kind="hypothesis"))
    if "recovery_off_grid" in X:
        e = X["recovery_off_grid"]; rng = np.random.default_rng(e["seed"]); out = {}
        for nz in e["noise"]:
            out[str(nz)] = recover(D, {k: P["grids"][k] for k in ("PH", "KF")}, off, nz, e["reps"], rng)
        res["recovery_off_grid"] = out
        chk.append(R.chk("H6", "recovery stays >= 70% at noise 0.1 when generating parameters are drawn OFF the fitting grid (removes the Cycle-2 optimism)", out, out["0.1"] >= 0.7, kind="hypothesis"))
    if "sensitivity" in X:
        e = X["sensitivity"]; rows = []
        for t2 in e["tau2"]:
            for s2 in e["sigma2"]:
                p = dict(dfl["KF"], tau2=t2, sigma2=s2); a = li("KF", p, e["n_pre"], e["n_acq"]); b = li("KF", p, e["n_pre"], e["n_acq"], delay=e["delay"])
                rows.append(dict(tau2=t2, sigma2=s2, li0=a, li_delay=b, drop=(a-b) if (a is not None and b is not None) else None))
        frac = float(np.mean([r["drop"] is not None and r["drop"] >= 0.1 for r in rows])); res["sensitivity"] = dict(rows=rows, frac_drop_ge_0_1=frac)
        chk.append(R.chk("H7", "the KF delay signature (LI drop >= 0.1) holds in >= 70% of a tau2 x sigma2 grid", frac, frac >= 0.7, kind="hypothesis"))
    if "three_models" in X:
        e = X["three_models"]; rng = np.random.default_rng(e["seed"]); out = {}
        for nz in e["noise"]:
            out[str(nz)] = recover(D, {k: P["grids"][k] for k in ("PH", "KF", "MK")}, off, nz, e["reps"], rng)
        res["recovery_three_models_off_grid"] = out
        chk.append(R.chk("H8", "adding a Mackintosh-type competitor, three-way recovery stays >= 70% at noise 0.1 (off-grid generators)", out, out["0.1"] >= 0.7, kind="hypothesis"))
    if "replicate" in X:
        e = X["replicate"]; rng = np.random.default_rng(e["seed"]); a = recover(D, {k: P["grids"][k] for k in ("PH", "KF")}, off, 0.1, e["reps"], rng)
        p6 = json.load(open(os.path.join(H, "..", "iter-6", "outputs", "results.json")))["recovery_off_grid"]["0.1"]
        res["replicate_off_grid_0.1"] = dict(new_seed=a, iter6=p6)
        chk.append(R.chk("H9", "iteration-6 off-grid recovery at noise 0.1 replicates with a new seed and 2x replicates (|diff| <= 0.05)", [a, p6], abs(a-p6) <= 0.05, kind="hypothesis"))
    R.finish(H, P, res, chk, t0)
if __name__ == "__main__": main()
