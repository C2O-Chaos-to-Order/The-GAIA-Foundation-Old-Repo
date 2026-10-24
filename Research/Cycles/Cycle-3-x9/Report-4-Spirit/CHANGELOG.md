# Report-4-Spirit — Cycle 3 change log

## Claims added or annotated (what and why)
- C0v2-R4-09 (E): Cycle 3 repeats C1-R4-07's common-outcome E-value (about 1.97) and adds an exact proportional-hazards conversion (2.24) (C3-R4-03).
- C0v2-R4-12 (E): Refined in Cycle 3: the required confounding strength depends on outcome-frequency handling, about 2.0-2.35 (C3-R4-03, C3-R4-04).
- C1-R4-01 (E): Contrast added in Cycle 3: a Swedish cohort's association disappeared after adjusting for social participation (C3-R4-01).
- C3-R4-01 (P): New in Cycle 3.
- C3-R4-02 (E): New in Cycle 3.
- C3-R4-03 (E): New in Cycle 3.
- C3-R4-04 (E): New in Cycle 3.
- C3-R4-05 (E): New in Cycle 3.

## Simulation iterations (what changed and why)
- iter-1: Code check: reproduce S12's own E-values and the bound's defining properties.
- iter-2: S12 has 18% cumulative mortality; S14 advises an approximation for common outcomes. How much does the E-value change?
- iter-3: Check the arithmetic in a synthetic S12-sized cohort with no true effect.
- iter-4: Tipping-point curve: which combinations of confounder strengths would explain the association away?
- iter-5: Challenge: could residual 'healthy attender' selection (people in poor health attend less and die more) alone produce S12's estimate?
- iter-6: Many weak confounders instead of one strong one.
- iter-7: X11 (Sweden) found the association disappeared after adjusting for social participation. Does that show confounding?
- iter-8: Sensitivity of the E-value to how 'common' the outcome is, using an exact proportional-hazards conversion.
- iter-9: Consolidation: replicate the iteration-3 cohort check.

## Development disclosure
Simulation code was smoke-tested before the official runs; official iterations were run in this tree and re-executed byte-identically by `Research/tools` (`gaia_tools.rerun`). Pre-registered checks were not changed after seeing results; any re-runs are listed in `../CHANGELOG.md`.
