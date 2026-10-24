# SIM-IN-HUM-A - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P28's random walk at the threshold (HUM pass 3): with delta = 0 (P28's choice) and M = 500 exemplars, 400 runs: does every run complete the change (finite stochastic transmission time, P28 Fig. 6b), and is the latency longer than the growth?

## Phase operationalization tested
HUM Insurgence = latency then S-growth (P28).

## Sources this run draws on
P28 (read in full in INA): sections 3.3 and 4.1 (P28 used M = 5000 and 10,000 runs).

## Refinement from previous iteration
Follows iter-1 (deterministic threshold): the stochastic walk at the threshold.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | some runs complete |
| H1 | hypothesis | all runs complete within 2,000 time units |
| H2 | hypothesis | mean latency > mean growth |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
M = 500, not 5000 (compute budget); latency defined as time from x_c - 0.1 to x_c + 0.1 (agent's definition, not P28's trap boundaries). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-IN-HUM-A",
 "iteration": 2,
 "kind": "feltgen_semantic",
 "seed": 20502,
 "mode": "stoch",
 "beta": 0.808,
 "delta": 0.0,
 "M": 500,
 "runs": 400,
 "w": 0.1,
 "max_steps": 1000000,
 "h1_text": "is 1",
 "h1_expr": "s == 1"
}
```

## Command
`python sim_hum.py iter-2` (run from `Humanities/simulation/`)
