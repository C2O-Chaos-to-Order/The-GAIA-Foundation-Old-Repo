# SIM-SPIRIT-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Original awe experiments reported effects on several outcome families (agency detection, prosociality, well-being, supernatural belief: K05). Under no true effect, how often is at least one of four outcomes significant?

## Sources this run draws on
K05 (outcome families listed in its Study 1 hypotheses).

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | r = 0 matches 1 - .95^4 |
| H1 | hypothesis | r = .3: family-wise rate > .15 |
| R1 | reporting | rate by r |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Equicorrelated normal outcomes; no correction. Says nothing about any specific original study's analysis. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SPIRIT-A",
 "iteration": 3,
 "kind": "multiple_outcomes",
 "seed": 303,
 "k": 4,
 "n": 60,
 "r_grid": [
  0.0,
  0.3,
  0.6
 ],
 "r_test": 0.3,
 "reps": 6000
}
```

## Command
`python sim_spirit.py iter-3` (run from `Spirit/simulation/`)
