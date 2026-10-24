"""SIM-SOUL: Soul topic simulations (track cycles A-D). Usage: python sim_soul.py iter-<k>  (from Soul/simulation/)."""
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

# ---------------- Track Cycle C kinds ----------------
def _pow1(n, d, alpha, tails=1):
    df = n - 1; nc = d * np.sqrt(n); tc = stats.t.ppf(1 - alpha / tails, df)
    return float(1 - stats.nct.cdf(tc, df, nc) + (stats.nct.cdf(-tc, df, nc) if tails == 2 else 0.0))

def small_n_power(P, rng):
    """One-sample (within-subject contrast) power at a voxel/ROI for n participants at a given alpha (K38: n = 15, p < .001 uncorrected)."""
    an = {f"n={n},d={d}": _pow1(n, d, P["alpha"]) for n in P["n_grid"] for d in P["d_grid"]}
    n0, d0 = P["n_test"], P["d_test"]; x = rng.normal(d0, 1, (P["reps"], n0))
    t = x.mean(1) / (x.std(1, ddof=1) / np.sqrt(n0)); mc = float(np.mean(t > stats.t.ppf(1 - P["alpha"], n0 - 1)))
    k = f"n={n0},d={d0}"
    c = [chk("V1", "Monte Carlo power within 0.01 of the noncentral-t value", [mc, an[k]], abs(mc - an[k]) <= 0.01),
         chk("H1", f"{k}, alpha {P['alpha']}: power < 0.5, so a non-significant region is weak evidence of no activation", an[k], an[k] < 0.5, "hypothesis"),
         chk("R1", "power grid", {kk: round(v, 3) for kk, v in an.items()}, True, "reporting")]
    return dict(power=an, power_mc=mc), c

def null_clusters(P, rng):
    """Null-data cluster inference: n subjects of pure Gaussian noise smoothed with a Gaussian kernel (sigma voxels) in a 3-D grid;
    one-sample t map, cluster-forming threshold p < alpha (one-sided), clusters of >= k voxels counted. How often does a dataset
    with NO true activation show at least one 'activation'?"""
    from scipy import ndimage
    hits, counts = 0, []
    for _ in range(P["reps"]):
        X = rng.normal(size=(P["n"],) + tuple(P["grid"]))
        X = np.stack([ndimage.gaussian_filter(x, P["sigma"]) for x in X])
        t = X.mean(0) / (X.std(0, ddof=1) / np.sqrt(P["n"])); m = t > stats.t.ppf(1 - P["alpha"], P["n"] - 1)
        lab, nl = ndimage.label(m); sizes = np.bincount(lab.ravel())[1:] if nl else np.array([])
        k = int(np.sum(sizes >= P["k"])); counts.append(k); hits += k > 0
    # voxelwise false-positive rate check on unsmoothed-equivalent: proportion of suprathreshold voxels ~ alpha
    X = rng.normal(size=(P["n"], 200000)); t = X.mean(0) / (X.std(0, ddof=1) / np.sqrt(P["n"])); fpr = float(np.mean(t > stats.t.ppf(1 - P["alpha"], P["n"] - 1)))
    res = dict(share_null_datasets_with_cluster=hits / P["reps"], mean_clusters=float(np.mean(counts)), voxel_fpr=fpr)
    c = [chk("V1", f"voxelwise false-positive rate on independent noise within 0.0005 of alpha = {P['alpha']}", fpr, abs(fpr - P["alpha"]) <= 0.0005),
         chk("H1", f"with p < {P['alpha']} uncorrected and k >= {P['k']}, >= 50% of pure-noise datasets show at least one 'activation' cluster", res["share_null_datasets_with_cluster"], res["share_null_datasets_with_cluster"] >= 0.5, "hypothesis"),
         chk("R1", "mean number of false clusters per dataset", res["mean_clusters"], True, "reporting")]
    return res, c

