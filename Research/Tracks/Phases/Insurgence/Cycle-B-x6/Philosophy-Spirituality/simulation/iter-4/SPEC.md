# SIM-IN-PHI-B - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Clique delay with u = 0.7: is the delay still linear in -ln p/(2u - 1) (r^2 > 0.95)?

## Phase operationalization tested
PHI Insurgence = spread out of a clique.

## Sources this run draws on
P30 (read in full in INA): Eq. 1 and its a = 1 logistic case; P30 notes abrupt utility changes are not in its model. P35 (van der Hoek 2023, Int J Lat Am Relig, CC BY; read in full in INB) for the historical case of a prophetic hope abandoned after news of the 1906 earthquake.

## Refinement from previous iteration
Iteration 4 of the x6 family for PHI; follows iteration 3 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | all reach 0.5 |
| H1 | hypothesis | r^2 > 0.95 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-PHI-B",
 "iteration": 4,
 "kind": "abrams_groups",
 "seed": 21604,
 "mode": "cliques",
 "c": 1.0,
 "u": 0.7,
 "x0": 0.1,
 "p_values": [
  0.001,
  0.01,
  0.03,
  0.1,
  0.3,
  1.0
 ],
 "dt": 0.01,
 "tmax": 5000,
 "h1": 0.95
}
```

## Command
`python sim_phi.py iter-4` (run from `Philosophy-Spirituality/simulation/`)
