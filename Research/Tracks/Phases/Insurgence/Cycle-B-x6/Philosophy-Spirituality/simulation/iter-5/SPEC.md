# SIM-IN-PHI-B - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Neutral utility u = 0.5 with a = 1: does the stance stay where it starts (no insurgence without a utility edge)?

## Phase operationalization tested
PHI Insurgence = no growth without advantage.

## Sources this run draws on
P30 (read in full in INA): Eq. 1 and its a = 1 logistic case; P30 notes abrupt utility changes are not in its model. P35 (van der Hoek 2023, Int J Lat Am Relig, CC BY; read in full in INB) for the historical case of a prophetic hope abandoned after news of the 1906 earthquake.

## Refinement from previous iteration
Iteration 5 of the x6 family for PHI; follows iteration 4 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | RK4 matches logistic |
| H1 | hypothesis | t_half <= 20 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
At u = 0.5 the logistic rate is 0, so t_half is infinite; H1 is expected not supported (foreknown by the formula; documents the null case). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-PHI-B",
 "iteration": 5,
 "kind": "abrams_groups",
 "seed": 21605,
 "mode": "logistic",
 "c": 1.0,
 "u": 0.5000001,
 "x0": 0.01,
 "dt": 0.01,
 "steps": 5000,
 "quantiles": [
  0.1,
  0.5,
  0.9
 ],
 "t_check": 20
}
```

## Command
`python sim_phi.py iter-5` (run from `Philosophy-Spirituality/simulation/`)
