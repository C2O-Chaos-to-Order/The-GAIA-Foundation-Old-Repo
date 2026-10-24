# SIM-DV-FOR-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Divergence as separation of nearby trajectories: check the Lyapunov exponent of the logistic map and the predicted separation time.

## Phase operationalization tested
FOR Divergence = exponential separation of neighbouring trajectories (positive global Lyapunov exponent; P09 Chaos_lambda).

## Sources this run draws on
P09 (SEP 'Chaos': Lyapunov exponent as average rate of divergence of neighbouring trajectories; Chaos_lambda definition and its critics).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | lambda(4) within 0.01 of ln 2 |
| V2 | validation | lambda(3.2) < 0 |
| H1 | hypothesis | median separation steps within 25% of ln(sep/delta0)/ln 2 |
| R1 | reporting | lambda by r |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
One-dimensional map; finite-time estimates; floating point limits orbits (double precision shadows true orbits only for a bounded time). Says nothing about chaos in physical systems.

## Parameters
```json
{
 "sim_id": "SIM-DV-FOR-0",
 "iteration": 1,
 "kind": "logistic_lyapunov",
 "seed": 1502,
 "r_values": [
  2.8,
  3.2,
  3.5,
  3.9,
  4.0
 ],
 "burn": 1000,
 "n": 200000,
 "pairs": 200,
 "delta0": 1e-10,
 "sep": 0.1
}
```

## Command
`python sim_for.py iter-1` (run from `Formal-Sciences/simulation/`)
