"""SIM-R4-C3: sensitivity analysis for unmeasured confounding calibrated to S12 (carried item 'R4 sensitivity analysis calibrated to S12').
S12 (Li et al. 2016, Nurses' Health Study, 74,534 women, 13,537 deaths) reports HR 0.67 (95% CI 0.62-0.71) for attending religious services
more than once per week vs never, and E-values 2.35 (estimate) and 2.16 (CI limit). S14 (VanderWeele & Ding 2017) gives the E-value
formula and, for a common outcome (> 15%), the approximation RR ~ (1-0.5^sqrt(HR))/(1-0.5^sqrt(1/HR)). Everything here is arithmetic on
published numbers plus synthetic cohorts; no individual data are used. These analyses bound bias; they cannot show a causal effect,
and they say nothing about spiritual meaning (Philosophical/Spiritual framing is kept separate)."""
import sys, os, json, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "tools")); import runner as R
def evalue(rr):
    rr = 1/rr if rr < 1 else rr; return rr + np.sqrt(rr*(rr-1))
def hr_to_rr_common(hr): return (1-0.5**np.sqrt(hr))/(1-0.5**np.sqrt(1/hr))
def bias_bound(a, b): return a*b/(a+b-1)
def bias_binary(p1, p0, rr_ud): return (p1*(rr_ud-1)+1)/(p0*(rr_ud-1)+1)
def cohort(rng, n, pA, p_u1, p_u0, base, rr_ud, rr_true=1.0):
    A = rng.random(n) < pA; U = np.where(A, rng.random(n) < p_u1, rng.random(n) < p_u0)
    risk = np.clip(base*rr_ud**U*rr_true**A, 0, 1); Y = rng.random(n) < risk
    return Y[A].mean()/Y[~A].mean()
