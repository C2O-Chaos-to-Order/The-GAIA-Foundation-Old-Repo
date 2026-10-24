# SIM-CV-NAT-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P68's two-group Sakaguchi-Kuramoto model: does the cooperator/cheater two-cluster state persist exactly when n_ch < 1/(1 - cos alpha) (N = 200 oscillators, alpha pi/3, 2pi/3, 5pi/6; n_ch 0.3-0.9), and does P68's replicator dynamic at alpha pi/2 settle at the 50-50 population?

## Phase operationalization tested
NAT Convergence = synchronisation: oscillators converging on a common rhythm (Kuramoto order parameter R; P68). Competing reading: convergent evolution (not used in CV0).

## Sources this run draws on
P68 (Amichay, Gong & Abrams 2026, 'Modeling the Evolution of Collective Synchrony', Ann N Y Acad Sci 1557:e70226, PMC12955760, CC BY; read in full in CV0): Sakaguchi-Kuramoto Eq. 1 with phase-lag strategies; two-group cooperator/cheater model; stability bound n_ch < (1 - cos alpha_ch)^-1; payoffs g(R) = R, f = 1 - cos(dtheta); Fig. 2B equilibrium population 50-50 at alpha_ch = pi/2.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | classical Kuramoto (all lags 0) from random phases gives R > 0.99 |
| H1 | hypothesis | alpha pi/3 (bound 2): two-cluster state persists for every n_ch tested |
| H2 | hypothesis | alpha 2pi/3 and 5pi/6: two-cluster state persists iff n_ch is below 1/(1 - cos alpha) |
| H3 | hypothesis | replicator at alpha pi/2 from n_ch 0.2 ends within 0.01 of 0.5 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic apart from the initial noise (eps 0.05). RK4 with dt 0.05 to T 150; 'two-cluster' = gap within 0.05 rad of alpha and both clusters with |mean phasor| > 0.99 (agent's operational criterion). Replicator uses P68's closed-form payoffs; k = 1 and the 0.01 time step are the agent's choices. Foreknowledge from reading: the bound is analytic in P68 (Eq. 9 and linear stability).Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so every outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-NAT-0",
 "iteration": 1,
 "kind": "sync_cheaters",
 "seed": 29101,
 "N": 200,
 "K": 1.0,
 "T": 150,
 "dt": 0.05,
 "eps": 0.05,
 "alphas": [
  1.0471975511965976,
  2.0943951023931953,
  2.6179938779914944
 ],
 "n_ch_values": [
  0.3,
  0.5,
  0.6,
  0.7,
  0.9
 ],
 "replicator": {
  "alpha": 1.5707963267948966,
  "n0": 0.2,
  "T": 400,
  "dt": 0.01
 },
 "hyps": [
  [
   "alpha pi/3 (bound 2): two-cluster state persists for every n_ch tested",
   "all(v['two_cluster'] for k,v in o['grid'].items() if k.startswith('a1.0472'))"
  ],
  [
   "alpha 2pi/3 and 5pi/6: two-cluster state persists iff n_ch is below 1/(1 - cos alpha)",
   "all(v['two_cluster']==v['below_bound'] for k,v in o['grid'].items() if not k.startswith('a1.0472'))"
  ],
  [
   "replicator at alpha pi/2 from n_ch 0.2 ends within 0.01 of 0.5",
   "abs(o['replicator']['n_end']-0.5)<0.01"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-1` (run from `Natural-Sciences/simulation/`)
