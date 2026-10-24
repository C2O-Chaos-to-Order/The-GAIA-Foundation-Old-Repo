# SIM-SPIRIT-D - iteration 10 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle D iteration with changed assumptions; it is not a new source-based question. Weaker general factor (loading 0.6) and mean 0.55.

## Sources this run draws on
K49 (as iteration 2).

## Refinement from previous iteration
Iteration 2 used loading 0.8, mean 0.6.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | no disagreement |
| H1 | hypothesis | >= 10% |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 2.

## Parameters
```json
{
 "sim_id": "SIM-SPIRIT-D",
 "iteration": 10,
 "kind": "cutoff_reliability",
 "seed": 1210,
 "alphas": [
  0.97,
  0.92,
  0.86,
  0.9
 ],
 "lam": 0.6,
 "mean": 0.55,
 "sd": 0.2,
 "n": 400000,
 "h1": 0.1
}
```

## Command
`python sim_spirit.py iter-10` (run from `Spirit/simulation/`)
