# SIM-AS-NAT-B - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P85's other high-peak thresholds on HoC (8 sites): is P1% < P5% < P14% < P25%, each above its uniform share?

## Phase operationalization tested
NAT Ascendence = adaptive walks climbing a fitness landscape (P85).

## Sources this run draws on
P85 (Li & Zhang 2025, 'On the Probability of Reaching High Peaks in Fitness Landscapes by Adaptive Walks', Mol Biol Evol, PMC11975533, CC BY-NC; read in full in AS0): SSWM adaptive walks; P14% (probability of reaching the top 14% of peaks); RMF F = -D(x, x*) + eta, eta ~ N(0.5, sigma); HoC; NK; RMF P14% 96.3% at sigma 0.5 to 26.4% at sigma 10; NK 100% at K 0 to 24.8% at K 8; HoC about 25%; R_ph-bs 0.69-0.97 across empirical landscapes.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | an additive landscape has one peak reached by every walk |
| H1 | hypothesis | HoC, 8 sites: P1% < P5% < P14% < P25% |
| H2 | hypothesis | HoC: every P_x% exceeds x (walks favour high peaks) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
5 landscapes; 'top x%' = floor(x n_peaks), at least 1. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-NAT-B",
 "iteration": 3,
 "kind": "adaptive_walk",
 "seed": 36103,
 "L": 8,
 "A": 4,
 "reps": 5,
 "fracs": [
  0.01,
  0.05,
  0.14,
  0.25
 ],
 "max_basin_peaks": 0,
 "landscapes": [
  {
   "name": "hoc",
   "model": "hoc"
  }
 ],
 "hyps": [
  [
   "HoC, 8 sites: P1% < P5% < P14% < P25%",
   "(lambda v: v['P0.01'] < v['P0.05'] < v['P0.14'] < v['P0.25'])(o['landscapes']['hoc'])"
  ],
  [
   "HoC: every P_x% exceeds x (walks favour high peaks)",
   "(lambda v: v['P0.01'] > 0.01 and v['P0.05'] > 0.05 and v['P0.14'] > 0.14 and v['P0.25'] > 0.25)(o['landscapes']['hoc'])"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-3` (run from `Natural-Sciences/simulation/`)
