# SIM-IN-SOC-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Threshold cascades (SOC pass 2; threshold model as described in P25): N = 100, thresholds 0..99 give a full cascade, and raising one threshold stops it; with normal thresholds (mean 25) does the final size jump as the spread grows from 5 to 20?

## Phase operationalization tested
SOC Insurgence = a cascade of joining once enough others have joined (threshold model).

## Sources this run draws on
P25 (read in full in IN0) describes threshold models of collective behaviour (Granovetter, as cited in P25); the uniform and one-change cases are the agent's construction, not numbers from P25.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | uniform thresholds give a full cascade |
| H1 | hypothesis | one changed threshold stops it at 1 |
| H2 | hypothesis | mean final size jumps by > 0.3 between adjacent sd values |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic thresholds; 100 draws per sd; agent's toy. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-IN-SOC-A",
 "iteration": 1,
 "kind": "threshold_cascade",
 "seed": 20301,
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
`python sim_soc.py iter-1` (run from `Social-Sciences/simulation/`)
