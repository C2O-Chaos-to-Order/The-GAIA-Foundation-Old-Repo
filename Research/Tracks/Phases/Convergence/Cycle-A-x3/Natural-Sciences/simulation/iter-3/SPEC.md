# SIM-CV-NAT-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P68's statement that persistent populations are 'always 50-50': does P68's replicator dynamic end at 0.5 for alpha pi/3, pi/2, 2pi/3 and 5pi/6 from n0 0.2 and 0.8?

## Phase operationalization tested
NAT Convergence = synchronisation with evolving strategies.

## Sources this run draws on
P68 (Amichay, Gong & Abrams 2026, 'Modeling the Evolution of Collective Synchrony', Ann N Y Acad Sci 1557:e70226, PMC12955760, CC BY; read in full in CV0): Sakaguchi-Kuramoto Eq. 1 with phase-lag strategies; two-group cooperator/cheater model; stability bound n_ch < (1 - cos alpha_ch)^-1; payoffs g(R) = R, f = 1 - cos(dtheta); Fig. 2B equilibrium population 50-50 at alpha_ch = pi/2.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | classical Kuramoto (all lags 0) from random phases gives R > 0.99 |
| H1 | hypothesis | P68's 'always 50-50': replicator ends within 0.01 of 0.5 for alpha pi/3, pi/2, 2pi/3, 5pi/6 from n0 0.2 and 0.8 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Uses P68's closed-form payoffs; k = 1, dt 0.01, T 600 are the agent's; small alpha means small payoff differences and slow approach (disclosed). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-NAT-A",
 "iteration": 3,
 "kind": "sync_cheaters",
 "seed": 30103,
 "N": 100,
 "K": 1.0,
 "T": 50,
 "dt": 0.05,
 "eps": 0.05,
 "alphas": [
  1.5707963267948966
 ],
 "n_ch_values": [
  0.5
 ],
 "replicators": [
  {
   "alpha": 1.0471975511965976,
   "n0": 0.2,
   "T": 600,
   "dt": 0.01
  },
  {
   "alpha": 1.0471975511965976,
   "n0": 0.8,
   "T": 600,
   "dt": 0.01
  },
  {
   "alpha": 1.5707963267948966,
   "n0": 0.2,
   "T": 600,
   "dt": 0.01
  },
  {
   "alpha": 1.5707963267948966,
   "n0": 0.8,
   "T": 600,
   "dt": 0.01
  },
  {
   "alpha": 2.0943951023931953,
   "n0": 0.2,
   "T": 600,
   "dt": 0.01
  },
  {
   "alpha": 2.0943951023931953,
   "n0": 0.8,
   "T": 600,
   "dt": 0.01
  },
  {
   "alpha": 2.6179938779914944,
   "n0": 0.2,
   "T": 600,
   "dt": 0.01
  },
  {
   "alpha": 2.6179938779914944,
   "n0": 0.8,
   "T": 600,
   "dt": 0.01
  }
 ],
 "hyps": [
  [
   "P68's 'always 50-50': replicator ends within 0.01 of 0.5 for alpha pi/3, pi/2, 2pi/3, 5pi/6 from n0 0.2 and 0.8",
   "all(abs(r['n_end']-0.5) < 0.01 for r in o['replicators'])"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-3` (run from `Natural-Sciences/simulation/`)
