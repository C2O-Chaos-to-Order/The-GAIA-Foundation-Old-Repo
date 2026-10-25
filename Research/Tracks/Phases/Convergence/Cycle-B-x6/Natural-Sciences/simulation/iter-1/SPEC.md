# SIM-CV-NAT-B - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P76's Kuramoto model with Lorentzian frequencies (half-width 0.5, N = 2000): is K_c = 1, does the simulated order parameter follow sqrt(1 - K_c/K) above K_c and stay incoherent below it?

## Phase operationalization tested
NAT Convergence = synchronisation. Heterogeneous oscillators (P76) generalise P68's identical-frequency model.

## Sources this run draws on
P76 (Wikipedia contributors, 'Kuramoto model', English Wikipedia, revision fetched 2026-10-24, CC BY-SA 4.0; read in full in CVB): d theta_i/dt = omega_i + (1/N) sum_j K_ij sin(theta_j - theta_i); order parameter r; for unimodal symmetric g, K_c = 2/(pi g(0)) and r ~ sqrt(16/(pi K_c^3)) sqrt(mu/(-g''(0))) for K = K_c(1 + mu); N = 2: locking when K > K_c = 2|omega_1|; chaos first at N = 4.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | identical frequencies with K = 1 synchronise (r > 0.99) |
| H1 | hypothesis | P76's K_c = 2/(pi g(0)) equals 2 gamma = 1.0 for the Lorentzian (within 1e-9) |
| H2 | hypothesis | self-consistency solution within 0.01 of the closed form sqrt(1 - K_c/K) for K = 1.2-3 |
| H3 | hypothesis | simulated r within 0.05 of sqrt(1 - K_c/K) for K = 1.2-3 |
| H4 | hypothesis | below K_c (K = 0.5, 0.8) the simulated r stays below 0.1 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic frequency quantiles, clipped at +-50 gamma (1.3% of the Lorentzian mass is clipped; these oscillators drift either way); random initial phases; RK4 dt 0.01, r averaged over t = 100-200. The closed form sqrt(1 - K_c/K) for the Lorentzian is standard theory (Ott-Antonsen), not stated in P76; foreknown. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-NAT-B",
 "iteration": 1,
 "kind": "kuramoto_hetero",
 "seed": 31101,
 "N": 2000,
 "dist": "lorentz",
 "width": 0.5,
 "clip": 50,
 "K_values": [
  0.5,
  0.8,
  1.2,
  1.5,
  2.0,
  3.0
 ],
 "T": 200,
 "dt": 0.01,
 "hyps": [
  [
   "P76's K_c = 2/(pi g(0)) equals 2 gamma = 1.0 for the Lorentzian (within 1e-9)",
   "abs(o['Kc']-1.0) < 1e-9"
  ],
  [
   "self-consistency solution within 0.01 of the closed form sqrt(1 - K_c/K) for K = 1.2-3",
   "all(abs(v['r_selfconsistent']-v['r_lorentz_exact']) < 0.01 for k, v in o['by_K'].items() if float(k) > 1)"
  ],
  [
   "simulated r within 0.05 of sqrt(1 - K_c/K) for K = 1.2-3",
   "all(abs(v['r_sim']-v['r_lorentz_exact']) < 0.05 for k, v in o['by_K'].items() if float(k) > 1)"
  ],
  [
   "below K_c (K = 0.5, 0.8) the simulated r stays below 0.1",
   "all(v['r_sim'] < 0.1 for k, v in o['by_K'].items() if float(k) < 1)"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-1` (run from `Natural-Sciences/simulation/`)
