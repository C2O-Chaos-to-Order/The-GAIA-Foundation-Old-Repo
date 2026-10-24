# SIM-SOUL-C - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K46 reports that NDE narratives showed 'descriptively higher' frequencies of six features than NDE-like narratives (23 vs 25). With NO true difference, how often would at least one feature look 15 points higher?

## Sources this run draws on
K46: six named features; groups of 23 and 25. Base rates ILLUSTRATIVE.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | null share ~ normal approx |
| H1 | hypothesis | P(any >= 15 points) >= .5 under no difference |
| R1 | reporting | shares |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Independent features; one direction only. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SOUL-C",
 "iteration": 4,
 "kind": "descriptive_differences",
 "seed": 614,
 "n1": 23,
 "n2": 25,
 "base_rates": [
  0.5,
  0.4,
  0.3,
  0.3,
  0.2,
  0.15
 ],
 "true_shift": 0.0,
 "delta": 0.15,
 "reps": 100000
}
```

## Command
`python sim_soul.py iter-4` (run from `Soul/simulation/`)
