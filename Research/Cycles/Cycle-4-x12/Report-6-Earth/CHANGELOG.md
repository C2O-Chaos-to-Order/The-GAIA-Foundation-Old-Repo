# Report-6-Earth — Cycle 4 change log

## Claims added or annotated (what and why)
- C3-R6-05 (E): Extended in Cycle 4 over a wider forcing range: our constrained variant reaches L_max 1.77, still short of the published 2.32 (C4-R6-01); W03 still closed.
- C4-R6-01 (E): New in Cycle 4.
- C4-R6-02 (E): New in Cycle 4.

## Simulation iterations (what changed and why)
- iter-1: Code checks: vectorised copy reproduces Cycle 3; extending the range leaves the original model unchanged.
- iter-2: Does the constrained variant reach the published L_max once the range is not truncated?
- iter-3: Unbounded adaptation over the extended range.
- iter-4: Cost width R.
- iter-5: Adaptation bounds.
- iter-6: Regulation over the extended range.
- iter-7: Cost shape.
- iter-8: Hysteresis of the original model (reverse sweep).
- iter-9: Numerical robustness of the extended constrained run.
- iter-10: Calibration against the published row (disclosed as calibration).
- iter-11: One-at-a-time sensitivity of the constrained L_max.
- iter-12: Consolidation: was the Cycle-3 mismatch a range artefact?

## Development disclosure
Simulation code was smoke-tested before the official runs; official iterations were run in this tree and re-executed byte-identically by `Research/tools` (`gaia_tools.rerun`). Pre-registered checks were not changed after seeing results; any re-runs are listed in `../CHANGELOG.md`.
