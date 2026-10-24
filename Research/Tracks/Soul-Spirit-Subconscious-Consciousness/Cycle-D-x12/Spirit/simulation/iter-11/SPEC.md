# SIM-SPIRIT-D - iteration 11 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle D iteration with changed assumptions; it is not a new source-based question. Milder selection (top 50%) and higher test-retest r (0.85).

## Sources this run draws on
K52 (as iteration 7).

## Refinement from previous iteration
Iteration 7 used r 0.7, top 30%.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | 0 |
| H1 | hypothesis | >= .3 |
| R1 | reporting | d |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 7.

## Parameters
```json
{
 "sim_id": "SIM-SPIRIT-D",
 "iteration": 11,
 "kind": "prepost_rtm",
 "seed": 1211,
 "n": 400000,
 "r": 0.85,
 "q": 0.5,
 "h1": 0.3
}
```

## Command
`python sim_spirit.py iter-11` (run from `Spirit/simulation/`)
