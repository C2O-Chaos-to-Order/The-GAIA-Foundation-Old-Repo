# SIM-CV-APP-D - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Kink off the nodes: orders.

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
| H1 | hypothesis | kink off the nodes (|x - 0.3|): trapezoid order within 0.3 of 2 |
| H2 | hypothesis | Simpson order below 3 (kink limits it) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds/options in CVD (stats_audit, instrument_core, levelling_voter bias_mode=selection) were smoke-tested once at trivial size (seed 99, temporary directory, nothing kept) with printed values suppressed; existing kinds were not smoke-tested. CVC results were known when these hypotheses were written (replications say so).

## Parameters
```json
{
 "sim_id": "SIM-CV-APP-D",
 "iteration": 6,
 "kind": "trap_simpson",
 "seed": 33406,
 "f": "abs(x-0.3)",
 "a": 0.0,
 "b": 1.0,
 "exact": 0.29,
 "m_values": [
  65,
  129,
  257
 ],
 "hyps": [
  [
   "kink off the nodes (|x - 0.3|): trapezoid order within 0.3 of 2",
   "abs(o['order_trap'] - 2) < 0.3"
  ],
  [
   "Simpson order below 3 (kink limits it)",
   "o['order_simp'] < 3"
  ]
 ]
}
```

## Command
`python sim_app.py iter-6` (run from `Applied-Sciences/simulation/`)
