# SIM-CV-NAT-A - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P68's bound near its edge: with N = 500 and alpha 2pi/3, 3pi/4, 5pi/6, 11pi/12 (bounds 0.667, 0.586, 0.536, 0.509), does the two-cluster state persist exactly below the bound for n_ch 0.45-0.70, including cells within 0.02 of it?

## Phase operationalization tested
NAT Convergence = synchronisation.

## Sources this run draws on
P68 (Amichay, Gong & Abrams 2026, 'Modeling the Evolution of Collective Synchrony', Ann N Y Acad Sci 1557:e70226, PMC12955760, CC BY; read in full in CV0): Sakaguchi-Kuramoto Eq. 1 with phase-lag strategies; two-group cooperator/cheater model; stability bound n_ch < (1 - cos alpha_ch)^-1; payoffs g(R) = R, f = 1 - cos(dtheta); Fig. 2B equilibrium population 50-50 at alpha_ch = pi/2.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | classical Kuramoto (all lags 0) from random phases gives R > 0.99 |
| H1 | hypothesis | two-cluster state persists exactly when n_ch < 1/(1 - cos alpha), including cells within 0.02 of the bound |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic apart from initial noise; T 200 may be short for cells very close to the bound (critical slowing; disclosed). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-NAT-A",
 "iteration": 2,
 "kind": "sync_cheaters",
 "seed": 30102,
 "N": 500,
 "K": 1.0,
 "T": 200,
 "dt": 0.05,
 "eps": 0.05,
 "alphas": [
  2.0943951023931953,
  2.356194490192345,
  2.6179938779914944,
  2.8797932657906435
 ],
 "n_ch_values": [
  0.45,
  0.5,
  0.55,
  0.6,
  0.65,
  0.7
 ],
 "hyps": [
  [
   "two-cluster state persists exactly when n_ch < 1/(1 - cos alpha), including cells within 0.02 of the bound",
   "all(v['two_cluster'] == v['below_bound'] for v in o['grid'].values())"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-2` (run from `Natural-Sciences/simulation/`)
