# SIM-AS-FOR-D - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Euler natural dt 1.0 on the grid

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
| H1 | hypothesis | Euler natural-gradient dt 1.0 (the limit): no grid start converges |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-FOR-D",
 "iteration": 6,
 "kind": "grad_steps",
 "seed": 38206,
 "tol": 1e-06,
 "mode": "euler_natural",
 "dt_values": [
  1.0
 ],
 "starts": [
  [
   -1.95,
   -1.95
  ],
  [
   -1.95,
   -0.95
  ],
  [
   -1.95,
   0.05
  ],
  [
   -1.95,
   1.05
  ],
  [
   -1.95,
   2.05
  ],
  [
   -0.95,
   -1.95
  ],
  [
   -0.95,
   -0.95
  ],
  [
   -0.95,
   0.05
  ],
  [
   -0.95,
   1.05
  ],
  [
   -0.95,
   2.05
  ],
  [
   0.05,
   -1.95
  ],
  [
   0.05,
   -0.95
  ],
  [
   0.05,
   0.05
  ],
  [
   0.05,
   1.05
  ],
  [
   0.05,
   2.05
  ],
  [
   1.05,
   -1.95
  ],
  [
   1.05,
   -0.95
  ],
  [
   1.05,
   0.05
  ],
  [
   1.05,
   1.05
  ],
  [
   1.05,
   2.05
  ],
  [
   2.05,
   -1.95
  ],
  [
   2.05,
   -0.95
  ],
  [
   2.05,
   0.05
  ],
  [
   2.05,
   1.05
  ],
  [
   2.05,
   2.05
  ]
 ],
 "k_max": 50000,
 "hyps": [
  [
   "Euler natural-gradient dt 1.0 (the limit): no grid start converges",
   "len([v for v in o['results']['1.0'].values() if v['conv']]) == 0"
  ]
 ]
}
```

## Command
`python sim_for.py iter-6` (run from `Formal-Sciences/simulation/`)
