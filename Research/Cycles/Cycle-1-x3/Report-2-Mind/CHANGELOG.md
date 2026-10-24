# Report-2-Mind — Cycle 1 change log

## Claims revised or added (what and why)
- C0v2-R2-04 (E): Upgraded to full text V04; counter-view C1-R2-02 linked.
- C0v2-R2-12 (E): Upgraded to full text V05.
- C0v2-R2-13 (E): Carried forward; cites the Cycle-0 run. Re-tested with LOOCV/bootstrap in C1-R2-07.
- C1-R2-01 (P): New in Cycle 1.
- C1-R2-02 (P): New in Cycle 1.
- C1-R2-03 (P): New in Cycle 1.
- C1-R2-04 (P): New in Cycle 1.
- C1-R2-05 (E): New in Cycle 1.
- C1-R2-06 (E): New in Cycle 1.
- C1-R2-07 (E): New in Cycle 1.

## Simulation iterations (what changed and why)
- iter-1: Rescorla-Wagner blocking over learning rate x pretraining amount: where does blocking (ratio < 0.1) fail?
- iter-2: Challenge pass: a known failure of Rescorla-Wagner is latent inhibition (pre-exposure slows later learning). Compare RW with a Pearce-Hall-type associability model.
- iter-3: Refit the forgetting curves (S04 Table 3: Ebbinghaus 1885 and Murre & Dros 2015 savings) with leave-one-out CV and bootstrap, not AIC alone (C0 used AIC only).

## Development disclosure
Simulation code was smoke-tested in a scratch folder before the official runs; official iterations were run from scratch in this tree. Pre-registered checks were not changed after seeing results except for the bug fixes and the one scope refinement listed in `../CHANGELOG.md`.
