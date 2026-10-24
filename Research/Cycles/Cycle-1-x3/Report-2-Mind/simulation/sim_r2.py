"""SIM-R2 (Cycle 1+): associative-learning and forgetting-curve models. Data: Ebbinghaus/Dros retention values from S04 Table 3."""
import sys, os, json, numpy as np
from scipy.optimize import curve_fit
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools")); import runner as R
def rw_block(alpha, beta, lam, n_pre, n_comp, pre="A"):
    V = {"A": 0.0, "B": 0.0, "X": 0.0}
    for _ in range(n_pre): V[pre] += alpha*beta*(lam-V[pre])
    for _ in range(n_comp):
        e = lam-(V["A"]+V["X"])
        for c in ("A", "X"): V[c] += alpha*beta*e
    return V
def acquisition(model, n_pre, n_acq, p):
    """Latent-inhibition test: n_pre non-reinforced exposures to X (lambda=0), then n_acq X->US trials (lambda=p['lam']). Returns V_X.
    RW: dV = alpha*beta*(lambda-V).  PH (Pearce-Hall-type): dV = S*a*(lambda-V); a <- gamma*|lambda-V| + (1-gamma)*a."""
    V = 0.0; a = p["alpha0"]
    for lam, n in ((0.0, n_pre), (p["lam"], n_acq)):
        for _ in range(n):
            e = lam-V
            if model == "RW": V += p["alpha0"]*p["beta"]*e
            else: V += p["S"]*a*e; a = p["gamma"]*abs(e)+(1-p["gamma"])*a
    return V
MODELS = {"exponential": (lambda t, a, k: a*np.exp(-k*t), [0.5, 0.01]), "power": (lambda t, a, c: a*t**(-c), [0.4, 0.1]),
          "log": (lambda t, a, c: a-c*np.log(t), [0.45, 0.03])}
def fit(m, t, y):
    fn, p0 = MODELS[m]; p, _ = curve_fit(fn, t, y, p0=p0, maxfev=20000); return p, fn
def aic(m, t, y):
    p, fn = fit(m, t, y); sse = float(((fn(t, *p)-y)**2).sum()); n = len(y); return n*np.log(sse/n)+4
def loocv(m, t, y):
    errs = []
    for i in range(len(t)):
        msk = np.arange(len(t)) != i; p, fn = fit(m, t[msk], y[msk]); errs.append(float((fn(t[i], *p)-y[i])**2))
    return float(np.mean(errs))
def main():
    P, prev, H = R.start(sys.argv[1]); t0 = R.now(); X = P["experiments"]; res = {}; chk = []
    D = P["data"]; t = np.array(D["hours"])
    if "rw_grid" in X:
        g = X["rw_grid"]; cells = []
        for a in g["alpha"]:
            for n_pre in g["n_pre"]:
                vb = rw_block(a, 1.0, 1.0, n_pre, g["n_comp"]); vc = rw_block(a, 1.0, 1.0, n_pre, g["n_comp"], pre="B")
                cells.append(dict(alpha=a, n_pre=n_pre, VX_block=vb["X"], VX_control=vc["X"], ratio=vb["X"]/vc["X"]))
        res["rw_grid"] = dict(cells=cells, frac_blocking_ratio_lt_0_1=float(np.mean([c["ratio"] < 0.1 for c in cells])),
                              failing=[(c["alpha"], c["n_pre"], round(c["ratio"], 3)) for c in cells if c["ratio"] >= 0.1])
        mono = True
        for a_ in g["alpha"]:
            rs = [c["ratio"] for c in sorted([c for c in cells if c["alpha"] == a_], key=lambda c: c["n_pre"])]
            mono = mono and all(x >= y-1e-12 for x, y in zip(rs, rs[1:]))
        chk.append(R.chk("W1", "blocking ratio is monotone non-increasing in n_pre at every alpha", None, mono))
        chk.append(R.chk("W2", "blocking (ratio<0.1) is not universal: it fails for weak pretraining (low alpha x n_pre) - report the boundary", res["rw_grid"]["failing"][:10], len(res["rw_grid"]["failing"]) > 0, kind="hypothesis"))
    if "latent_inhibition" in X:
        L = X["latent_inhibition"]; out = {}
        for m in ("RW", "PH"):
            out[m] = dict(no_pre=acquisition(m, 0, L["n_acq"], L), pre=acquisition(m, L["n_pre"], L["n_acq"], L))
            out[m]["LI_ratio"] = out[m]["pre"]/out[m]["no_pre"]
        res["latent_inhibition"] = out
        chk.append(R.chk("L1", "Rescorla-Wagner predicts NO latent inhibition (ratio = 1 exactly: preexposure with lambda=0 leaves V=0)", out["RW"]["LI_ratio"], abs(out["RW"]["LI_ratio"]-1) < 1e-12))
        chk.append(R.chk("L2", "Pearce-Hall-type associability decay produces latent inhibition (ratio < 0.9)", out["PH"]["LI_ratio"], out["PH"]["LI_ratio"] < 0.9, kind="hypothesis"))
    if "forgetting_cv" in X:
        F = X["forgetting_cv"]; out = {}
        for ds in F["datasets"]:
            y = np.array(D[ds]); out[ds] = {m: dict(AIC=aic(m, t, y), LOOCV_MSE=loocv(m, t, y)) for m in MODELS}
            out[ds]["best_AIC"] = min(MODELS, key=lambda m: out[ds][m]["AIC"]); out[ds]["best_LOOCV"] = min(MODELS, key=lambda m: out[ds][m]["LOOCV_MSE"])
            rng = np.random.default_rng(F["seed"]); wins = {m: 0 for m in MODELS}
            for _ in range(F["boot"]):
                idx = np.sort(rng.choice(len(t), len(t), replace=True))
                if len(set(idx)) < 4: continue
                try: wins[min(MODELS, key=lambda m: aic(m, t[idx], y[idx]))] += 1
                except Exception: pass
            out[ds]["bootstrap_AIC_wins"] = wins
        res["forgetting_cv"] = out
        e = out.get("ebbinghaus")
        if e: chk.append(R.chk("F1", "Ebbinghaus: exponential is not the best model by AIC or by LOOCV", [e["best_AIC"], e["best_LOOCV"]], e["best_AIC"] != "exponential" and e["best_LOOCV"] != "exponential", kind="hypothesis"))
        if prev and "forgetting_cv" in prev:
            chk.append(R.chk("F2", "best-model choice agrees with previous iteration", None, all(prev["forgetting_cv"][d]["best_AIC"] == out[d]["best_AIC"] for d in out if d in prev["forgetting_cv"]), kind="hypothesis"))
        agree = {d: out[d]["best_AIC"] == out[d]["best_LOOCV"] for d in out}
        chk.append(R.chk("F3", "report whether AIC and LOOCV agree per dataset (reporting check)", agree, True, kind="reporting"))
    R.finish(H, P, res, chk, t0)
if __name__ == "__main__": main()
