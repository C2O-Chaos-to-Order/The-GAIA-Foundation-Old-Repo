# SIM-DV-FOR-C - iteration 7 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication of DVB iteration 4 with a new seed and longer orbits.

## Phase operationalization tested
FOR Divergence = average separation coexisting with local convergence (P09).

## Sources this run draws on
P09 (re-read in full in DVB).

## Refinement from previous iteration
n 20,000 -> 50,000; seed changes.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | share within 4 SE of analytic |
| H1 | hypothesis | share > 0.1 |
| H2 | hypothesis | all finite-time exponents positive |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As DVB. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-FOR-C",
 "iteration": 7,
 "kind": "local_shrink",
 "seed": 17207,
 "orbits": 200,
 "burn": 100,
 "n": 50000,
 "tol_se": 4,
 "h1": 0.1
}
```

## Command
`python sim_for.py iter-7` (run from `Formal-Sciences/simulation/`)
