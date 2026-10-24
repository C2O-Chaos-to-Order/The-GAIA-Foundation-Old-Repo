# Report-6-Earth — Cycle 1 change log

## Claims revised or added (what and why)
- C0v2-R6-01 (P): Downgraded Established -> Plausible (abstract-only); V08 added.
- C0v2-R6-02 (E): Upgraded to full text V02.
- C0v2-R6-04 (P): Downgraded Established -> Plausible (abstract-only).
- C0v2-R6-05 (E): Upgraded to full text V03 (Richardson 2023); wording updated.
- C0v2-R6-07 (E): Carried forward (Cycle-0 run). Robustness re-tested in C1-R6-07/08: regulation is parameter-dependent.
- C0v2-R6-13 (E): Upgraded to full preprint text V09.
- C0v2-R6-14 (P): Counter-evidence V30 added (challenge pass).
- C0v2-R6-17 (E): Carried forward (Cycle-0 run). Conductivity range widened in C1-R6-09.
- C0v2-R6-18 (P): Sources widened.
- C1-R6-01 (P): New in Cycle 1.
- C1-R6-02 (E): New in Cycle 1.
- C1-R6-03 (P): New in Cycle 1.
- C1-R6-04 (P): New in Cycle 1.
- C1-R6-05 (P): New in Cycle 1.
- C1-R6-06 (E): New in Cycle 1.
- C1-R6-07 (E): New in Cycle 1.
- C1-R6-08 (E): New in Cycle 1.
- C1-R6-09 (E): New in Cycle 1.

## Simulation iterations (what changed and why)
- iter-1: Is Daisyworld regulation robust to death rate, heat-transfer parameter q and albedo contrast?
- iter-2: Toy test related to the Darwinization critique (V23-V25, V39): if daisies adapt their optimum temperature to local conditions, does planetary regulation survive? Unbounded and bounded adaptation.
- iter-3: Geomagnetic spectrum (Lowes-Mauersberger) at Earth's surface and downward-continued to the core-mantle boundary for four epochs; free-decay time across the disputed conductivity range (V09 high vs V30 low, converted with Wiedemann-Franz).

## Development disclosure
Simulation code was smoke-tested in a scratch folder before the official runs; official iterations were run from scratch in this tree. Pre-registered checks were not changed after seeing results except for the bug fixes and the one scope refinement listed in `../CHANGELOG.md`.
