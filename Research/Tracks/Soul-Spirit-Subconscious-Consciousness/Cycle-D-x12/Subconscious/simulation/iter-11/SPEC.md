# SIM-SUBC-D - iteration 11 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle D iteration with changed assumptions; it is not a new source-based question. Very selective outcome (top 2%).

## Sources this run draws on
K56 (as iteration 2).

## Refinement from previous iteration
Iteration 2 selected the top 10%.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | ratio 1 |
| H1 | hypothesis | >= 1.2 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 2.

## Parameters
```json
{
 "sim_id": "SIM-SUBC-D",
 "iteration": 11,
 "kind": "aggregate_disparity",
 "seed": 1311,
 "n": 1000000,
 "r_shift": 0.2,
 "top": 0.02,
 "h1": 1.2
}
```

## Command
`python sim_subc.py iter-11` (run from `Subconscious/simulation/`)
