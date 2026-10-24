"""SIM-SOUL: Soul topic simulations (track cycles A-C). Usage: python sim_soul.py iter-<k>  (from Soul/simulation/)."""
import os, sys, itertools, numpy as np
from scipy import stats, optimize
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
import track_runner as R
chk = R.chk

def continuity_vignette(P, rng):
    """Latent-threshold model of 'does she still ...?' continuity judgments (3 physical, 3 mental items) after a vignette death.
    Person propensity z ~ N(0,1); item j answered 'continues' if z + e_j > threshold_j (e ~ N(0, s)); thresholds set so marginals = p."""
    N, s = P["N"], P["item_noise"]; sd = np.sqrt(1 + s ** 2)
    th = [stats.norm.ppf(1 - p) * sd for p in [P["p_phys"]] * 3 + [P["p_ment"]] * 3]
    z = rng.normal(0, 1, N)[:, None]; Y = (z + rng.normal(0, s, (N, 6)) > np.array(th)).astype(int)
    phys, ment = Y[:, :3].sum(1), Y[:, 3:].sum(1); d = ment - phys
    tt = stats.ttest_1samp(d, 0); all_cease = float(np.mean(Y.sum(1) == 0)); dual = float(np.mean((ment > 0) & (phys == 0)))
    pats = {"all cease": all_cease, "mental only (dualist pattern)": dual, "physical and mental continue": float(np.mean((ment > 0) & (phys > 0))),
            "physical only": float(np.mean((ment == 0) & (phys > 0)))}
    pw = 0
    for _ in range(P["reps_small"]):
        zz = rng.normal(0, 1, P["n_small"])[:, None]; YY = (zz + rng.normal(0, s, (P["n_small"], 6)) > np.array(th)).astype(int)
        pw += stats.ttest_1samp(YY[:, 3:].sum(1) - YY[:, :3].sum(1), 0).pvalue < 0.05
    res = dict(marginals=Y.mean(0), mean_diff_items=float(d.mean()), t=float(tt.statistic), p=float(tt.pvalue), patterns=pats,
               power_small_n=pw / P["reps_small"])
    c = [chk("V1", "simulated item marginals within 0.01 of targets", res["marginals"], all(abs(m - p) <= 0.01 for m, p in zip(Y.mean(0), [P["p_phys"]] * 3 + [P["p_ment"]] * 3))),
         chk("H1", f"mental > physical continuity is significant (p < .001) at N = {N}", float(tt.pvalue), tt.pvalue < 0.001 and d.mean() > 0, "hypothesis"),
         chk("H2", "the modal response pattern is 'all states cease' (share > 0.5)", all_cease, all_cease > 0.5, "hypothesis"),
         chk("H3", "fewer than 25% show the 'dualist' pattern (some mental continuity, no physical continuity)", dual, dual < 0.25, "hypothesis"),
         chk("R1", f"power to detect the mental-physical difference at n = {P['n_small']}", pw / P["reps_small"], True, "reporting")]
    return res, c

