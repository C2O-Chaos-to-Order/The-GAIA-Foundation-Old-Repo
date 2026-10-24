"""SIM-R4-C2: mediation analysis under the conditions flagged by the literature (synthetic data only).
Motivation: Li et al. 2016 (S12, full text) report proportions mediated for religious-service attendance -> mortality
(e.g. depressive symptoms 11%, smoking 22%, optimism 9%, social integration 23%; risk-difference scale) and state that the methods
'assume baseline covariates suffice to control for exposure-outcome, mediator-outcome, and exposure-mediator confounding'.
W09 (Daniel et al. 2015): with several causally ordered mediators 'there are many ways in which decomposition can be done'.
We test, on synthetic data with known truth, how these assumptions and choices move the estimates. Nothing here re-analyses S12's data."""
import sys, os, json, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools")); import runner as R
def ols(y, *xs):
    X = np.column_stack([np.ones(len(y))] + list(xs)); b, *_ = np.linalg.lstsq(X, y, rcond=None)
    r = y - X @ b; s2 = r @ r/(len(y)-X.shape[1]); V = s2*np.linalg.inv(X.T @ X); return b, np.sqrt(np.diag(V))
def logit_fit(y, *xs, it=50):
    X = np.column_stack([np.ones(len(y))] + list(xs)); b = np.zeros(X.shape[1])
    for _ in range(it):
        p = 1/(1+np.exp(-X @ b)); W = p*(1-p); b = b + np.linalg.solve(X.T @ (X*W[:, None]), X.T @ (y-p))
    return b
def gen(rng, n, g):
    L = rng.standard_normal(n); U = rng.standard_normal(n)
    A = (rng.random(n) < 1/(1+np.exp(-(g["aL"]*L)))).astype(float)
    M1 = g["a1"]*A + g["lm"]*L + g["u_m"]*U + rng.standard_normal(n)
    M2 = g["a2"]*A + g["c12"]*M1 + g["lm"]*L + rng.standard_normal(n)
    Y = g["c"]*A + g["b1"]*M1 + g["b2"]*M2 + g["ly"]*L + g["u_y"]*U + rng.standard_normal(n)
    return L, U, A, M1, M2, Y
def truth(g):
    """Linear SEM, no interactions: total = c + a1*b1 + a1*c12*b2 + a2*b2; indirect via M1 (all paths through M1) = a1*(b1 + c12*b2)."""
    tot = g["c"] + g["a1"]*g["b1"] + g["a1"]*g["c12"]*g["b2"] + g["a2"]*g["b2"]
    return dict(total=tot, ie_M1=g["a1"]*(g["b1"]+g["c12"]*g["b2"]), ie_M2_direct_path=g["a2"]*g["b2"], ie_joint=tot-g["c"], de=g["c"])
def single_med(L, A, M, Y):
    a, sa = ols(M, A, L); b, sb = ols(Y, A, M, L); tot, _ = ols(Y, A, L)
    ie = a[1]*b[2]; se = np.sqrt((a[1]*sb[2])**2 + (b[2]*sa[1])**2)
    return dict(ie=ie, se=se, total=tot[1], pm=ie/tot[1])
