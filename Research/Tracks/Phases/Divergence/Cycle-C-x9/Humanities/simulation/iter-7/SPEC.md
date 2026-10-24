# SIM-DV-HUM-C - iteration 7 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
List-size run at half the DVA replacement rate (r = 0.035).

## Phase operationalization tested
HUM Divergence = lexical replacement on word lists.

## Sources this run draws on
As DVA.

## Refinement from previous iteration
Only r and seed change.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | as DVA |
| H1 | hypothesis | as DVA |
| R1 | reporting | as DVA |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As DVA. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-HUM-C",
 "iteration": 7,
 "kind": "list_size",
 "seed": 17507,
 "r": 0.035,
 "T": 3.0,
 "list_sizes": [
  40,
  100,
  200
 ],
 "reps": 20000,
 "tol_se": 4,
 "h1": 0.25
}
```

## Command
`python sim_hum.py iter-7` (run from `Humanities/simulation/`)
