# SIM-DV-APP-C - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P17 error scaling for a faster decay (a = -2).

## Phase operationalization tested
APP Divergence = discretisation error and its O(h) scaling (P17).

## Sources this run draws on
P17 (read in full in DVB).

## Refinement from previous iteration
a -0.5 -> -2.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | iteration = closed form |
| H1 | hypothesis | slope within 0.1 of 1 |
| R1 | reporting | errors, slope |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As DVB. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-APP-C",
 "iteration": 5,
 "kind": "euler_order",
 "seed": 17405,
 "a": -2.0,
 "y0": 1.0,
 "T": 10,
 "h_values": [
  0.1,
  0.05,
  0.02,
  0.01,
  0.005
 ],
 "h1": 0.1
}
```

## Command
`python sim_app.py iter-5` (run from `Applied-Sciences/simulation/`)
