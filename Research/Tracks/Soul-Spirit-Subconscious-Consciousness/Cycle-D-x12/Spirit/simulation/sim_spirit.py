"""SIM-SPIRIT: Spirit topic simulations (track cycles A-D). Usage: python sim_spirit.py iter-<k>  (from Spirit/simulation/)."""
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

# ---- Track Cycle B kinds ----
def _dl(y, v):
    """DerSimonian-Laird random-effects estimate; returns (mu, se, tau2)."""
    w = 1 / v; mu_f = np.sum(w * y) / w.sum(); Q = np.sum(w * (y - mu_f) ** 2); k = len(y)
    C = w.sum() - np.sum(w ** 2) / w.sum(); tau2 = max(0.0, (Q - (k - 1)) / C) if C > 0 else 0.0
    ws = 1 / (v + tau2); mu = np.sum(ws * y) / ws.sum(); return float(mu), float(np.sqrt(1 / ws.sum())), float(tau2)


def evalue(P, rng):
    """E-value (VanderWeele & Ding 2017 formula) for a protective observational risk ratio (K19: RR 0.87, CI upper 0.91)."""
    def ev(rr):
        r = 1 / rr if rr < 1 else rr; return float(r + np.sqrt(r * (r - 1)))
    e_pt, e_ci = ev(P["rr"]), ev(P["ci_upper"]); bf = e_pt * e_pt / (2 * e_pt - 1)
    res = dict(e_value_point=e_pt, e_value_ci=e_ci, bias_factor_at_e=float(bf), check_example=ev(3.9))
    c = [chk("V1", "formula reproduces the worked example RR 3.9 -> E-value 7.26", res["check_example"], abs(res["check_example"] - 7.26) < 0.01),
         chk("V2", "bias factor at RR_UD = RR_UY = E equals 1/RR within 1e-9", [bf, 1 / P["rr"]], abs(bf - 1 / P["rr"]) < 1e-9),
         chk("H1", "the point E-value is below 2 (an unmeasured confounder associated with both exposure and outcome by RR < 2 could explain the association)", e_pt, e_pt < 2, "hypothesis"),
         chk("R1", "E-value for the confidence limit closest to 1", e_ci, True, "reporting")]
    return res, c

def small_k_meta(P, rng):
    """Coverage of DerSimonian-Laird (z) and Hartung-Knapp (t) 95% CIs with k studies and heterogeneity tau (K20: k = 8, high heterogeneity)."""
    out = {}
    for tau in P["tau_grid"]:
        dl = hk = 0
        for _ in range(P["reps"]):
            n = rng.integers(P["n_lo"], P["n_hi"] + 1, P["k"]); th = rng.normal(P["mu"], tau, P["k"]); v = 2 / n + th ** 2 / (4 * n); y = rng.normal(th, np.sqrt(v))
            mu, se, t2 = _dl(y, v); dl += abs(mu - P["mu"]) <= 1.96 * se
            w = 1 / (v + t2); q = np.sum(w * (y - mu) ** 2) / (P["k"] - 1); sh = np.sqrt(q / w.sum()); hk += abs(mu - P["mu"]) <= stats.t.ppf(0.975, P["k"] - 1) * sh
        out[str(tau)] = dict(dl_coverage=dl / P["reps"], hk_coverage=hk / P["reps"])
    tt = str(P["tau_test"])
    c = [chk("V1", "tau = 0: DL coverage >= 0.93", out["0.0"]["dl_coverage"], out["0.0"]["dl_coverage"] >= 0.93),
         chk("H1", f"tau = {tt}, k = {P['k']}: DL 95% CI coverage < 0.90", out[tt]["dl_coverage"], out[tt]["dl_coverage"] < 0.90, "hypothesis"),
         chk("R1", "coverage by tau", out, True, "reporting")]
    return dict(by_tau=out), c

