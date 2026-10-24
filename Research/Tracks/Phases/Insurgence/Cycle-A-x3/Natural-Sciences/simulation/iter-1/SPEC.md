# SIM-IN-NAT-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Why onsets near a threshold are slow (NAT pass 2): in the saddle-node normal form dx/dt = r + x^2 just past the bifurcation, does the passage time from -10 to +10 match 2 arctan(L/sqrt r)/sqrt r and scale as r^(-1/2)?

## Phase operationalization tested
NAT Insurgence = a new state breaking out once a bottleneck opens (saddle-node 'ghost'); P22 treats the saddle-node bifurcation.

## Sources this run draws on
P22 (Sayama, LibreTexts section 8.2, read in full in DVC): saddle-node bifurcation. The closed-form passage time is a direct integral (agent's derivation, not from P22).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | within 0.5% of the integral |
| H1 | hypothesis | log-log slope within 0.05 of -1/2 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic RK4, dt 0.01; finite L. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-IN-NAT-A",
 "iteration": 1,
 "kind": "saddle_bottleneck",
 "seed": 20101,
 "r_values": [
  0.0001,
  0.001,
  0.01,
  0.1
 ],
 "L": 10,
 "dt": 0.01,
 "tol": 0.005,
 "h1": 0.05
}
```

## Command
`python sim_nat.py iter-1` (run from `Natural-Sciences/simulation/`)