def marginals_bounds(P, rng):
    """What do agreement marginals on five non-exclusive mind-brain positions (K03) force about co-endorsement? LP over 2^5 patterns."""
    names = list(P["marginals"]); m = np.array([P["marginals"][k] for k in names])
    pats = np.array(list(itertools.product([0, 1], repeat=5))); A_eq = np.vstack([pats.T, np.ones(32)]); b_eq = np.append(m, 1)
    def lp(cvec, sense=1):
        r = optimize.linprog(sense * cvec, A_eq=A_eq, b_eq=b_eq, bounds=[(0, 1)] * 32, method="highs"); return sense * r.fun
    i, j = names.index(P["pair"][0]), names.index(P["pair"][1])
    both = (pats[:, i] & pats[:, j]).astype(float)
    pair_min, pair_max = lp(both), lp(both, -1)
    ge2 = (pats.sum(1) >= 2).astype(float); ge2_min = lp(ge2); none_max = lp((pats.sum(1) == 0).astype(float), -1)
    indep = float(m[i] * m[j])
    res = dict(sum_of_marginals=float(m.sum()), pair=P["pair"], pair_min=pair_min, pair_max=pair_max, pair_if_independent=indep,
               share_endorsing_2plus_min=ge2_min, share_endorsing_none_max=none_max)
    fre = (max(0, m[i] + m[j] - 1), min(m[i], m[j]))
    c = [chk("V1", "LP bounds for the pair equal the analytic Frechet bounds within 1e-6", [pair_min, pair_max, fre], abs(pair_min - fre[0]) < 1e-6 and abs(pair_max - fre[1]) < 1e-6),
         chk("H1", f"the published marginals alone force at least 10% of respondents to agree with both {P['pair'][0]} and {P['pair'][1]}", pair_min, pair_min >= 0.10, "hypothesis"),
         chk("H2", "the marginals force at least 25% of respondents to agree with two or more of the five positions", ge2_min, ge2_min >= 0.25, "hypothesis"),
         chk("R1", "co-endorsement share if the two agreements were independent", indep, True, "reporting")]
    return res, c

def kappa_prevalence(P, rng):
    """Cohen's kappa paradox for a reported (percent agreement, kappa) pair: implied chance agreement, prevalence and coder error."""
    po, k = P["p_o"], P["kappa"]; pe = (po - k) / (1 - k)
    pi = optimize.brentq(lambda x: x ** 2 + (1 - x) ** 2 - pe, 1e-6, 0.5)
    def stats_for(pi, e):
        a = pi * (1 - e) + (1 - pi) * e  # each coder's marginal 'present' rate
        po_ = pi * ((1 - e) ** 2 + e ** 2) + (1 - pi) * ((1 - e) ** 2 + e ** 2)
        pe_ = a ** 2 + (1 - a) ** 2; return po_, (po_ - pe_) / (1 - pe_)
    e = optimize.brentq(lambda x: stats_for(pi, x)[1] - k, 1e-6, 0.3)
    n = P["n_units"]; ks = []
    for _ in range(P["reps"]):
        t = rng.random(n) < pi; c1 = t ^ (rng.random(n) < e); c2 = t ^ (rng.random(n) < e)
        po_ = np.mean(c1 == c2); a1, a2 = c1.mean(), c2.mean(); pe_ = a1 * a2 + (1 - a1) * (1 - a2); ks.append((po_ - pe_) / (1 - pe_))
    grid = {str(p): round(stats_for(p, e)[1], 4) for p in P["pi_grid"]}
    res = dict(implied_chance_agreement=pe, implied_prevalence=pi, implied_coder_error=e, po_at_fit=stats_for(pi, e)[0],
               simulated_kappa_mean=float(np.mean(ks)), kappa_by_prevalence_same_coders=grid)
    c = [chk("V1", "implied chance agreement (p_o - kappa)/(1 - kappa) computed", pe, abs(pe - (po - k) / (1 - k)) < 1e-12),
         chk("V2", "simulated kappa at the fitted prevalence and coder error within 0.02 of the reported kappa", float(np.mean(ks)), abs(np.mean(ks) - k) <= 0.02),
         chk("H1", "with the SAME coder error, kappa at prevalence 0.5 exceeds 0.90 (kappa depends on prevalence)", grid["0.5"], grid["0.5"] > 0.90, "hypothesis"),
         chk("R1", "percent agreement implied by the two-coder symmetric-error model at the fit (reported 0.96)", stats_for(pi, e)[0], True, "reporting")]
    return res, c

KINDS = dict(continuity_vignette=continuity_vignette, marginals_bounds=marginals_bounds, kappa_prevalence=kappa_prevalence)
if __name__ == "__main__":
    P, H, t0 = R.start(sys.argv[1]); rng = np.random.default_rng(P["seed"])
    res, checks = KINDS[P["kind"]](P, rng); R.finish(H, P, res, checks, t0)
