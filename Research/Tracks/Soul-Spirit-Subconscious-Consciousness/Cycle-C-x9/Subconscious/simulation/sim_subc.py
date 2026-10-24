"""SIM-SUBC: Subconscious topic simulations (track cycles A-C). Usage: python sim_subc.py iter-<k>  (from Subconscious/simulation/)."""
import os, sys, numpy as np
from scipy import stats
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
import track_runner as R
chk = R.chk

def power_t1(n, dz, alpha):
    df = n - 1; nc = dz * np.sqrt(n); tc = stats.t.ppf(1 - alpha / 2, df)
    return float(1 - stats.nct.cdf(tc, df, nc) + stats.nct.cdf(-tc, df, nc))

def awareness_power(P, rng):
    dz, a = P["dz"], P["alpha"]
    an = {n: power_t1(n, dz, a) for n in P["n_list"]}
    sim = {}
    for n in P["n_list"]:
        x = rng.normal(dz, 1, size=(P["reps"], n)); t = x.mean(1) / (x.std(1, ddof=1) / np.sqrt(n))
        sim[n] = float(np.mean(np.abs(t) > stats.t.ppf(1 - a / 2, n - 1)))
    n80 = next(n for n in range(5, 400) if power_t1(n, dz, a) >= 0.8)
    # literatures of k tests at median n: fixed-effect pooled dz CI excludes 0?
    k, n = P["n_tests"], P["n_median"]; det = 0; nsig = []
    for _ in range(P["lit_reps"]):
        x = rng.normal(dz, 1, size=(k, n)); d = x.mean(1) / x.std(1, ddof=1)
        se = np.sqrt(1 / n + d ** 2 / (2 * n)); w = 1 / se ** 2; m = np.sum(w * d) / w.sum(); lo = m - 1.96 / np.sqrt(w.sum())
        det += lo > 0; t = d * np.sqrt(n); nsig.append(np.mean(np.abs(t) > stats.t.ppf(1 - a / 2, n - 1)))
    res = dict(analytic_power=an, simulated_power=sim, n80_two_tailed=n80, literature_detect_rate=det / P["lit_reps"],
               mean_share_significant_in_literature=float(np.mean(nsig)))
    n0 = P["n_median"]
    c = [chk("V1", f"analytic power at n={n0}, dz={dz} within 0.02 of K09's ~0.21", an[n0], abs(an[n0] - 0.21) <= 0.02),
         chk("V2", "simulated power within 0.015 of analytic for every n", {n: round(sim[n] - an[n], 4) for n in an}, all(abs(sim[n] - an[n]) <= 0.015 for n in an)),
         chk("V3", "n for 80% power (two-tailed) within 2 of K09's 84", n80, abs(n80 - 84) <= 2),
         chk("H1", f"at n={n0} at least 75% of awareness tests are non-significant although awareness is real", 1 - an[n0], 1 - an[n0] >= 0.75, "hypothesis"),
         chk("H2", f"pooling {k} such tests detects awareness (CI excludes 0) in >=95% of simulated literatures", det / P["lit_reps"], det / P["lit_reps"] >= 0.95, "hypothesis")]
    return res, c

