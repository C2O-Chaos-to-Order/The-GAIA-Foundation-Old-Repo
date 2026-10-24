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

KINDS = {k: v for k, v in globals().items() if callable(v) and k in ("awareness_power", "posthoc_unaware", "dream_sampling")}

if __name__ == "__main__":
    P, H, t0 = R.start(sys.argv[1]); rng = np.random.default_rng(P["seed"])
    res, checks = KINDS[P["kind"]](P, rng); R.finish(H, P, res, checks, t0)
