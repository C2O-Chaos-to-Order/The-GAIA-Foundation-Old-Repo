# SIM-AS-FOR-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P86's contraction analysis: do Example 3's printed natural-gradient field and contraction identity (rate 2) hold numerically at 2000 random points, does Example 5's metric (as read from the garbled extracted text) give rate 2, and does natural gradient flow reach the Rosenbrock minimum sooner than plain gradient flow?

## Phase operationalization tested
FOR Ascendence = steepest ascent (equivalently descent of -f) toward an optimum; P86: natural gradient is 'the direction of steepest ascent on the manifold'.

## Sources this run draws on
P86 (Wensing & Slotine 2020, 'Beyond convexity - Contraction and global convergence of gradient descent', PLoS One, PMC7402485, CC BY; read in full in AS0): natural gradient as 'the direction of steepest ascent on the manifold'; Example 3 (Rosenbrock, metric M, h(x) = -2[x1 - 1, x1^2 - 2x1 + x2], contraction rate 2, coordinates z1 = 10x1^2 - 10x2, z2 = x1 - 1); Example 5 (f = x1^2 + x2^2 + x1^2 x2^2, metric printed in a garbled layout in the extracted text).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | Example 3 in z-coordinates decays exactly as e^-2t |
| H1 | hypothesis | Example 3: -M^-1 grad f equals P86's printed h(x) (max relative error < 1e-9) |
| H2 | hypothesis | Example 3: M A + A^T M + Mdot = -4 M (contraction rate 2; max relative error < 1e-9) |
| H3 | hypothesis | Example 5 (metric as read from P86's text): largest generalized eigenvalue <= -4 + 1e-9 at every sampled point (rate 2) |
| H4 | hypothesis | from (-1.5, 2) natural gradient flow reaches within 1e-4 of (1, 1) sooner than plain gradient flow (or plain flow fails by T 60) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic apart from the random test points (box [-3, 3]^2). Example 5's metric is the agent's reading of a garbled matrix layout; a pass confirms that reading is self-consistent, not the typesetting. Flow comparison from one start point (-1.5, 2) only; RK4 with dt 0.001 (natural) and 1e-4 (plain).Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so every outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-FOR-0",
 "iteration": 1,
 "kind": "contraction_check",
 "seed": 34201,
 "box": 3.0,
 "n_points": 2000,
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
   "Example 3: -M^-1 grad f equals P86's printed h(x) (max relative error < 1e-9)",
   "o['ex3_h_maxrelerr'] < 1e-9"
  ],
  [
   "Example 3: M A + A^T M + Mdot = -4 M (contraction rate 2; max relative error < 1e-9)",
   "o['ex3_contraction_maxrelerr'] < 1e-9"
  ],
  [
   "Example 5 (metric as read from P86's text): largest generalized eigenvalue <= -4 + 1e-9 at every sampled point (rate 2)",
   "o['ex5_max_gen_eig'] <= -4 + 1e-9"
  ],
  [
   "from (-1.5, 2) natural gradient flow reaches within 1e-4 of (1, 1) sooner than plain gradient flow (or plain flow fails by T 60)",
   "o['t_natural'] is not None and (o['t_gradient'] is None or o['t_natural'] < o['t_gradient'])"
  ]
 ]
}
```

## Command
`python sim_for.py iter-1` (run from `Formal-Sciences/simulation/`)