def posthoc_unaware(P, rng):
    """Latent conscious knowledge k ~ N(mu, 1); awareness score aw = mu + sqrt(r)(k - mu) + sqrt(1 - r) e (chance level = 0);
    priming effect = b k + noise, i.e. ALL priming is carried by conscious knowledge. Select 'unaware' = aw < cut, test effect > 0."""
    mu, r, N = P["mu"], P["reliability"], P["N"]; out = {}
    for b in P["b_list"]:
        s = 0; mk = []; ma = []
        for _ in range(P["reps"]):
            k = rng.normal(mu, 1, N); aw = mu + np.sqrt(r) * (k - mu) + np.sqrt(1 - r) * rng.normal(0, 1, N)
            eff = b * k + rng.normal(0, 1, N); sel = aw < P["cut"]
            tt = stats.ttest_1samp(eff[sel], 0); s += (tt.pvalue / 2 < P["alpha"]) and eff[sel].mean() > 0
            mk.append(k[sel].mean()); ma.append(aw[sel].mean())
        out[str(b)] = dict(rate_significant=s / P["reps"], mean_true_knowledge_selected=float(np.mean(mk)), mean_awareness_score_selected=float(np.mean(ma)))
    bmax = str(P["b_list"][-1])
    res = dict(by_b=out)
    c = [chk("V1", "with b = 0 (effect unrelated to knowledge) the selected subgroup shows a significant positive effect at about alpha (<= 0.08)", out["0.0"]["rate_significant"], out["0.0"]["rate_significant"] <= 0.08),
         chk("H1", f"with ALL priming carried by conscious knowledge (b = {bmax}) and awareness measured with reliability {r}, the post-hoc 'unaware' subgroup (awareness score below chance) still shows a significant positive priming effect in >= 50% of studies",
             out[bmax]["rate_significant"], out[bmax]["rate_significant"] >= 0.5, "hypothesis"),
         chk("R1", "mean TRUE knowledge of the selected 'unaware' subgroup (latent units; > 0 means aware on average)", {b: round(v["mean_true_knowledge_selected"], 3) for b, v in out.items()}, True, "reporting")]
    return res, c

def dream_sampling(P, rng):
    S, M, Rn, s, g = P["subjects"], P["memories"], P["reactivated"], P["dreamed"], P["gain"]
    sp1 = sp2 = 0; diffs1 = []; diffs2 = []
    for _ in range(P["reps"]):
        d1 = []; d2 = []
        for _ in range(S):
            base = rng.normal(0, 1, M); react = np.zeros(M, bool); react[rng.choice(M, Rn, replace=False)] = True
            dream = np.zeros(M, bool); dream[rng.choice(np.where(react)[0], s, replace=False)] = True
            recall = base + g * react + rng.normal(0, P["noise"], M)
            d1.append(recall[dream].mean() - recall[~dream].mean()); d2.append(recall[dream].mean() - recall[react & ~dream].mean())
        p1 = stats.ttest_1samp(d1, 0).pvalue; p2 = stats.ttest_1samp(d2, 0).pvalue
        sp1 += p1 < 0.05; sp2 += p2 < 0.05; diffs1.append(np.mean(d1)); diffs2.append(np.mean(d2))
    res = dict(dreamed_vs_all_other=dict(rate_significant=sp1 / P["reps"], mean_diff=float(np.mean(diffs1))),
               dreamed_vs_reactivated_not_dreamed=dict(rate_significant=sp2 / P["reps"], mean_diff=float(np.mean(diffs2))))
    exp1 = g * (1 - (Rn - s) / (M - s))
    c = [chk("V1", f"mean dreamed-minus-other difference within 0.03 of analytic g*(1-(R-s)/(M-s)) = {exp1:.4f}", float(np.mean(diffs1)), abs(np.mean(diffs1) - exp1) <= 0.03),
         chk("H1", "dreamed memories are recalled better than all non-dreamed memories in >= 80% of simulated studies, although dreaming has no causal role in the model", sp1 / P["reps"], sp1 / P["reps"] >= 0.8, "hypothesis"),
         chk("H2", "against reactivated-but-not-dreamed memories the difference is significant at no more than 0.07 (about alpha)", sp2 / P["reps"], sp2 / P["reps"] <= 0.07, "hypothesis")]
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

