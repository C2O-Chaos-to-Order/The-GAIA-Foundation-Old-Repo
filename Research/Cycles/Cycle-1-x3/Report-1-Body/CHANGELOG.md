# Report-1-Body — Cycle 1 change log

## Claims revised or added (what and why)
- C0v2-R1-09 (E): Upgraded to full-text source V06 (Cycle-1 access rule); wording aligned to V06.
- C0v2-R1-11 (P): Limits updated (full-text attempt failed).
- C0v2-R1-12 (E): Carried forward; cites the Cycle-0 run (C0: prefix). Extended by C1-R1-02..04.
- C0v2-R1-13 (E): Carried forward; cites the Cycle-0 run (C0: prefix). Robustness re-tested in C1-R1-03/04.
- C1-R1-01 (E): New in Cycle 1.
- C1-R1-02 (E): New in Cycle 1.
- C1-R1-03 (E): New in Cycle 1.
- C1-R1-04 (E): New in Cycle 1.

## Simulation iterations (what changed and why)
- iter-1: Map the controller-gain space of the C0 toy loop (step load D=1, plant leak kl=0.1) and record the best-peak gain pair for iteration 2.
- iter-2: Add sensor/effector delay (the main way real feedback fails) and parameter uncertainty. The iteration-1 best-peak gains are added to the PI delay scan (adaptive refinement).
- iter-3: Core/shell thermal toy: a skin (shell) signal used as feedforward for core regulation, the structure OpenStax describes (V06: hypothalamic thermostat, skin and core). Robustness to +/-50% parameter perturbation.

## Development disclosure
Simulation code was smoke-tested in a scratch folder before the official runs; official iterations were run from scratch in this tree. Pre-registered checks were not changed after seeing results except for the bug fixes and the one scope refinement listed in `../CHANGELOG.md`.
