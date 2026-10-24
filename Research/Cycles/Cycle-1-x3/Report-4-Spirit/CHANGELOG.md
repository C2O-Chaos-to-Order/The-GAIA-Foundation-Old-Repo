# Report-4-Spirit — Cycle 1 change log

## Claims revised or added (what and why)
- C0v2-R4-10 (P): Downgraded Established -> Plausible (abstract-only).
- C0v2-R4-12 (E): Carried forward; cites the Cycle-0 run. Extended to five estimates in C1-R4-07.
- C0v2-R4-13 (E): Carried forward; cites the Cycle-0 run. Extended by probabilistic bias analysis C1-R4-08.
- C0v2-R4-14 (H): Updated with Cycle-1 evidence; label unchanged (Hypothetical).
- C1-R4-01 (E): New in Cycle 1.
- C1-R4-02 (E): New in Cycle 1.
- C1-R4-03 (E): New in Cycle 1.
- C1-R4-04 (P): New in Cycle 1.
- C1-R4-05 (P): New in Cycle 1.
- C1-R4-06 (E): New in Cycle 1.
- C1-R4-07 (E): New in Cycle 1.
- C1-R4-08 (E): New in Cycle 1.
- C1-R4-09 (E): New in Cycle 1.

## Simulation iterations (what changed and why)
- iter-1: Recompute E-values for every attendance-health estimate read in full (S12, V12, V13) plus the abstract-only meta-analysis (T08), and check against the E-values the papers report.
- iter-2: Probabilistic bias analysis: draw confounder strengths (RR_EU, RR_UD) from a prior and report how often each association is fully explained away; sweep the prior spread because the prior is our assumption.
- iter-3: What do the sibling fixed-effects and instrument designs of V16/V17 buy? Simulate known truth (beta = -0.1) under family-only confounding, individual confounding, and an instrument that violates exclusion.

## Development disclosure
Simulation code was smoke-tested in a scratch folder before the official runs; official iterations were run from scratch in this tree. Pre-registered checks were not changed after seeing results except for the bug fixes and the one scope refinement listed in `../CHANGELOG.md`.