def posthoc_unaware_nonneg(P, rng):
    """Redo of Cycle A iteration 2 with NON-NEGATIVE latent conscious knowledge k ~ Gamma(shape, mu/shape) (k = 0 means no knowledge).
    Awareness score aw = k + e, e ~ N(0, s_e) with s_e set so reliability = var(k)/var(aw) = r; chance level = 0.
    Priming = b k + noise (ALL priming carried by conscious knowledge). 'Unaware' = aw < cut (below chance)."""
    mu, r, N, sh = P["mu"], P["reliability"], P["N"], P["shape"]; vk = sh * (mu / sh) ** 2; se = np.sqrt(vk * (1 - r) / r); out = {}; kmin = np.inf
    for b in P["b_list"]:
        s = 0; mk = []; ns = []
        for _ in range(P["reps"]):
            k = rng.gamma(sh, mu / sh, N); kmin = min(kmin, k.min()); aw = k + rng.normal(0, se, N)
            eff = b * k + rng.normal(0, 1, N); sel = aw < P["cut"]
            if sel.sum() >= 3:
                tt = stats.ttest_1samp(eff[sel], 0); s += (tt.pvalue / 2 < P["alpha"]) and eff[sel].mean() > 0
            mk.append(k[sel].mean() if sel.any() else np.nan); ns.append(sel.sum())
        out[str(b)] = dict(rate_significant=s / P["reps"], mean_true_knowledge_selected=float(np.nanmean(mk)), mean_n_selected=float(np.mean(ns)))
    bmax = str(P["b_list"][-1])
    c = [chk("V1", "latent knowledge is non-negative in every simulated participant", float(kmin), kmin >= 0),
         chk("V2", "b = 0: selected-subgroup positive-significance rate <= 0.08", out["0.0"]["rate_significant"], out["0.0"]["rate_significant"] <= 0.08),
         chk("H1", f"b = {bmax}: the post-hoc 'unaware' subgroup (awareness score below chance) shows significant positive priming in >= 50% of studies although all priming is carried by conscious knowledge", out[bmax]["rate_significant"], out[bmax]["rate_significant"] >= 0.5, "hypothesis"),
         chk("R1", "mean TRUE knowledge of the selected subgroup (population mean = mu)", {b: round(v["mean_true_knowledge_selected"], 3) for b, v in out.items()}, True, "reporting")]
    return dict(by_b=out, population_mean_knowledge=mu, error_sd=float(se)), c

def prediction_interval(P, rng):
    """From a meta-analytic estimate, CI and prediction interval (K23), back out between-setting SD tau and the share of settings with a true effect <= 0."""
    g, (lo, hi), (plo, phi) = P["g"], P["ci"], P["pi"]; se = (hi - lo) / (2 * 1.96); hw = (phi - plo) / 2
    tau = float(np.sqrt(max(0, (hw / 1.96) ** 2 - se ** 2))); share = float(stats.norm.cdf(-g / tau)); simv = float(np.mean(rng.normal(g, tau, P["draws"]) <= 0))
    res = dict(se=se, tau=tau, share_true_effect_le_0=share, simulated_share=simv, share_true_effect_ge_0_2=float(1 - stats.norm.cdf((0.2 - g) / tau)))
    c = [chk("V1", "simulated share within 0.005 of analytic", [share, simv], abs(share - simv) <= 0.005),
         chk("H1", "the published interval implies that >= 10% of settings have a true priming effect <= 0", share, share >= 0.10, "hypothesis"),
         chk("R1", "implied between-setting SD tau", tau, True, "reporting")]
    return res, c

def dream_selection(P, rng):
    """Refinement of iteration 3 (Cycle A): dreams sample reactivated memories with probability proportional to exp(beta * encoding strength).
    Dreaming still has NO causal effect. Does 'dreamed > reactivated-but-not-dreamed' then appear?"""
    S, M, Rn, s, g = P["subjects"], P["memories"], P["reactivated"], P["dreamed"], P["gain"]; out = {}
    for beta in P["beta_list"]:
        sp = 0; md = []
        for _ in range(P["reps"]):
            d2 = []
            for _ in range(S):
                base = rng.normal(0, 1, M); ridx = rng.choice(M, Rn, replace=False); w = np.exp(beta * base[ridx]); w /= w.sum()
                didx = rng.choice(ridx, s, replace=False, p=w); react = np.zeros(M, bool); react[ridx] = True; dream = np.zeros(M, bool); dream[didx] = True
                recall = base + g * react + rng.normal(0, P["noise"], M); d2.append(recall[dream].mean() - recall[react & ~dream].mean())
            sp += stats.ttest_1samp(d2, 0).pvalue < 0.05; md.append(np.mean(d2))
        out[str(beta)] = dict(rate_significant=sp / P["reps"], mean_diff=float(np.mean(md)))
    bt = str(P["beta_test"])
    c = [chk("V1", "beta = 0 (uniform selection): dreamed vs reactivated-not-dreamed significant at <= 0.07", out["0.0"]["rate_significant"], out["0.0"]["rate_significant"] <= 0.07),
         chk("H1", f"beta = {bt}: dreamed > reactivated-not-dreamed significant in >= 80% of studies although dreams have no causal role", out[bt]["rate_significant"], out[bt]["rate_significant"] >= 0.8, "hypothesis"),
         chk("R1", "rate and mean difference by beta", out, True, "reporting")]
    return dict(by_beta=out), c