def fisher_small(P, rng):
    """Two-group comparison of a binary feature (K46: Chinese cultural motifs in 4 of 23 NDE vs 1 of 25 NDE-like narratives).
    Observed Fisher exact p; Monte Carlo power at the observed proportions for the observed and larger group sizes."""
    (a, n1), (b, n2) = P["g1"], P["g2"]; p_obs = float(stats.fisher_exact([[a, n1 - a], [b, n2 - b]])[1])
    def pw(m1, m2):
        x = rng.binomial(m1, a / n1, P["reps"]); y = rng.binomial(m2, b / n2, P["reps"])
        return float(np.mean([stats.fisher_exact([[i, m1 - i], [j, m2 - j]])[1] < P["alpha"] for i, j in zip(x, y)]))
    pw_obs = pw(n1, n2); pw_big = {str(m): pw(m, m) for m in P["n_grid"]}
    c = [chk("V1", "Fisher p for a table with identical proportions is 1", float(stats.fisher_exact([[5, 5], [5, 5]])[1]), abs(stats.fisher_exact([[5, 5], [5, 5]])[1] - 1) < 1e-12),
         chk("H1", f"power of a {n1} vs {n2} design at the observed proportions is < 0.5", pw_obs, pw_obs < 0.5, "hypothesis"),
         chk("R1", "observed two-sided Fisher p; power for larger equal groups", [p_obs, pw_big], True, "reporting")]
    return dict(p_observed=p_obs, power_observed_design=pw_obs, power_by_n=pw_big), c

def descriptive_differences(P, rng):
    """K46 compared feature frequencies between 23 NDE and 25 NDE-like narratives descriptively. If all features have the SAME true
    frequency in both groups, how often does at least one of m features differ by >= delta (percentage points)?"""
    n1, n2 = P["n1"], P["n2"]; base = np.array(P["base_rates"]); shift = np.zeros_like(base); shift[0] = P["true_shift"]
    x = rng.binomial(n1, np.clip(base + shift, 0, 1), (P["reps"], len(base))) / n1; y = rng.binomial(n2, base, (P["reps"], len(base))) / n2
    dif = x - y; anyd = float(np.mean(np.any(dif >= P["delta"], axis=1))); first = float(np.mean(dif[:, 0] >= P["delta"]))
    z = rng.binomial(n1, base, (P["reps"], len(base))) / n1; null_any = float(np.mean(np.any((z - y) >= P["delta"], axis=1)))
    se = np.sqrt(base * (1 - base) * (1 / n1 + 1 / n2)); an1 = float(1 - np.prod(stats.norm.cdf(P["delta"] / se)))
    c = [chk("V1", "null share with any difference >= delta within 0.05 of a normal-approximation value (discreteness tolerance)", [null_any, an1], abs(null_any - an1) <= 0.05),
         chk("H1", f"with true shift {P['true_shift']} on feature 1: P(at least one feature 'descriptively higher' by >= {P['delta']}) >= 0.5", anyd, anyd >= 0.5, "hypothesis"),
         chk("R1", "share with feature 1 >= delta; null share any", [first, null_any], True, "reporting")]
    return dict(share_any=anyd, share_feature1=first, null_share_any=null_any, normal_approx=an1), c

def cutoff_misclass(P, rng):
    """Cut-off classification on a scale measured with error (reliability rel): what share of 'cases' (observed >= cut) are true
    non-cases and vice versa? Illustrative for self-report NDE classification (K46)."""
    T = rng.normal(0, 1, P["N"]); O = np.sqrt(P["rel"]) * T + np.sqrt(1 - P["rel"]) * rng.normal(0, 1, P["N"])
    ct = np.quantile(T, 1 - P["prev"]); co = np.quantile(O, 1 - P["prev"]); tc, oc = T >= ct, O >= co
    ppv = float(np.mean(tc[oc])); agree = float(np.mean(tc == oc))
    rho = np.sqrt(P["rel"]); joint = stats.multivariate_normal([0, 0], [[1, rho], [rho, 1]]).cdf([-stats.norm.ppf(1 - P["prev"])] * 2)
    an_both = joint  # by symmetry P(T>=c, O>=c) = Phi2(-c, -c; rho)
    an_ppv = float(an_both / P["prev"])
    c = [chk("V1", "simulated PPV within 0.01 of the bivariate-normal value", [ppv, an_ppv], abs(ppv - an_ppv) <= 0.01),
         chk("H1", f"with reliability {P['rel']} and a {P['prev']:.0%} case rate, >= 20% of classified cases are true non-cases", 1 - ppv, 1 - ppv >= 0.2, "hypothesis"),
         chk("R1", "overall agreement", agree, True, "reporting")]
    return dict(ppv=ppv, ppv_analytic=an_ppv, agreement=agree), c



