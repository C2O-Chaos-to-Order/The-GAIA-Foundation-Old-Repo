# SIM-SUBC-C - iteration 7 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Second PDP assumption (K33): recollection must act the same way in inclusion and exclusion. If some recollected items slip through in exclusion (crosstalk c), how biased are the estimates?

## Sources this run draws on
K33: the assumption that R and F are the same in inclusion and exclusion conditions, and possible crosstalk between the processes.

## Refinement from previous iteration
Iteration 1 varied the R-F correlation; this iteration varies crosstalk with independence held.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | c 0: |F bias| <= .01 |
| H1 | hypothesis | c .1: |F bias| >= .05 |
| R1 | reporting | grid |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 1. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SUBC-C",
 "iteration": 7,
 "kind": "pdp_dependence",
 "seed": 517,
 "items": 200000,
 "aR": -0.5,
 "aF": 0.0,
 "s": 1.0,
 "rho_grid": [
  0.0
 ],
 "c_grid": [
  0.0,
  0.05,
  0.1,
  0.2
 ],
 "rho_test": 0.0,
 "c_test": 0.1
}
```

## Command
`python sim_subc.py iter-7` (run from `Subconscious/simulation/`)
