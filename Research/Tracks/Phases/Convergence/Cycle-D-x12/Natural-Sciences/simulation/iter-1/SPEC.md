# SIM-CV-NAT-D - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P68 bound at frequency sd 0.03 (between CVB's 0.02 and CVC's 0.05).

## Phase operationalization tested
NAT Convergence = synchronisation.

## Sources this run draws on
P68 (Amichay, Gong & Abrams 2026, 'Modeling the Evolution of Collective Synchrony', Ann N Y Acad Sci 1557:e70226, PMC12955760, CC BY; read in full in CV0): Sakaguchi-Kuramoto Eq. 1 with phase-lag strategies; two-group cooperator/cheater model; stability bound n_ch < (1 - cos alpha_ch)^-1; payoffs g(R) = R, f = 1 - cos(dtheta); Fig. 2B equilibrium population 50-50 at alpha_ch = pi/2. P76 (Wikipedia contributors, 'Kuramoto model', English Wikipedia, revision fetched 2026-10-24, CC BY-SA 4.0; read in full in CVB): d theta_i/dt = omega_i + (1/N) sum_j K_ij sin(theta_j - theta_i); order parameter r; for unimodal symmetric g, K_c = 2/(pi g(0)) and r ~ sqrt(16/(pi K_c^3)) sqrt(mu/(-g''(0))) for K = K_c(1 + mu); N = 2: locking when K > K_c = 2|omega_1|; chaos first at N = 4.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | classical Kuramoto (all lags 0) from random phases gives R > 0.99 |
| H1 | hypothesis | frequency sd 0.03: the two-cluster state persists exactly when n_ch < 1/(1 - cos alpha) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Same two-cluster test as CV0-CVC. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds/options in CVD (stats_audit, instrument_core, levelling_voter bias_mode=selection) were smoke-tested once at trivial size (seed 99, temporary directory, nothing kept) with printed values suppressed; existing kinds were not smoke-tested. CVC results were known when these hypotheses were written (replications say so).

## Parameters
```json
{
 "sim_id": "SIM-CV-NAT-D",
 "iteration": 1,
 "kind": "sync_cheaters",
 "seed": 33101,
 "N": 500,
 "T": 200,
 "dt": 0.05,
 "eps": 0.05,
 "alphas": [
  2.0943951023931953,
  2.6179938779914944
 ],
 "n_ch_values": [
  0.5,
  0.6
 ],
 "K": 1.0,
 "freq_sd": 0.03,
 "hyps": [
  [
   "frequency sd 0.03: the two-cluster state persists exactly when n_ch < 1/(1 - cos alpha)",
   "all(v['two_cluster'] == v['below_bound'] for v in o['grid'].values())"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-1` (run from `Natural-Sciences/simulation/`)
