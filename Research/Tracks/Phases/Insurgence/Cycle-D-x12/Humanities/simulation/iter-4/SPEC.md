# SIM-IN-HUM-D - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication of INC-HUM iter-4 on a new seed (x12 replication pass; adds no new source).

## Phase operationalization tested
HUM Insurgence = latency then S-growth (P28).

## Sources this run draws on
P28 (read in full in INA).

## Refinement from previous iteration
Iteration 4 of the x12 family for HUM; follows iteration 3 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | some complete |
| H1 | hypothesis | all complete |
| H2 | hypothesis | latency > growth |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Replication or variant of an earlier run (new seed); no new source. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-HUM-D",
 "iteration": 4,
 "kind": "feltgen_semantic",
 "seed": 23504,
 "mode": "stoch",
 "beta": 0.808,
 "delta": 0.0,
 "M": 5000,
 "runs": 50,
 "w": 0.1,
 "max_steps": 40000000,
 "h1_text": "is 1",
 "h1_expr": "s == 1"
}
```

## Command
`python sim_hum.py iter-4` (run from `Humanities/simulation/`)
