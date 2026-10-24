# SIM-CONS-D - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K60 had usable EEG in 9 of 36 patients, 3 of whom showed delta waves during arrest. How much can be concluded about the prevalence of such activity?

## Sources this run draws on
K60: 9/36 usable EEG; 3/9 delta; 0/35 explicit recall; 3/35 other memories.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | coverage >= .9 |
| H1 | hypothesis | width > .5 |
| R1 | reporting | intervals |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Wilson intervals; missing EEG assumed unrelated to brain state. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-CONS-D",
 "iteration": 4,
 "kind": "small_ci",
 "seed": 1404,
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
 "focus": "delta_during_arrest",
 "reps": 20000,
 "h1": 0.5
}
```

## Command
`python sim_cons.py iter-4` (run from `Consciousness/simulation/`)
