# SIM-AS-FOR-B - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Euler natural-gradient steps from far starts ((10, -10), (-5, 25), (3, 9)) at dt 0.5 and 0.9

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
| H1 | hypothesis | far starts: Euler natural-gradient steps converge at dt 0.5 and 0.9 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-FOR-B",
 "iteration": 5,
 "kind": "grad_steps",
 "seed": 36205,
 "mode": "euler_natural",
 "dt_values": [
  0.5,
  0.9
 ],
 "starts": [
  [
   10.0,
   -10.0
  ],
  [
   -5.0,
   25.0
  ],
  [
   3.0,
   9.0
  ]
 ],
 "k_max": 50000,
 "tol": 1e-06,
 "hyps": [
  [
   "far starts: Euler natural-gradient steps converge at dt 0.5 and 0.9",
   "all(v['conv'] for d in ['0.5', '0.9'] for v in o['results'][d].values())"
  ]
 ]
}
```

## Command
`python sim_for.py iter-5` (run from `Formal-Sciences/simulation/`)