def _pow2(n, d, a=0.05):
    df = 2 * n - 2; nc = d * np.sqrt(n / 2); tc = stats.t.ppf(1 - a / 2, df)
    return float(1 - stats.nct.cdf(tc, df, nc) + stats.nct.cdf(-tc, df, nc))

def ute_mixed(P, rng):
    """K22 found an unconscious-thought effect in two of three experiments. With an illustrative n per condition, how often does a small true effect give >= 2 of 3 significant, and how often a mixed pattern?"""
    n, k = P["n_per_group"], P["k_exp"]; out = {}
    for d in P["d_grid"]:
        pw = _pow2(n, d); pmix = 1 - pw ** k - (1 - pw) ** k; pge2 = sum(stats.binom.pmf(j, k, pw) for j in range(2, k + 1))
        out[str(d)] = dict(power=pw, p_at_least_2_of_3=float(pge2), p_mixed=float(pmix))
    x = rng.normal(0.2, 1, (P["reps"], n)); y = rng.normal(0, 1, (P["reps"], n)); simp = float(np.mean(stats.ttest_ind(x, y, axis=1).pvalue < 0.05))
    c = [chk("V1", "simulated power at d = 0.2 within 0.015 of analytic", [simp, out["0.2"]["power"]], abs(simp - out["0.2"]["power"]) <= 0.015),
         chk("H1", "true d = 0.2: >= 2 of 3 experiments significant with probability >= 0.5", out["0.2"]["p_at_least_2_of_3"], out["0.2"]["p_at_least_2_of_3"] >= 0.5, "hypothesis"),
         chk("R1", "power, P(>=2 of 3) and P(mixed) by d", out, True, "reporting")]
    return dict(by_d=out, simulated_power_d02=simp), c

def objective_subjective(P, rng):
    """Single-process signal-detection toy: evidence x = s d/2 + N(0,1), s = +-1. Report 'seen' if |x| > c; discrimination = sign(x).
    There is NO separate unconscious route. Accuracy on 'unseen' trials?"""
    def acc_unseen(d, c):
        m = d / 2; num = stats.norm.cdf(c - m) - stats.norm.cdf(-m); den = stats.norm.cdf(c - m) - stats.norm.cdf(-c - m)
        return float(num / den), float(den)
    out = {}
    for d in P["d_grid"]:
        a, u = acc_unseen(d, P["c"]); out[str(d)] = dict(accuracy_unseen=a, share_unseen=u)
    d = P["d_test"]; s = rng.choice([-1, 1], P["trials"]); x = s * d / 2 + rng.normal(0, 1, P["trials"]); un = np.abs(x) < P["c"]
    sim_acc = float(np.mean(np.sign(x[un]) == s[un]))
    c = [chk("V1", "d' = 0: accuracy on unseen trials = 0.5 (analytic)", out["0.0"]["accuracy_unseen"], abs(out["0.0"]["accuracy_unseen"] - 0.5) < 1e-9),
         chk("V2", f"simulated unseen accuracy at d' = {d} within 0.01 of analytic", [sim_acc, out[str(d)]["accuracy_unseen"]], abs(sim_acc - out[str(d)]["accuracy_unseen"]) <= 0.01),
         chk("H1", f"d' = {d}, criterion {P['c']}: accuracy on subjectively 'unseen' trials >= 0.55 (would be read as unconscious perception)", out[str(d)]["accuracy_unseen"], out[str(d)]["accuracy_unseen"] >= 0.55, "hypothesis"),
         chk("R1", "share of trials reported unseen by d'", {k: round(v["share_unseen"], 3) for k, v in out.items()}, True, "reporting")]
    return dict(by_d=out, simulated_accuracy_unseen=sim_acc), c

