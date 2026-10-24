# Report-2-Mind — Cycle 3 change log

## Claims added or annotated (what and why)
- C2-R2-03 (E): Optimism addressed in Cycle 3: with a new design, off-grid generators still gave 98% recovery for PH vs KF (C3-R2-04).
- C3-R2-01 (E): New in Cycle 3.
- C3-R2-02 (P): New in Cycle 3.
- C3-R2-03 (E): New in Cycle 3.
- C3-R2-04 (E): New in Cycle 3.
- C3-R2-05 (E): New in Cycle 3.

## Simulation iterations (what changed and why)
- iter-1: Code check: copied learning rules reproduce Cycle 2; empty delay steps are inert for weights.
- iter-2: Would a parametric pre-exposure design (LI vs number of pre-exposures) separate PH from KF?
- iter-3: Context specificity: LI in animals is attenuated by a context change; do the models reproduce that with context as a cue?
- iter-4: Delay signature: does an interval between pre-exposure and conditioning separate the accounts?
- iter-5: Model recovery with the combined parametric + delay design, generators at defaults.
- iter-6: Remove the Cycle-2 optimism: generating parameters drawn uniformly within (not on) the grid.
- iter-7: Sensitivity: how much of the KF parameter space shows the delay signature?
- iter-8: Challenge: does a third, Mackintosh-type account break recovery?
- iter-9: Consolidation: replicate iteration 6 with a new seed and twice the replicates.

## Development disclosure
Simulation code was smoke-tested before the official runs; official iterations were run in this tree and re-executed byte-identically by `Research/tools` (`gaia_tools.rerun`). Pre-registered checks were not changed after seeing results; any re-runs are listed in `../CHANGELOG.md`.
