# SIM-SOUL-D - iteration 7 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle D iteration with changed assumptions; it is not a new source-based question. Item rates 20% lower (country-level variation).

## Sources this run draws on
K61 (as iteration 1).

## Refinement from previous iteration
Iteration 1 used the pooled rates.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | sim P(any) = analytic |
| H1 | hypothesis | gap >= .20 |
| H2 | hypothesis | factor >= 2 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 1.

## Parameters
```json
{
 "sim_id": "SIM-SOUL-D",
 "iteration": 7,
 "kind": "continuity_dependence",
 "seed": 1107,
 "p_bodily": 0.13,
 "p_mental": 0.38,
 "n_items_each": 3,
 "share_any_reported": 0.61,
 "share_all_reported": 0.02,
 "h1_gap": 0.2,
 "n": 500000
}
```

## Command
`python sim_soul.py iter-7` (run from `Soul/simulation/`)
