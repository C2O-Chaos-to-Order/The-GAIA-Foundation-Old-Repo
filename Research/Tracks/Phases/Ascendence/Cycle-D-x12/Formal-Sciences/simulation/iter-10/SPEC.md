# SIM-AS-FOR-D - iteration 10 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Example 3 identity and Example 5 rate on [-50, 50]^2

## Phase operationalization tested
FOR Ascendence = steepest ascent / descent (P86), continuous and discrete.

## Sources this run draws on
P86 (Wensing & Slotine 2020, 'Beyond convexity - Contraction and global convergence of gradient descent', PLoS One, PMC7402485, CC BY; read in full in AS0): natural gradient as 'the direction of steepest ascent on the manifold'; Example 3 (Rosenbrock, metric M, h(x) = -2[x1 - 1, x1^2 - 2x1 + x2], contraction rate 2, coordinates z1 = 10x1^2 - 10x2, z2 = x1 - 1); Example 5 (f = x1^2 + x2^2 + x1^2 x2^2, metric printed in a garbled layout in the extracted text).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | Example 3 in z-coordinates decays as e^-2t |
| H1 | hypothesis | box [-50, 50]^2: Example 3 identity and Example 5 rate hold |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Example 5's metric reading is the agent's. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-FOR-D",
 "iteration": 10,
 "kind": "contraction_check",
 "seed": 38210,
 "box": 50.0,
 "n_points": 5000,
 "x0": [
  -1.5,
  2.0
 ],
 "dt": 0.001,
 "dt_gd": 0.0001,
 "T": 60.0,
 "tol": 0.0001,
 "hyps": [
  [
   "box [-50, 50]^2: Example 3 identity and Example 5 rate hold",
   "o['ex3_contraction_maxrelerr'] < 1e-9 and o['ex5_max_gen_eig'] <= -4 + 1e-9"
  ]
 ]
}
```

## Command
`python sim_for.py iter-10` (run from `Formal-Sciences/simulation/`)
