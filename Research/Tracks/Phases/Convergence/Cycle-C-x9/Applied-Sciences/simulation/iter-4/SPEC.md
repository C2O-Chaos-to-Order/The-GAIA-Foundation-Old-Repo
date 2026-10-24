# SIM-CV-APP-C - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P79's 'full integral of a Gaussian ... with 1% accuracy ... using just 4 points' and 'Simpson's rule requires 1.8 times more points': reproduced under the agent's operationalisation?

## Phase operationalization tested
APP Convergence = convergence of quadrature rules (P79).

## Sources this run draws on
P79 (Wikipedia contributors, 'Trapezoidal rule', English Wikipedia, revision fetched 2026-10-24, CC BY-SA 4.0; read in full in CVB): composite rule error E = -(b - a)^3/(12 N^2) f''(xi); asymptotic E = -(b - a)^2/(12 N^2)[f'(b) - f'(a)] + O(N^-3); concave-up integrands are overestimated; worked examples ln 3 (N = 3: 356/315, error 0.031546, 2.87148%; N = 6: 2789/2520, 8.13e-3, 0.74036%; N = 116 for 1e-4) and int_0.1^1.3 5x e^-2x dx (0.84385 vs 0.89387, error 0.05002, 5.5959%).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | Simpson exact for x^3 with 5 nodes |
| H1 | hypothesis | P79: the full Gaussian integral to 1% with just 4 points (best spacing, symmetric equally spaced nodes) |
| H2 | hypothesis | P79: Simpson needs about 1.8 times more points (ratio within 20% of 1.8) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's operationalisation (P79 gives none): m symmetric equally spaced nodes, spacing optimised on a 5901-point grid in [0.05, 3], plain h sum f (trapezoid with negligible end weights) vs Simpson weights; smallest m with relative error < 1%. Another operationalisation could give other counts. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds in CVC (kuramoto_lyap, kuramoto_fss, crowd_bound, trap_simpson, levelling_voter, common_core) were smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before the SPECs; printed values were suppressed except one kuramoto_lyap smoke (N = 3 and 4, K = 1, 3 settings, T 400) whose maxima (both slightly negative) were seen (disclosed). Thresholds were not informed by smoke values. Existing kinds were not smoke-tested.

## Parameters
```json
{
 "sim_id": "SIM-CV-APP-C",
 "iteration": 4,
 "kind": "trap_simpson",
 "seed": 32404,
 "gauss": {
  "tol": 0.01,
  "m_max": 12
 },
 "hyps": [
  [
   "P79: the full Gaussian integral to 1% with just 4 points (best spacing, symmetric equally spaced nodes)",
   "o['gauss']['m_trap'] is not None and o['gauss']['m_trap'] <= 4"
  ],
  [
   "P79: Simpson needs about 1.8 times more points (ratio within 20% of 1.8)",
   "o['gauss']['ratio'] is not None and abs(o['gauss']['ratio']/1.8 - 1) < 0.2"
  ]
 ]
}
```

## Command
`python sim_app.py iter-4` (run from `Applied-Sciences/simulation/`)
