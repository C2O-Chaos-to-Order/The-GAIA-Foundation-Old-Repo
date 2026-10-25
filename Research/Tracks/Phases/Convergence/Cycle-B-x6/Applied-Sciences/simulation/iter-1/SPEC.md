# SIM-CV-APP-B - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P79's ln 3 worked example: are T_3 = 356/315, T_6 = 2789/2520, the printed absolute and relative errors and N = 116 reproduced, and does the concave-up rule hold?

## Phase operationalization tested
APP Convergence = convergence of the trapezoidal rule (P79).

## Sources this run draws on
P79 (Wikipedia contributors, 'Trapezoidal rule', English Wikipedia, revision fetched 2026-10-24, CC BY-SA 4.0; read in full in CVB): composite rule error E = -(b - a)^3/(12 N^2) f''(xi); asymptotic E = -(b - a)^2/(12 N^2)[f'(b) - f'(a)] + O(N^-3); concave-up integrands are overestimated; worked examples ln 3 (N = 3: 356/315, error 0.031546, 2.87148%; N = 6: 2789/2520, 8.13e-3, 0.74036%; N = 116 for 1e-4) and int_0.1^1.3 5x e^-2x dx (0.84385 vs 0.89387, error 0.05002, 5.5959%).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | trapezoidal rule exact for 2x + 1 |
| H1 | hypothesis | T_3 = 356/315 (P79) within 1e-9 |
| H2 | hypothesis | T_6 = 2789/2520 (P79) within 1e-9 |
| H3 | hypothesis | P79's absolute error 0.031546 (N = 3) within 5e-7 |
| H4 | hypothesis | P79's relative error 2.87148% (N = 3) within 5e-5 |
| H5 | hypothesis | P79's absolute error 8.13e-3 (N = 6) within 5e-6 |
| H6 | hypothesis | P79's relative error 0.74036% (N = 6) within 5e-5 |
| H7 | hypothesis | P79's N = 116 guarantees 1e-4 |
| H8 | hypothesis | 1/x is concave up, so T overestimates (P79's sign rule) at N = 3 and 6 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic; derivatives supplied by the agent. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-APP-B",
 "iteration": 1,
 "kind": "trap_error",
 "seed": 31401,
 "case": "ln3",
 "f": "1/x",
 "d1": "-1/x**2",
 "d2": "2/x**3",
 "a": 1.0,
 "b": 3.0,
 "exact": "np.log(3)",
 "N_values": [
  3,
  6
 ],
 "hyps": [
  [
   "T_3 = 356/315 (P79) within 1e-9",
   "abs(o['rows']['3']['T']-356/315) < 1e-9"
  ],
  [
   "T_6 = 2789/2520 (P79) within 1e-9",
   "abs(o['rows']['6']['T']-2789/2520) < 1e-9"
  ],
  [
   "P79's absolute error 0.031546 (N = 3) within 5e-7",
   "abs(o['rows']['3']['abs_err']-0.031546) < 5e-7"
  ],
  [
   "P79's relative error 2.87148% (N = 3) within 5e-5",
   "abs(o['rows']['3']['rel_pct']-2.87148) < 5e-5"
  ],
  [
   "P79's absolute error 8.13e-3 (N = 6) within 5e-6",
   "abs(o['rows']['6']['abs_err']-8.13e-3) < 5e-6"
  ],
  [
   "P79's relative error 0.74036% (N = 6) within 5e-5",
   "abs(o['rows']['6']['rel_pct']-0.74036) < 5e-5"
  ],
  [
   "P79's N = 116 guarantees 1e-4",
   "o['tol']['N_bound'] == 116"
  ],
  [
   "1/x is concave up, so T overestimates (P79's sign rule) at N = 3 and 6",
   "all(v['overestimates'] for v in o['rows'].values())"
  ]
 ],
 "tol": 0.0001,
 "N_cap": 100000
}
```

## Command
`python sim_app.py iter-1` (run from `Applied-Sciences/simulation/`)
