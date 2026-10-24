# SIM-IN-SOC-A - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Threshold cascades at N = 1000 (SOC pass 2): same check with thresholds mean 250 and spread 40 to 140 (step 5); is the jump still sudden?

## Phase operationalization tested
SOC Insurgence = threshold cascade (larger population).

## Sources this run draws on
As iter-1.

## Refinement from previous iteration
Follows iter-1: tenfold population.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | uniform thresholds give a full cascade |
| H1 | hypothesis | one changed threshold stops it at 1 |
| H2 | hypothesis | mean final size jumps by > 0.3 between adjacent sd values |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
50 draws per sd; not smoke-tested at this size. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-SOC-A",
 "iteration": 2,
 "kind": "threshold_cascade",
 "seed": 20302,
 "N": 1000,
 "mu": 250,
 "sd_values": [
  40,
  45,
  50,
  55,
  60,
  65,
  70,
  75,
  80,
  85,
  90,
  95,
  100,
  105,
  110,
  115,
  120,
  125,
  130,
  135,
  140
 ],
 "reps": 50,
 "h2": 0.3
}
```

## Command
`python sim_soc.py iter-2` (run from `Social-Sciences/simulation/`)
