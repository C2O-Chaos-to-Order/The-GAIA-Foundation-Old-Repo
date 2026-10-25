# SIM-CV-NAT-C - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P76's 'N = 3 ... cannot be chaotic': is the largest Lyapunov exponent below 0.01 in 90 random N = 3 settings (K 0.5, 1, 1.5)?

## Phase operationalization tested
NAT Convergence = synchronisation. Small-N dynamics of P76.

## Sources this run draws on
P76 (Wikipedia contributors, 'Kuramoto model', English Wikipedia, revision fetched 2026-10-24, CC BY-SA 4.0; read in full in CVB): d theta_i/dt = omega_i + (1/N) sum_j K_ij sin(theta_j - theta_i); order parameter r; for unimodal symmetric g, K_c = 2/(pi g(0)) and r ~ sqrt(16/(pi K_c^3)) sqrt(mu/(-g''(0))) for K = K_c(1 + mu); N = 2: locking when K > K_c = 2|omega_1|; chaos first at N = 4.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | N = 2 identical pair: transverse exponent -K within 0.02 |
| H1 | hypothesis | P76: N = 3 cannot be chaotic - the largest Lyapunov exponent stays below 0.01 in all 90 settings |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Benettin method, RK4 dt 0.02, T 800 (burn-in 100), renormalisation every time unit, tangent kept orthogonal to (1, ..., 1); frequencies uniform on [-1, 1] and centred. The threshold 0.01 separates chaos from numerical zero; a quasi-periodic orbit gives ~0. Exponents for chaotic N = 4 Kuramoto attractors in the literature are small (agent recollection, no number recalled), so a miss is possible with only 30 random settings per K. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds in CVC (kuramoto_lyap, kuramoto_fss, crowd_bound, trap_simpson, levelling_voter, common_core) were smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before the SPECs; printed values were suppressed except one kuramoto_lyap smoke (N = 3 and 4, K = 1, 3 settings, T 400) whose maxima (both slightly negative) were seen (disclosed). Thresholds were not informed by smoke values. Existing kinds were not smoke-tested.

## Parameters
```json
{
 "sim_id": "SIM-CV-NAT-C",
 "iteration": 1,
 "kind": "kuramoto_lyap",
 "seed": 32101,
 "T": 800,
 "dt": 0.02,
 "renorm": 1.0,
 "burn": 100.0,
 "thr": 0.01,
 "N_values": [
  3
 ],
 "K_values": [
  0.5,
  1.0,
  1.5
 ],
 "settings": 30,
 "hyps": [
  [
   "P76: N = 3 cannot be chaotic - the largest Lyapunov exponent stays below 0.01 in all 90 settings",
   "all(v['max_lyap'] < 0.01 for v in o['by_case'].values())"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-1` (run from `Natural-Sciences/simulation/`)
