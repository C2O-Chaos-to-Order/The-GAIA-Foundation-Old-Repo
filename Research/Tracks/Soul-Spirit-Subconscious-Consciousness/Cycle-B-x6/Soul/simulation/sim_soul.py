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

# ---- Track Cycle B kinds ----
def _dl(y, v):
    """DerSimonian-Laird random-effects estimate; returns (mu, se, tau2)."""
    w = 1 / v; mu_f = np.sum(w * y) / w.sum(); Q = np.sum(w * (y - mu_f) ** 2); k = len(y)
    C = w.sum() - np.sum(w ** 2) / w.sum(); tau2 = max(0.0, (Q - (k - 1)) / C) if C > 0 else 0.0
    ws = 1 / (v + tau2); mu = np.sum(ws * y) / ws.sum(); return float(mu), float(np.sqrt(1 / ws.sum())), float(tau2)

def selection_meta(P, rng):
    """Literature simulation: true effects g_i ~ N(g_true, tau); two-group studies with n per group ~ U[n_lo, n_hi];
    significant positive results always published, others with probability p_pub_ns; naive DL estimate of the published set."""
    def lit(p_ns):
        ys, vs = [], []
        while len(ys) < P["k_published"]:
            n = int(rng.integers(P["n_lo"], P["n_hi"] + 1)); gi = rng.normal(P["g_true"], P["tau"])
            x = rng.normal(gi, 1, n); y = rng.normal(0, 1, n); sp = np.sqrt((x.var(ddof=1) + y.var(ddof=1)) / 2)
            d = (x.mean() - y.mean()) / sp; v = 2 / n + d ** 2 / (4 * n); z = d / np.sqrt(v)
            if (z > 1.96) or rng.random() < p_ns: ys.append(d); vs.append(v)
        return _dl(np.array(ys), np.array(vs))
    sel = [lit(P["p_pub_ns"])[0] for _ in range(P["reps"])]; nosel = [lit(1.0)[0] for _ in range(P["reps"])]
    res = dict(naive_estimate_with_selection=float(np.mean(sel)), sd_with_selection=float(np.std(sel)), naive_estimate_no_selection=float(np.mean(nosel)))
    c = [chk("V1", f"without selection the naive estimate is within 0.03 of the true mean {P['g_true']}", res["naive_estimate_no_selection"], abs(res["naive_estimate_no_selection"] - P["g_true"]) <= 0.03),
         chk("H1", f"with selection (non-significant results published with probability {P['p_pub_ns']}) a true mean of {P['g_true']} yields a naive pooled estimate >= {P['h1_threshold']}", res["naive_estimate_with_selection"], res["naive_estimate_with_selection"] >= P["h1_threshold"], "hypothesis"),
         chk("R1", "SD of the naive estimate across simulated literatures", res["sd_with_selection"], True, "reporting")]
    return res, c

def marginals_pairs(P, rng):
    """Frechet lower bounds for every pair of non-exclusive agreement marginals, plus an LP check over all 2^m patterns for the named pair."""
    names = list(P["marginals"]); m = np.array([P["marginals"][k] for k in names]); M = len(m)
    pairs = {f"{names[i]}+{names[j]}": float(max(0, m[i] + m[j] - 1)) for i in range(M) for j in range(i + 1, M)}
    pats = np.array(list(itertools.product([0, 1], repeat=M))); A_eq = np.vstack([pats.T, np.ones(len(pats))]); b_eq = np.append(m, 1)
    i, j = names.index(P["pair"][0]), names.index(P["pair"][1]); both = (pats[:, i] & pats[:, j]).astype(float)
    r = optimize.linprog(both, A_eq=A_eq, b_eq=b_eq, bounds=[(0, 1)] * len(pats), method="highs"); lpmin = float(r.fun)
    best = max(pairs, key=pairs.get)
    c = [chk("V1", "LP minimum for the named pair equals the Frechet lower bound within 1e-6", [lpmin, pairs[f"{names[i]}+{names[j]}"]], abs(lpmin - pairs[f"{names[i]}+{names[j]}"]) < 1e-6),
         chk("H1", f"at least one pair of positions is forced to be co-endorsed by >= {P['h1_threshold']:.0%} of respondents", [best, pairs[best]], pairs[best] >= P["h1_threshold"], "hypothesis"),
         chk("R1", "Frechet lower bound for every pair", pairs, True, "reporting")]
    return dict(pair_lower_bounds=pairs, largest_forced_pair=best, lp_check=lpmin), c

