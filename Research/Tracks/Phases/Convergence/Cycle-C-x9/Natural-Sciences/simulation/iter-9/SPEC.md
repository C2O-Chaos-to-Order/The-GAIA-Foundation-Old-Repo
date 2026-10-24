# SIM-CV-NAT-C - iteration 9 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication of CVB iter-1 at N = 1000 and dt 0.02: does r still follow sqrt(1 - K_c/K) above K_c and stay below 0.1 below it?

## Phase operationalization tested
NAT Convergence = synchronisation.

## Sources this run draws on
P76 (Wikipedia contributors, 'Kuramoto model', English Wikipedia, revision fetched 2026-10-24, CC BY-SA 4.0; read in full in CVB): d theta_i/dt = omega_i + (1/N) sum_j K_ij sin(theta_j - theta_i); order parameter r; for unimodal symmetric g, K_c = 2/(pi g(0)) and r ~ sqrt(16/(pi K_c^3)) sqrt(mu/(-g''(0))) for K = K_c(1 + mu); N = 2: locking when K > K_c = 2|omega_1|; chaos first at N = 4.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | identical frequencies with K = 1 synchronise (r > 0.99) |
| H1 | hypothesis | replication (N = 1000, dt 0.02): simulated r within 0.05 of sqrt(1 - K_c/K) for K = 1.2-3 |
| H2 | hypothesis | below K_c (K = 0.5, 0.8) r stays below 0.1 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Pure replication with coarser settings (expected to add little). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds in CVC (kuramoto_lyap, kuramoto_fss, crowd_bound, trap_simpson, levelling_voter, common_core) were smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before the SPECs; printed values were suppressed except one kuramoto_lyap smoke (N = 3 and 4, K = 1, 3 settings, T 400) whose maxima (both slightly negative) were seen (disclosed). Thresholds were not informed by smoke values. Existing kinds were not smoke-tested.

## Parameters
```json
{
 "sim_id": "SIM-CV-NAT-C",
 "iteration": 9,
 "kind": "kuramoto_hetero",
 "seed": 32109,
 "N": 1000,
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
 "dt": 0.02,
 "hyps": [
  [
   "replication (N = 1000, dt 0.02): simulated r within 0.05 of sqrt(1 - K_c/K) for K = 1.2-3",
   "all(abs(v['r_sim']-v['r_lorentz_exact']) < 0.05 for k, v in o['by_K'].items() if float(k) > 1)"
  ],
  [
   "below K_c (K = 0.5, 0.8) r stays below 0.1",
   "all(v['r_sim'] < 0.1 for k, v in o['by_K'].items() if float(k) < 1)"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-9` (run from `Natural-Sciences/simulation/`)
