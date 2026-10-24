# SIM-CV-NAT-B - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P76's onset formulas for a unit Gaussian g: is K_c = 1.59577, does the simulation follow the self-consistency equation, and how good is P76's small-mu approximation at mu = 0.034 and 0.097?

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
| H1 | hypothesis | P76's K_c for a unit Gaussian is 2 sqrt(2 pi)/pi = 1.59577 (within 1e-5) |
| H2 | hypothesis | simulated r within 0.05 of the self-consistency solution at K = 2.0 and 2.5 |
| H3 | hypothesis | P76's small-mu approximation within 0.05 of the self-consistency solution at K = 1.65 (mu = 0.034) |
| H4 | hypothesis | P76's small-mu approximation within 0.05 of the self-consistency solution at K = 1.75 (mu = 0.097) |
| H5 | hypothesis | near threshold (K = 1.65) the N = 2000 simulation is within 0.1 of the self-consistency solution |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Same integrator; self-consistency solved by root-finding on a 4001-point grid of P76's integral. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-NAT-B",
 "iteration": 2,
 "kind": "kuramoto_hetero",
 "seed": 31102,
 "N": 2000,
 "dist": "gauss",
 "width": 1.0,
 "K_values": [
  1.4,
  1.65,
  1.75,
  2.0,
  2.5
 ],
 "T": 200,
 "dt": 0.01,
 "hyps": [
  [
   "P76's K_c for a unit Gaussian is 2 sqrt(2 pi)/pi = 1.59577 (within 1e-5)",
   "abs(o['Kc']-1.59577) < 1e-5"
  ],
  [
   "simulated r within 0.05 of the self-consistency solution at K = 2.0 and 2.5",
   "all(abs(o['by_K'][k]['r_sim']-o['by_K'][k]['r_selfconsistent']) < 0.05 for k in ['2.0', '2.5'])"
  ],
  [
   "P76's small-mu approximation within 0.05 of the self-consistency solution at K = 1.65 (mu = 0.034)",
   "abs(o['by_K']['1.65']['r_small_mu']-o['by_K']['1.65']['r_selfconsistent']) < 0.05"
  ],
  [
   "P76's small-mu approximation within 0.05 of the self-consistency solution at K = 1.75 (mu = 0.097)",
   "abs(o['by_K']['1.75']['r_small_mu']-o['by_K']['1.75']['r_selfconsistent']) < 0.05"
  ],
  [
   "near threshold (K = 1.65) the N = 2000 simulation is within 0.1 of the self-consistency solution",
   "abs(o['by_K']['1.65']['r_sim']-o['by_K']['1.65']['r_selfconsistent']) < 0.1"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-2` (run from `Natural-Sciences/simulation/`)
