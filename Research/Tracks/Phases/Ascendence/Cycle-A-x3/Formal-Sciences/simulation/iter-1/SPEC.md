# SIM-AS-FOR-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Discrete steps on P86's Example 3: do Euler steps of the natural-gradient field converge from three starts for dt 0.5 and 0.9 and fail for dt 1.1 and 1.5 (in z-coordinates the linear map 1 - 2dt converges iff dt < 1)?

## Phase operationalization tested
FOR Ascendence = steepest ascent / descent in discrete steps (P86's continuous flow discretised).

## Sources this run draws on
P86 (Wensing & Slotine 2020, 'Beyond convexity - Contraction and global convergence of gradient descent', PLoS One, PMC7402485, CC BY; read in full in AS0): natural gradient as 'the direction of steepest ascent on the manifold'; Example 3 (Rosenbrock, metric M, h(x) = -2[x1 - 1, x1^2 - 2x1 + x2], contraction rate 2, coordinates z1 = 10x1^2 - 10x2, z2 = x1 - 1); Example 5 (f = x1^2 + x2^2 + x1^2 x2^2, metric printed in a garbled layout in the extracted text).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | the z-map (1 - 2 dt) shrinks |z| by 0.5 per step at dt 0.25 |
| H1 | hypothesis | Euler steps of P86's natural-gradient field converge from all three starts for dt 0.5 and 0.9 |
| H2 | hypothesis | for dt 1.5 (beyond the linear z-coordinate limit dt < 1) no start converges |
| H3 | hypothesis | dt 1.1 converges from no start (the x-coordinate Euler map has the same dt < 1 limit as the z-coordinate one) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic; three start points; dt grid and the 1e8 divergence cap are the agent's. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-FOR-A",
 "iteration": 1,
 "kind": "grad_steps",
 "seed": 35201,
 "mode": "euler_natural",
 "dt_values": [
  0.5,
  0.9,
  1.0,
  1.1,
  1.5
 ],
 "starts": [
  [
   -1.5,
   2.0
  ],
  [
   2.0,
   -1.0
  ],
  [
   0.0,
   0.0
  ]
 ],
 "k_max": 20000,
 "tol": 1e-06,
 "hyps": [
  [
   "Euler steps of P86's natural-gradient field converge from all three starts for dt 0.5 and 0.9",
   "all(v['conv'] for d in ['0.5', '0.9'] for v in o['results'][d].values())"
  ],
  [
   "for dt 1.5 (beyond the linear z-coordinate limit dt < 1) no start converges",
   "not any(v['conv'] for v in o['results']['1.5'].values())"
  ],
  [
   "dt 1.1 converges from no start (the x-coordinate Euler map has the same dt < 1 limit as the z-coordinate one)",
   "not any(v['conv'] for v in o['results']['1.1'].values())"
  ]
 ]
}
```

## Command
`python sim_for.py iter-1` (run from `Formal-Sciences/simulation/`)
