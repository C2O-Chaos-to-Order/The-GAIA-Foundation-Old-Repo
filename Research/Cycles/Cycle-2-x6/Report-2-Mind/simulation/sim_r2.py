"""SIM-R2-C2: associative-learning models compared on blocking and latent inhibition, plus model identifiability.
Models (textbook forms, our own implementation): Rescorla-Wagner (RW); a Pearce-Hall-type hybrid (PH: delta rule scaled by an associability that tracks recent
|prediction error|, cf. S06 Holland & Schiffino 2016 and W06 Barto et al. 2013); a Kalman-filter learner (KF; Bayesian weights with
uncertainty - W06 notes a Bayesian account 'accomplishes what the Pearce-Hall model ... does'). No animal data are fitted."""
import sys, os, json, itertools, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools")); import runner as R
def run(model, p, trials, n_cues=3):
    """trials: list of (cue_vector, US). Returns list of predictions for each trial (before update) and final weights."""
    V = np.zeros(n_cues); al = np.full(n_cues, p.get("alpha0", p.get("alpha", 0.3))); S = np.eye(n_cues)*p.get("s0", 1.0); preds = []
    for x, us in trials:
        x = np.asarray(x, float); v = float(V @ x); preds.append(v); d = us - v
        if model == "RW": V = V + p["alpha"]*p["beta"]*d*x
        elif model == "PH":  # hybrid form: delta rule scaled by associability; associability tracks recent |prediction error| (gamma)
            V = V + p["S"]*al*d*x; al = np.where(x > 0, p["gamma"]*abs(d) + (1-p["gamma"])*al, al)
        elif model == "KF":
            S = S + np.eye(n_cues)*p["tau2"]; k = S @ x / (x @ S @ x + p["sigma2"]); V = V + k*d; S = S - np.outer(k, x @ S)
        else: raise ValueError(model)
    return np.array(preds), V
A, X, B = [1, 0, 0], [0, 1, 0], [1, 1, 0]
def li_index(model, p, n_pre, n_acq):
    pre, _ = run(model, p, [(A, 0.0)]*n_pre + [(A, 1.0)]*n_acq); ctl, _ = run(model, p, [(A, 1.0)]*n_acq)
    vp = pre[-1]; vc = ctl[-1]; return float(1 - vp/vc) if vc > 0 else None, pre[n_pre:], ctl
def block_index(model, p, n1, n2):
    _, Vb = run(model, p, [(A, 1.0)]*n1 + [(B, 1.0)]*n2); _, Vc = run(model, p, [(B, 1.0)]*n2)
    return float(1 - Vb[1]/Vc[1]) if Vc[1] > 0 else None
def curve(model, p, design):
    if design == "acquisition": pr, _ = run(model, p, [(A, 1.0)]*20); return pr
    li = li_index(model, p, 20, 20)[1]; _, Vb = run(model, p, [(A, 1.0)]*10 + [(B, 1.0)]*10); _, Vc = run(model, p, [(B, 1.0)]*10)
    acq, _ = run(model, p, [(A, 1.0)]*20)
    return np.concatenate([acq, li, [Vb[1], Vc[1]]])
def fit(y, design, grids):
    best = {}
    for m, G in grids.items():
        keys = list(G); errs = []
        for vals in itertools.product(*[G[k] for k in keys]):
            p = dict(zip(keys, vals)); errs.append(float(np.mean((curve(m, p, design)-y)**2)))
        best[m] = min(errs)
    return min(best, key=best.get), best
