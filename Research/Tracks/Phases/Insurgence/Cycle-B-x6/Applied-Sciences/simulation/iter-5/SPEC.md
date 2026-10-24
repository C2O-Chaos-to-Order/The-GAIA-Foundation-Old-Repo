# SIM-IN-APP-B - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication of INA-APP-04 (R0 = 0.95, 1.05, 1.2, Poisson) on a new seed.

## Phase operationalization tested
APP Insurgence = near-threshold emergence (replication).

## Sources this run draws on
P26; standard branching model.

## Refinement from previous iteration
Iteration 5 of the x6 family for APP; follows iteration 4 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | within 4 SE (+0.002) of 1 - q |
| H1 | hypothesis | no major outbreak when R0 (1 - v) < 1 |
| H2 | hypothesis | calendar time scales |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-APP-B",
 "iteration": 5,
 "kind": "branching_outbreak",
 "seed": 21405,
 "R0": [
  0.95,
  1.05,
  1.2
 ],
 "reps": 20000,
 "K": 1000,
 "Tg": [
  3,
  15
 ],
 "tol_se": 4
}
```

## Command
`python sim_app.py iter-5` (run from `Applied-Sciences/simulation/`)
