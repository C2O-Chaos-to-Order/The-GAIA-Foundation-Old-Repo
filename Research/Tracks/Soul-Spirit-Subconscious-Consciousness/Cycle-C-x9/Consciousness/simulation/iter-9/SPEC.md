# SIM-CONS-C - iteration 9 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle C iteration with changed assumptions; it is not a new source-based question. Extreme timing assumptions within K32's ranges (immediate 10.4%, delayed 5.9%, clinical 3%, experimental 40%).

## Sources this run draws on
K32 (as iteration 3).

## Refinement from previous iteration
Iteration 3 used midpoints.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | sim = arithmetic |
| H1 | hypothesis | timing explains < 20% |
| R1 | reporting | retention |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 3.

## Parameters
```json
{
 "sim_id": "SIM-CONS-C",
 "iteration": 9,
 "kind": "recall_gap",
 "seed": 819,
 "recall_immediate": 0.104,
 "recall_delayed": 0.059,
 "clinical_typical": 0.03,
 "experimental_typical": 0.4
}
```

## Command
`python sim_cons.py iter-9` (run from `Consciousness/simulation/`)
