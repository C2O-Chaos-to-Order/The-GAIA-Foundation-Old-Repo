# SIM-IN-NAT-D - iteration 9 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication of INC-NAT iter-9 on a new seed (x12 replication pass; adds no new source).

## Phase operationalization tested
NAT Insurgence = onset timing under noise.

## Sources this run draws on
P22 Eq. 8.8 (read in full in DVC).

## Refinement from previous iteration
Iteration 9 of the x12 family for NAT; follows iteration 8 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | no censoring |
| H1 | hypothesis | advance > 4 SE |
| H2 | hypothesis | CV > 0.1 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Replication or variant of an earlier run (new seed); no new source. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-NAT-D",
 "iteration": 9,
 "kind": "transcritical_noise",
 "seed": 23109,
 "r": 0.05,
 "x0": 0.001,
 "sigma": 0.002,
 "dt": 0.05,
 "reps": 200,
 "tmax": 2000,
 "tol_se": 4,
 "h2": 0.1
}
```

## Command
`python sim_nat.py iter-9` (run from `Natural-Sciences/simulation/`)
