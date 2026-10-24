# SIM-SUBC-C - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Jacoby's process dissociation procedure (K33) separates conscious recollection (R) from automatic influence (F) under an independence assumption. If R and F are positively correlated across items, how biased is the estimate of the automatic (unconscious) component?

## Sources this run draws on
K33 (Balota 2026): the PDP equations, the independence assumption and its criticism (correlated R and F estimates reported by Curran & Hintzman, cited in K33). Distribution parameters are ILLUSTRATIVE.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | rho 0, c 0: |F bias| <= 0.01 |
| H1 | hypothesis | rho .5: |F bias| >= .05 |
| R1 | reporting | grid |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Probit item model; one inclusion and one exclusion condition. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SUBC-C",
 "iteration": 1,
 "kind": "pdp_dependence",
 "seed": 511,
 "items": 200000,
 "aR": -0.5,
 "aF": 0.0,
 "s": 1.0,
 "rho_grid": [
  0.0,
  0.3,
  0.5,
  -0.3
 ],
 "c_grid": [
  0.0
 ],
 "rho_test": 0.5,
 "c_test": 0.0
}
```

## Command
`python sim_subc.py iter-1` (run from `Subconscious/simulation/`)