# ---------------- Track Cycle D (x12) kinds ----------------
def continuity_dependence(P, rng):
    """K61: 6 vignette states (3 bodily, 3 mental). Reported: mean continuity bodily pb, mental pm; share judging >= 1 state to continue; share judging all 6.
    Compare an independence model and a two-class (cessation vs continuity) model against the reported shares."""
    pb, pm, k = P["p_bodily"], P["p_mental"], P["n_items_each"]
    ind_any = 1 - (1 - pb) ** k * (1 - pm) ** k; ind_all = pb ** k * pm ** k
    w = P["share_any_reported"]; cb, cm = pb / w, pm / w
    two_all = w * cb ** k * cm ** k
    sims = rng.random((P["n"], 2 * k)) < np.r_[[pb] * k, [pm] * k]; sim_any = float(sims.any(1).mean())
    c = [chk("V1", "simulated independence P(>=1) within 0.005 of the analytic value", [sim_any, ind_any], abs(sim_any - ind_any) <= 0.005),
         chk("H1", f"independence over-predicts the share judging >= 1 state to continue by >= {P['h1_gap']} (responses cluster within persons)", ind_any - w, ind_any - w >= P["h1_gap"], "hypothesis"),
         chk("H2", "a two-class model (cessation class + independent continuity class) still under-predicts 'all six continue' by a factor >= 2", [two_all, P["share_all_reported"]], P["share_all_reported"] >= 2 * two_all, "hypothesis"),
         chk("R1", "independence P(any), P(all six); two-class P(all six)", [ind_any, ind_all, two_all], True, "reporting")]
    return dict(independence_any=ind_any, independence_all=ind_all, two_class_all=two_all, class_rates=[cb, cm]), c

def hetero_sign(P, rng):
    """K61: framing effect on the logit scale, mean mu, between-country SD sigma, 24 countries. How often would >= 1 country show a negative true
    effect, and how often a negative *estimated* effect once country-level estimation error (se) is added?"""
    mu, sd, m, se = P["mu"], P["sigma"], P["countries"], P["se"]
    p_neg_true = stats.norm.cdf(-mu / sd); p_neg_est = stats.norm.cdf(-mu / np.sqrt(sd ** 2 + se ** 2))
    eff = rng.normal(mu, sd, (P["reps"], m)); est = eff + rng.normal(0, se, eff.shape)
    any_true = float((eff < 0).any(1).mean()); any_est = float((est < 0).any(1).mean())
    an_true = 1 - (1 - p_neg_true) ** m
    c = [chk("V1", "simulated P(>=1 negative true effect) within 0.01 of 1-(1-p)^m", [any_true, an_true], abs(any_true - an_true) <= 0.01),
         chk("H1", f"P(>= 1 of {m} countries shows a negative estimated effect) >= {P['h1']} (a single exception such as Morocco is unsurprising)", any_est, any_est >= P["h1"], "hypothesis"),
         chk("R1", "per-country P(negative) true / estimated; P(any) true / estimated", [float(p_neg_true), float(p_neg_est), any_true, any_est], True, "reporting")]
    return dict(p_neg_true=float(p_neg_true), p_neg_est=float(p_neg_est), any_true=any_true, any_est=any_est), c

def collinear_betas(P, rng):
    """K55 Table 2: zero-order correlations of three meaning subscales (comprehension, purpose, mattering) with each other and with mind-upload approval.
    Standardised simultaneous-regression betas follow from the correlation matrix alone; simulate data with that matrix to check."""
    R = np.array(P["R_xx"]); r = np.array(P["r_xy"]); beta = np.linalg.solve(R, r)
    S = np.block([[R, r[:, None]], [r[None, :], np.ones((1, 1))]]); X = rng.multivariate_normal(np.zeros(4), S, P["n"])
    Z = (X - X.mean(0)) / X.std(0); b_sim = np.linalg.lstsq(Z[:, :3], Z[:, 3], rcond=None)[0]
    c = [chk("V1", "betas from simulated data within 0.01 of the analytic betas", [b_sim.tolist(), beta.tolist()], np.max(np.abs(b_sim - beta)) <= 0.01),
         chk("H1", f"the analytic simultaneous betas of comprehension and purpose are both within +/-{P['h1']} of 0 (the 'full mediation' pattern follows from the correlations alone)", beta[:2].tolist(), bool(np.all(np.abs(beta[:2]) <= P["h1"])), "hypothesis"),
         chk("R1", "analytic standardised betas (comprehension, purpose, mattering); R^2", [beta.tolist(), float(beta @ r)], True, "reporting")]
    return dict(beta=beta.tolist(), R2=float(beta @ r)), c

