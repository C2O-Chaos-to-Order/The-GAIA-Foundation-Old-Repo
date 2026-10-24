"""SIM-CONS: Consciousness topic simulations (track cycles A-D). Usage: python sim_cons.py iter-<k>  (from Consciousness/simulation/)."""
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

# ---------------- Track Cycle C kinds ----------------
def predictions_battery(P, rng):
    """K42 tested several preregistered predictions per theory; K41 argues a single failed prediction should not 'falsify' a theory.
    If a theory is TRUE and each of m independent critical tests has power pw, P(all pass) = pw^m. Posterior that the theory is
    true after f failures, with prior pi, power pw (true theory passes a test) and pass rate q for a false theory."""
    m, pw, q, pi = P["m"], P["power"], P["q_false"], P["prior"]
    an = pw ** m; sim = float(np.mean(np.all(rng.random((P["reps"], m)) < pw, axis=1)))
    post = {}
    for f in range(m + 1):
        lt = stats.binom.pmf(m - f, m, pw); lf = stats.binom.pmf(m - f, m, q); post[str(f)] = float(pi * lt / (pi * lt + (1 - pi) * lf))
    c = [chk("V1", "simulated P(all predictions pass | true theory) within 0.01 of power^m", [sim, an], abs(sim - an) <= 0.01),
         chk("H1", f"a TRUE theory tested on {m} critical predictions at power {pw} fails at least one with probability >= 0.4", 1 - an, 1 - an >= 0.4, "hypothesis"),
         chk("H2", f"after {P['f_test']} failure(s) the posterior that the theory is true stays >= {P['h2_threshold']} (prior {pi})", post[str(P["f_test"])], post[str(P["f_test"])] >= P["h2_threshold"], "hypothesis"),
         chk("R1", "posterior by number of failed predictions", post, True, "reporting")]
    return dict(p_all_pass=an, p_all_pass_sim=sim, posterior_by_failures=post), c

def rare_association_power(P, rng):
    """K32: dream recall was not associated with intraoperative awareness, but awareness is rare (0-2.5% in the clinical studies
    that reported it). Power of a single study (N patients) to detect a risk ratio RR for awareness among dream recallers."""
    N, pr, pa, RR = P["N"], P["p_recall"], P["p_aware_nonrecall"], P["RR"]
    def pw(n, rr):
        hit = 0
        for _ in range(P["reps"]):
            r = rng.random(n) < pr; a = rng.random(n) < np.where(r, pa * rr, pa)
            tab = [[int(np.sum(r & a)), int(np.sum(r & ~a))], [int(np.sum(~r & a)), int(np.sum(~r & ~a))]]
            hit += (stats.fisher_exact(tab)[1] < 0.05) if (tab[0][0] + tab[1][0]) > 0 else 0
        return hit / P["reps"]
    out = {str(n): pw(n, RR) for n in P["N_grid"]}; fpr = pw(N, 1.0)
    exp_aware = N * (pr * pa * RR + (1 - pr) * pa)
    tol = 0.05 + 3 * np.sqrt(0.05 * 0.95 / P["reps"])
    c = [chk("V1", f"RR = 1: false-positive rate of the Fisher test <= 0.05 + 3 Monte Carlo SE = {tol:.4f} (the exact test is conservative)", fpr, fpr <= tol),
         chk("H1", f"N = {N}, recall {pr:.0%}, awareness {pa:.1%}: power to detect RR = {RR} is < 0.5", out[str(N)], out[str(N)] < 0.5, "hypothesis"),
         chk("R1", "power by N; expected number of aware patients at the test N", [out, exp_aware], True, "reporting")]
    return dict(power_by_N=out, expected_aware=exp_aware), c

def recall_gap(P, rng):
    """K32: clinical recall rates are typically 3-8%, experimental often 40-80%; immediate interviews give higher recall (about
    10%) than interviews delayed >= 24 h (about 6%). If the delay effect is exponential forgetting with the implied 24-h retention,
    what share of the clinical-experimental gap can assessment timing explain? (Deterministic arithmetic; cross-study figures.)"""
    ret = P["recall_delayed"] / P["recall_immediate"]
    clinical_if_immediate = P["clinical_typical"] / ret
    gap = P["experimental_typical"] - P["clinical_typical"]; explained = (clinical_if_immediate - P["clinical_typical"]) / gap
    sim = float(np.mean(rng.random(2000000) < P["recall_immediate"] * ret))
    c = [chk("V1", "simulated delayed recall within 0.001 of immediate * retention", [sim, P["recall_delayed"]], abs(sim - P["recall_delayed"]) <= 0.001),
         chk("H1", "assessment timing alone explains < 20% of the clinical-experimental gap", float(explained), explained < 0.2, "hypothesis"),
         chk("R1", "implied 24-h retention; clinical recall if all interviews were immediate", [float(ret), float(clinical_if_immediate)], True, "reporting")]
    return dict(retention_24h=float(ret), clinical_if_immediate=float(clinical_if_immediate), share_gap_explained=float(explained)), c

