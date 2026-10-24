# SIM-DV-APP-C - iteration 7 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
DVA clonal-tail run repeated (N = 5000) with a new seed: the DVA R^2 < 0.98 finding replicated?

## Phase operationalization tested
APP Divergence = neutral subclonal tail 1/f (P04).

## Sources this run draws on
P04 (re-read in full in DVB; quality flag).

## Refinement from previous iteration
Seed only.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | as DVA |
| H1 | hypothesis | as DVA (R^2 >= 0.98) |
| R1 | reporting | as DVA |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As DVA. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-APP-C",
 "iteration": 7,
 "kind": "clonal_branching_reps",
 "seed": 17407,
 "N": 5000,
 "birth": 1.0,
 "death": 0.3,
 "u": 2.0,
 "fmin": 0.1,
 "fmax": 0.4,
 "reps": 5,
 "h1": 0.98
}
```

## Command
`python sim_app.py iter-7` (run from `Applied-Sciences/simulation/`)
