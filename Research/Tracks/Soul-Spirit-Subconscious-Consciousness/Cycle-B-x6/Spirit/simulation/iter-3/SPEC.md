# SIM-SPIRIT-B - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Sensitivity of SIM-SPIRIT-A iteration 2: with a stricter cut (80th percentile on every subscale) how stable is a binary 'complete experience' classification?

## Sources this run draws on
K04 (Stocker et al. 2026) as in Cycle A; cut ILLUSTRATIVE.

## Refinement from previous iteration
Cycle A used the 60th percentile; here the 80th.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | omega 1 agreement 1 |
| H1 | hypothesis | >= 80% re-classified |
| R1 | reporting | kappa |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As Cycle A. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SPIRIT-B",
 "iteration": 3,
 "kind": "threshold_classification",
 "seed": 313,
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
 "cut_quantile": 0.8
}
```

## Command
`python sim_spirit.py iter-3` (run from `Spirit/simulation/`)