# ---------------- Track Cycle C kinds ----------------
def pdp_dependence(P, rng):
    """Process-dissociation procedure (K33): Inclusion I = R + (1-R)F, Exclusion E = (1-R)F + c*R (c = crosstalk: recollected
    items that slip through in exclusion). Item-level R and F are probit-transformed bivariate normals with correlation rho.
    Estimates R^ = I - E, F^ = E / (1 - R^); bias = mean F^ - true mean F."""
    def one(rho, c):
        z = rng.multivariate_normal([0, 0], [[1, rho], [rho, 1]], P["items"])
        Ri = stats.norm.cdf(P["aR"] + P["s"] * z[:, 0]); Fi = stats.norm.cdf(P["aF"] + P["s"] * z[:, 1])
        I = np.mean(Ri + (1 - Ri) * Fi); E = np.mean((1 - Ri) * Fi + c * Ri); Rh = I - E; Fh = E / (1 - Rh)
        return dict(true_R=float(Ri.mean()), true_F=float(Fi.mean()), R_hat=float(Rh), F_hat=float(Fh), F_bias=float(Fh - Fi.mean()), R_bias=float(Rh - Ri.mean()))
    grid = {f"rho={r},c={c}": one(r, c) for r in P["rho_grid"] for c in P["c_grid"]}
    base = grid[f"rho=0.0,c=0.0"]; tk = f"rho={P['rho_test']},c={P['c_test']}"
    c = [chk("V1", "independence and no crosstalk (rho = 0, c = 0): |F bias| <= 0.01 (Monte Carlo tolerance)", base["F_bias"], abs(base["F_bias"]) <= 0.01),
         chk("H1", f"{tk}: |bias of the automatic (F) estimate| >= 0.05", grid[tk]["F_bias"], abs(grid[tk]["F_bias"]) >= 0.05, "hypothesis"),
         chk("R1", "F and R bias across the grid", {k: (round(v["F_bias"], 3), round(v["R_bias"], 3)) for k, v in grid.items()}, True, "reporting")]
    return dict(grid=grid), c

def _weib(x, a, b, lapse=0.0): return 0.5 + (0.5 - lapse) * (1 - np.exp(-(np.maximum(x, 0) / a) ** b))

