# Report-7-Unified — Cycle 3 change log

## Claims added or annotated (what and why)
- C3-R7-01 (E): New in Cycle 3.
- C3-R7-02 (E): New in Cycle 3.
- C3-R7-03 (E): New in Cycle 3.
- C3-R7-04 (E): New in Cycle 3.

## Simulation iterations (what changed and why)
- iter-1: Code checks: strict rule reproduces Cycle 2; essential-claim definition on toy links.
- iter-2: Apply the strict rule to the Cycle-3 ledger and register (27 links incl. L25-L27).
- iter-3: Does the essential-claim rule change the Cycle-2 downgrades (starting from the Cycle-1 labels)?
- iter-4: Label-error sensitivity of the Established links.
- iter-5: Connectivity under Established links only, with the new links.
- iter-6: Did Cycle 3 fill empty Being x Lens cells?
- iter-7: Carried item 'two-coder lens placement': keyword rule vs hand coding on a seeded 40-claim sample.
- iter-8: GAIA motherthread separability audit.
- iter-9: Diminishing-returns audit: did anything carried from Cycle 2 change label or status?

## Development disclosure
Simulation code was smoke-tested before the official runs; official iterations were run in this tree and re-executed byte-identically by `Research/tools` (`gaia_tools.rerun`). Pre-registered checks were not changed after seeing results; any re-runs are listed in `../CHANGELOG.md`.
