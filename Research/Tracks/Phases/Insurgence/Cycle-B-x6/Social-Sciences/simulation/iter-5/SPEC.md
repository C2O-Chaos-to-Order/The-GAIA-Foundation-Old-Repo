# SIM-IN-SOC-B - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication of INA-SOC-04 (N = 100) on a new seed.

## Phase operationalization tested
SOC Insurgence = threshold cascade (replication).

## Sources this run draws on
P25 (read in full in IN0); agent's toy.

## Refinement from previous iteration
Iteration 5 of the x6 family for SOC; follows iteration 4 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | uniform full cascade |
| H1 | hypothesis | one change stops it |
| H2 | hypothesis | jump > 0.3 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-SOC-B",
 "iteration": 5,
 "kind": "threshold_cascade",
 "seed": 21305,
 "N": 100,
 "mu": 25,
 "sd_values": [
  5,
  6,
  7,
  8,
  9,
  10,
  11,
  12,
  13,
  14,
  15,
  16,
  17,
  18,
  19,
  20
 ],
 "reps": 100,
 "h2": 0.3
}
```

## Command
`python sim_soc.py iter-5` (run from `Social-Sciences/simulation/`)
