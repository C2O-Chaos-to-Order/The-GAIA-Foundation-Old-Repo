"""SIM-R5-C4: a better criticality measure under subsampling (carried item 'R5 better criticality measure').
Model: Poisson autoregressive branching process (PAR) A_{t+1} ~ Poisson(m*A_t + h), as used by Wilting & Priesemann 2018 (Y01);
subsampling a_t ~ Binomial(A_t, alpha). Conventional estimator = slope r_1 of a_{t+1} on a_t. Multistep-regression (MR) estimator (Y01):
slopes r_k of a_{t+k} on a_t for k = 1..kmax, fit r_k = b*m^k (all r_k share the subsampling bias b). Avalanche analysis follows the
usual definition (runs of non-empty bins), which needs separation of time scales (Priesemann et al. 2014, Y02). Toy; nothing fitted to data."""
import sys, os, numpy as np
from scipy.optimize import curve_fit
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "tools")); import runner as R
def par(m, h, T, seed, A0=None, hfun=None):
    rng = np.random.default_rng(seed); A = np.empty(T, dtype=np.int64); a = int(A0 if A0 is not None else max(h / (1 - m), 0) if m < 1 else 1)
    for t in range(T):
        hh = h if hfun is None else hfun(t); a = rng.poisson(m * a + hh); A[t] = a
    return A
def sub(A, alpha, seed): return A if alpha >= 1 else np.random.default_rng(seed + 7919).binomial(A, alpha)
def slope(x, y):
    x = x - x.mean(); y = y - y.mean(); v = (x * x).sum(); return float((x * y).sum() / v) if v > 0 else 0.0
def conv(a): return slope(a[:-1].astype(float), a[1:].astype(float))
def mr(a, kmax=40):
    a = a.astype(float); ks = np.arange(1, kmax + 1); r = np.array([slope(a[:-k], a[k:]) for k in ks])
    try:
        (b, m), _ = curve_fit(lambda k, b, m: b * m ** k, ks, r, p0=(max(r[0], 1e-3), 0.9), bounds=([-np.inf, -1.5], [np.inf, 1.5]), maxfev=20000)
    except Exception: b, m = np.nan, np.nan
    return float(m), float(b), r
def aval(a):
    s = []; c = 0
    for x in a:
        if x > 0: c += int(x)
        elif c > 0: s.append(c); c = 0
    return np.array(s)
def tau_mle(s, smin=1):
    s = s[s >= smin].astype(float); return float(1 + len(s) / np.log(s / (smin - 0.5)).sum()) if len(s) > 10 else np.nan
