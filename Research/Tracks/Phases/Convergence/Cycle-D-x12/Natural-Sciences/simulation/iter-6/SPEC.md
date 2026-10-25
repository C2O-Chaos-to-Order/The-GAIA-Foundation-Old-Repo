# SIM-CV-NAT-D - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Below K_c closer to onset (K = 1.2): N^-1/2 scaling?

## Phase operationalization tested
NAT Convergence = synchronisation.

## Sources this run draws on
P76 (Wikipedia contributors, 'Kuramoto model', English Wikipedia, revision fetched 2026-10-24, CC BY-SA 4.0; read in full in CVB): d theta_i/dt = omega_i + (1/N) sum_j K_ij sin(theta_j - theta_i); order parameter r; for unimodal symmetric g, K_c = 2/(pi g(0)) and r ~ sqrt(16/(pi K_c^3)) sqrt(mu/(-g''(0))) for K = K_c(1 + mu); N = 2: locking when K > K_c = 2|omega_1|; chaos first at N = 4.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | uniform random phases (N 100000) give r < 0.02 |
| H1 | hypothesis | below K_c (K = 1.2): r sqrt(N) within a factor 1.5 across N |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Random Gaussian frequencies (sd 1, K_c 1.596), random phases, RK4 dt 0.05, r averaged over t = 50-100. The N^-1/2 incoherent scaling and slower decay at K_c are standard finite-size theory (foreknown in outline), not stated in P76. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds/options in CVD (stats_audit, instrument_core, levelling_voter bias_mode=selection) were smoke-tested once at trivial size (seed 99, temporary directory, nothing kept) with printed values suppressed; existing kinds were not smoke-tested. CVC results were known when these hypotheses were written (replications say so).

## Parameters
```json
{
 "sim_id": "SIM-CV-NAT-D",
 "iteration": 6,
 "kind": "kuramoto_fss",
 "seed": 33106,
 "width": 1.0,
 "T": 100,
 "dt": 0.05,
 "N_values": [
  100,
  400,
  1600,
  6400
 ],
 "K_values": [
  1.2
 ],
 "reps": 8,
 "hyps": [
  [
   "below K_c (K = 1.2): r sqrt(N) within a factor 1.5 across N",
   "max(v['r_sqrtN'] for v in o['by_K']['1.2']['by_N'].values()) / min(v['r_sqrtN'] for v in o['by_K']['1.2']['by_N'].values()) < 1.5"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-6` (run from `Natural-Sciences/simulation/`)
