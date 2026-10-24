# SIM-SOUL-C - iteration 8 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle C iteration with changed assumptions; it is not a new source-based question. Reliability .9 instead of .8.

## Sources this run draws on
K46 (as iteration 5).

## Refinement from previous iteration
Iteration 5 used reliability .8.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | PPV = bivariate normal |
| H1 | hypothesis | >= 20% false cases |
| R1 | reporting | agreement |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 5.

## Parameters
```json
{
 "sim_id": "SIM-SOUL-C",
 "iteration": 8,
 "kind": "cutoff_misclass",
 "seed": 618,
 "N": 1000000,
 "rel": 0.9,
 "prev": 0.37
}
```

## Command
`python sim_soul.py iter-8` (run from `Soul/simulation/`)
