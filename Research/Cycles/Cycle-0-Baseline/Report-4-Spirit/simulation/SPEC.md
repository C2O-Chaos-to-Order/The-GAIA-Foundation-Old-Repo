# SIM-R4-C0 — E-value sensitivity analysis for the attendance–mortality association (Baseline v2 specification, written before the v2 run)

**Status:** Specified 2026-10-24 before execution. Class: Mathematical/computational. Concerns only the *demonstrable* side of Report 4 (a measured association with mortality); it says nothing about spirit as vitality, transcendence, connection or inspiration.

## Question
How strong would unmeasured confounding have to be to explain away the association reported by Li et al. 2016 (S12: weekly-plus attendance vs never, HR 0.67, 95% CI 0.62–0.71; 13,537 deaths among 74,534 women), and does a correctly specified confounding simulation reproduce the E-value's defining property?

## Formal model
- E-value (S14): for RR ≥ 1, E = RR + sqrt(RR·(RR−1)); protective RR inverted first. Common-outcome HR→RR approximation (S14): RR ≈ (1−0.5^√HR)/(1−0.5^√(1/HR)); outcome risk 18% so the common-outcome scale is primary.
- Bounding factor (S14): B(RR_EU, RR_UD) = RR_EU·RR_UD/(RR_EU+RR_UD−1); E is the value with B(E,E) = observed RR on the harm scale (RR* = 1/RR).
- **Corrected Monte Carlo (fixes the v1 specification error):** harm scale; exposure X = non-attendance (P = 0.3); **no causal effect of X on death**; binary U with P(D|U=1)/P(D|U=0) = RR_UD and P(U|X=1)/P(U|X=0) = RR_EU, using the allocation that attains the bound, P(U|X=1) = 1 and P(U|X=0) = 1/RR_EU; baseline risk q = 0.10; n = 2,000,000; seed 20261024. The crude RR is then inverted back to the attendance-vs-never scale for comparison with the observed RR.

## Pre-registered checks
- E1: E-values > 1 on both scales.
- E2a: analytic B(E,E) equals RR* to 1e-9 (algebraic identity check).
- E2: under the null with RR_EU = RR_UD = E, the simulated crude RR reproduces the observed common-scale RR within ±0.02.
- E2b: with both confounder strengths at 0.9·E, the crude RR stays above observed RR + 0.02 (confounding weaker than E cannot fully explain the association, even in the worst-case allocation).
- E3: weak confounding (1.2, 1.2) under the null gives crude RR > 0.9.

## Failure criteria
Any check failing is recorded as Fail and not rewritten.

## What this does NOT show
Whether such a confounder exists; E-values bound confounding, they do not detect it. Selection, measurement error and reverse causation are not modelled.

## v1 → v2 correction (kept on record)
In v1 (archived in `archive_v1/`), check E2 FAILED (crude RR 0.8977 vs required ≤ 0.807). Cause: the v1 confounder was parameterised as a multiplier on P(attend | U) and a divisor on P(death | U) with P(U) = 0.5, which is not the E-value's risk-ratio-scale confounder–exposure association and is not the allocation that attains the bound. v1 drew no conclusion from E2. v2 implements the definition above; v1 files are retained unaltered in `archive_v1/`.
