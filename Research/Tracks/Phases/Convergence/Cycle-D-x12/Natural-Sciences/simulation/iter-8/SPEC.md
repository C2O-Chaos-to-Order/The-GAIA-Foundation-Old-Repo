# SIM-CV-NAT-D - iteration 8 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication of CVC's marginal N = 4 positive exponent near K 0.8 (60 new settings).

## Phase operationalization tested
NAT Convergence = synchronisation.

## Sources this run draws on
P76 (Wikipedia contributors, 'Kuramoto model', English Wikipedia, revision fetched 2026-10-24, CC BY-SA 4.0; read in full in CVB): d theta_i/dt = omega_i + (1/N) sum_j K_ij sin(theta_j - theta_i); order parameter r; for unimodal symmetric g, K_c = 2/(pi g(0)) and r ~ sqrt(16/(pi K_c^3)) sqrt(mu/(-g''(0))) for K = K_c(1 + mu); N = 2: locking when K > K_c = 2|omega_1|; chaos first at N = 4.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | N = 2 identical pair: transverse exponent -K within 0.02 |
| H1 | hypothesis | N = 4 near K 0.8: at least one of 60 settings has a largest exponent above 0.01 (replicating CVC's marginal positive) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Benettin method, RK4 dt 0.02, T 800 (burn-in 100), renormalisation every time unit, tangent kept orthogonal to (1, ..., 1); frequencies uniform on [-1, 1] and centred. The threshold 0.01 separates chaos from numerical zero; a quasi-periodic orbit gives ~0. Exponents for chaotic N = 4 Kuramoto attractors in the literature are small (agent recollection, no number recalled), so a miss is possible with only 30 random settings per K. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds/options in CVD (stats_audit, instrument_core, levelling_voter bias_mode=selection) were smoke-tested once at trivial size (seed 99, temporary directory, nothing kept) with printed values suppressed; existing kinds were not smoke-tested. CVC results were known when these hypotheses were written (replications say so).

## Parameters
```json
{
 "sim_id": "SIM-CV-NAT-D",
 "iteration": 8,
 "kind": "kuramoto_lyap",
 "seed": 33108,
 "T": 800,
 "dt": 0.02,
 "renorm": 1.0,
 "burn": 100.0,
 "thr": 0.01,
 "N_values": [
  4
 ],
 "K_values": [
  0.7,
  0.8,
  0.9
 ],
 "settings": 20,
 "hyps": [
  [
   "N = 4 near K 0.8: at least one of 60 settings has a largest exponent above 0.01 (replicating CVC's marginal positive)",
   "any(v['max_lyap'] > 0.01 for v in o['by_case'].values())"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-8` (run from `Natural-Sciences/simulation/`)
