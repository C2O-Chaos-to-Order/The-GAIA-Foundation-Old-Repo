# SIM-CV-APP-B - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P79's second worked example (int_0.1^1.3 5x e^-2x dx, N = 3): are 0.84385, 0.89387, 0.05002 and 5.5959% reproduced?

## Phase operationalization tested
APP Convergence = trapezoidal error.

## Sources this run draws on
P79 (Wikipedia contributors, 'Trapezoidal rule', English Wikipedia, revision fetched 2026-10-24, CC BY-SA 4.0; read in full in CVB): composite rule error E = -(b - a)^3/(12 N^2) f''(xi); asymptotic E = -(b - a)^2/(12 N^2)[f'(b) - f'(a)] + O(N^-3); concave-up integrands are overestimated; worked examples ln 3 (N = 3: 356/315, error 0.031546, 2.87148%; N = 6: 2789/2520, 8.13e-3, 0.74036%; N = 116 for 1e-4) and int_0.1^1.3 5x e^-2x dx (0.84385 vs 0.89387, error 0.05002, 5.5959%).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | trapezoidal rule exact for 2x + 1 |
| H1 | hypothesis | P79's T_3 = 0.84385 within 5e-6 |
| H2 | hypothesis | P79's exact 0.89387 within 5e-6 |
| H3 | hypothesis | P79's true error 0.05002 within 5e-6 |
| H4 | hypothesis | P79's relative error 5.5959% within 5e-4 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic; the exact integral uses the agent's antiderivative. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-APP-B",
 "iteration": 2,
 "kind": "trap_error",
 "seed": 31402,
 "case": "5xexp",
 "f": "5*x*np.exp(-2*x)",
 "d1": "5*np.exp(-2*x)*(1-2*x)",
 "d2": "20*(x-1)*np.exp(-2*x)",
 "a": 0.1,
 "b": 1.3,
 "exact": "5*((0.1/2+0.25)*np.exp(-0.2)-(1.3/2+0.25)*np.exp(-2.6))",
 "N_values": [
  3
 ],
 "hyps": [
  [
   "P79's T_3 = 0.84385 within 5e-6",
   "abs(o['rows']['3']['T']-0.84385) < 5e-6"
  ],
  [
   "P79's exact 0.89387 within 5e-6",
   "abs(o['exact']-0.89387) < 5e-6"
  ],
  [
   "P79's true error 0.05002 within 5e-6",
   "abs(o['rows']['3']['E']-0.05002) < 5e-6"
  ],
  [
   "P79's relative error 5.5959% within 5e-4",
   "abs(o['rows']['3']['rel_pct']-5.5959) < 5e-4"
  ]
 ]
}
```

## Command
`python sim_app.py iter-2` (run from `Applied-Sciences/simulation/`)
