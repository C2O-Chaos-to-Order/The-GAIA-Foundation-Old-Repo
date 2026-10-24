# SIM-SUBC-D - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K63 (registered report) found Bayesian evidence that reducing free-will belief changes neither cognitive control nor automaticity. At its sample size, how often would a small true effect (d = 0.2) still yield BF01 >= 3?

## Sources this run draws on
K63: Bayesian sequential registered report; manipulation check d = .75 with n = 309 (pro) and 272 (anti); main analyses mostly supported the null. Default JZS prior r = 0.707 assumed (K63's exact prior not re-read).

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | known BF range |
| H1 | hypothesis | P(BF01>=3 | d=.2) <= .05 |
| R1 | reporting | rates |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Two-sample t on one index; K63 used several indices and sequential stopping. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SUBC-D",
 "iteration": 1,
 "kind": "bf_null_design",
 "seed": 1301,
 "n1": 309,
 "n2": 272,
 "d_grid": [
  0.0,
  0.2,
  0.3
 ],
 "d_test": 0.2,
 "reps": 1000,
 "h1": 0.05
}
```

## Command
`python sim_subc.py iter-1` (run from `Subconscious/simulation/`)
