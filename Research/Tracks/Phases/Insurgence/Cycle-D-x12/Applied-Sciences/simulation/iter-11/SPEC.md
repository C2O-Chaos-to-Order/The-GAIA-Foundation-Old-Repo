# SIM-IN-APP-D - iteration 11 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication of INB-APP iter-4 (immunity plus heterogeneity).

## Phase operationalization tested
APP Insurgence = emergence suppressed by immunity, heterogeneous.

## Sources this run draws on
P26 (effective R), P32 (k).

## Refinement from previous iteration
Iteration 11 of the x12 family for APP; follows iteration 10 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | within 4 SE (+0.002) of 1 - q |
| H1 | hypothesis | no major outbreak when R0 (1 - v) < 1 |
| H2 | hypothesis | calendar time scales |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Replication or variant of an earlier run (new seed); no new source. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-APP-D",
 "iteration": 11,
 "kind": "branching_outbreak",
 "seed": 23411,
 "R0": [
  1.6,
  2.5,
  4.0
 ],
 "k": 0.27,
 "v": 0.5,
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
`python sim_app.py iter-11` (run from `Applied-Sciences/simulation/`)
