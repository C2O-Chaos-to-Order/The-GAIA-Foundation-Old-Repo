# SIM-SPIRIT-D - iteration 12 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle D iteration with changed assumptions; it is not a new source-based question. Lower reliabilities (0.80 on every subscale).

## Sources this run draws on
K49 (as iteration 2).

## Refinement from previous iteration
Iteration 2 used K49's reliabilities.

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
 "iteration": 12,
 "kind": "cutoff_reliability",
 "seed": 1212,
 "alphas": [
  0.8,
  0.8,
  0.8,
  0.8
 ],
 "lam": 0.8,
 "mean": 0.6,
 "sd": 0.2,
 "n": 400000,
 "h1": 0.1
}
```

## Command
`python sim_spirit.py iter-12` (run from `Spirit/simulation/`)
