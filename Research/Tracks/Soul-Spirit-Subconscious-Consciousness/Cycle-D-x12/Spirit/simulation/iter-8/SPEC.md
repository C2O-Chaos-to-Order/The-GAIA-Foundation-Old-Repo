# SIM-SPIRIT-D - iteration 8 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle D iteration with changed assumptions; it is not a new source-based question. The blinded rater's guesses on day 8 (12/17 psilocybin, 15/17 niacin).

## Sources this run draws on
K51 (as iteration 4).

## Refinement from previous iteration
Iteration 4 used participants' day-365 guesses.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | BI = 0 |
| H1 | hypothesis | BI >= .8 every arm |
| R1 | reporting | BI |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 4.

## Parameters
```json
{
 "sim_id": "SIM-SPIRIT-D",
 "iteration": 8,
 "kind": "blinding_index",
 "seed": 1208,
 "arms": {
  "psilocybin": [
   12,
   17
  ],
  "niacin": [
   15,
   17
  ]
 },
 "reps": 200000,
 "h1": 0.8
}
```

## Command
`python sim_spirit.py iter-8` (run from `Spirit/simulation/`)
