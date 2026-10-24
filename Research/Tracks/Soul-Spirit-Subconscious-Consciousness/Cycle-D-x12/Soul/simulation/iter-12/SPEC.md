# SIM-SOUL-D - iteration 12 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle D iteration with changed assumptions; it is not a new source-based question. Upper credible bound of heterogeneity (sigma 0.32) and no estimation error.

## Sources this run draws on
K61 (as iteration 2).

## Refinement from previous iteration
Iteration 2 used sigma 0.22 and SE 0.15.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | sim = analytic |
| H1 | hypothesis | >= .2 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 2.

## Parameters
```json
{
 "sim_id": "SIM-SOUL-D",
 "iteration": 12,
 "kind": "hetero_sign",
 "seed": 1112,
 "mu": 0.52,
 "sigma": 0.32,
 "countries": 24,
 "se": 0.0,
 "reps": 200000,
 "h1": 0.2
}
```

## Command
`python sim_soul.py iter-12` (run from `Soul/simulation/`)