def holm_outcomes(P, rng):
    """k correlated outcomes, one with a true effect d: family-wise error under the null and power cost of Holm correction."""
    S = np.full((P["k"], P["k"]), P["r"]) + np.eye(P["k"]) * (1 - P["r"]); fw = 0; pu = ph = 0; delta = np.zeros(P["k"]); delta[0] = P["d"]
    def holm(p):
        o = np.argsort(p); rej = np.zeros(len(p), bool)
        for i, j in enumerate(o):
            if p[j] <= 0.05 / (len(p) - i): rej[j] = True
            else: break
        return rej
    for _ in range(P["reps"]):
        x = rng.multivariate_normal(np.zeros(P["k"]), S, P["n"]); y = rng.multivariate_normal(np.zeros(P["k"]), S, P["n"]); fw += holm(stats.ttest_ind(x, y).pvalue).any()
        x = rng.multivariate_normal(delta, S, P["n"]); p = stats.ttest_ind(x, y).pvalue; pu += p[0] < 0.05; ph += holm(p)[0]
    res = dict(holm_familywise_null=fw / P["reps"], power_uncorrected=pu / P["reps"], power_holm=ph / P["reps"]); loss = res["power_uncorrected"] - res["power_holm"]
    c = [chk("V1", "Holm family-wise error under the null <= 0.06", res["holm_familywise_null"], res["holm_familywise_null"] <= 0.06),
         chk("H1", "Holm costs <= 10 percentage points of power for the one true outcome", loss, loss <= 0.10, "hypothesis"),
         chk("R1", "power uncorrected vs Holm", [res["power_uncorrected"], res["power_holm"]], True, "reporting")]
    return res, c

def metareg_k8(P, rng):
    """Meta-regression with k studies and a null moderator (true slope 0) under heterogeneity tau: false-positive rate of a fixed-effect weighted z-test vs a t-based test with DL tau."""
    out = {}
    for tau in P["tau_grid"]:
        fz = rt = 0
        for _ in range(P["reps"]):
            n = rng.integers(P["n_lo"], P["n_hi"] + 1, P["k"]); v = 2 / n; x = rng.normal(0, 1, P["k"]); y = rng.normal(P["mu"], np.sqrt(v + tau ** 2))
            X = np.column_stack([np.ones(P["k"]), x])
            def wls(w):
                W = np.diag(w); XtWX = X.T @ W @ X; b = np.linalg.solve(XtWX, X.T @ W @ y); return b, np.linalg.inv(XtWX)
            b, V = wls(1 / v); fz += abs(b[1] / np.sqrt(V[1, 1])) > 1.96
            res_ = y - X @ b; Q = np.sum(res_ ** 2 / v); w0 = 1 / v; C = w0.sum() - np.trace(np.linalg.inv(X.T @ np.diag(w0) @ X) @ (X.T @ np.diag(w0 ** 2) @ X))
            t2 = max(0, (Q - (P["k"] - 2)) / C); b2, V2 = wls(1 / (v + t2)); r2 = y - X @ b2; s2 = np.sum(r2 ** 2 / (v + t2)) / (P["k"] - 2)
            rt += abs(b2[1] / np.sqrt(V2[1, 1] * max(s2, 1e-12))) > stats.t.ppf(0.975, P["k"] - 2)
        out[str(tau)] = dict(fe_z_fpr=fz / P["reps"], re_t_fpr=rt / P["reps"])
    tt = str(P["tau_test"])
    c = [chk("V1", "tau = 0: fixed-effect z-test false-positive rate within 0.02 of 0.05", out["0.0"]["fe_z_fpr"], abs(out["0.0"]["fe_z_fpr"] - 0.05) <= 0.02),
         chk("H1", f"tau = {tt}: fixed-effect z-test false-positive rate for a null moderator > 0.10", out[tt]["fe_z_fpr"], out[tt]["fe_z_fpr"] > 0.10, "hypothesis"),
         chk("R1", "false-positive rates by tau", out, True, "reporting")]
    return dict(by_tau=out), c

def qual_saturation(P, rng):
    """Probability that a theme present in a share p of groups is never observed in g focus groups (K21: 2 groups x 3 communities)."""
    an = {str(p): float((1 - p) ** P["groups"]) for p in P["p_grid"]}
    sim = {str(p): float(np.mean((rng.random((P["reps"], P["groups"])) < p).sum(1) == 0)) for p in P["p_grid"]}
    pt = str(P["p_test"])
    c = [chk("V1", "simulated miss probability within 0.01 of analytic for every p", {p: round(sim[p] - an[p], 4) for p in an}, all(abs(sim[p] - an[p]) <= 0.01 for p in an)),
         chk("H1", f"a theme present in {float(pt):.0%} of groups is missed entirely with probability >= 0.5", an[pt], an[pt] >= 0.5, "hypothesis"),
         chk("R1", "miss probability by prevalence", an, True, "reporting")]
    return dict(miss_probability=an, simulated=sim), c

