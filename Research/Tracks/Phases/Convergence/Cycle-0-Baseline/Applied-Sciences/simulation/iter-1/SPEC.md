# SIM-CV-APP-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P70's quadrature claims: do composite trapezoid, Simpson and 2-point Gauss errors for exp(-x^2) on [0, 1] at n = 8, 16, 32 subintervals match Table 1, does the trapezoid reach 1e-8 in 256 evaluations, is the asymptotic eta 2/5 (Lemma 2.6), and do Table 2's own counts give the 40-62% reduction over adaptive Simpson claimed in the abstract?

## Phase operationalization tested
APP Convergence = numerical convergence (error decreasing at a known order as the mesh is refined; P70).

## Sources this run draws on
P70 (Asgedom & Kefela 2026, adaptive hybrid Simpson-Gauss quadrature (AHQS), PLoS One e0335582, PMC12928599, CC BY; read in full in CV0 incl. peer-review history): Table 1 errors for exp(-x^2) on [0, 1] at n = 8, 16, 32; Table 2 evaluations to 1e-8; Lemma 2.6 eta <= 2/5; Algorithm 1; abstract claim 40-62% fewer evaluations than adaptive Simpson; Section 4.3 claim 20-35% fewer than Gauss-Kronrod for f2-f5.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | Simpson and 2-point Gauss integrate a cubic exactly |
| H1 | hypothesis | printed trapezoid error at n = 8 (2.13e-3) within 10% of computed |
| H2 | hypothesis | printed Simpson errors at n = 8, 16, 32 within 10% of computed |
| H3 | hypothesis | printed 2-point Gauss errors within 10% of computed |
| H4 | hypothesis | trapezoid reaches 1e-8 within P70's printed 256 evaluations |
| H5 | hypothesis | asymptotic eta within 0.01 of P70 Lemma 2.6's bound 2/5 |
| H6 | hypothesis | Table 2 hybrid-vs-adaptive-Simpson reductions all lie in P70's claimed 40-62% range |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic. 'n' is read as the number of subintervals for every rule (P70 does not define it explicitly; other readings were not exhaustively tried). Algorithm 1 is implemented as printed (sigma 0.8, L 1, eps 1e-8) and its evaluation count is reported only. Foreknowledge: hand estimates before running (trapezoid n = 8 error about 9.6e-4; about 2500 evaluations for 1e-8).Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so every outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-APP-0",
 "iteration": 1,
 "kind": "quad_convergence",
 "seed": 29401,
 "n_values": [
  8,
  16,
  32
 ],
 "target": 1e-08,
 "eps": 1e-08,
 "eta_h": 0.01,
 "eta_x0": 0.3,
 "printed": {
  "trapezoid": [
   0.00213,
   0.000533,
   0.000133
  ],
  "simpson": [
   1.47e-05,
   9.17e-07,
   5.73e-08
  ],
  "gauss2": [
   8.92e-06,
   5.58e-07,
   3.49e-08
  ],
  "evals_1e8": {
   "trapezoid": 256,
   "simpson": 64
  }
 },
 "reductions": {
  "vsAS_f1": [
   36,
   48
  ],
  "vsAS_f2": [
   247,
   384
  ],
  "vsAS_f3": [
   523,
   768
  ],
  "vsAS_f4": [
   128,
   192
  ],
  "vsAS_f5": [
   127,
   96
  ],
  "vsGK_f1": [
   36,
   45
  ],
  "vsGK_f2": [
   247,
   315
  ],
  "vsGK_f3": [
   523,
   640
  ],
  "vsGK_f4": [
   128,
   180
  ],
  "vsGK_f5": [
   127,
   165
  ]
 },
 "hyps": [
  [
   "printed trapezoid error at n = 8 (2.13e-3) within 10% of computed",
   "abs(o['table']['trapezoid']['errors']['8']/2.13e-3-1)<0.1"
  ],
  [
   "printed Simpson errors at n = 8, 16, 32 within 10% of computed",
   "all(abs(o['table']['simpson']['errors'][n]/p-1)<0.1 for n,p in zip(['8','16','32'],[1.47e-5,9.17e-7,5.73e-8]))"
  ],
  [
   "printed 2-point Gauss errors within 10% of computed",
   "all(abs(o['table']['gauss2']['errors'][n]/p-1)<0.1 for n,p in zip(['8','16','32'],[8.92e-6,5.58e-7,3.49e-8]))"
  ],
  [
   "trapezoid reaches 1e-8 within P70's printed 256 evaluations",
   "o['table']['trapezoid']['evals_for_target']<=256"
  ],
  [
   "asymptotic eta within 0.01 of P70 Lemma 2.6's bound 2/5",
   "abs(o['eta']-0.4)<0.01"
  ],
  [
   "Table 2 hybrid-vs-adaptive-Simpson reductions all lie in P70's claimed 40-62% range",
   "all(40<=o['reductions_pct'][f'vsAS_f{i}']<=62 for i in range(1,6))"
  ]
 ]
}
```

## Command
`python sim_app.py iter-1` (run from `Applied-Sciences/simulation/`)
