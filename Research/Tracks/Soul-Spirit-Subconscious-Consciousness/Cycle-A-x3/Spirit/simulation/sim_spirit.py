"""SIM-SPIRIT: Spirit topic simulations (track cycles A-C). Usage: python sim_spirit.py iter-<k>  (from Spirit/simulation/)."""
import os, sys, itertools, numpy as np
from scipy import stats, optimize
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
import track_runner as R
chk = R.chk

def pow2(n, d, a=0.05):
    df = 2 * n - 2; nc = d * np.sqrt(n / 2); tc = stats.t.ppf(1 - a / 2, df)
    return float(1 - stats.nct.cdf(tc, df, nc) + stats.nct.cdf(-tc, df, nc))

def replication_runs(P, rng):
    """Original two-group studies (n0 per group) published only if p < .05 in the predicted direction; direct replications at mult*n0."""
    n0, nr, out = P["n0"], int(round(P["mult"] * P["n0"])), {}
    for d in P["d_grid"]:
        x = rng.normal(d, 1, (P["reps"], n0)); y = rng.normal(0, 1, (P["reps"], n0))
        t, p = stats.ttest_ind(x, y, axis=1); dhat = (x.mean(1) - y.mean(1)) / np.sqrt((x.var(1, ddof=1) + y.var(1, ddof=1)) / 2)
        pub = (p < 0.05) & (t > 0); pw = pow2(nr, d)
        out[str(d)] = dict(share_published=float(pub.mean()), mean_published_d=float(dhat[pub].mean()) if pub.any() else None,
                           mean_unselected_d=float(dhat.mean()), replication_power=pw, p_all_k_fail=(1 - pw) ** P["k_reps"])
    res = dict(n0=n0, n_rep=nr, by_true_d=out)
    c = [chk("V1", "unselected mean d within 0.02 of true d = 0.5", out["0.5"]["mean_unselected_d"], abs(out["0.5"]["mean_unselected_d"] - 0.5) <= 0.02),
         chk("H1", f"if the true effect is d = 0.2, all {P['k_reps']} direct replications at {P['mult']}x n failing has probability < 0.10 (i.e. a run of failures is strong evidence against a small true effect)",
             out["0.2"]["p_all_k_fail"], out["0.2"]["p_all_k_fail"] < 0.10, "hypothesis"),
         chk("H2", "if the true effect is 0, published originals still average d > 0.4", out["0.0"]["mean_published_d"], out["0.0"]["mean_published_d"] > 0.4, "hypothesis"),
         chk("R1", "replication power by true d", {k: round(v["replication_power"], 3) for k, v in out.items()}, True, "reporting")]
    return res, c

def threshold_classification(P, rng):
    """Binary 'all k subscales above a cut' classification from subscales with reliability omega; test-retest agreement of the binary."""
    out = {}
    for om in P["omega_grid"]:
        T = rng.multivariate_normal(np.zeros(P["k"]), np.full((P["k"], P["k"]), P["r_between"]) + np.eye(P["k"]) * (1 - P["r_between"]), P["N"])
        e = np.sqrt((1 - om) / om)
        X1 = T + rng.normal(0, e, T.shape); X2 = T + rng.normal(0, e, T.shape)
        cut = np.quantile(X1, P["cut_quantile"], axis=0)
        c1 = (X1 > cut).all(1); c2 = (X2 > cut).all(1); tr = (T > np.quantile(T, P["cut_quantile"], axis=0)).all(1)
        po = np.mean(c1 == c2); pe = c1.mean() * c2.mean() + (1 - c1.mean()) * (1 - c2.mean())
        out[str(om)] = dict(share_classified=float(c1.mean()), test_retest_agreement=float(po), kappa=float((po - pe) / (1 - pe)),
                            share_of_classified_also_on_retest=float((c1 & c2).sum() / c1.sum()), agreement_with_true=float(np.mean(c1 == tr)))
    o = str(P["omega_test"])
    res = dict(by_omega=out)
    c = [chk("V1", "with omega = 1 (no error) test-retest agreement is 1", out["1.0"]["test_retest_agreement"], out["1.0"]["test_retest_agreement"] == 1.0),
         chk("H1", f"at omega = {o} at least 80% of those classified at test are classified again at retest", out[o]["share_of_classified_also_on_retest"], out[o]["share_of_classified_also_on_retest"] >= 0.8, "hypothesis"),
         chk("R1", "test-retest kappa of the binary classification by omega", {k: round(v["kappa"], 3) for k, v in out.items()}, True, "reporting")]
    return res, c

def multiple_outcomes(P, rng):
    """Probability that at least one of k correlated outcomes is significant (two-group, n per group) when no effect exists."""
    out = {}
    for r in P["r_grid"]:
        S = np.full((P["k"], P["k"]), r) + np.eye(P["k"]) * (1 - r); hits = 0
        for _ in range(P["reps"]):
            x = rng.multivariate_normal(np.zeros(P["k"]), S, P["n"]); y = rng.multivariate_normal(np.zeros(P["k"]), S, P["n"])
            hits += (stats.ttest_ind(x, y).pvalue < 0.05).any()
        out[str(r)] = hits / P["reps"]
    a = 1 - 0.95 ** P["k"]
    c = [chk("V1", f"r = 0: family-wise rate within 0.015 of 1 - 0.95^{P['k']} = {a:.4f}", out["0.0"], abs(out["0.0"] - a) <= 0.015),
         chk("H1", f"at r = {P['r_test']} the family-wise false-positive rate still exceeds 0.15", out[str(P["r_test"])], out[str(P["r_test"])] > 0.15, "hypothesis"),
         chk("R1", "family-wise rate by correlation", out, True, "reporting")]
    return dict(familywise_rate_by_r=out), c

KINDS = dict(replication_runs=replication_runs, threshold_classification=threshold_classification, multiple_outcomes=multiple_outcomes)
if __name__ == "__main__":
    P, H, t0 = R.start(sys.argv[1]); rng = np.random.default_rng(P["seed"])
    res, checks = KINDS[P["kind"]](P, rng); R.finish(H, P, res, checks, t0)