# ---------------- Track Cycle C kinds ----------------
def mediation_confound(P, rng):
    """K39: acute subjective effects (ASE, e.g. mystical experience) correlate with lasting outcomes. A common cause C (e.g. drug
    response/expectancy) drives both ASE and outcome; ASE's own causal effect on outcome is `direct_ase` (0 = none).
    Reports the observed ASE-outcome correlation and the naive regression 'effect' of ASE on outcome."""
    n = P["n"]; out = {}
    for k in ("null", "test"):
        dase = 0.0 if k == "null" else P["direct_ase"]; g = 0.0 if k == "null" else P["confound"]
        rs = []
        for _ in range(P["reps"]):
            C = rng.normal(size=n); A = g * C + rng.normal(size=n); Y = g * C + dase * A + rng.normal(size=n)
            rs.append(np.corrcoef(A, Y)[0, 1])
        out[k] = dict(mean_r=float(np.mean(rs)), share_sig=float(np.mean([abs(r) * np.sqrt((n - 2) / (1 - r * r)) > stats.t.ppf(0.975, n - 2) for r in rs])))
    g, d = P["confound"], P["direct_ase"]
    # exact: Var A = g2+1; Cov(A,Y) = g2 + d(g2+1); Var Y = g2 + d^2(g2+1) + 2 d g2 + 1
    vA = g * g + 1; cov = g * g + d * vA; vY = g * g + d * d * vA + 2 * d * g * g + 1; an = float(cov / np.sqrt(vA * vY))
    c = [chk("V1", "simulated mean correlation within 0.02 of the analytic value", [out["test"]["mean_r"], an], abs(out["test"]["mean_r"] - an) <= 0.02),
         chk("H1", f"with a common cause of strength {g} and ASE direct effect {d}, the ASE-outcome correlation is >= 0.30", an, an >= 0.3, "hypothesis"),
         chk("R1", "share of studies (n = %d) with a significant ASE-outcome correlation; null condition = no common cause and no ASE effect" % n, out, True, "reporting")]
    return dict(analytic_r=an, sim=out), c

def attrition_mnar(P, rng):
    """K45: 654 participants at baseline, 379 at the post-experience time point. If staying in the study depends on the (later)
    outcome, how much does the baseline-outcome correlation among completers differ from the full-sample value?
    Retention probability = logistic(a + m * Y), a chosen so that the expected retention matches retain_target."""
    n, rho = P["n"], P["rho"]; res = {}
    for m in P["m_grid"]:
        rs, kept = [], []
        a = optimize.brentq(lambda a: np.mean(1 / (1 + np.exp(-(a + m * rng.normal(size=20000))))) - P["retain_target"], -10, 10) if m else np.log(P["retain_target"] / (1 - P["retain_target"]))
        for _ in range(P["reps"]):
            X = rng.normal(size=n); Y = rho * X + np.sqrt(1 - rho * rho) * rng.normal(size=n)
            keep = rng.random(n) < 1 / (1 + np.exp(-(a + m * Y))); rs.append(np.corrcoef(X[keep], Y[keep])[0, 1]); kept.append(keep.mean())
        res[str(m)] = dict(mean_r_completers=float(np.mean(rs)), retention=float(np.mean(kept)))
    t = res[str(P["m_test"])]; bias = t["mean_r_completers"] - rho
    c = [chk("V1", "random dropout (m = 0): completer correlation within 0.01 of the true value", res["0.0"]["mean_r_completers"], abs(res["0.0"]["mean_r_completers"] - rho) <= 0.01),
         chk("H1", f"outcome-dependent dropout (m = {P['m_test']}) shifts the correlation by >= 0.05 in absolute value", float(bias), abs(bias) >= 0.05, "hypothesis"),
         chk("R1", "completer correlation and retention by m", res, True, "reporting")]
    return dict(by_m=res, bias_test=float(bias)), c

def attenuation(P, rng):
    """Spearman attenuation: observed r = true r * sqrt(rel_x * rel_y). Disattenuated r = observed r / sqrt(rel_x * rel_y)."""
    out = {}
    for name, (r_true, rx, ry) in P["cases"].items():
        an = r_true * np.sqrt(rx * ry); T = rng.multivariate_normal([0, 0], [[1, r_true], [r_true, 1]], P["N"])
        X = np.sqrt(rx) * T[:, 0] + np.sqrt(1 - rx) * rng.normal(size=P["N"]); Y = np.sqrt(ry) * T[:, 1] + np.sqrt(1 - ry) * rng.normal(size=P["N"])
        out[name] = dict(observed_analytic=float(an), observed_sim=float(np.corrcoef(X, Y)[0, 1]), loss=float(r_true - an))
    k = P["test_case"]; dis = {nm: float(r / np.sqrt(rx * ry)) for nm, (r, rx, ry) in P.get("observed", {}).items()}
    c = [chk("V1", "simulated observed correlations within 0.01 of r*sqrt(rel_x*rel_y)", {n: [v['observed_sim'], v['observed_analytic']] for n, v in out.items()}, all(abs(v["observed_sim"] - v["observed_analytic"]) <= 0.01 for v in out.values())),
         chk("H1", f"case '{k}': measurement error alone lowers the observed correlation by >= 0.05", out[k]["loss"], out[k]["loss"] >= 0.05, "hypothesis"),
         chk("R1", "disattenuated values for reported correlations (assumed reliabilities)", dis, True, "reporting")]
    return dict(cases=out, disattenuated=dis), c

