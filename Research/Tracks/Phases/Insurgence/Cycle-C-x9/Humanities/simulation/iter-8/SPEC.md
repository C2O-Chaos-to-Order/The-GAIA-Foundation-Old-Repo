# SIM-IN-HUM-C - iteration 8 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication of INB-HUM iter-5 (delta = -0.05) on a new seed.

## Phase operationalization tested
HUM Insurgence = escape by fluctuation.

## Sources this run draws on
P28.

## Refinement from previous iteration
Iteration 8 of the x9 family for HUM; follows iteration 7 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | some complete |
| H1 | hypothesis | share strictly between 0 and 1 |
| H2 | hypothesis | latency > growth |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Replication or variant of an earlier run (new seed); no new source. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-HUM-C",
 "iteration": 8,
 "kind": "feltgen_semantic",
 "seed": 22508,
 "mode": "stoch",
 "beta": 0.808,
 "delta": -0.05,
 "M": 500,
 "runs": 400,
 "w": 0.1,
 "max_steps": 1000000,
 "h1_text": "is strictly between 0 and 1",
 "h1_expr": "0 < s < 1"
}
```

## Command
`python sim_hum.py iter-8` (run from `Humanities/simulation/`)
