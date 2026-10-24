# SIM-CV-APP-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P70 Table 2 for f4 (x sin(10 x)): do composite trapezoid and Simpson need P70's printed evaluations (within 10%) to reach 1e-8, and does Algorithm 1 as printed need P70's hybrid count (within 25%) with error below 1e-8? Is its error below eps at eps 1e-6, 1e-8 and 1e-10?

## Phase operationalization tested
APP Convergence = numerical convergence and its cost.

## Sources this run draws on
P70 (Asgedom & Kefela 2026, adaptive hybrid Simpson-Gauss quadrature (AHQS), PLoS One e0335582, PMC12928599, CC BY; read in full in CV0 incl. peer-review history): Table 1 errors for exp(-x^2) on [0, 1] at n = 8, 16, 32; Table 2 evaluations to 1e-8; Lemma 2.6 eta <= 2/5; Algorithm 1; abstract claim 40-62% fewer evaluations than adaptive Simpson; Section 4.3 claim 20-35% fewer than Gauss-Kronrod for f2-f5.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | Simpson and 2-point Gauss integrate a cubic exactly |
| H1 | hypothesis | trapezoid evaluations to 1e-8 within 10% of P70 Table 2's 1024 |
| H2 | hypothesis | Simpson evaluations within 10% of Table 2's 256 |
| H3 | hypothesis | Algorithm 1 as printed (eps 1e-8) within 25% of Table 2's hybrid count 128 |
| H4 | hypothesis | Algorithm 1 error at eps 1e-8 is below 1e-8 |
| H5 | hypothesis | Algorithm 1 error below eps at eps 1e-6, 1e-8, 1e-10 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic. 'Evaluations' for composite rules = number of nodes (n + 1), the agent's reading. Exact integrals: (sin 10 - 10 cos 10)/100. f5 (x^-0.5) is singular at 0 and not used. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-APP-A",
 "iteration": 3,
 "kind": "quad_convergence",
 "seed": 30403,
 "func": "f4",
 "n_values": [
  8,
  16,
  32
 ],
 "target": 1e-08,
 "eps": 1e-08,
 "eta_h": 0.01,
 "eta_x0": 0.3,
 "n_cap": 200000,
 "eps_values": [
  1e-06,
  1e-08,
  1e-10
 ],
 "hyps": [
  [
   "trapezoid evaluations to 1e-8 within 10% of P70 Table 2's 1024",
   "abs(o['table']['trapezoid']['evals_for_target']/1024-1) < 0.1"
  ],
  [
   "Simpson evaluations within 10% of Table 2's 256",
   "abs(o['table']['simpson']['evals_for_target']/256-1) < 0.1"
  ],
  [
   "Algorithm 1 as printed (eps 1e-8) within 25% of Table 2's hybrid count 128",
   "abs(o['ahqs']['evals']/128-1) < 0.25"
  ],
  [
   "Algorithm 1 error at eps 1e-8 is below 1e-8",
   "o['ahqs']['error'] < 1e-8"
  ],
  [
   "Algorithm 1 error below eps at eps 1e-6, 1e-8, 1e-10",
   "all(v['error'] < float(k) for k, v in o['ahqs_by_eps'].items())"
  ]
 ]
}
```

## Command
`python sim_app.py iter-3` (run from `Applied-Sciences/simulation/`)
