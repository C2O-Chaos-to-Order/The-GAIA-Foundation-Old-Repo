# SIM-IN-HUM-B - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Deterministic threshold at another nonlinearity, beta = 0.5: does the delta^(-1/2) law hold?

## Phase operationalization tested
HUM Insurgence = threshold for semantic invasion.

## Sources this run draws on
P28.

## Refinement from previous iteration
Iteration 6 of the x6 family for HUM; follows iteration 5 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | stuck below, completes above |
| H1 | hypothesis | slope within 0.1 of -1/2 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-HUM-B",
 "iteration": 6,
 "kind": "feltgen_semantic",
 "seed": 21506,
 "mode": "det",
 "beta": 0.5,
 "deltas": [
  -0.05,
  -0.01,
  0.001,
  0.003,
  0.01,
  0.03,
  0.1
 ],
 "dt": 0.01,
 "tmax": 5000,
 "h1": 0.1
}
```

## Command
`python sim_hum.py iter-6` (run from `Humanities/simulation/`)