def dose_plateau(P, rng):
    """K40 reports sigmoid-like dose-response curves plateauing around 100 ug. Synthetic study-level means at the given doses follow
    an Emax curve E = Emax * D^h / (ED50^h + D^h) plus between-study noise; a 'plateau test' compares studies at 200 vs 100 ug.
    How often does the test call a plateau (no significant increase) although the true curve still rises by `rise` (fraction)?"""
    D = np.array(P["doses"], float)
    def emax(d): return P["Emax"] * d ** P["h"] / (P["ED50"] ** P["h"] + d ** P["h"])
    rise = float((emax(200) - emax(100)) / emax(100)); miss = 0
    for _ in range(P["reps"]):
        a = emax(100) + rng.normal(0, P["sd_between"], P["k100"]); b = emax(200) + rng.normal(0, P["sd_between"], P["k200"])
        miss += stats.ttest_ind(b, a, equal_var=False).pvalue >= 0.05 or b.mean() <= a.mean()
    share = miss / P["reps"]
    c = [chk("V1", "Emax at ED50 equals half of Emax", float(emax(P['ED50']) / P['Emax']), abs(emax(P["ED50"]) / P["Emax"] - 0.5) < 1e-12),
         chk("H1", f"true rise from 100 to 200 ug = {rise:.1%}: a {P['k100']} vs {P['k200']} study comparison calls a 'plateau' in >= 50%", share, share >= 0.5, "hypothesis"),
         chk("R1", "true relative rise 100->200 ug", rise, True, "reporting")]
    return dict(true_rise=rise, share_plateau_called=share), c



# ---------------- Track Cycle D (x12) kinds ----------------
def meq_contingency(P, rng):
    """K49 Table 2: MEQ30- vs MEQ43-derived 'complete mystical experience' (TP, FP, FN, TN). Recompute hit rate, false-alarm rate,
    proportion correct, Cohen's kappa and d' under several standard conventions, and compare with the reported d'."""
    TP, FP, FN, TN = P["TP"], P["FP"], P["FN"], P["TN"]; N = TP + FP + FN + TN
    h, f = TP / (TP + FN), FP / (FP + TN); pc = (TP + TN) / N
    pe = ((TP + FP) * (TP + FN) + (FN + TN) * (FP + TN)) / N ** 2; kappa = (pc - pe) / (1 - pe)
    z = stats.norm.ppf; dp = {"plain": z(h) - z(f), "loglinear": z((TP + .5) / (TP + FN + 1)) - z((FP + .5) / (FP + TN + 1)),
          "1/(2N)_bounds": z(min(h, 1 - 1 / (2 * (TP + FN)))) - z(max(f, 1 / (2 * (FP + TN))))}
    dp = {k: float(v) for k, v in dp.items()}
    sim = rng.random((P["reps"], TP + FN)) < h; hs = float(sim.mean())
    close = [k for k, v in dp.items() if abs(v - P["reported_dprime"]) <= 0.1]
    c = [chk("V1", "hit, false-alarm and proportion correct reproduce the reported 0.95, 0.14 and 90.2% (rounded)", [h, f, pc], abs(h - 0.95) < 0.005 and abs(f - 0.14) < 0.005 and abs(pc - 0.902) < 0.0005),
         chk("V2", "simulated hit rate within 0.005 of TP/(TP+FN)", [hs, h], abs(hs - h) <= 0.005),
         chk("H1", f"no standard d' convention reproduces the reported d' = {P['reported_dprime']} within 0.1", dp, len(close) == 0, "hypothesis"),
         chk("R1", "Cohen's kappa; d' by convention", [float(kappa), dp], True, "reporting")]
    return dict(hit=h, fa=f, pc=pc, kappa=float(kappa), dprime=dp), c

