# Report-6-Earth — Cycle 3 change log

## Claims added or annotated (what and why)
- C2-R6-01 (E): Confirmed qualitatively in published equations (C3-R6-05); W03 still abstract only.
- C2-R6-04 (E): Extended in Cycle 3 from published equations (W01): Table 1 reproduced (C3-R6-04); unbounded adaptation removes regulation (C3-R6-05).
- C3-R6-01 (P): New in Cycle 3.
- C3-R6-02 (P): New in Cycle 3.
- C3-R6-03 (P): New in Cycle 3.
- C3-R6-04 (E): New in Cycle 3.
- C3-R6-05 (E): New in Cycle 3.

## Simulation iterations (what changed and why)
- iter-1: Code checks of the published energy balance and growth function.
- iter-2: Reproduce W01 Table 1 'Original Daisyworld' from the published equations.
- iter-3: Reproduce the neutral-daisy control and test our reading of 'total life'.
- iter-4: Sensitivity to an unstated detail (seed floor).
- iter-5: Robertson & Robinson-type unbounded adaptation inside the published equations.
- iter-6: Bounded, costed adaptation (W01's verbal description + eq. 15 with our cost form).
- iter-7: Quantitative comparison with the published constrained row (we lack W03's equations).
- iter-8: Sensitivity of the constrained result over adaptation rate and cost width.
- iter-9: Numerical robustness of the reproduction (iteration 2).

## Development disclosure
Simulation code was smoke-tested before the official runs; official iterations were run in this tree and re-executed byte-identically by `Research/tools` (`gaia_tools.rerun`). Pre-registered checks were not changed after seeing results; any re-runs are listed in `../CHANGELOG.md`.
