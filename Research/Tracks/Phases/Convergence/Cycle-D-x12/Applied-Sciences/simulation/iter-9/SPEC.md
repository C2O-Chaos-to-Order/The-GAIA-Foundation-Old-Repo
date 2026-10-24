# SIM-CV-APP-D - iteration 9 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
cos^2 over its period: exact?

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
| H1 | hypothesis | cos^2 over its period: trapezoid exact (< 1e-14) from 3 nodes |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds/options in CVD (stats_audit, instrument_core, levelling_voter bias_mode=selection) were smoke-tested once at trivial size (seed 99, temporary directory, nothing kept) with printed values suppressed; existing kinds were not smoke-tested. CVC results were known when these hypotheses were written (replications say so).

## Parameters
```json
{
 "sim_id": "SIM-CV-APP-D",
 "iteration": 9,
 "kind": "trap_simpson",
 "seed": 33409,
 "f": "cos(x)**2",
 "a": 0.0,
 "b": 3.141592653589793,
 "exact": 1.5707963267948966,
 "m_values": [
  3,
  5,
  9
 ],
 "hyps": [
  [
   "cos^2 over its period: trapezoid exact (< 1e-14) from 3 nodes",
   "all(v['trap_err'] < 1e-14 for v in o['rows'].values())"
  ]
 ]
}
```

## Command
`python sim_app.py iter-9` (run from `Applied-Sciences/simulation/`)