def main():
    P, prev, H = R.start(sys.argv[1]); t0 = R.now(); X = P["experiments"]; C = []; res = {}
    k = P["iteration"]; T = X.get("T", 100000)
    if k == 1:
        A = par(0.9, 10.0, T, 1); mu = A.mean(); e = conv(A)
        res.update(mean=mu, mean_theory=100.0, conv_full=e)
        C += [R.chk("V1", "stationary mean within 2% of h/(1-m) = 100", mu, abs(mu - 100) / 100 < 0.02), R.chk("V2", "full sampling: conventional estimate within 0.01 of m = 0.9", e, abs(e - 0.9) < 0.01)]
    elif k in (2, 3):
        A = par(0.9, 10.0, T, 2); a = sub(A, 0.1, 2); c = conv(a); m, b, _ = mr(a)
        res.update(conv=c, mr=m, b=b)
        C += [R.chk("H2", "alpha 0.1, m 0.9: conventional estimate underestimates m by > 0.1 (Y01)", c, 0.9 - c > 0.1, "hypothesis")] if k == 2 else \
             [R.chk("H3", "alpha 0.1, m 0.9: MR estimate within 0.02 of m", m, abs(m - 0.9) < 0.02, "hypothesis")]
    elif k in (4, 11):
        grid = []; seed0 = 100 if k == 4 else 500
        for i, m0 in enumerate(X["m"]):
            for j, al in enumerate(X["alpha"]):
                A = par(m0, X["h"], T, seed0 + 10 * i + j); a = sub(A, al, seed0 + 10 * i + j); m, b, _ = mr(a); grid.append(dict(m=m0, alpha=al, mr=m, conv=conv(a), err=m - m0))
        ok = np.mean([abs(g["err"]) < 0.03 for g in grid]); res.update(grid=grid, share_ok=ok)
        C += [R.chk(f"H{k}", "MR |error| < 0.03 in >= 90% of (m, alpha) cells" + (" (replication, new seeds)" if k == 11 else ""), ok, ok >= 0.9, "hypothesis"),
              R.chk(f"H{k}r", "conventional estimate at alpha 0.01, mean over m", float(np.mean([g["conv"] for g in grid if g["alpha"] == 0.01])), True, "reporting")]
    elif k == 5:
        out = {}
        for TT in X["Ts"]:
            errs = [mr(sub(par(0.99, X["h"], TT, 300 + s), 0.01, 300 + s))[0] - 0.99 for s in range(X["seeds"])]; out[str(TT)] = dict(mean_abs_err=float(np.nanmean(np.abs(errs))), errs=errs)
        res.update(by_T=out); e = out[str(max(X["Ts"]))]["mean_abs_err"]
        C += [R.chk("H5", "m 0.99, alpha 0.01: mean |MR error| < 0.01 at the longest recording", e, e < 0.01, "hypothesis"), R.chk("H5r", "error by recording length", {t: v["mean_abs_err"] for t, v in out.items()}, True, "reporting")]
    elif k == 6:
        A = par(X["m"], X["h"], T, 6); tf = tau_mle(aval(A)); ts = tau_mle(aval(sub(A, X["alpha"], 6)))
        res.update(tau_full=tf, tau_sub=ts, n_aval_full=len(aval(A)), n_aval_sub=len(aval(sub(A, X["alpha"], 6))))
        C += [R.chk("H6", "avalanche-size exponent estimate changes by > 0.2 under subsampling (Y02: subsampling distorts avalanche statistics)", [tf, ts], abs(tf - ts) > 0.2, "hypothesis")]
    elif k == 7:
        out = []
        for h in X["h"]:
            A = par(X["m"], h, T, 7); z = float((A == 0).mean()); out.append(dict(h=h, zero_share=z, n_aval=len(aval(A)), mr=mr(sub(A, X["alpha"], 7))[0]))
        res.update(by_h=out)
        C += [R.chk("H7", "at the highest input the share of empty bins is < 1%, so avalanches are ill-defined, while MR still estimates m within 0.03", out[-1], out[-1]["zero_share"] < 0.01 and abs(out[-1]["mr"] - X["m"]) < 0.03, "hypothesis")]
    elif k == 8:
        est = {str(m0): [mr(sub(par(m0, X["h"], T, 800 + s), 0.01, 800 + s))[0] for s in range(X["seeds"])] for m0 in X["m"]}
        lo, hi = est[str(X["m"][0])], est[str(X["m"][1])]; res.update(est=est)
        C += [R.chk("H8", "alpha 0.01: MR separates m 0.98 from 0.999 (ranges across seeds do not overlap)", [max(lo), min(hi)], max(lo) < min(hi), "hypothesis")]
    elif k == 9:
        hf = lambda t: X["h"] * (1 + X["amp"] * np.sin(2 * np.pi * t / X["period"]))
        A = par(X["m"], X["h"], T, 9, hfun=hf); m, b, _ = mr(sub(A, X["alpha"], 9)); res.update(mr=m, conv=conv(sub(A, X["alpha"], 9)))
        C += [R.chk("H9", "slowly varying input (+-50%): MR bias < 0.03", m - X["m"], abs(m - X["m"]) < 0.03, "hypothesis")]
    elif k == 10:
        taus = {str(m0): -X["bin_ms"] / np.log(m0) for m0 in X["m"]}; res.update(tau_ms=taus)
        C += [R.chk("V3", "tau = -dt/ln m: m = 0.984 with 4 ms bins gives about 248 ms (inside Y01's 100-2000 ms range)", taus["0.984"], abs(taus["0.984"] - 248) < 2)]
    elif k == 12:
        A = sub(par(X["m"], X["h"], T, 12), X["alpha"], 12); sh = np.random.default_rng(12).permutation(A); rs = mr(sh)[2]; mo = mr(A)[0]
        res.update(max_abs_r_shuffled=float(np.max(np.abs(rs))), mr_original=mo)
        C += [R.chk("H12", "negative control: after shuffling time bins all lagged slopes vanish (max |r_k| < 0.05) while the original gives m within 0.03", [float(np.max(np.abs(rs))), mo], np.max(np.abs(rs)) < 0.05 and abs(mo - X["m"]) < 0.03, "hypothesis")]
    R.finish(H, P, res, C, t0)
if __name__ == "__main__": main()