def main():
    P, prev, H = R.start(sys.argv[1]); t0 = R.now(); X_ = P["experiments"]; res = {}; chk = []; D = P["defaults"]
    if prev: res["carried_from_prev"] = {k: prev[k] for k in P.get("carry", []) if k in prev}
    if "phenomena" in X_:
        e = X_["phenomena"]; out = {}
        pr, V = run("RW", D["RW"], [(A, 1.0)]*200)
        chk.append(R.chk("V1", "RW single cue converges to lambda=1 (|V-1| < 1e-6 after 200 trials)", float(V[0]), abs(V[0]-1) < 1e-6))
        li_rw = li_index("RW", D["RW"], e["n_pre"], e["n_acq"])[0]
        chk.append(R.chk("V2", "RW shows no latent inhibition (LI index exactly 0: V stays 0 during non-reinforced pre-exposure)", li_rw, abs(li_rw) < 1e-12))
        for m in e["models"]:
            out[m] = dict(LI=li_index(m, D[m], e["n_pre"], e["n_acq"])[0], blocking=block_index(m, D[m], e["n1"], e["n2"]))
        res["phenomena"] = out
        chk.append(R.chk("V3", "RW blocking index >= 0.8 (textbook result)", out["RW"]["blocking"], out["RW"]["blocking"] >= 0.8))
        for m in [m for m in e["models"] if m != "RW"]:
            chk.append(R.chk(f"H_{m}", f"{m} at default parameters shows BOTH latent inhibition (index >= {e['li_min']}) and blocking (index >= {e['block_min']})",
                             out[m], out[m]["LI"] >= e["li_min"] and out[m]["blocking"] >= e["block_min"], kind="hypothesis"))
    if "sweep" in X_:
        e = X_["sweep"]; fr = {}
        for m, G in e["grids"].items():
            keys = list(G); rows = []
            for vals in itertools.product(*[G[k] for k in keys]):
                p = dict(zip(keys, vals)); li = li_index(m, p, e["n_pre"], e["n_acq"])[0]; bl = block_index(m, p, e["n1"], e["n2"])
                rows.append(dict(p=p, LI=li, blocking=bl, both=(li or 0) >= e["li_min"] and (bl or 0) >= e["block_min"]))
            fr[m] = dict(frac_both=float(np.mean([r["both"] for r in rows])), frac_LI=float(np.mean([(r["LI"] or 0) >= e["li_min"] for r in rows])),
                         frac_block=float(np.mean([(r["blocking"] or 0) >= e["block_min"] for r in rows])), n=len(rows))
        res["sweep"] = fr
        chk.append(R.chk("S1", "RW never shows LI over its grid (frac_LI == 0)", fr["RW"]["frac_LI"], fr["RW"]["frac_LI"] == 0))
        chk.append(R.chk("S2", "PH shows both phenomena in >= 50% of its grid", fr["PH"]["frac_both"], fr["PH"]["frac_both"] >= 0.5, kind="hypothesis"))
        chk.append(R.chk("S3", "KF shows both phenomena in >= 50% of its grid", fr["KF"]["frac_both"], fr["KF"]["frac_both"] >= 0.5, kind="hypothesis"))
    if "li_dose" in X_:
        e = X_["li_dose"]; from scipy.stats import spearmanr; out = {}
        for m in e["models"]:
            li = [li_index(m, D[m], n, e["n_acq"])[0] for n in e["n_pre"]]; out[m] = dict(n_pre=e["n_pre"], LI=li, spearman=float(spearmanr(e["n_pre"], li).correlation))
        res["li_dose"] = out
        for m in e["models"]:
            chk.append(R.chk(f"D_{m}", f"{m}: LI grows with the number of pre-exposures (Spearman >= 0.9)", out[m]["spearman"], out[m]["spearman"] >= 0.9, kind="hypothesis"))
    if "recovery" in X_:
        e = X_["recovery"]; rng = np.random.default_rng(e["seed"]); G = e["fit_grids"]; out = {}
        for design in e["designs"]:
            for noise in e["noise"]:
                conf = {m: {n: 0 for n in G} for m in G}
                for m in G:
                    keys = list(G[m])
                    for _ in range(e["reps"]):
                        p = {k: float(rng.choice(G[m][k])) for k in keys}; y = curve(m, p, design) + noise*rng.standard_normal(len(curve(m, p, design)))
                        conf[m][fit(y, design, G)[0]] += 1
                acc = float(np.mean([conf[m][m]/e["reps"] for m in G])); out[f"{design}|{noise}"] = dict(confusion=conf, accuracy=acc)
        res["recovery"] = out
        for noise in e["noise"]:
            a_diag = out[f"diagnostic|{noise}"]["accuracy"] if "diagnostic" in e["designs"] else None
            a_acq = out[f"acquisition|{noise}"]["accuracy"] if "acquisition" in e["designs"] else None
            if a_diag is not None and e.get("test_accuracy"):
                chk.append(R.chk(f"MR_{noise}", f"diagnostic design (acquisition + LI + blocking) recovers the generating model with mean accuracy >= {e['test_accuracy']} at noise {noise}", a_diag, a_diag >= e["test_accuracy"], kind="hypothesis"))
            if a_diag is not None and a_acq is not None and e.get("test_gain"):
                chk.append(R.chk(f"MG_{noise}", f"diagnostic design beats acquisition-only by >= {e['test_gain']} accuracy at noise {noise}", [a_diag, a_acq], a_diag-a_acq >= e["test_gain"], kind="hypothesis"))
        chk.append(R.chk("MR_r", "report confusion matrices", {k: v["accuracy"] for k, v in out.items()}, True, kind="reporting"))
    R.finish(H, P, res, chk, t0)
if __name__ == "__main__": main()
