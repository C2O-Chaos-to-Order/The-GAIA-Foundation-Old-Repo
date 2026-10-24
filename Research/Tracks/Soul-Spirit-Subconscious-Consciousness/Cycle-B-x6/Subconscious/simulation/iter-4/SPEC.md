# SIM-SUBC-B - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K22 found an unconscious-thought effect in two of three experiments (822 participants). What patterns across three experiments does a small true effect predict?

## Sources this run draws on
K22 (Steindorf, Rummel & Boywitt 2021): 822 participants, three experiments, effect present in the first two only; authors note power limits. n per condition here (90) is ILLUSTRATIVE, not K22's.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | simulated power = analytic |
| H1 | hypothesis | d = .2: >= 2 of 3 significant with p >= .5 |
| R1 | reporting | patterns by d |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Two-group t-tests; independent experiments; illustrative n. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SUBC-B",
 "iteration": 4,
 "kind": "ute_mixed",
 "seed": 114,
 "n_per_group": 90,
 "k_exp": 3,
 "d_grid": [
  0.0,
  0.2,
  0.35,
  0.5
 ],
 "reps": 20000
}
```

## Command
`python sim_subc.py iter-4` (run from `Subconscious/simulation/`)