def main():
    P, prev, H = R.start(sys.argv[1]); t0 = R.now(); X = P["experiments"]; G = P["gen"]; res = {}; chk = []
    if prev: res["carried_from_prev"] = {k: prev[k] for k in P.get("carry", []) if k in prev}
    rng = np.random.default_rng(P["seed"])
    if "no_confounding" in X:
        e = X["no_confounding"]; g = dict(G, u_m=0.0, u_y=0.0, a2=0.0, b2=0.0, c12=0.0); T = truth(g)
        L, U, A, M1, M2, Y = gen(rng, e["n"], g); s = single_med(L, A, M1, Y)
        res["no_confounding"] = dict(truth=T, est=s)
        chk.append(R.chk("V1", "no unmeasured confounding: product-of-coefficients estimate within 3 SE of the true indirect effect", [s["ie"], T["ie_M1"], s["se"]], abs(s["ie"]-T["ie_M1"]) <= 3*s["se"]))
        chk.append(R.chk("V1b", "proportion mediated within 0.02 of truth", [s["pm"], T["ie_M1"]/T["total"]], abs(s["pm"]-T["ie_M1"]/T["total"]) <= 0.02))
    if "mediator_outcome_confounding" in X:
        e = X["mediator_outcome_confounding"]; out = []
        for u in e["u"]:
            g = dict(G, u_m=u, u_y=u, a2=0.0, b2=0.0, c12=0.0); T = truth(g); L, U, A, M1, M2, Y = gen(rng, e["n"], g); s = single_med(L, A, M1, Y)
            # linear-SEM bias formula for b: cov(U,M|A,L)/var(M|A,L) * u_y ; exact correction using the known U path
            corr = ols(Y - g["u_y"]*U, A, M1, L)[0][2]*ols(M1, A, L)[0][1]
            out.append(dict(u=u, pm_true=T["ie_M1"]/T["total"], pm_est=s["pm"], rel_bias_pm=(s["pm"]-T["ie_M1"]/T["total"])/(T["ie_M1"]/T["total"]), ie_corrected=corr, ie_true=T["ie_M1"]))
        res["mediator_outcome_confounding"] = out
        chk.append(R.chk("V2", "removing the known U contribution recovers the true indirect effect (|diff| < 0.02) in every setting", [(o["u"], o["ie_corrected"], o["ie_true"]) for o in out], all(abs(o["ie_corrected"]-o["ie_true"]) < 0.02 for o in out)))
        mod = [o for o in out if o["u"] == e["moderate_u"]][0]
        chk.append(R.chk("H1", f"moderate unmeasured M-Y confounding (u = {e['moderate_u']} on both paths) biases the proportion mediated by >= 25% (relative)", mod["rel_bias_pm"], abs(mod["rel_bias_pm"]) >= 0.25, kind="hypothesis"))
        res["u_needed_for_25pct_bias"] = next((o["u"] for o in out if abs(o["rel_bias_pm"]) >= 0.25), None)
    if "multiple_mediators" in X:
        e = X["multiple_mediators"]; out = []
        for c12 in e["c12"]:
            g = dict(G, u_m=0.0, u_y=0.0, c12=c12); T = truth(g); L, U, A, M1, M2, Y = gen(rng, e["n"], g)
            s1 = single_med(L, A, M1, Y); s2 = single_med(L, A, M2, Y)
            bj, _ = ols(Y, A, M1, M2, L); tot = ols(Y, A, L)[0][1]; pm_joint = (tot-bj[1])/tot
            out.append(dict(c12=c12, pm_M1_alone=s1["pm"], pm_M2_alone=s2["pm"], sum_single=s1["pm"]+s2["pm"], pm_joint=pm_joint, pm_joint_true=T["ie_joint"]/T["total"]))
        res["multiple_mediators"] = out
        z = [o for o in out if o["c12"] == 0][0]
        chk.append(R.chk("V3", "independent mediators: sum of single-mediator PMs equals the joint PM within 0.02", [z["sum_single"], z["pm_joint"]], abs(z["sum_single"]-z["pm_joint"]) <= 0.02))
        chk.append(R.chk("V3b", "joint PM (difference method) within 0.02 of truth for every c12", [(o["c12"], o["pm_joint"], o["pm_joint_true"]) for o in out], all(abs(o["pm_joint"]-o["pm_joint_true"]) <= 0.02 for o in out)))
        hi = [o for o in out if o["c12"] == e["test_c12"]][0]
        chk.append(R.chk("H2", f"causally ordered mediators (M1 -> M2, c12 = {e['test_c12']}): summing single-mediator PMs overstates the joint PM by >= 0.10", [hi["sum_single"], hi["pm_joint"]], hi["sum_single"]-hi["pm_joint"] >= 0.10, kind="hypothesis"))
        res["s12_sum_of_reported_pms"] = e.get("s12_reported_pms_sum")
    if "binary_outcome_scale" in X:
        e = X["binary_outcome_scale"]; out = []
        for b0 in e["intercepts"]:
            n = e["n"]; L = rng.standard_normal(n); A = (rng.random(n) < 0.5).astype(float); M = G["a1"]*A + rng.standard_normal(n)
            lin = lambda a, m: b0 + e["c"]*a + e["b"]*m + 0.3*L
            p = lambda a, m: 1/(1+np.exp(-lin(a, m)))
            M0 = M - G["a1"]*A; M1_ = M0 + G["a1"]
            r11 = p(1, M1_).mean(); r10 = p(1, M0).mean(); r00 = p(0, M0).mean()
            pm_rd = (r11-r10)/(r11-r00); Y = (rng.random(n) < p(A, M)).astype(float)
            bt = logit_fit(Y, A, L); bd = logit_fit(Y, A, M, L); pm_or = (bt[1]-bd[1])/bt[1]
            out.append(dict(intercept=b0, prevalence=float(Y.mean()), pm_rd_true=pm_rd, pm_or_difference_method=pm_or, gap=pm_or-pm_rd))
        res["binary_outcome_scale"] = out
        rare = [o for o in out if o["prevalence"] < 0.1]; common = [o for o in out if o["prevalence"] >= 0.3]
        chk.append(R.chk("H3", "PM on the odds-ratio 'difference' scale departs from the risk-difference PM by >= 0.05 when the outcome is common (>= 30%)", [(round(o["prevalence"], 3), o["gap"]) for o in common], all(abs(o["gap"]) >= 0.05 for o in common), kind="hypothesis"))
        chk.append(R.chk("H3b", "and by <= 0.05 when the outcome is rare (< 10%)", [(round(o["prevalence"], 3), o["gap"]) for o in rare], all(abs(o["gap"]) <= 0.05 for o in rare), kind="hypothesis"))
    if "coverage" in X:
        e = X["coverage"]; out = []
        for u in e["u"]:
            g = dict(G, u_m=u, u_y=u, a2=0.0, b2=0.0, c12=0.0); T = truth(g); hits = 0
            for _ in range(e["reps"]):
                L, U, A, M1, M2, Y = gen(rng, e["n"], g); s = single_med(L, A, M1, Y); hits += abs(s["ie"]-T["ie_M1"]) <= 1.96*s["se"]
            out.append(dict(u=u, coverage=hits/e["reps"]))
        res["coverage"] = out; c0 = out[0]["coverage"]
        chk.append(R.chk("V4", f"no confounding: Sobel 95% CI coverage within [0.90, 0.99] over {e['reps']} replicates", c0, 0.90 <= c0 <= 0.99))
        mod = [o for o in out if o["u"] == e["moderate_u"]][0]["coverage"]
        chk.append(R.chk("H4", f"moderate confounding (u = {e['moderate_u']}) drives coverage below 0.5 at n = {e['n']}", mod, mod < 0.5, kind="hypothesis"))
    R.finish(H, P, res, chk, t0)
if __name__ == "__main__": main()
