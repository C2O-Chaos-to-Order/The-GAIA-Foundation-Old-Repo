# SIM-SPIRIT-C - iteration 8 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle C iteration with changed assumptions; it is not a new source-based question. Twice as many studies per dose (12 vs 6).

## Sources this run draws on
K40 (as iteration 4).

## Refinement from previous iteration
Iteration 4 used 6 vs 3 studies.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | Emax(ED50) |
| H1 | hypothesis | plateau called >= 50% |
| R1 | reporting | true rise |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 4.

## Parameters
```json
{
 "sim_id": "SIM-SPIRIT-C",
 "iteration": 8,
 "kind": "dose_plateau",
 "seed": 718,
 "doses": [
  25,
  50,
  100,
  200
 ],
 "Emax": 100.0,
 "ED50": 50.0,
 "h": 2.0,
 "sd_between": 15.0,
 "k100": 12,
 "k200": 6,
 "reps": 20000
}
```

## Command
`python sim_spirit.py iter-8` (run from `Spirit/simulation/`)