def staircase_subliminal(P, rng):
    """Virtual observers with Weibull 2AFC psychometric functions (threshold a ~ U[a_lo, a_hi], slope b). The 'upper subliminal
    threshold' theta1 is the largest intensity with accuracy <= 0.5 + eps. A 1-up-2-down staircase on objective accuracy
    (Levitt 1971: converges near 70.7% correct) is run for `trials` trials; calibrated intensity = mean of the last 6 reversals."""
    accs, over = [], []
    for _ in range(P["observers"]):
        a = rng.uniform(P["a_lo"], P["a_hi"]); b = P["b"]; th1 = a * (-np.log(1 - P["eps"] / 0.5)) ** (1 / b)
        x, step, run, rev, last = P["x0"], P["step"], 0, [], None
        for t in range(P["trials"]):
            ok = rng.random() < _weib(x, a, b)
            if ok: run += 1
            if ok and run == 2: d, run = -1, 0
            elif not ok: d, run = +1, 0
            else: continue
            if last is not None and d != last: rev.append(x)
            last = d; x = max(0.0, x + d * step)
        xc = float(np.mean(rev[-6:])) if len(rev) >= 2 else x
        accs.append(_weib(xc, a, b)); over.append(xc / th1)
    accs = np.array(accs); res = dict(mean_accuracy_at_calibrated=float(accs.mean()), share_acc_ge_060=float(np.mean(accs >= 0.6)), median_ratio_to_theta1=float(np.median(over)))
    c = [chk("V1", "analytic: accuracy at theta1 equals 0.5 + eps (to 1e-9)", float(_weib(1.0 * (-np.log(1 - P['eps'] / 0.5)) ** (1 / P['b']), 1.0, P['b'])), abs(_weib(1.0 * (-np.log(1 - P['eps'] / 0.5)) ** (1 / P['b']), 1.0, P['b']) - (0.5 + P['eps'])) < 1e-9),
         chk("H1", "a standard 1-up-2-down staircase lands at an intensity with objective accuracy >= 0.60 (i.e. not subliminal) for >= 80% of observers", res["share_acc_ge_060"], res["share_acc_ge_060"] >= 0.8, "hypothesis"),
         chk("R1", "median calibrated intensity / true upper subliminal threshold", res["median_ratio_to_theta1"], True, "reporting")]
    return res, c

