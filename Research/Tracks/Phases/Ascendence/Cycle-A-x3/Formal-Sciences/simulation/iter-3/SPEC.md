# SIM-AS-FOR-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Global convergence claim of P86 for Example 3: from 200 random starts in [-3, 3]^2 does natural gradient flow always reach (1, 1), faster than plain gradient flow, in the time predicted by zdot = -2z?

## Phase operationalization tested
FOR Ascendence = steepest ascent / descent (P86).

## Sources this run draws on
P86 (Wensing & Slotine 2020, 'Beyond convexity - Contraction and global convergence of gradient descent', PLoS One, PMC7402485, CC BY; read in full in AS0): natural gradient as 'the direction of steepest ascent on the manifold'; Example 3 (Rosenbrock, metric M, h(x) = -2[x1 - 1, x1^2 - 2x1 + x2], contraction rate 2, coordinates z1 = 10x1^2 - 10x2, z2 = x1 - 1); Example 5 (f = x1^2 + x2^2 + x1^2 x2^2, metric printed in a garbled layout in the extracted text).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | the z-map (1 - 2 dt) shrinks |z| by 0.5 per step at dt 0.25 |
| H1 | hypothesis | natural gradient flow converges from all 200 random starts within T 40 |
| H2 | hypothesis | natural gradient flow is faster than plain gradient flow from at least 90% of starts |
| H3 | hypothesis | natural gradient time to tol never exceeds the z-coordinate prediction ln(|z0|/tol)/2 by more than 0.05 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
LSODA integration (rtol 1e-9). Design note (agent): the stopping rule |x - x*| < tol is in x, while the prediction ln(|z0|/tol)/2 is for |z| < tol, so H3 compares unlike norms. Before this SPEC, the smoke-test version used RK4 with dt 1e-4 for the plain flow and was too slow; it was replaced by LSODA before any recorded run. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-FOR-A",
 "iteration": 3,
 "kind": "grad_steps",
 "seed": 35203,
 "mode": "random_starts",
 "n_starts": 200,
 "box": 3.0,
 "dt": 0.002,
 "dt_gd": 0.0001,
 "T": 40.0,
 "tol": 0.0001,
 "hyps": [
  [
   "natural gradient flow converges from all 200 random starts within T 40",
   "o['results']['nat_conv'] == 1.0"
  ],
  [
   "natural gradient flow is faster than plain gradient flow from at least 90% of starts",
   "o['results']['nat_faster_share'] >= 0.9"
  ],
  [
   "natural gradient time to tol never exceeds the z-coordinate prediction ln(|z0|/tol)/2 by more than 0.05",
   "o['results']['nat_t_minus_zpred_max'] <= 0.05"
  ]
 ]
}
```

## Command
`python sim_for.py iter-3` (run from `Formal-Sciences/simulation/`)
