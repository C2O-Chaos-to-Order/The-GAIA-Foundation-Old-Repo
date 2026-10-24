# Report-7-Unified — Cycle 1 change log

## Claims revised or added (what and why)
- C0v2-R7-03 (E): Updated to the Cycle-1 register.
- C0v2-R7-05 (E): Carried forward (Cycle-0 run; the grid is not regenerated in Cycle 1).
- C0v2-R7-06 (E): Carried forward (Cycle-0 run).
- C1-R7-01 (PS): New in Cycle 1.
- C1-R7-02 (E): New in Cycle 1.
- C1-R7-03 (E): New in Cycle 1.

## Simulation iterations (what changed and why)
- iter-1: Audit the Cycle-1 ledger (all claims, register, link register, all Cycle-1 execution records).
- iter-2: Robustness of the cross-report argument: does the R1-R7 link graph stay connected when weaker links are removed?
- iter-3: Mechanical rejection screen: for every link, do its Cycle-1 simulation tests or contested basis claims trigger its rejection criterion?

## Development disclosure
Simulation code was smoke-tested in a scratch folder before the official runs; official iterations were run from scratch in this tree. Pre-registered checks were not changed after seeing results except for the bug fixes and the one scope refinement listed in `../CHANGELOG.md`.
