# SIM-SUBC-D - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K56 cites a state-level correlation of 0.64 between the 1860 enslaved-to-free ratio and mean implicit race bias today. How does a state-level correlation relate to the individual-level association?

## Sources this run draws on
K56 (r = 0.64, state level; r = 0.32 with current Black representation). Individual-level slope 0.05, 50 states and 2,000 respondents per state ILLUSTRATIVE.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | individual r = analytic |
| H1 | hypothesis | state r >= .6 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
No confounding at state level unless state_noise > 0. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SUBC-D",
 "iteration": 3,
 "kind": "ecological_inflation",
 "seed": 1303,
 "states": 50,
 "per_state": 2000,
 "b_ind": 0.05,
 "state_noise": 0.02,
 "reps": 200,
 "h1": 0.6
}
```

## Command
`python sim_subc.py iter-3` (run from `Subconscious/simulation/`)
