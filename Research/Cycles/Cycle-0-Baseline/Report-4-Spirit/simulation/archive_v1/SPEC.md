# SIM-R4-C0 — Confounding sensitivity of the attendance–mortality association (specification, written before execution)

**Status:** Specified before execution. Class: Mathematical/computational (epidemiological sensitivity analysis). It does NOT measure "spirit"; it bounds how strong unmeasured confounding would have to be to explain one published association (S12) away.

## Question
For Li et al. 2016 (S12; Nurses' Health Study, n = 74,534; >1×/week vs never attendance, all-cause mortality HR 0.67, 95% CI 0.62–0.71), what is the E-value (S14), and can a synthetic cohort with **zero** causal effect but an unmeasured confounder of that strength reproduce an apparent protective ratio of that size?

## Model
(a) E-value for RR<1: RR* = 1/RR; E = RR* + sqrt(RR*(RR*−1)). Computed (i) treating HR≈RR (rare-outcome approximation) and (ii) with the common-outcome conversion RR ≈ (1−0.5^√HR)/(1−0.5^√(1/HR)) because the outcome is not rare (13,537 deaths / 74,534 ≈ 18%, S12). Applied to point estimate and to the CI limit closest to 1 (0.71).
(b) Monte Carlo: binary U (prevalence 0.5); P(attend | U=1) / P(attend | U=0) = RR_EU; P(death | U=1)/P(death | U=0) = RR_UD; attendance has **no** effect on death. Baseline death risk 0.15 in U=0. n = 200,000, seed = 20261023. Measure crude RR(death | attend vs not).

## Expected outputs
- E1: E-values computed and > 1.
- E2: with RR_EU = RR_UD = E-value(point, common-outcome conversion), the synthetic crude RR is ≤ the converted target RR + 0.02 (i.e., confounding alone suffices to produce it in this toy).
- E3: with RR_EU = RR_UD = 1.2, crude RR stays > 0.9 (weak confounding cannot produce it).
**Failure criteria:** E1–E3 not met → Fail recorded.
**Not shown:** whether such a confounder exists; whether attendance causes lower mortality; anything about spiritual realities.

## Result note recorded after execution (Fail preserved)
E2 **failed** (synthetic crude RR 0.851 vs target ≤ 0.778). Diagnosis: the toy parameterised the confounder by P(attend | U) ratios and P(death | U) ratios at a fixed 50% prevalence, whereas the E-value is defined on the risk-ratio scale for the confounder–exposure association (prevalence ratio of U across exposure groups) and is a bound over all confounder prevalences. The toy mapping therefore did not implement the E-value's premise. This is a **specification error in SIM-R4-C0**, not evidence about the published association. The run is preserved as executed; a corrected parameterisation is deferred to a separately recorded later run.
