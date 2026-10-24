# SIM-IN-HUM-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Just below the threshold (HUM pass 3): delta = -0.02; does noise still let some runs escape (P28: no clear-cut transition in the stochastic model), but not all within 2,000 time units?

## Phase operationalization tested
HUM Insurgence = escape from a trap by fluctuations.

## Sources this run draws on
P28 (read in full in INA): section 3.3, 'there is no more clear-cut transition'.

## Refinement from previous iteration
Follows iter-2: just below the threshold.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | some runs complete |
| H1 | hypothesis | share completing strictly between 0 and 1 |
| H2 | hypothesis | mean latency > mean growth |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Not smoke-tested below threshold. If no run completes, V1 fails and the run is reported as such. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-HUM-A",
 "iteration": 3,
 "kind": "feltgen_semantic",
 "seed": 20503,
 "mode": "stoch",
 "beta": 0.808,
 "delta": -0.02,
 "M": 500,
 "runs": 400,
 "w": 0.1,
 "max_steps": 1000000,
 "h1_text": "is strictly between 0 and 1",
 "h1_expr": "0 < s < 1"
}
```

## Command
`python sim_hum.py iter-3` (run from `Humanities/simulation/`)
