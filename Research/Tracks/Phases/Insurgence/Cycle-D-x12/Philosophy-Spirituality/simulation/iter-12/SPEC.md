# SIM-IN-PHI-D - iteration 12 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication of INB-PHI iter-2 (late shock).

## Phase operationalization tested
PHI Insurgence = reversal of an established stance.

## Sources this run draws on
P30 (read in full in INA): Eq. 1 and its a = 1 logistic case; P30 notes abrupt utility changes are not in its model. P35 (van der Hoek 2023, Int J Lat Am Relig, CC BY; read in full in INB) for the historical case of a prophetic hope abandoned after news of the 1906 earthquake.

## Refinement from previous iteration
Iteration 12 of the x12 family for PHI; follows iteration 11 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | x in [0, 1] |
| H1 | hypothesis | below 0.05 by t = 120 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Replication or variant of an earlier run (new seed); no new source. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-PHI-D",
 "iteration": 12,
 "kind": "abrams_groups",
 "seed": 23612,
 "mode": "shock",
 "c": 1.0,
 "u": 0.65,
 "u_after": 0.4,
 "x0": 0.01,
 "t_shock": 30,
 "dt": 0.01,
 "tmax": 120,
 "h1": 0.05
}
```

## Command
`python sim_phi.py iter-12` (run from `Philosophy-Spirituality/simulation/`)
