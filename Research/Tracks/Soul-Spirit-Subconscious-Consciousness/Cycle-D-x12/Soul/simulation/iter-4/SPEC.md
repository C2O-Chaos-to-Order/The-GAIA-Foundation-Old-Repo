# SIM-SOUL-D - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K55: mattering slopes on mind-upload approval were -0.28 (uncertain about an afterlife) and -0.18 (certain there is none). Is the difference between the slopes itself significant?

## Sources this run draws on
K55 Results: B = -0.28 [-0.43, -0.12] (uncertain); B = -0.18 [-0.35, -0.01] (no afterlife).

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | sim z = analytic |
| H1 | hypothesis | |z| < 1.96 |
| R1 | reporting | z, p |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Treats the two slopes as independent estimates; the proper test is the interaction term in K55's model. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SOUL-D",
 "iteration": 4,
 "kind": "slope_diff",
 "seed": 1104,
 "b1": -0.28,
 "ci1": [
  -0.43,
  -0.12
 ],
 "b2": -0.18,
 "ci2": [
  -0.35,
  -0.01
 ],
 "reps": 500000
}
```

## Command
`python sim_soul.py iter-4` (run from `Soul/simulation/`)
