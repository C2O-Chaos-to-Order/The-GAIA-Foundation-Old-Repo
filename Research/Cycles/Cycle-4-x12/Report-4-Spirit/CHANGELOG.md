# Report-4-Spirit — Cycle 4 change log

## Claims added or annotated (what and why)
- C0v2-R4-12 (E): Cycle 4 adds negative-control design analysis (C4-R4-01 to C4-R4-04): such controls detect strong but not weak confounding at typical cohort sizes; no real negative-control study of attendance was read.
- C4-R4-01 (E): New in Cycle 4.
- C4-R4-02 (E): New in Cycle 4.
- C4-R4-03 (E): New in Cycle 4.
- C4-R4-04 (E): New in Cycle 4.

## Simulation iterations (what changed and why)
- iter-1: Code check: null cohort and U-stratified recovery of a known effect.
- iter-2: Does a negative-control outcome (NCO) detect confounding that alone produces an apparent protective effect?
- iter-3: False-flag rate when there is no confounding but a true effect.
- iter-4: When can the NCO also correct the estimate (ratio OR_D/OR_N)?
- iter-5: Negative-control exposure (Y03's second type).
- iter-6: Selection bias (Y04): entry into the cohort depends on attendance and health.
- iter-7: How weak a confounder can an NCO detect?
- iter-8: Sample size for the weak scenario.
- iter-9: Rare outcomes, as for cause-specific mortality.
- iter-10: Imperfect NCO (Y03 warns these are common).
- iter-11: Replication of iteration 2 with new seeds.
- iter-12: Consolidation: confounding plus a true effect.

## Development disclosure
Simulation code was smoke-tested before the official runs; official iterations were run in this tree and re-executed byte-identically by `Research/tools` (`gaia_tools.rerun`). Pre-registered checks were not changed after seeing results; any re-runs are listed in `../CHANGELOG.md`.
