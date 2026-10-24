# SIM-IN-PHI-C - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication of INB-PHI iter-3 (a = 1.2 critical mass).

## Phase operationalization tested
PHI Insurgence = critical mass.

## Sources this run draws on
P30 (read in full in INA): Eq. 1 and its a = 1 logistic case; P30 notes abrupt utility changes are not in its model. P35 (van der Hoek 2023, Int J Lat Am Relig, CC BY; read in full in INB) for the historical case of a prophetic hope abandoned after news of the 1906 earthquake.

## Refinement from previous iteration
Iteration 6 of the x9 family for PHI; follows iteration 5 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | one interior point |
| H1 | hypothesis | below declines |
| H2 | hypothesis | above dominates |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Replication or variant of an earlier run (new seed); no new source. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-PHI-C",
 "iteration": 6,
 "kind": "abrams_groups",
 "seed": 22606,
 "mode": "bistable",
 "a": 1.2,
 "c": 1.0,
 "u": 0.6,
 "x0_values": [
  0.05,
  0.1,
  0.3,
  0.5
 ],
 "dt": 0.01,
 "steps": 40000
}
```

## Command
`python sim_phi.py iter-6` (run from `Philosophy-Spirituality/simulation/`)
