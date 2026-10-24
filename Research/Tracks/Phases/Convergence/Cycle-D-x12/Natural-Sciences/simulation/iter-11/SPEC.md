# SIM-CV-NAT-D - iteration 11 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication: Gaussian frequencies, N 1000.

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
| H1 | hypothesis | replication (Gaussian, N 1000): r within 0.05 of self-consistency at K 2.0 and 2.5 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Pure replication. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds/options in CVD (stats_audit, instrument_core, levelling_voter bias_mode=selection) were smoke-tested once at trivial size (seed 99, temporary directory, nothing kept) with printed values suppressed; existing kinds were not smoke-tested. CVC results were known when these hypotheses were written (replications say so).

## Parameters
```json
{
 "sim_id": "SIM-CV-NAT-D",
 "iteration": 11,
 "kind": "kuramoto_hetero",
 "seed": 33111,
 "N": 1000,
 "dist": "gauss",
 "width": 1.0,
 "K_values": [
  2.0,
  2.5
 ],
 "T": 200,
 "dt": 0.02,
 "hyps": [
  [
   "replication (Gaussian, N 1000): r within 0.05 of self-consistency at K 2.0 and 2.5",
   "all(abs(v['r_sim']-v['r_selfconsistent']) < 0.05 for v in o['by_K'].values())"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-11` (run from `Natural-Sciences/simulation/`)
