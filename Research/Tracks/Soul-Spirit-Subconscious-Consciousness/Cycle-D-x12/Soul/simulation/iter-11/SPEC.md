# SIM-SOUL-D - iteration 11 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle D iteration with changed assumptions; it is not a new source-based question. Optimistic stages (survival 0.25, interviewable 0.7, OBE 0.2, target room 0.5, in view 0.5).

## Sources this run draws on
K53, K54 (as iteration 6).

## Refinement from previous iteration
Iteration 6 used central illustrative stages.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | sim P = .8 |
| H1 | hypothesis | N >= 1000 |
| R1 | reporting | N |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 6.

## Parameters
```json
{
 "sim_id": "SIM-SOUL-D",
 "iteration": 11,
 "kind": "veridical_yield",
 "seed": 1111,
 "stages": [
  0.25,
  0.7,
  0.2,
  0.5,
  0.5
 ],
 "power": 0.8,
 "reps": 200000,
 "h1": 1000
}
```

## Command
`python sim_soul.py iter-11` (run from `Soul/simulation/`)
