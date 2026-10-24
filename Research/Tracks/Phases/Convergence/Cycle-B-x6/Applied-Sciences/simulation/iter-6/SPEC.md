# SIM-CV-APP-B - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P70's f4 (x sin(10 x)) against P79's error theory: is the N needed for 1e-8 within P79's bound and predicted within 1% by P79's asymptotic estimate, and is P70's printed trapezoid count (1024) at least the evaluations needed, or close to the bound-guaranteed count?

## Phase operationalization tested
APP Convergence = numerical convergence and its cost; an independent check of P70's reading of 'n'.

## Sources this run draws on
P70 (Asgedom & Kefela 2026, adaptive hybrid Simpson-Gauss quadrature (AHQS), PLoS One e0335582, PMC12928599, CC BY; read in full in CV0 incl. peer-review history): Table 1 errors for exp(-x^2) on [0, 1] at n = 8, 16, 32; Table 2 evaluations to 1e-8; Lemma 2.6 eta <= 2/5; Algorithm 1; abstract claim 40-62% fewer evaluations than adaptive Simpson; Section 4.3 claim 20-35% fewer than Gauss-Kronrod for f2-f5. P79 (Wikipedia contributors, 'Trapezoidal rule', English Wikipedia, revision fetched 2026-10-24, CC BY-SA 4.0; read in full in CVB): composite rule error E = -(b - a)^3/(12 N^2) f''(xi); asymptotic E = -(b - a)^2/(12 N^2)[f'(b) - f'(a)] + O(N^-3); concave-up integrands are overestimated; worked examples ln 3 (N = 3: 356/315, error 0.031546, 2.87148%; N = 6: 2789/2520, 8.13e-3, 0.74036%; N = 116 for 1e-4) and int_0.1^1.3 5x e^-2x dx (0.84385 vs 0.89387, error 0.05002, 5.5959%).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | trapezoidal rule exact for 2x + 1 |
| H1 | hypothesis | the N actually needed for 1e-8 does not exceed the N guaranteed by P79's bound |
| H2 | hypothesis | P79's asymptotic estimate predicts the needed N within 1% |
| H3 | hypothesis | P70 Table's printed trapezoid count 1024 is at least the evaluations actually needed |
| H4 | hypothesis | P70's printed 1024 within 10% of the bound-guaranteed evaluations (P70 used the bound) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic scan N = 1, 2, ... ('evaluations' = N + 1 nodes, as in CVA). Foreknowledge: CV0/CVA already found P70's counts far below the needed evaluations, so H3 was expected not supported; the asymptotic N for f1 and f3 was estimated by arithmetic before writing (disclosed). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-APP-B",
 "iteration": 6,
 "kind": "trap_error",
 "seed": 31406,
 "case": "f4",
 "f": "x*np.sin(10*x)",
 "d1": "np.sin(10*x)+10*x*np.cos(10*x)",
 "d2": "20*np.cos(10*x)-100*x*np.sin(10*x)",
 "a": 0.0,
 "b": 1.0,
 "exact": "(np.sin(10)-10*np.cos(10))/100",
 "N_values": [
  8,
  16,
  32
 ],
 "hyps": [
  [
   "the N actually needed for 1e-8 does not exceed the N guaranteed by P79's bound",
   "o['tol']['N_actual'] <= o['tol']['N_bound']"
  ],
  [
   "P79's asymptotic estimate predicts the needed N within 1%",
   "abs(o['tol']['N_asym']/o['tol']['N_actual']-1) < 0.01"
  ],
  [
   "P70 Table's printed trapezoid count 1024 is at least the evaluations actually needed",
   "1024 >= o['tol']['evals_actual']"
  ],
  [
   "P70's printed 1024 within 10% of the bound-guaranteed evaluations (P70 used the bound)",
   "abs(o['tol']['evals_bound']/1024-1) < 0.1"
  ]
 ],
 "tol": 1e-08,
 "N_cap": 100000,
 "printed_evals": 1024
}
```

## Command
`python sim_app.py iter-6` (run from `Applied-Sciences/simulation/`)
