# SIM-SPIRIT-D - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K50 argues functional unblinding mixes drug effects with positive (active arm) and negative (placebo arm) expectancy. With K51's sample size and outcome SD, how often would expectancy alone produce a significant result?

## Sources this run draws on
K50 (functional unblinding; positive and negative expectancy); K51: n = 17 vs 18; SD of MADRS change derived from the day-8 CI (-12.89 to -1.65): SE 2.87, SD about 8.5. Expectancy +/-3.5 points is ILLUSTRATIVE.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | e = 0 FPR = .05 |
| H1 | hypothesis | P(p<.05) >= .5 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Normal outcomes; no true drug effect by construction. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SPIRIT-D",
 "iteration": 5,
 "kind": "expectancy_bias",
 "seed": 1205,
 "n1": 17,
 "n2": 18,
 "sd": 8.5,
 "e": 3.5,
 "reps": 50000,
 "h1": 0.5
}
```

## Command
`python sim_spirit.py iter-5` (run from `Spirit/simulation/`)
