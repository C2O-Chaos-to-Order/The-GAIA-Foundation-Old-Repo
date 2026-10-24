# SIM-SOUL-D - iteration 10 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle D iteration with changed assumptions; it is not a new source-based question. Twice as many cases (34).

## Sources this run draws on
K53 (as iteration 5).

## Refinement from previous iteration
Iteration 5 used 17 cases.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | alpha = 1 |
| H1 | hypothesis | range >= .15 |
| R1 | reporting | quantiles |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 5.

## Parameters
```json
{
 "sim_id": "SIM-SOUL-D",
 "iteration": 10,
 "kind": "alpha_precision",
 "seed": 1110,
 "cases": 34,
 "raters": 14,
 "latent_icc": 0.5,
 "cuts": [
  -0.8,
  0.0,
  0.8
 ],
 "reps": 2000,
 "h1": 0.15
}
```

## Command
`python sim_soul.py iter-10` (run from `Soul/simulation/`)
