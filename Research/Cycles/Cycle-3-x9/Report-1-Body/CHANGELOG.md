# Report-1-Body — Cycle 3 change log

## Claims added or annotated (what and why)
- C2-R1-02 (P): Context added in Cycle 3: a small cross-over study found adaptations generally maintained 7 days after HA (C3-R1-02).
- C2-R1-04 (E): Remedy tested in Cycle 3: a two-state memory meets both W05 anchors only in 2 of 180 fine-grid settings and the result is fragile (C3-R1-06 to C3-R1-08).
- C3-R1-01 (P): New in Cycle 3.
- C3-R1-02 (P): New in Cycle 3.
- C3-R1-03 (P): New in Cycle 3.
- C3-R1-04 (E): New in Cycle 3.
- C3-R1-05 (P): New in Cycle 3.
- C3-R1-06 (E): New in Cycle 3.
- C3-R1-07 (E): New in Cycle 3.
- C3-R1-08 (E): New in Cycle 3.

## Simulation iterations (what changed and why)
- iter-1: Code check before new work: the copied Cycle-2 session model and single-state learner must reproduce the Cycle-2 result, and the new two-state code must collapse to it.
- iter-2: Can a fast-plus-slow memory meet BOTH W05 anchors (about 1 HA day lost per 2 decay days, and 8-12x faster re-induction) that a single state could not?
- iter-3: Mechanism check: is the re-induction advantage carried by the slow state's retention?
- iter-4: Distinguishing prediction: does decay slow down with longer absence more in the two-state model than in a single exponential?
- iter-5: Could a realistic study design tell the two memories apart? Model recovery with peak temperatures on 9 test days.
- iter-6: Robustness of the selected setting to day-to-day load noise.
- iter-7: Sensitivity analysis: one-at-a-time +-20% perturbation of the four memory parameters and two loop parameters.
- iter-8: Second distinguishing prediction: do savings accumulate over repeated acclimation/decay cycles (e.g. seasons)?
- iter-9: Consolidation: replicate the iteration-2 answer on an independent, finer grid.

## Development disclosure
Simulation code was smoke-tested before the official runs; official iterations were run in this tree and re-executed byte-identically by `Research/tools` (`gaia_tools.rerun`). Pre-registered checks were not changed after seeing results; any re-runs are listed in `../CHANGELOG.md`.
