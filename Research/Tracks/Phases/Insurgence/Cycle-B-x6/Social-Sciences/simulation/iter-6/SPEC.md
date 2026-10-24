# SIM-IN-SOC-B - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Higher mean threshold (mean 40, N = 100): is a larger spread needed before the cascade jumps?

## Phase operationalization tested
SOC Insurgence = threshold cascade with reluctant population.

## Sources this run draws on
P25; agent's toy.

## Refinement from previous iteration
Iteration 6 of the x6 family for SOC; follows iteration 5 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | uniform full cascade |
| H1 | hypothesis | one change stops it |
| H2 | hypothesis | jump > 0.3 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Not smoke-tested at this mean. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-SOC-B",
 "iteration": 6,
 "kind": "threshold_cascade",
 "seed": 21306,
 "N": 100,
 "mu": 40,
 "sd_values": [
  10,
  12,
  14,
  16,
  18,
  20,
  22,
  24,
  26,
  28,
  30,
  32,
  34,
  36,
  38,
  40
 ],
 "reps": 100,
 "h2": 0.3
}
```

## Command
`python sim_soc.py iter-6` (run from `Social-Sciences/simulation/`)