def chisq_3group(P, rng):
    """K47: preference never to limit life-sustaining treatment in three vignette groups (47%, 63%, 67%; p = .052; 360 neurologists).
    Power of a chi-square test with n per group at these proportions; Monte Carlo and analytic (noncentral chi-square)."""
    p = np.array(P["props"]); n = P["n_per_group"]; out = {}
    def an_pow(m):
        pbar = p.mean(); lam = m * np.sum((p - pbar) ** 2) / (pbar * (1 - pbar)); cr = stats.chi2.ppf(0.95, 2); return float(stats.ncx2.sf(cr, 2, lam))
    hits = 0
    for _ in range(P["reps"]):
        k = rng.binomial(n, p); tab = np.array([k, n - k]); hits += stats.chi2_contingency(tab, correction=False)[1] < 0.05
    mc = hits / P["reps"]; out = {str(m): an_pow(m) for m in P["n_grid"]}
    c = [chk("V1", "Monte Carlo power within 0.03 of the noncentral chi-square approximation", [mc, an_pow(n)], abs(mc - an_pow(n)) <= 0.03),
         chk("H1", f"n = {n} per group: power at the observed proportions is < 0.8 (so p = .052 is expected often even if the differences are real)", mc, mc < 0.8, "hypothesis"),
         chk("R1", "analytic power by n per group", out, True, "reporting")]
    return dict(power_mc=mc, power_by_n=out), c



# ---------------- Track Cycle D (x12) kinds ----------------
def _jzs1(t, n, r=0.707):
    """Default one-sample/paired JZS Bayes factor BF10 (Rouder et al. 2009)."""
    nu = n - 1
    f = lambda g: (1 + n * g) ** -0.5 * (1 + t ** 2 / ((1 + n * g) * nu)) ** (-(nu + 1) / 2) * r / np.sqrt(2 * np.pi) * g ** -1.5 * np.exp(-r ** 2 / (2 * g))
    from scipy import integrate
    return integrate.quad(f, 0, np.inf, limit=200)[0] / (1 + t ** 2 / nu) ** (-(nu + 1) / 2)

def bf_sequential(P, rng):
    """K59 sampling plan: Bayesian t-tests (Cauchy r = .707), collect until BF >= 10 for either hypothesis, minimum n_min and maximum n_max
    sessions. Simulated per-session effects d (ILLUSTRATIVE); one-sample test across sessions. How often does the plan end with strong
    evidence, and how often is that evidence misleading?"""
    out = {}
    for d in P["d_grid"]:
        res = []
        for _ in range(P["reps"]):
            x = rng.normal(d, 1, P["n_max"]); verdict = "inconclusive"
            for n in range(P["n_min"], P["n_max"] + 1):
                s = x[:n]; t = s.mean() / (s.std(ddof=1) / np.sqrt(n)); b = _jzs1(t, n)
                if b >= P["bound"]: verdict = "H1"; break
                if b <= 1 / P["bound"]: verdict = "H0"; break
            res.append(verdict)
        res = np.array(res); out[str(d)] = {v: float(np.mean(res == v)) for v in ("H1", "H0", "inconclusive")}
    c = [chk("V1", "with d = 0, strong evidence for H1 (misleading) occurs in <= 5% of runs", out["0.0"]["H1"], out["0.0"]["H1"] <= 0.05),
         chk("H1", f"with d = 0 and at most {P['n_max']} sessions, the plan ends inconclusive in >= {P['h1']:.0%} of runs (BF >= 10 for the null needs many sessions)", out["0.0"]["inconclusive"], out["0.0"]["inconclusive"] >= P["h1"], "hypothesis"),
         chk("R1", "share ending H1 / H0 / inconclusive by true d", out, True, "reporting")]
    return out, c

