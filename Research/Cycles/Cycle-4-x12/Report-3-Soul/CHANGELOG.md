# Report-3-Soul — Cycle 4 change log

## Claims added or annotated (what and why)
- C1-R3-05 (PS): Remains Indeterminate; Cycle 4 shows the partition is not stable even within coding A (attribute bootstrap ARI 0.44; C4-R3-01).
- C2-R3-03 (E): Consistent with Cycle 4: flipping uncertain cells gives mean ARI 0.34 (C4-R3-01).
- C3-R3-03 (E): Consistent with Cycle 4 (C4-R3-01, C4-R3-02).
- C4-R3-01 (E): New in Cycle 4.
- C4-R3-02 (E): New in Cycle 4.

## Simulation iterations (what changed and why)
- iter-1: Code check; counts of uncertain cells and cluster sizes.
- iter-2: Attribute bootstrap.
- iter-3: Jackknife over conceptions.
- iter-4: Was k = 4 a good choice?
- iter-5: Linkage sensitivity.
- iter-6: Do coder A's uncertain cells drive the partition?
- iter-7: Distance sensitivity.
- iter-8: Which conceptions form stable cores?
- iter-9: Is there more structure than chance?
- iter-10: Coder C's partition and its stability (reporting only).
- iter-11: Replication of iteration 2.
- iter-12: Consolidation.

## Development disclosure
Simulation code was smoke-tested before the official runs; official iterations were run in this tree and re-executed byte-identically by `Research/tools` (`gaia_tools.rerun`). Pre-registered checks were not changed after seeing results; any re-runs are listed in `../CHANGELOG.md`.
