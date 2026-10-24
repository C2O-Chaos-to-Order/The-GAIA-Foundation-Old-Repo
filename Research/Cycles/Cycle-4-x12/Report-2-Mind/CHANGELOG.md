# Report-2-Mind — Cycle 4 change log

## Claims added or annotated (what and why)
- C3-R2-03 (E): Cycle 4 adds a limit: if PH associability recovers during the delay, PH also shows a delay effect (C4-R2-04).
- C3-R2-04 (E): Extended in Cycle 4 (ablations, power, mis-specified range; C4-R2-03) with a limit (C4-R2-04).
- C3-R2-05 (E): Faithful Mackintosh (1975) rule still BLOCKED by access in Cycle 4 (Y05 abstract only; C4-R2-02); not re-tested.
- C4-R2-01 (P): New in Cycle 4.
- C4-R2-02 (P): New in Cycle 4.
- C4-R2-03 (E): New in Cycle 4.
- C4-R2-04 (E): New in Cycle 4.

## Simulation iterations (what changed and why)
- iter-1: Code check: the copied rules (Mackintosh branch removed) reproduce Cycle 3; the new rho option leaves weights unchanged on empty steps.
- iter-2: Design power: how many subjects per group would detect the KF delay effect in a real experiment?
- iter-3: Which part of the design discriminates? Delay arms only.
- iter-4: Ablation: pre-exposure curve only.
- iter-5: Noise ceiling of the combined design.
- iter-6: Mis-specification: KF generators with tau2 far outside the fitting grid.
- iter-7: What does the two-model comparison do with data that are neither model (a 50/50 mixture)?
- iter-8: How long must the delay be?
- iter-9: Challenge: if PH associability recovers with time, does PH also show a delay effect?
- iter-10: Recovery when PH may recover during the delay.
- iter-11: Replication of iteration 3 (delay-only) with new seed and 2x replicates.
- iter-12: Consolidation across iterations 3-11.

## Development disclosure
Simulation code was smoke-tested before the official runs; official iterations were run in this tree and re-executed byte-identically by `Research/tools` (`gaia_tools.rerun`). Pre-registered checks were not changed after seeing results; any re-runs are listed in `../CHANGELOG.md`.