def constant_stimuli_threshold(P, rng):
    """Method of constant stimuli with K34's design (9 levels, n_per trials each). Naive rule: the subliminal threshold is the highest
    level whose accuracy is NOT significantly above 0.5 (one-sided binomial, alpha). Compared with the true highest level whose
    accuracy is <= 0.5 + eps. Counts how often the naive rule picks a level ABOVE the true one (overestimation)."""
    lv = np.array(P["levels"], float); over, exact = 0, 0; diffs = []
    for _ in range(P["observers"]):
        a = rng.uniform(P["a_lo"], P["a_hi"]); p = _weib(lv, a, P["b"], P["lapse"])
        true_idx = int(np.max(np.where(p <= 0.5 + P["eps"])[0])) if np.any(p <= 0.5 + P["eps"]) else -1
        k = rng.binomial(P["n_per"], p); pv = stats.binom.sf(k - 1, P["n_per"], 0.5)
        ns = np.where(pv >= P["alpha"])[0]; naive = int(ns.max()) if len(ns) else -1
        diffs.append(naive - true_idx); over += naive > true_idx; exact += naive == true_idx
    n = P["observers"]; res = dict(share_overestimate=over / n, share_exact=exact / n, mean_level_difference=float(np.mean(diffs)))
    pchk = float(stats.binom.sf(P["n_per"] // 2 - 1, P["n_per"], 0.5))
    c = [chk("V1", "binomial sf sanity: P(X >= n/2 | p = .5) between 0.5 and 0.6 for n = n_per", pchk, 0.5 <= pchk <= 0.6),
         chk("H1", "the naive 'not significantly above chance' rule overestimates the subliminal threshold for >= 50% of observers", res["share_overestimate"], res["share_overestimate"] >= 0.5, "hypothesis"),
         chk("R1", "share exact, mean level difference", [res["share_exact"], res["mean_level_difference"]], True, "reporting")]
    return res, c

def country_power(P, rng):
    """Power of a country-level OLS slope test given the reported slope b and its SE (K35: b = 0.65, SE = 0.74, 38 countries).
    Analytic (normal approximation) plus Monte Carlo with n countries, x SD sx and residual SD chosen to reproduce the SE."""
    z = stats.norm.ppf(1 - P["alpha"] / 2); lam = abs(P["b"]) / P["se"]
    an = float(stats.norm.cdf(lam - z) + stats.norm.cdf(-lam - z))
    n = P["n_countries"]; sx = P["sx"]; sres = P["se"] * sx * np.sqrt(n - 1); hits = 0
    for _ in range(P["reps"]):
        x = rng.normal(0, sx, n); y = P["b"] * x + rng.normal(0, sres, n)
        r = stats.linregress(x, y); hits += r.pvalue < P["alpha"]
    mc = hits / P["reps"]
    need = {str(m): float(stats.norm.cdf(lam * np.sqrt(m / n) - z) + stats.norm.cdf(-lam * np.sqrt(m / n) - z)) for m in P["n_grid"]}
    c = [chk("V1", "Monte Carlo power within 0.03 of the analytic normal approximation (t vs z and sampled x)", [mc, an], abs(mc - an) <= 0.03),
         chk("H1", f"power to detect a true slope of {P['b']} with this precision is < 0.5", an, an < 0.5, "hypothesis"),
         chk("R1", "analytic power if more countries had data (same per-country precision)", need, True, "reporting")]
    return dict(power_analytic=an, power_mc=mc, by_n=need), c

def cles(P, rng):
    """Common-language effect size for a standardized slope: r ~ b / SD_y (ignoring covariates); probability that, of two random
    people, the one with higher free will belief is also more punitive = 0.5 + arcsin(r)/pi (bivariate normal)."""
    r = P["b"] / P["sd_y"]; an = 0.5 + np.arcsin(r) / np.pi
    x = rng.multivariate_normal([0, 0], [[1, r], [r, 1]], P["pairs"] * 2)
    a, b = x[: P["pairs"]], x[P["pairs"]:]
    mc = float(np.mean(np.sign(a[:, 0] - b[:, 0]) == np.sign(a[:, 1] - b[:, 1])))
    c = [chk("V1", "Monte Carlo concordance within 0.005 of analytic", [mc, float(an)], abs(mc - an) <= 0.005),
         chk("H1", "the individual-level association is small: concordance probability < 0.60", float(an), an < 0.6, "hypothesis"),
         chk("R1", "approximate r and share of variance", [float(r), float(r * r)], True, "reporting")]
    return dict(r=float(r), concordance_analytic=float(an), concordance_mc=mc), c

def _learn(rng, trials, noise, lr):
    w = 0.0; traj = []
    for t in range(trials):
        u = rng.normal(); i = u + rng.normal(0, noise); act = float(u > 0)
        pred = 1 / (1 + np.exp(-np.clip(w * i, -50, 50))); w += lr * (act - pred) * i
        if (t + 1) % max(1, trials // 10) == 0: traj.append(float(w))
    u = rng.normal(size=100000); i = u + rng.normal(0, noise, u.size)
    pr = float(np.mean(((1 / (1 + np.exp(-np.clip(w * i, -50, 50)))) > 0.5) == (u > 0)))
    return w, pr, traj

def superstitious_conditioning(P, rng):
    """Toy of K36's HYPOTHESIS (not a test of it). On each trial a prior neural cause u ~ N(0,1) determines the action (act if u > 0).
    A felt 'intention' i = u + noise precedes the action. A delta-rule learner associates felt intention with action outcome.
    The intention has NO causal role (the action is fixed by u), yet the learned association grows: 'I intended it, so I did it'."""
    w, pr, traj = _learn(rng, P["trials"], P["noise"], P["lr"])
    w0, pr0, _ = _learn(rng, P["trials"], P["noise_null"], P["lr"])
    c = [chk("V1", f"control: when the felt intention carries no information about the cause (noise {P['noise_null']}), the learned association predicts the action at chance (within 0.03 of 0.5)", pr0, abs(pr0 - 0.5) <= 0.03),
         chk("H1", f"after {P['trials']} trials the learned intention->action association predicts the action on >= 80% of trials although the intention is causally idle", pr, pr >= 0.8, "hypothesis"),
         chk("R1", "association weight trajectory", traj, True, "reporting")]
    return dict(final_w=float(w), predictive_accuracy=pr, control_accuracy=pr0, trajectory=traj), c

KINDS = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_') and k not in ('chk','power_t1','pow2') and getattr(v,'__module__',None)=='__main__'}

if __name__ == "__main__":
    P, H, t0 = R.start(sys.argv[1]); rng = np.random.default_rng(P["seed"])
    res, checks = KINDS[P["kind"]](P, rng); R.finish(H, P, res, checks, t0)
