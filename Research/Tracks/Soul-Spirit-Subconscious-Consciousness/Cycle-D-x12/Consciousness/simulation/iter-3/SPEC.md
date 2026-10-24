# SIM-CONS-D - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K60: none of 36 patients recalled the three fruit names played during deep hypothermic circulatory arrest, but 3 'correctly guessed' them, read as a possible sign of implicit learning. Is 3/36 above chance?

## Sources this run draws on
K60 Abstract/Results: 3/36 (9%) correctly guessed. Fruit-pool sizes ILLUSTRATIVE (K60's guessing chance is not stated in the parts read).

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | sim tail = .05 |
| H1 | hypothesis | cut-off chance < .03 |
| R1 | reporting | p by pool |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Unordered guess of 3 from a pool; guesses independent. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-CONS-D",
 "iteration": 3,
 "kind": "implicit_guess",
 "seed": 1403,
 "k": 3,
 "n": 36,
 "pools": [
  5,
  8,
  10,
  20
 ],
 "reps": 1000000,
 "h1": 0.03
}
```

## Command
`python sim_cons.py iter-3` (run from `Consciousness/simulation/`)
