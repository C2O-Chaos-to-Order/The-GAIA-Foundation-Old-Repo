"""SIM-CONS: Consciousness topic simulations (track cycles A-C). Usage: python sim_cons.py iter-<k>  (from Consciousness/simulation/)."""
import os, sys, itertools, numpy as np
from scipy import stats, optimize
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
import track_runner as R
chk = R.chk

def report_confound(P, rng):
    """Toy threshold model (NOT K13's active-inference model): sensory evidence S; access A = S > theta; 'PFC' activity =
    g*A (working-memory gating) + r*A*report (report demand) + noise. Contrast visible minus invisible in report vs no-report."""
    N = P["trials"]; out = {}
    for cond, rep in (("report", 1), ("no_report", 0)):
        S = rng.normal(P["stim"], 1, N); A = S > P["theta"]
        pfc = P["g"] * A + P["r"] * A * rep + rng.normal(0, P["noise"], N)
        out[cond] = dict(contrast=float(pfc[A].mean() - pfc[~A].mean()), share_visible=float(A.mean()),
                         visible_trials_above_tau=float(np.mean(pfc[A] > P["tau"])), invisible_trials_above_tau=float(np.mean(pfc[~A] > P["tau"])))
    S = rng.normal(P["stim"], 1, N); A = S > P["theta"]; pfc0 = 0 * A + rng.normal(0, P["noise"], N)
    red = 1 - out["no_report"]["contrast"] / out["report"]["contrast"]
    res = dict(conditions=out, reduction_of_contrast=red, contrast_g0=float(pfc0[A].mean() - pfc0[~A].mean()))
    c = [chk("V1", "g = 0 and no report: PFC contrast within 0.05 of 0", res["contrast_g0"], abs(res["contrast_g0"]) <= 0.05),
         chk("H1", "removing report reduces the visible-invisible PFC contrast by >= 50%", red, red >= 0.5, "hypothesis"),
         chk("H2", "without report, >= 80% of visible trials still exceed the reportability threshold tau", out["no_report"]["visible_trials_above_tau"], out["no_report"]["visible_trials_above_tau"] >= 0.8, "hypothesis")]
    return res, c

def _parallel(X, rng, n_null, q):
    n, p = X.shape; ev = np.sort(np.linalg.eigvalsh(np.corrcoef(X, rowvar=False)))[::-1]
    nulls = np.array([np.sort(np.linalg.eigvalsh(np.corrcoef(rng.normal(size=(n, p)), rowvar=False)))[::-1] for _ in range(n_null)])
    thr = np.quantile(nulls, q, axis=0); k = 0
    while k < p and ev[k] > thr[k]: k += 1
    return ev, k

def kaiser_null(P, rng):
    """No factor structure: p items, n respondents. How many factors do Kaiser (eigenvalue > 1) and parallel analysis retain?"""
    ks, pa = [], []
    for _ in range(P["reps"]):
        X = rng.normal(size=(P["n"], P["p"])); ev, k = _parallel(X, rng, P["n_null"], P["q"]); ks.append(int((ev > 1).sum())); pa.append(k)
    mp = (1 + np.sqrt(P["p"] / P["n"])) ** 2
    res = dict(kaiser_counts=ks, parallel_counts=pa, marchenko_pastur_upper_edge=float(mp))
    c = [chk("V1", "parallel analysis retains 0 factors under no structure in >= 90% of replications", float(np.mean(np.array(pa) == 0)), np.mean(np.array(pa) == 0) >= 0.9),
         chk("H1", "the Kaiser rule retains >= 10 spurious factors under no structure (mean)", float(np.mean(ks)), np.mean(ks) >= 10, "hypothesis"),
         chk("R1", "upper edge of the null eigenvalue spectrum (Marchenko-Pastur)", float(mp), True, "reporting")]
    return res, c

def factor_recovery(P, rng):
    """k true factors, p items (simple structure, items assigned round-robin), loading lambda, n respondents."""
    out = {}
    for lam in P["lambda_grid"]:
        pa, ve = [], []
        for _ in range(P["reps"]):
            L = np.zeros((P["p"], P["k"])); L[np.arange(P["p"]), np.arange(P["p"]) % P["k"]] = lam
            F = rng.normal(size=(P["n"], P["k"])); X = F @ L.T + rng.normal(size=(P["n"], P["p"])) * np.sqrt(1 - lam ** 2)
            ev, k = _parallel(X, rng, P["n_null"], P["q"]); pa.append(k); ve.append(float(ev[:P["k"]].sum() / P["p"]))
        out[str(lam)] = dict(parallel_counts=pa, share_exact=float(np.mean(np.array(pa) == P["k"])), var_explained_first_k=float(np.mean(ve)))
    lt = str(P["lambda_test"])
    res = dict(by_lambda=out)
    c = [chk("V1", f"lambda = {P['lambda_grid'][-1]} (strong): parallel analysis recovers exactly k in >= 90% of replications", out[str(P["lambda_grid"][-1])]["share_exact"], out[str(P["lambda_grid"][-1])]["share_exact"] >= 0.9),
         chk("H1", f"at lambda = {lt} parallel analysis recovers exactly k = {P['k']} in >= 90% of replications", out[lt]["share_exact"], out[lt]["share_exact"] >= 0.9, "hypothesis"),
         chk("H2", f"at lambda = {lt} the first k components explain 0.44 +- 0.05 of item variance (K14 reports 44%)", out[lt]["var_explained_first_k"], abs(out[lt]["var_explained_first_k"] - 0.44) <= 0.05, "hypothesis"),
         chk("R1", "variance explained by first k components, by lambda", {k: round(v["var_explained_first_k"], 3) for k, v in out.items()}, True, "reporting")]
    return res, c

KINDS = dict(report_confound=report_confound, kaiser_null=kaiser_null, factor_recovery=factor_recovery)
if __name__ == "__main__":
    P, H, t0 = R.start(sys.argv[1]); rng = np.random.default_rng(P["seed"])
    res, checks = KINDS[P["kind"]](P, rng); R.finish(H, P, res, checks, t0)
