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

# ---- Track Cycle B kinds ----
def cmd_bayes(P, rng):
    """Covert consciousness (K26, K30): prevalence of CMD among UWS-diagnosed patients and an imperfect test. P(conscious | negative test)."""
    pr, sp = P["prevalence"], P["specificity"]; out = {}
    for se in P["sens_grid"]:
        neg = pr * (1 - se) + (1 - pr) * sp; pos = 1 - neg; out[str(se)] = dict(p_conscious_given_negative=float(pr * (1 - se) / neg), ppv=float(pr * se / pos))
    s = P["sens_test"]; c_ = rng.random(P["N"]) < pr; t = np.where(c_, rng.random(P["N"]) < s, rng.random(P["N"]) > sp); simv = float(c_[~t].mean())
    c = [chk("V1", "simulated P(conscious | negative) within 0.01 of analytic", [simv, out[str(s)]["p_conscious_given_negative"]], abs(simv - out[str(s)]["p_conscious_given_negative"]) <= 0.01),
         chk("H1", f"sensitivity {s}: P(conscious | negative test) >= 0.10", out[str(s)]["p_conscious_given_negative"], out[str(s)]["p_conscious_given_negative"] >= 0.10, "hypothesis"),
         chk("R1", "P(conscious | negative) and PPV by sensitivity", out, True, "reporting")]
    return dict(by_sensitivity=out, simulated=simv), c

def or_to_rates(P, rng):
    """Translate K26's odds ratios into detection rates and risk ratios at illustrative baseline (TBI) rates."""
    out = {}
    for p0 in P["baseline_grid"]:
        o0 = p0 / (1 - p0); row = {}
        for name, OR in P["odds_ratios"].items():
            p1 = OR * o0 / (1 + OR * o0); row[name] = dict(rate=float(p1), risk_ratio=float(p1 / p0), back_or=float((p1 / (1 - p1)) / o0))
        out[str(p0)] = row
    bt = str(P["baseline_test"]); an = out[bt]["anoxic"]
    c = [chk("V1", "back-converted odds ratios equal the inputs within 1e-9", True, all(abs(v["back_or"] - P["odds_ratios"][k]) < 1e-9 for r in out.values() for k, v in r.items())),
         chk("H1", f"at baseline {bt}, the anoxic risk ratio differs from the odds ratio by > 0.05 (reading an OR as a RR misstates the gap)", [an["risk_ratio"], P["odds_ratios"]["anoxic"]], abs(an["risk_ratio"] - P["odds_ratios"]["anoxic"]) > 0.05, "hypothesis"),
         chk("R1", "rates and risk ratios by baseline", out, True, "reporting")]
    return dict(by_baseline=out), c

def decoding_nonconscious(P, rng):
    """Stimulus category is encoded in 'posterior' channels on ALL trials; awareness is independent of that code. Decoder trained on seen trials, tested on unseen."""
    out = {}
    for sig in P["signal_grid"]:
        accs = []
        for _ in range(P["reps"]):
            N, V = P["trials"], P["channels"]; cat = rng.integers(0, 2, N); w = rng.normal(0, 1, V)
            X = np.outer(2 * cat - 1, w) * sig + rng.normal(0, 1, (N, V)); seen = rng.random(N) < P["p_seen"]
            m1 = X[seen & (cat == 1)].mean(0); m0 = X[seen & (cat == 0)].mean(0); pred = ((X - (m1 + m0) / 2) @ (m1 - m0)) > 0
            accs.append(np.mean(pred[~seen] == (cat[~seen] == 1)))
        out[str(sig)] = float(np.mean(accs))
    st = str(P["signal_test"])
    c = [chk("V1", "signal 0: unseen-trial decoding accuracy within 0.02 of 0.5", out["0.0"], abs(out["0.0"] - 0.5) <= 0.02),
         chk("H1", f"signal {st}: unseen-trial decoding accuracy >= 0.6 although nothing in the model is conscious on those trials", out[st], out[st] >= 0.6, "hypothesis"),
         chk("R1", "accuracy by signal", out, True, "reporting")]
    return dict(unseen_accuracy_by_signal=out), c

def _ols_p(X, y):
    X = np.column_stack([np.ones(len(y)), X]); b, *_ = np.linalg.lstsq(X, y, rcond=None); r = y - X @ b; df = len(y) - X.shape[1]
    s2 = r @ r / df; se = np.sqrt(np.diag(s2 * np.linalg.inv(X.T @ X))); return 2 * stats.t.sf(np.abs(b / se), df)

def compassion_mediation(P, rng):
    """Serial mediation X -> M1 -> M2 -> Y with no direct effect (K28 design size n = 80). Power of the total effect vs joint significance of the indirect path."""
    def run(a1):
        tot = ind = 0
        for _ in range(P["reps"]):
            n = P["n"]; X = np.repeat([0, 1], n // 2).astype(float); M1 = a1 * X + rng.normal(0, 1, n); M2 = P["d"] * M1 + rng.normal(0, 1, n); Y = P["b"] * M2 + P["c_direct"] * X + rng.normal(0, 1, n)
            tot += _ols_p(X, Y)[1] < 0.05
            pa = _ols_p(X, M1)[1]; pd = _ols_p(np.column_stack([M1, X]), M2)[1]; pb = _ols_p(np.column_stack([M2, M1, X]), Y)[1]
            ind += (pa < 0.05) and (pd < 0.05) and (pb < 0.05)
        return tot / P["reps"], ind / P["reps"]
    t0, i0 = run(0.0); t1, i1 = run(P["a1"])
    res = dict(null=dict(total_power=t0, indirect_joint_sig=i0), effect=dict(total_power=t1, indirect_joint_sig=i1))
    c = [chk("V1", "a1 = 0: indirect joint-significance rate <= 0.05", i0, i0 <= 0.05),
         chk("H1", "the total effect is detected in < 50% of n = 80 studies", t1, t1 < 0.5, "hypothesis"),
         chk("H2", "the serial indirect path is jointly significant in > 50% of the same studies", i1, i1 > 0.5, "hypothesis")]
    return res, c

def kaiser_likert(P, rng):
    """Cycle A iteration 2 with 5-point ordinal (skewed) items instead of normal items: no factor structure."""
    th = np.array(P["thresholds"]); ks, pa = [], []
    for _ in range(P["reps"]):
        Z = rng.normal(size=(P["n"], P["p"])); X = (Z[..., None] > th).sum(-1).astype(float); ev, k = _parallel(X, rng, P["n_null"], P["q"]); ks.append(int((ev > 1).sum())); pa.append(k)
    res = dict(kaiser_counts=ks, parallel_counts=pa)
    c = [chk("V1", "parallel analysis retains 0 factors in >= 90% of replications", float(np.mean(np.array(pa) == 0)), np.mean(np.array(pa) == 0) >= 0.9),
         chk("H1", "Kaiser rule retains >= 10 spurious factors (mean) with ordinal items", float(np.mean(ks)), np.mean(ks) >= 10, "hypothesis")]
    return res, c

KINDS = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_') and k not in ('chk','power_t1','pow2') and getattr(v,'__module__',None)=='__main__'}

if __name__ == "__main__":
    P, H, t0 = R.start(sys.argv[1]); rng = np.random.default_rng(P["seed"])
    res, checks = KINDS[P["kind"]](P, rng); R.finish(H, P, res, checks, t0)