def auxiliary_test(P, rng):
    """K58 (Duhem-Quine / Lakatos): a prediction is tested only if an auxiliary condition holds (e.g., neurons truly 'silent' yet able to fire).
    If the condition is verified with probability q, a failed prediction is shared between the theory and the auxiliary. Posterior of the theory
    after one failure, by q. Theory true -> prediction passes when the auxiliary holds; fails otherwise with prob f_aux."""
    out = {}
    for q in P["q_grid"]:
        pT, pw = P["prior"], P["power"]
        fail_T = (1 - q) * P["f_aux"]; fail_F = q * pw + (1 - q) * P["f_aux"]
        post = pT * fail_T / (pT * fail_T + (1 - pT) * fail_F); out[str(q)] = float(post)
    T = rng.random(P["reps"]) < P["prior"]; A = rng.random(P["reps"]) < P["q_test"]
    fail = np.where(A, np.where(T, False, rng.random(P["reps"]) < P["power"]), rng.random(P["reps"]) < P["f_aux"]); sim_post = float(T[fail].mean())
    c = [chk("V1", f"simulated posterior at q = {P['q_test']} within 0.01 of the analytic value", [sim_post, out[str(P['q_test'])]], abs(sim_post - out[str(P["q_test"])]) <= 0.01),
         chk("H1", f"with q = {P['q_test']} a failed prediction leaves the theory's posterior >= {P['h1']}", out[str(P["q_test"])], out[str(P["q_test"])] >= P["h1"], "hypothesis"),
         chk("R1", "posterior after one failure by q", out, True, "reporting")]
    return out, c

def implicit_guess(P, rng):
    """K60: 3 of 36 patients 'correctly guessed' the three fruit names presented during deep hypothermic circulatory arrest. Is 3/36 above chance?
    Depends on the unknown chance rate of guessing all three; grid over fruit-pool sizes (ILLUSTRATIVE; unordered guesses of 3 from a pool)."""
    from math import comb
    out = {}
    for pool in P["pools"]:
        p0 = 1 / comb(pool, 3); out[str(pool)] = dict(p0=p0, p_value=float(stats.binom.sf(P["k"] - 1, P["n"], p0)))
    p_cut = optimize.brentq(lambda p: stats.binom.sf(P["k"] - 1, P["n"], p) - 0.05, 1e-6, 0.5)
    sims = rng.binomial(P["n"], p_cut, P["reps"]); emp = float(np.mean(sims >= P["k"]))
    c = [chk("V1", "simulated P(X >= k) at the cut-off chance rate within 0.005 of 0.05", emp, abs(emp - 0.05) <= 0.005),
         chk("H1", f"3/36 is significant at .05 only if the chance rate is below {P['h1']}", float(p_cut), p_cut < P["h1"], "hypothesis"),
         chk("R1", "chance-rate cut-off; p by pool size", [float(p_cut), out], True, "reporting")]
    return dict(p_cut=float(p_cut), by_pool=out), c

def small_ci(P, rng):
    """K60: usable EEG in 9/36; delta waves during arrest in 3/9; explicit recall 0/35; other recalled memories 3/35. Wilson 95% intervals
    and simulated coverage at the observed rate."""
    def wil(k, n):
        z = 1.959964; p = k / n; c0 = (p + z * z / (2 * n)) / (1 + z * z / n); h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n); return [float(c0 - h), float(c0 + h)]
    out = {k: wil(*v) for k, v in P["counts"].items()}
    k0, n0 = P["counts"][P["focus"]]; p = k0 / n0; ks = rng.binomial(n0, p, P["reps"]); cov = float(np.mean([wil(k, n0)[0] <= p <= wil(k, n0)[1] for k in ks]))
    w = out[P["focus"]][1] - out[P["focus"]][0]
    c = [chk("V1", "Wilson interval coverage at the observed rate >= 0.90 (simulation)", cov, cov >= 0.90),
         chk("H1", f"the 95% interval for '{P['focus']}' is wider than {P['h1']} (too few usable recordings to estimate prevalence)", float(w), w > P["h1"], "hypothesis"),
         chk("R1", "Wilson intervals", out, True, "reporting")]
    return out, c


KINDS = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_') and k not in ('chk','power_t1','pow2') and getattr(v,'__module__',None)=='__main__'}

if __name__ == "__main__":
    P, H, t0 = R.start(sys.argv[1]); rng = np.random.default_rng(P["seed"])
    res, checks = KINDS[P["kind"]](P, rng); R.finish(H, P, res, checks, t0)
