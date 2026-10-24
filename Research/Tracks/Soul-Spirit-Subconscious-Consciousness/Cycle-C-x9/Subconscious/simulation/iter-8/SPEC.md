# SIM-SUBC-C - iteration 8 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle C iteration with changed assumptions; it is not a new source-based question. K35 country-level power if all 44 countries had death-penalty data (SE scaled by sqrt(38/44)).

## Sources this run draws on
K35 (as iteration 4).

## Refinement from previous iteration
Iteration 4 used 38 countries.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | MC within .03 |
| H1 | hypothesis | power < .5 |
| R1 | reporting | power by n |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 4.

## Parameters
```json
{
 "sim_id": "SIM-SUBC-C",
 "iteration": 8,
 "kind": "country_power",
 "seed": 518,
 "b": 0.65,
 "se": 0.6877,
 "n_countries": 44,
 "sx": 0.3,
 "alpha": 0.05,
 "reps": 20000,
 "n_grid": [
  44,
  100,
  200,
  400
 ]
}
```

## Command
`python sim_subc.py iter-8` (run from `Subconscious/simulation/`)
