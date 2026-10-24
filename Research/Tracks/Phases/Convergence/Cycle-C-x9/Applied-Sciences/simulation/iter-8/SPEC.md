# SIM-CV-APP-C - iteration 8 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
sin^2 over its period: is the trapezoid exact for N = 2, 4, 8, as P79's asymptotic estimate (zero leading term) suggests?

## Phase operationalization tested
APP Convergence = convergence of quadrature rules (P79).

## Sources this run draws on
P79 (Wikipedia contributors, 'Trapezoidal rule', English Wikipedia, revision fetched 2026-10-24, CC BY-SA 4.0; read in full in CVB): composite rule error E = -(b - a)^3/(12 N^2) f''(xi); asymptotic E = -(b - a)^2/(12 N^2)[f'(b) - f'(a)] + O(N^-3); concave-up integrands are overestimated; worked examples ln 3 (N = 3: 356/315, error 0.031546, 2.87148%; N = 6: 2789/2520, 8.13e-3, 0.74036%; N = 116 for 1e-4) and int_0.1^1.3 5x e^-2x dx (0.84385 vs 0.89387, error 0.05002, 5.5959%).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | trapezoidal rule exact for 2x + 1 |
| H1 | hypothesis | sin^2 over its period: trapezoid exact (error < 1e-14) for N = 2, 4, 8 |
| H2 | hypothesis | P79's asymptotic estimate (f'(b) - f'(a) = 0) predicts zero leading error (|asym| < 1e-15) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds in CVC (kuramoto_lyap, kuramoto_fss, crowd_bound, trap_simpson, levelling_voter, common_core) were smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before the SPECs; printed values were suppressed except one kuramoto_lyap smoke (N = 3 and 4, K = 1, 3 settings, T 400) whose maxima (both slightly negative) were seen (disclosed). Thresholds were not informed by smoke values. Existing kinds were not smoke-tested.

## Parameters
```json
{
 "sim_id": "SIM-CV-APP-C",
 "iteration": 8,
 "kind": "trap_error",
 "seed": 32408,
 "case": "sin2",
 "f": "np.sin(x)**2",
 "d1": "np.sin(2*x)",
 "d2": "2*np.cos(2*x)",
 "a": 0.0,
 "b": 3.141592653589793,
 "exact": "np.pi/2",
 "N_values": [
  2,
  4,
  8
 ],
 "hyps": [
  [
   "sin^2 over its period: trapezoid exact (error < 1e-14) for N = 2, 4, 8",
   "all(v['abs_err'] < 1e-14 for v in o['rows'].values())"
  ],
  [
   "P79's asymptotic estimate (f'(b) - f'(a) = 0) predicts zero leading error (|asym| < 1e-15)",
   "all(abs(v['asym']) < 1e-15 for v in o['rows'].values())"
  ]
 ]
}
```

## Command
`python sim_app.py iter-8` (run from `Applied-Sciences/simulation/`)