def cutoff_reliability(P, rng):
    """K49: a 'complete' experience requires >= 60% of the maximum on each of the four MEQ30 subscales. With the reported subscale
    reliabilities, how often would two parallel administrations of the same experience disagree on the classification?
    True scores share a second-order factor (loading lam); means and SD on the 0-1 scale are ILLUSTRATIVE."""
    rel = np.array(P["alphas"]); k = len(rel); lam = P["lam"]; n = P["n"]
    g = rng.normal(size=n)[:, None]; T = lam * g + np.sqrt(1 - lam ** 2) * rng.normal(size=(n, k))
    def obs(): return P["mean"] + P["sd"] * (np.sqrt(rel) * T + np.sqrt(1 - rel) * rng.normal(size=(n, k)))
    A, B = obs(), obs(); ca, cb = (A >= 0.6).all(1), (B >= 0.6).all(1); dis = float(np.mean(ca != cb))
    one = rng.normal(size=(n, k)) * 0 + 1.0; perfect_rel = float(np.mean((P["mean"] + P["sd"] * T >= 0.6).all(1) != (P["mean"] + P["sd"] * T >= 0.6).all(1)))
    c = [chk("V1", "with error-free scores the two administrations never disagree", perfect_rel, perfect_rel == 0),
         chk("H1", f"the two administrations disagree on 'complete' for >= {P['h1']:.0%} of experiences", dis, dis >= P["h1"], "hypothesis"),
         chk("R1", "share 'complete' in administration A; disagreement; disagreement among those classified complete in A", [float(ca.mean()), dis, float(np.mean(~cb[ca]))], True, "reporting")]
    return dict(share_complete=float(ca.mean()), disagreement=dis, flip_given_complete=float(np.mean(~cb[ca]))), c

def evalue_harmful(P, rng):
    """E-value (VanderWeele & Ding 2017) for an observational RR > 1 and its lower confidence limit; compare with values reported by the source."""
    def ev(rr): return float(rr + np.sqrt(rr * (rr - 1))) if rr > 1 else 1.0
    e_pt, e_ci = ev(P["rr"]), ev(P["ci_lower"]); bf = e_pt * e_pt / (2 * e_pt - 1)
    c = [chk("V1", "formula reproduces the worked example RR 3.9 -> E-value 7.26", ev(3.9), abs(ev(3.9) - 7.26) < 0.01),
         chk("V2", "bias factor at RR_UD = RR_UY = E equals the RR within 1e-9", [bf, P["rr"]], abs(bf - P["rr"]) < 1e-9),
         chk("V3", "recomputed E-values match the source's reported values within 0.01", [e_pt, e_ci, P["reported"]], abs(e_pt - P["reported"][0]) <= 0.01 and abs(e_ci - P["reported"][1]) <= 0.01),
         chk("H1", "the point E-value is below 2 (a moderate unmeasured confounder could explain the association)", e_pt, e_pt < 2, "hypothesis"),
         chk("R1", "E-values (point, CI limit)", [e_pt, e_ci], True, "reporting")]
    return dict(e_point=e_pt, e_ci=e_ci), c

def blinding_index(P, rng):
    """K51: correct allocation guesses per arm. Bang's blinding index per arm, BI = (correct - incorrect)/n (no 'don't know' option);
    BI = 0 is ideal blinding, 1 complete unblinding. Bootstrap 95% interval."""
    out = {}
    for arm, (k, n) in P["arms"].items():
        bi = (2 * k - n) / n; bs = (2 * rng.binomial(n, k / n, P["reps"]) - n) / n
        out[arm] = dict(bi=bi, lo=float(np.quantile(bs, 0.025)), hi=float(np.quantile(bs, 0.975)))
    k0 = (2 * rng.binomial(40, 0.5, P["reps"]) - 40) / 40
    c = [chk("V1", "under random guessing (p = .5, n = 40) the mean simulated BI is within 0.01 of 0", float(k0.mean()), abs(k0.mean()) <= 0.01),
         chk("H1", f"BI >= {P['h1']} in every arm (blinding essentially failed)", {a: v['bi'] for a, v in out.items()}, all(v["bi"] >= P["h1"] for v in out.values()), "hypothesis"),
         chk("R1", "BI and bootstrap interval per arm", out, True, "reporting")]
    return out, c

