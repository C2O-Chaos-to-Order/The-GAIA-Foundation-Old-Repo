# Report-3-Soul — Cycle 1 change log

## Claims revised or added (what and why)
- C0v2-R3-17 (PS): Carried forward (Cycle-0 result). Cycle 1 replaces the single-partition reading with robustness tests C1-R3-02..04.
- C1-R3-01 (E): New in Cycle 1.
- C1-R3-02 (E): New in Cycle 1.
- C1-R3-03 (E): New in Cycle 1.
- C1-R3-04 (E): New in Cycle 1.
- C1-R3-05 (PS): New in Cycle 1.

## Simulation iterations (what changed and why)
- iter-1: C0 typology recurred in 0.13% of perturbations. Test alternative codings of the 36 uncertain cells and alternative distance metrics against the C0 base partition.
- iter-2: Alternative clustering methods and k, with silhouette as a structure-strength measure.
- iter-3: Widen (C15 Jain jiva, V40) and report what is stable instead of a single partition: co-clustering frequencies across codings x metrics x linkages x k.

## Development disclosure
Simulation code was smoke-tested in a scratch folder before the official runs; official iterations were run from scratch in this tree. Pre-registered checks were not changed after seeing results except for the bug fixes and the one scope refinement listed in `../CHANGELOG.md`.
