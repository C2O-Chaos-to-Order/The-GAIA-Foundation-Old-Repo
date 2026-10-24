# SIM-IN-HUM-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P28's model of semantic expansion, deterministic limit (HUM pass 2): with beta = 0.808, is there a threshold gamma_c below which the new form is stuck, and does the transmission time diverge like delta^(-1/2) just above it?

## Phase operationalization tested
HUM Insurgence = a new linguistic form invading a context after a latency (P28).

## Sources this run draws on
P28 (Feltgen et al. 2017, R Soc Open Sci, CC BY; read in full in INA): Eqs. 3.1-3.4, saddle-node bifurcation, Fig. 6. The delta^(-1/2) law is the standard saddle-node bottleneck scaling (agent's expectation, not P28's statement).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | stuck below, completes above |
| H1 | hypothesis | slope within 0.1 of -1/2 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
P(x) implemented from Eqs. 3.1-3.2 (the text extraction of Eq. 3.3 loses the fraction layout; the implementation does not rely on it). gamma_c found by bisection on a grid; Euler dt 0.01. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-IN-HUM-A",
 "iteration": 1,
 "kind": "feltgen_semantic",
 "seed": 20501,
 "mode": "det",
 "beta": 0.808,
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
`python sim_hum.py iter-1` (run from `Humanities/simulation/`)