def main():
    P, prev, H = R.start(sys.argv[1]); t0 = R.now(); X = P["experiments"]; s = P["S12"]; res = {}; chk = []
    p_death = s["deaths"]/s["n"]; res["S12_cumulative_mortality"] = p_death
    if "reproduce" in X:
        e1, e2 = evalue(s["hr"]), evalue(s["hr_ci_upper"]); res["evalue_rare_formula"] = [e1, e2]
        chk.append(R.chk("V1", "E-value formula applied to HR 0.67 and CI limit 0.71 reproduces S12's 2.35 and 2.16 (to 2 decimals)", [e1, e2], round(e1, 2) == s["reported_evalue"] and round(e2, 2) == s["reported_evalue_ci"]))
        E = evalue(1.7); chk.append(R.chk("V2", "bias bound B(E, E) equals the target ratio exactly (definition of the E-value)", [bias_bound(E, E), 1.7], abs(bias_bound(E, E)-1.7) < 1e-12))
        g = np.linspace(0.01, 1, 100); worst = max(bias_binary(1.0, p0, 2.0)/bias_bound(1/p0, 2.0) for p0 in g)
        chk.append(R.chk("V3", "binary-confounder bias with P(U|A=1)=1 attains the bound (ratio 1 within 1e-12)", worst, abs(worst-1) < 1e-12))
    if "common_outcome" in X:
        rr, rrc = hr_to_rr_common(s["hr"]), hr_to_rr_common(s["hr_ci_upper"]); e1, e2 = evalue(rr), evalue(rrc)
        res["common_outcome"] = dict(rr_point=rr, rr_ci=rrc, evalue_point=e1, evalue_ci=e2, cumulative_mortality=p_death)
        chk.append(R.chk("H2", "with S12's cumulative mortality (18% > 15%), S14's common-outcome approximation still gives an E-value >= 1.5 for the point estimate", [e1, e2], e1 >= 1.5, kind="hypothesis"))
        chk.append(R.chk("H2r", "report the drop from the reported (rare-outcome) E-value", [s["reported_evalue"], e1, s["reported_evalue_ci"], e2], True, kind="reporting"))
    if "cohort_check" in X:
        e = X["cohort_check"]; rng = np.random.default_rng(e["seed"]); rr = hr_to_rr_common(s["hr"]); E = evalue(rr)
        p0 = 1/E; base = e["base"]; obs = cohort(rng, e["n"], e["pA"], p0, 1.0, base, E)  # run 2 fix: confounder LESS common among attenders (run 1 had the arguments swapped)
        res["cohort_check"] = dict(E=E, observed_rr_under_null=obs, target=rr)
        chk.append(R.chk("H3", "a synthetic S12-sized cohort with NO true effect and one confounder of strength E on both sides reproduces the observed RR within 5%", [obs, rr], abs(obs-rr)/rr <= 0.05, kind="hypothesis"))
    if "tipping" in X:
        e = X["tipping"]; rr = hr_to_rr_common(s["hr"]); target = 1/rr; g = np.round(np.arange(e["lo"], e["hi"]+1e-9, e["step"]), 4); out = []
        for a in g:
            need = next((b for b in g if bias_bound(a, b) >= target), None); out.append(dict(rr_eu=float(a), min_rr_ud=(float(need) if need is not None else None)))
        res["tipping"] = out; o15 = [o for o in out if abs(o["rr_eu"]-1.5) < 1e-9][0]["min_rr_ud"]
        chk.append(R.chk("H4", "a confounder whose association with attendance is only 1.5-fold must be associated with mortality >= 3-fold to explain away the (common-outcome) estimate", o15, o15 is not None and o15 >= 3, kind="hypothesis"))
    if "health_selection" in X:
        e = X["health_selection"]; out = []
        for p1, p0, r in e["scenarios"]: out.append(dict(p_poorhealth_attenders=p1, p_poorhealth_never=p0, rr_death=r, observed_rr_under_null=1/bias_binary(p0, p1, r)))
        res["health_selection"] = out; rr = hr_to_rr_common(s["hr"]); ok = [o for o in out if o["observed_rr_under_null"] <= rr]
        chk.append(R.chk("H5", "at least one pre-declared 'healthy attender' scenario (residual poor health, beyond adjustment) alone produces an RR as low as S12's", [round(o["observed_rr_under_null"], 4) for o in out], len(ok) > 0, kind="hypothesis"))
    if "many_weak" in X:
        e = X["many_weak"]; rr = hr_to_rr_common(s["hr"]); b1 = bias_bound(e["rr"], e["rr"]); k = int(np.ceil(np.log(1/rr)/np.log(b1)))
        res["many_weak"] = dict(bias_each=b1, k_needed=k, rr_each=e["rr"])
        chk.append(R.chk("H6", f"at most {e['k_max']} independent weak confounders (each {e['rr']}-fold on both sides, multiplicative worst-case bias) explain away the estimate", k, k <= e["k_max"], kind="hypothesis"))
    if "mediator_vs_confounder" in X:
        e = X["mediator_vs_confounder"]; rng = np.random.default_rng(e["seed"]); n = e["n"]; out = {}
        for dag in ("mediator", "confounder"):
            if dag == "mediator":
                A = rng.random(n) < 0.3; M = rng.random(n) < np.where(A, 0.7, 0.3)
            else:
                M = rng.random(n) < 0.45; A = rng.random(n) < np.where(M, 0.5, 0.14)
            Y = rng.random(n) < 0.18*np.where(M, e["rr_m"], 1.0)/((0.45*e["rr_m"]+0.55) if dag == "confounder" else (0.42*e["rr_m"]+0.58))
            crude = Y[A].mean()/Y[~A].mean(); strata = [Y[A & (M == m)].mean()/Y[~A & (M == m)].mean() for m in (0, 1)]
            adj = float(np.exp(np.mean(np.log(strata)))); out[dag] = dict(crude=crude, adjusted=adj, attenuation=(1-np.log(adj)/np.log(crude)) if crude != 1 else None)
        res["mediator_vs_confounder"] = out
        chk.append(R.chk("H7", "adjusting for social participation removes >= 80% of the (log) association both when it is a mediator and when it is a confounder: attenuation alone cannot tell them apart (relevant to X11)", out, all(v["attenuation"] is not None and v["attenuation"] >= 0.8 for v in out.values()), kind="hypothesis"))
    if "prevalence_curve" in X:
        e = X["prevalence_curve"]; out = []
        for p0 in e["p0"]:
            rr_exact = (1-(1-p0)**s["hr"])/p0  # proportional hazards, fixed follow-up: risk = 1-(1-p0)^HR
            out.append(dict(p0=p0, rr_exact=rr_exact, e_exact=evalue(rr_exact), e_rare=evalue(s["hr"]), e_common=evalue(hr_to_rr_common(s["hr"]))))
        res["prevalence_curve"] = out; near = min(out, key=lambda o: abs(o["p0"]-e["at"]))
        chk.append(R.chk("H8", "at S12's mortality level (~0.2 among never-attenders), the exact proportional-hazards E-value lies within 0.1 of S14's common-outcome approximation", [near["p0"], near["e_exact"], near["e_common"], near["e_rare"]], abs(near["e_exact"]-near["e_common"]) <= 0.1, kind="hypothesis"))
    if "replicate" in X:
        # run 2 fix (see superseded-run-1/README.md): prevalence arguments of cohort() swapped back in the next line
        e = X["replicate"]; rng = np.random.default_rng(e["seed"]); rr = hr_to_rr_common(s["hr"]); E = evalue(rr)
        reps = [cohort(rng, e["n"], 0.19, 1/E, 1.0, 0.15, E) for _ in range(e["reps"])]; m = float(np.mean(reps)); res["replicate"] = dict(mean=m, sd=float(np.std(reps)), target=rr)
        chk.append(R.chk("H9", "iteration-3 cohort check replicates over 20 new cohorts (mean within 2% of target)", [m, rr], abs(m-rr)/rr <= 0.02, kind="hypothesis"))
    R.finish(H, P, res, chk, t0)
if __name__ == "__main__": main()
