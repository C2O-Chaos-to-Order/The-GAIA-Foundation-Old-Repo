# Report-5-Consciousness — Cycle 4 change log

## Claims added or annotated (what and why)
- C0v2-R5-07 (H): Context added in Cycle 4: Y01/Y02 report reverberating, slightly subcritical dynamics in animal spike data (C4-R5-02). This claim concerns psychedelic states (entropic brain); label unchanged (Hypothetical).
- C3-R5-01 (P): Caution from Cycle 4: in MR estimates, non-stationary input can mimic near-criticality (C4-R5-05).
- C4-R5-01 (E): New in Cycle 4.
- C4-R5-02 (P): New in Cycle 4.
- C4-R5-03 (E): New in Cycle 4.
- C4-R5-04 (E): New in Cycle 4.
- C4-R5-05 (E): New in Cycle 4.

## Simulation iterations (what changed and why)
- iter-1: Code check for the new measure: PAR stationary mean and full-sampling estimator.
- iter-2: Replicate Y01's central claim: conventional estimation underestimates m under subsampling.
- iter-3: Does the MR estimator recover m under the same subsampling?
- iter-4: Generality across branching ratio and sampling fraction.
- iter-5: Near-critical, sparse sampling (m 0.99, alpha 0.01): how long must recordings be?
- iter-6: Avalanche statistics under subsampling (Y02).
- iter-7: Y02's 'driven' regime: with more input, avalanches merge; does MR still work?
- iter-8: Can sparse sampling (1%) still tell 'slightly subcritical' (0.98) from 'critical' (0.999)?
- iter-9: Challenge: non-stationary input, a known weakness of autoregressive estimators.
- iter-10: Translate m into an autocorrelation time, the quantity Y01 reports for cortex (100-2000 ms).
- iter-11: Replication of iteration 4 with new seeds.
- iter-12: Negative control: destroy temporal order.

## Development disclosure
Simulation code was smoke-tested before the official runs; official iterations were run in this tree and re-executed byte-identically by `Research/tools` (`gaia_tools.rerun`). Pre-registered checks were not changed after seeing results; any re-runs are listed in `../CHANGELOG.md`.
