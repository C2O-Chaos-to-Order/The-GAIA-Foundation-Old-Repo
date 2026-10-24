# Report-2-Mind — Cycle 2 change log

## Claims added or annotated (what and why)
- C0v2-R2-06 (PS): Counterevidence/limits field filled in Cycle 2 (was empty).
- C0v2-R2-07 (P): Counterevidence/limits field filled in Cycle 2 (was empty).
- C0v2-R2-08 (PS): Counterevidence/limits field filled in Cycle 2 (was empty).
- C0v2-R2-09 (PS): Counterevidence/limits field filled in Cycle 2 (was empty).
- C1-R2-06 (E): Corroborated by an independent Cycle-2 re-implementation (C2-R2-02).
- C2-R2-01 (P): New in Cycle 2.
- C2-R2-02 (E): New in Cycle 2.
- C2-R2-03 (E): New in Cycle 2.

## Simulation iterations (what changed and why)
- iter-1: Carried agenda (C1 R2): Rescorla-Wagner cannot produce latent inhibition (LI); test whether a Pearce-Hall-type hybrid and a Kalman-filter (Bayesian) learner produce BOTH LI and blocking.
- iter-2: Are the iteration-1 results properties of the models or of the default parameters? Sweep each model's parameter grid.
- iter-3: Dose-response: does LI grow with the number of pre-exposures in PH and KF?
- iter-4: Identifiability: if data came from one model, can a fit tell which? Model recovery with an acquisition-only design vs a diagnostic design (acquisition + LI + blocking).
- iter-5: Identifiability under more noise.
- iter-6: Consolidation: replicate the iteration-4 diagnostic-design recovery with a new seed and twice the replicates.

## Development disclosure
Simulation code was smoke-tested before the official runs; official iterations were run in this tree and re-executed byte-identically by `Research/tools` (`gaia_tools.rerun`). Pre-registered checks were not changed after seeing results; any re-runs are listed in `../CHANGELOG.md`.
