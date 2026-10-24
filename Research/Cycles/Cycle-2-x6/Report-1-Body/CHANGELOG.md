# Report-1-Body — Cycle 2 change log

## Claims added or annotated (what and why)
- C0v2-R1-02 (E): Counterevidence/limits field filled in Cycle 2 (was empty).
- C0v2-R1-04 (E): Counterevidence/limits field filled in Cycle 2 (was empty).
- C0v2-R1-07 (E): Counterevidence/limits field filled in Cycle 2 (was empty).
- C1-R1-03 (E): Extended in Cycle 2 by a learned feedforward (C2-R1-03 to C2-R1-06).
- C1-R1-04 (E): Extended in Cycle 2 by a learned feedforward (C2-R1-03 to C2-R1-06).
- C2-R1-01 (E): New in Cycle 2.
- C2-R1-02 (P): New in Cycle 2.
- C2-R1-03 (E): New in Cycle 2.
- C2-R1-04 (E): New in Cycle 2.
- C2-R1-05 (E): New in Cycle 2.
- C2-R1-06 (E): New in Cycle 2.

## Simulation iterations (what changed and why)
- iter-1: Add a learned, anticipatory (feedforward) term to the Cycle-1 bounded feedback loop and test whether 14 days of daily exposure lower the peak (direction per W04).
- iter-2: Decay and re-induction: calibrate the forgetting rate to W05's '1 day of HA is lost following 2 days of HAD', then TEST whether the same simple learner reproduces W05's 'HRA was 8-12 times faster than HAD'.
- iter-3: Cost of anticipation: when the cue arrives but the load does not, a learned feedforward cools below the set point. Can a bound on the learned gain keep that harm small while keeping most of the benefit?
- iter-4: R6 analogue (cross-link L01): if the body's set point itself adapts toward the prevailing temperature (like daisies adapting their optimum in SIM-R6-C2), does regulation erode when unbounded and recover when bounded?
- iter-5: Robustness of bounded learning feedforward over learning rate, feedback gain and effector capacity, with 20% day-to-day load noise.
- iter-6: Consolidation: does the iteration-1 acquisition result replicate across 20 seeds of day-to-day load noise?

## Development disclosure
Simulation code was smoke-tested before the official runs; official iterations were run in this tree and re-executed byte-identically by `Research/tools` (`gaia_tools.rerun`). Pre-registered checks were not changed after seeing results; any re-runs are listed in `../CHANGELOG.md`.
