# SIM-SPIRIT-D - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K51 (psilocybin vs niacin RCT in depression) reports that 16 of 17 psilocybin and 16 of 16 niacin participants guessed their allocation on day 365. How badly did blinding fail?

## Sources this run draws on
K51 'Blinding Integrity': 16/17 (94.1%) psilocybin, 16/16 (100%) niacin.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | random guessing BI = 0 |
| H1 | hypothesis | BI >= .8 in every arm |
| R1 | reporting | BI |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Bang index without a 'don't know' option. Guesses were collected at day 365, after outcomes were known to participants. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SPIRIT-D",
 "iteration": 4,
 "kind": "blinding_index",
 "seed": 1204,
 "arms": {
  "psilocybin": [
   16,
   17
  ],
  "niacin": [
   16,
   16
  ]
 },
 "reps": 200000,
 "h1": 0.8
}
```

## Command
`python sim_spirit.py iter-4` (run from `Spirit/simulation/`)