def slope_diff(P, rng):
    """K55: simple slopes of mattering on approval by afterlife-belief group with 95% CIs. z-test of the difference between two slopes
    from the reported CIs (independent groups; normal approximation)."""
    def se(ci): return (ci[1] - ci[0]) / (2 * 1.959964)
    b1, b2 = P["b1"], P["b2"]; s1, s2 = se(P["ci1"]), se(P["ci2"]); z = (b1 - b2) / np.sqrt(s1 ** 2 + s2 ** 2); p = 2 * stats.norm.sf(abs(z))
    d = rng.normal(b1, s1, P["reps"]) - rng.normal(b2, s2, P["reps"]); zs = float(d.mean() / d.std())
    c = [chk("V1", "simulated z within 0.02 of the analytic z", [zs, float(z)], abs(zs - z) <= 0.02),
         chk("H1", "the difference between the two slopes is not significant at .05 (|z| < 1.96)", [float(z), float(p)], abs(z) < 1.959964, "hypothesis"),
         chk("R1", "z, p, SEs", [float(z), float(p), s1, s2], True, "reporting")]
    return dict(z=float(z), p=float(p)), c

def _kalpha_interval(M):
    """Krippendorff's alpha (interval metric), M units x raters, no missing."""
    n_u, m = M.shape; v = M.ravel(); Do = np.mean([np.mean((row[:, None] - row[None, :]) ** 2) * m / (m - 1) for row in M])
    De = np.mean((v[:, None] - v[None, :]) ** 2) * len(v) / (len(v) - 1); return 1 - Do / De

def alpha_precision(P, rng):
    """K53: vNDE scale, overall Krippendorff alpha 0.49 (95% CI 0.40-0.58) across 17 cases and 14 raters. How wide is the sampling
    distribution of alpha with this few cases if the true reliability is ~0.49? Latent case strength + rater noise, 4-level ordinal ratings."""
    n, m = P["cases"], P["raters"]; rho = P["latent_icc"]; vals = []
    cuts = np.array(P["cuts"])
    for _ in range(P["reps"]):
        t = rng.normal(0, np.sqrt(rho), n)[:, None] + rng.normal(0, np.sqrt(1 - rho), (n, m)); vals.append(_kalpha_interval(np.digitize(t, cuts).astype(float)))
    vals = np.array(vals); perfect = _kalpha_interval(np.tile(np.arange(n) % 4, (m, 1)).T.astype(float))
    lo, hi = np.quantile(vals, [0.025, 0.975])
    c = [chk("V1", "alpha = 1 for perfect agreement", perfect, abs(perfect - 1) < 1e-12),
         chk("H1", f"with {n} cases the central 95% of alpha estimates spans >= {P['h1']} (the 17-case estimate is imprecise)", float(hi - lo), hi - lo >= P["h1"], "hypothesis"),
         chk("R1", "mean alpha, 2.5% and 97.5% quantiles", [float(vals.mean()), float(lo), float(hi)], True, "reporting")]
    return dict(mean=float(vals.mean()), q025=float(lo), q975=float(hi)), c

def veridical_yield(P, rng):
    """K53/K54: how many cardiac arrests must be screened to obtain >= 1 case in which a hidden visual target could have been perceived
    during an out-of-body experience? Product of stage probabilities (ILLUSTRATIVE) and a Poisson approximation."""
    q = np.prod(P["stages"]); n80 = int(np.ceil(np.log(1 - P["power"]) / np.log(1 - q)))
    hits = rng.binomial(n80, q, P["reps"]); emp = float(np.mean(hits >= 1))
    c = [chk("V1", f"simulated P(>=1 testable case) at N = {n80} within 0.01 of {P['power']}", emp, abs(emp - P["power"]) <= 0.01),
         chk("H1", f"N needed for 80% chance of >= 1 testable case is >= {P['h1']} arrests", n80, n80 >= P["h1"], "hypothesis"),
         chk("R1", "per-arrest probability of a testable case; N for 80%", [float(q), n80], True, "reporting")]
    return dict(per_arrest=float(q), n_for_power=n80), c


KINDS = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_') and k not in ('chk','power_t1','pow2') and getattr(v,'__module__',None)=='__main__'}

if __name__ == "__main__":
    P, H, t0 = R.start(sys.argv[1]); rng = np.random.default_rng(P["seed"])
    res, checks = KINDS[P["kind"]](P, rng); R.finish(H, P, res, checks, t0)
