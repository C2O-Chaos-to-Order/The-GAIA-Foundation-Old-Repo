# SIM-DV-APP-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Numerical divergence of an iterative solver: explicit Euler on y' = -lam y converges for h lam < 2 and diverges for h lam > 2.

## Phase operationalization tested
APP Divergence = numerical instability of an iterative method (listed as unsourced in DV0).

## Sources this run draws on
No source read in this track; standard linear stability of explicit Euler.

## Refinement from previous iteration
New run family (engineering/computing sense).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | |y| = |1 - h lam|^steps |
| V2 | validation | converge below 2, diverge above 2 |
| R1 | reporting | factors |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Linear test equation only; deterministic.

## Parameters
```json
{
 "sim_id": "SIM-DV-APP-A",
 "iteration": 3,
 "kind": "euler_stability",
 "seed": 15403,
 "hlam": [
  0.5,
  1.0,
  1.5,
  1.9,
  2.1,
  2.5
 ],
 "steps": 300
}
```

## Command
`python sim_app.py iter-3` (run from `Applied-Sciences/simulation/`)