def implicit_explicit(P, rng):
    """Latent dualism D ~ N(0,1); explicit endorsement if D > t (share p_endorse); implicit score = a + g D + noise.
    Among explicit REJECTERS, is the mean implicit score significantly > 0? a = belief-independent baseline association."""
    t = stats.norm.ppf(1 - P["p_endorse"]); ED = -stats.norm.pdf(t) / stats.norm.cdf(t); out = {}
    for a in P["a_grid"]:
        sig = 0; ms = []
        for _ in range(P["reps"]):
            D = rng.normal(0, 1, P["n"]); imp = a + P["g"] * D + rng.normal(0, P["noise"], P["n"]); rej = D <= t
            tt = stats.ttest_1samp(imp[rej], 0); sig += (tt.pvalue / 2 < 0.05) and imp[rej].mean() > 0; ms.append(imp[rej].mean())
        out[str(a)] = dict(rate_significant_positive=sig / P["reps"], mean_implicit_rejecters=float(np.mean(ms)), analytic_mean=float(a + P["g"] * ED))
    c = [chk("V1", "simulated mean implicit score of rejecters within 0.02 of analytic a + g E[D | D <= t] (a = 0)", [out["0.0"]["mean_implicit_rejecters"], out["0.0"]["analytic_mean"]], abs(out["0.0"]["mean_implicit_rejecters"] - out["0.0"]["analytic_mean"]) <= 0.02),
         chk("H1", "with no belief-independent component (a = 0), explicit rejecters show a significantly POSITIVE implicit dualism score in >= 50% of studies", out["0.0"]["rate_significant_positive"], out["0.0"]["rate_significant_positive"] >= 0.5, "hypothesis"),
         chk("R1", "rate and mean by baseline a", out, True, "reporting")]
    return dict(by_a=out, E_D_given_reject=float(ED)), c

def truncated_prevalence(P, rng):
    """End-of-life experiences (K16): experiencers (share p_true) have first ELE L days before death (L exponential, median from K16).
    Only a share f_death is followed until death; others are observed for a uniform fraction of their remaining time. Observed vs true prevalence."""
    lam = np.log(2) / P["median_lead_days"]
    def run(fd, reps):
        obs = []
        for _ in range(reps):
            N = P["N"]; S = rng.exponential(P["mean_survival_days"], N); exp_ = rng.random(N) < P["p_true"]; L = rng.exponential(1 / lam, N)
            onset = np.maximum(0, S - L); end = np.where(rng.random(N) < fd, S, rng.random(N) * S); obs.append(np.mean(exp_ & (onset <= end)))
        return float(np.mean(obs))
    full = run(1.0, P["reps"]); part = run(P["f_death"], P["reps"])
    k, n = P["observed_k"], P["N"]; ph = k / n; z = 1.96; den = 1 + z ** 2 / n; cen = (ph + z ** 2 / (2 * n)) / den; hw = z * np.sqrt(ph * (1 - ph) / n + z ** 2 / (4 * n ** 2)) / den
    res = dict(observed_prevalence_full_followup=full, observed_prevalence_partial_followup=part, ratio=part / P["p_true"], wilson_ci_reported=[float(cen - hw), float(cen + hw)])
    c = [chk("V1", "with complete follow-up to death, observed prevalence within 0.01 of the true prevalence", [full, P["p_true"]], abs(full - P["p_true"]) <= 0.01),
         chk("H1", f"with {P['f_death']:.0%} followed to death, observed prevalence < 0.8 x true prevalence", part / P["p_true"], part / P["p_true"] < 0.8, "hypothesis"),
         chk("R1", f"Wilson 95% CI for the reported {k}/{n}", res["wilson_ci_reported"], True, "reporting")]
    return res, c

def pooled_null_power(P, rng):
    """Power of a pooled (fixed-effect) analysis of k two-group studies with n per group to detect the uncorrected and bias-corrected TMT effects (K18)."""
    N = P["k"] * P["n_per_group"]; se = np.sqrt(2 / N); an = {str(g): float(1 - stats.norm.cdf(1.96 - g / se) + stats.norm.cdf(-1.96 - g / se)) for g in P["g_grid"]}
    sim = {}
    for g in P["g_grid"]:
        x = rng.normal(g, 1, (P["reps"], N)); y = rng.normal(0, 1, (P["reps"], N)); z = (x.mean(1) - y.mean(1)) / se; sim[str(g)] = float(np.mean(np.abs(z) > 1.96))
    c = [chk("V1", "simulated power within 0.015 of analytic for every g", {g: round(sim[g] - an[g], 4) for g in an}, all(abs(sim[g] - an[g]) <= 0.015 for g in an)),
         chk("H1", f"pooled power to detect g = {P['g_grid'][1]} (K18 uncorrected) >= 0.95", an[str(P["g_grid"][1])], an[str(P["g_grid"][1])] >= 0.95, "hypothesis"),
         chk("H2", f"pooled power to detect g = {P['g_grid'][0]} (top of K18's bias-corrected range) < 0.5", an[str(P["g_grid"][0])], an[str(P["g_grid"][0])] < 0.5, "hypothesis")]
    return dict(analytic_power=an, simulated_power=sim, total_per_group=N), c

KINDS = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_') and k not in ('chk','power_t1','pow2') and getattr(v,'__module__',None)=='__main__'}

if __name__ == "__main__":
    P, H, t0 = R.start(sys.argv[1]); rng = np.random.default_rng(P["seed"])
    res, checks = KINDS[P["kind"]](P, rng); R.finish(H, P, res, checks, t0)
