# SIM-CONS-D - iteration 9 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle D iteration with changed assumptions; it is not a new source-based question. Focus on usable-EEG rate (9/36).

## Sources this run draws on
K60 (as iteration 4).

## Refinement from previous iteration
Iteration 4 focused on delta waves.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | coverage |
| H1 | hypothesis | width > .5 |
| R1 | reporting | intervals |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 4.

## Parameters
```json
{
 "sim_id": "SIM-CONS-D",
 "iteration": 9,
 "kind": "small_ci",
 "seed": 1409,
 "counts": {
  "delta_during_arrest": [
   3,
   9
  ],
  "usable_eeg": [
   9,
   36
  ],
  "explicit_recall": [
   0,
   35
  ],
  "other_memories": [
   3,
   35
  ]
 },
 "focus": "usable_eeg",
 "reps": 20000,
 "h1": 0.5
}
```

## Command
`python sim_cons.py iter-9` (run from `Consciousness/simulation/`)
