# SIM-CV-NAT-D - iteration 12 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication: Lorentzian, N 500.

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
| H1 | hypothesis | replication (N 500): r < 0.15 at K 0.5 and within 0.05 of 0.8165 at K 3 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Pure replication. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds/options in CVD (stats_audit, instrument_core, levelling_voter bias_mode=selection) were smoke-tested once at trivial size (seed 99, temporary directory, nothing kept) with printed values suppressed; existing kinds were not smoke-tested. CVC results were known when these hypotheses were written (replications say so).

## Parameters
```json
{
 "sim_id": "SIM-CV-NAT-D",
 "iteration": 12,
 "kind": "kuramoto_hetero",
 "seed": 33112,
 "N": 500,
 "dist": "lorentz",
 "width": 0.5,
 "clip": 50,
 "K_values": [
  0.5,
  3.0
 ],
 "T": 200,
 "dt": 0.02,
 "hyps": [
  [
   "replication (N 500): r < 0.15 at K 0.5 and within 0.05 of 0.8165 at K 3",
   "o['by_K']['0.5']['r_sim'] < 0.15 and abs(o['by_K']['3.0']['r_sim'] - 0.8165) < 0.05"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-12` (run from `Natural-Sciences/simulation/`)
