# SIM-IN-NAT-B - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication of INA-NAT-03 with L = 20 and r down to 1e-5.

## Phase operationalization tested
NAT Insurgence = bottleneck (replication).

## Sources this run draws on
P22 (read in full in DVC); agent's integral.

## Refinement from previous iteration
Iteration 6 of the x6 family for NAT; follows iteration 5 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | within 0.5% |
| H1 | hypothesis | slope within 0.05 of -1/2 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-NAT-B",
 "iteration": 6,
 "kind": "saddle_bottleneck",
 "seed": 21106,
 "r_values": [
  1e-05,
  0.0001,
  0.001,
  0.01
 ],
 "L": 20,
 "dt": 0.01,
 "tol": 0.005,
 "h1": 0.05
}
```

## Command
`python sim_nat.py iter-6` (run from `Natural-Sciences/simulation/`)
