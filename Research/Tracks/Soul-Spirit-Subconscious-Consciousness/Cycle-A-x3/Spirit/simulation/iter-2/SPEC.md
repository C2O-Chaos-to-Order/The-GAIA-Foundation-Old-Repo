# SIM-SPIRIT-A - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Mystical-experience research often turns four MEQ30 subscales into a binary 'complete' experience by a cut on every subscale. With the high internal consistency K04 reports, how stable is such a binary across two measurements?

## Sources this run draws on
K04 (Stocker et al. 2026): English PES48/MEQ30 validation, 280 measurements, high internal consistency for the MEQ subscales. The cut used here (each subscale above its 60th percentile) is ILLUSTRATIVE; the standard 'complete mystical experience' criterion was not read in K04.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | omega = 1: agreement = 1 |
| H1 | hypothesis | omega = .9: >= 80% of classified are re-classified at retest |
| R1 | reporting | binary kappa by omega |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Classical test theory; errors independent across occasions; true scores stable (no real change between measurements). Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SPIRIT-A",
 "iteration": 2,
 "kind": "threshold_classification",
 "seed": 302,
 "k": 4,
 "N": 20000,
 "r_between": 0.6,
 "omega_grid": [
  0.8,
  0.85,
  0.9,
  0.95,
  1.0
 ],
 "omega_test": 0.9,
 "cut_quantile": 0.6
}
```

## Command
`python sim_spirit.py iter-2` (run from `Spirit/simulation/`)
