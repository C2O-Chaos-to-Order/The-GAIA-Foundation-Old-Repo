# Report-1-Body — Cycle 4 change log

## Claims added or annotated (what and why)
- C3-R1-06 (E): Cycle 4 removed the whole-day quantisation with a continuous metric: still 1 of 144 coarse settings (C4-R1-01); fragility persists (C4-R1-02).
- C3-R1-07 (E): Cycle 4 confirms the decay-deceleration prediction with the continuous selection (0.20x vs 0.69x; C4-R1-03).
- C3-R1-08 (E): Cycle 4 repeated the robustness tests with the continuous metric: still fragile (8/20 and 4/20 seeds; +-20% range 2.38-11.31; C4-R1-02).
- C4-R1-01 (E): New in Cycle 4.
- C4-R1-02 (E): New in Cycle 4.
- C4-R1-03 (E): New in Cycle 4.

## Simulation iterations (what changed and why)
- iter-1: Code check: imported Cycle-3 code and the new interpolated metric.
- iter-2: Re-run Cycle 3's pre-declared coarse grid with the continuous metric.
- iter-3: Re-run Cycle 3's fine grid with the continuous metric.
- iter-4: Robustness of the selected setting to day-to-day load noise (C3: 1 of 20 seeds).
- iter-5: Sensitivity: +-20% one at a time (C3: 2.2 to 11.3).
- iter-6: Does the answer depend on the re-induction threshold?
- iter-7: Third anchor not used for selection: W05's ~2.5% decay per day.
- iter-8: Negative control: can the single-state learner meet both anchors once quantisation is removed?
- iter-9: Distinguishing prediction from Cycle 3 (decay deceleration) with the continuous selection.
- iter-10: Independent third grid (no shared points).
- iter-11: Replication of iteration 4 with new seeds.
- iter-12: Consolidation: how common are settings meeting both anchors?

## Development disclosure
Simulation code was smoke-tested before the official runs; official iterations were run in this tree and re-executed byte-identically by `Research/tools` (`gaia_tools.rerun`). Pre-registered checks were not changed after seeing results; any re-runs are listed in `../CHANGELOG.md`.