def expectancy_bias(P, rng):
    """K50/K51: two-arm trial (n per arm from K51) with zero true drug effect. Functional unblinding adds an expectancy improvement e to the
    active arm and a disappointment worsening e to the placebo arm (e ILLUSTRATIVE). SD of change derived from K51's reported CI."""
    n1, n2, sd, e = P["n1"], P["n2"], P["sd"], P["e"]
    a = rng.normal(-e, sd, (P["reps"], n1)); b = rng.normal(+e, sd, (P["reps"], n2))
    t, p = stats.ttest_ind(a, b, axis=1); sig = float(np.mean(p < 0.05)); d0 = rng.normal(0, sd, (P["reps"], n1)); t0, p0 = stats.ttest_ind(d0, rng.normal(0, sd, (P["reps"], n2)), axis=1)
    c = [chk("V1", "with e = 0, false-positive rate within 0.05 +/- 3 MC SE", float(np.mean(p0 < 0.05)), abs(np.mean(p0 < 0.05) - 0.05) <= 3 * np.sqrt(0.05 * 0.95 / P["reps"])),
         chk("H1", f"with expectancy +/-{e} points and no drug effect, P(p < .05) >= {P['h1']}", sig, sig >= P["h1"], "hypothesis"),
         chk("R1", "mean spurious difference; P(p<.05)", [float((a.mean(1) - b.mean(1)).mean()), sig], True, "reporting")]
    return dict(power_spurious=sig), c

def meta_pi(P, rng):
    """K52: random-effects pooled d with 95% CI, k effect sizes, I^2. Back out total variance per study (tau^2 + v) from the CI and k,
    split it using I^2, and compute the 95% prediction interval. Simulate studies from the implied model to check coverage."""
    k, d, lo, hi, I2 = P["k"], P["d"], P["ci"][0], P["ci"][1], P["I2"]
    se = (hi - lo) / (2 * 1.959964); tot = k * se ** 2; tau2 = I2 * tot; v = tot - tau2
    tq = stats.t.ppf(0.975, k - 2); pi = (d - tq * np.sqrt(tau2 + se ** 2), d + tq * np.sqrt(tau2 + se ** 2))
    new = rng.normal(d, np.sqrt(tau2), P["reps"]); cov = float(np.mean((new > pi[0]) & (new < pi[1])))
    c = [chk("V1", "a new true effect falls inside the prediction interval in >= 95% of draws", cov, cov >= 0.95),
         chk("H1", "the 95% prediction interval includes 0 (some settings may show no reduction)", [float(pi[0]), float(pi[1])], pi[0] <= 0 <= pi[1], "hypothesis"),
         chk("R1", "implied tau, typical within-study SE, prediction interval", [float(np.sqrt(tau2)), float(np.sqrt(v)), [float(pi[0]), float(pi[1])]], True, "reporting")]
    return dict(tau=float(np.sqrt(tau2)), pi=[float(pi[0]), float(pi[1])]), c

def prepost_rtm(P, rng):
    """K52: all meta-analysed studies were within-subject pre-post designs. If participants are enrolled because their death anxiety is high
    (top share q) and test-retest correlation is r, regression to the mean alone yields an apparent pre-post 'reduction' (r, q ILLUSTRATIVE)."""
    n = P["n"]; r = P["r"]; T = rng.normal(size=n); pre = np.sqrt(r) * T + np.sqrt(1 - r) * rng.normal(size=n); post = np.sqrt(r) * T + np.sqrt(1 - r) * rng.normal(size=n)
    sel = pre >= np.quantile(pre, 1 - P["q"]); diff = pre[sel] - post[sel]; dz = float(diff.mean() / diff.std()); dav = float(diff.mean() / pre.std())
    sel0 = np.ones(n, bool); d0 = float((pre - post).mean() / pre.std())
    c = [chk("V1", "with no selection the mean pre-post difference is within 0.01 SD of 0", d0, abs(d0) <= 0.01),
         chk("H1", f"selection on high baseline alone yields an apparent reduction >= {P['h1']} SD (no treatment effect)", dav, dav >= P["h1"], "hypothesis"),
         chk("R1", "apparent reduction (population-SD units, d_z)", [dav, dz], True, "reporting")]
    return dict(d_pop=dav, d_z=dz), c


KINDS = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_') and k not in ('chk','power_t1','pow2') and getattr(v,'__module__',None)=='__main__'}

if __name__ == "__main__":
    P, H, t0 = R.start(sys.argv[1]); rng = np.random.default_rng(P["seed"])
    res, checks = KINDS[P["kind"]](P, rng); R.finish(H, P, res, checks, t0)
