# SIM-CONS-D - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K59 (protocol for an IIT-GNWT adversarial collaboration in macaques and mice) plans Bayesian t-tests until BF >= 10 for either hypothesis, with at least 9 and at most 15 recording sessions per macaque. How often will that plan end with strong evidence?

## Sources this run draws on
K59 'Bayes factor analysis': Cauchy r = .707, BF >= 10, minimum 9 sessions, maximum 15 per NHP. Per-session effect sizes ILLUSTRATIVE.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | misleading H1 <= 5% |
| H1 | hypothesis | d=0 inconclusive >= 50% |
| R1 | reporting | rates |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
One-sample test across sessions; sessions independent. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-CONS-D",
 "iteration": 1,
 "kind": "bf_sequential",
 "seed": 1401,
 "d_grid": [
  0.0,
  0.5,
  0.8,
  1.2
 ],
 "n_min": 9,
 "n_max": 15,
 "bound": 10,
 "reps": 1000,
 "h1": 0.5
}
```

## Command
`python sim_cons.py iter-1` (run from `Consciousness/simulation/`)
