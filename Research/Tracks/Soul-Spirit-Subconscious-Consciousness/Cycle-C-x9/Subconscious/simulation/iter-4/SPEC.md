# SIM-SUBC-C - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Mind x Justice. K35 found no country-level association between mean free will belief and death-penalty endorsement (b = 0.65, SE = 0.74, 38 countries) and attributes this to low power. Is that right?

## Sources this run draws on
K35 (Walton, Kirkland & Bastian 2026): b = 0.65, SE = 0.74, p = .385; death-penalty data for 38 of 44 countries.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | MC within .03 of analytic |
| H1 | hypothesis | power < .5 |
| R1 | reporting | power by n |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Treats the reported b as the true slope (a best case for power); sx is ILLUSTRATIVE and only scales the residual SD.

## Parameters
```json
{
 "sim_id": "SIM-SUBC-C",
 "iteration": 4,
 "kind": "country_power",
 "seed": 514,
 "b": 0.65,
 "se": 0.74,
 "n_countries": 38,
 "sx": 0.3,
 "alpha": 0.05,
 "reps": 20000,
 "n_grid": [
  38,
  44,
  100,
  200
 ]
}
```

## Command
`python sim_subc.py iter-4` (run from `Subconscious/simulation/`)
