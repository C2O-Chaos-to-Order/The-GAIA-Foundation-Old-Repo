# SIM-AS-FOR-C - iteration 7 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Natural vs plain flow from 100 starts in [-0.1, 0.1]^2

## Phase operationalization tested
FOR Ascendence = steepest ascent / descent (P86), continuous and discrete.

## Sources this run draws on
P86 (Wensing & Slotine 2020, 'Beyond convexity - Contraction and global convergence of gradient descent', PLoS One, PMC7402485, CC BY; read in full in AS0): natural gradient as 'the direction of steepest ascent on the manifold'; Example 3 (Rosenbrock, metric M, h(x) = -2[x1 - 1, x1^2 - 2x1 + x2], contraction rate 2, coordinates z1 = 10x1^2 - 10x2, z2 = x1 - 1); Example 5 (f = x1^2 + x2^2 + x1^2 x2^2, metric printed in a garbled layout in the extracted text).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | the z-map (1 - 2 dt) shrinks |z| by 0.5 per step at dt 0.25 |
| H1 | hypothesis | box [-0.1, 0.1]^2 (far from the minimum at (1, 1) relative to tol): natural gradient flow faster from every start |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
LSODA rtol 1e-9. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-FOR-C",
 "iteration": 7,
 "kind": "grad_steps",
 "seed": 37207,
 "mode": "random_starts",
 "n_starts": 100,
 "box": 0.1,
 "dt": 0.002,
 "dt_gd": 0.0001,
 "T": 60.0,
 "tol": 0.0001,
 "hyps": [
  [
   "box [-0.1, 0.1]^2 (far from the minimum at (1, 1) relative to tol): natural gradient flow faster from every start",
   "o['results']['nat_faster_share'] == 1.0"
  ]
 ]
}
```

## Command
`python sim_for.py iter-7` (run from `Formal-Sciences/simulation/`)
