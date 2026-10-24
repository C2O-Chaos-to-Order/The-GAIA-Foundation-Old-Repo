# SIM-AS-NAT-B - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
RMF sigma 1 at P85's size: is P14% between P85's sigma 0.5 and 10 values?

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
| H1 | hypothesis | 9 sites, RMF sigma 1: P14% between P85's sigma 0.5 and sigma 10 values (0.264 < P14% < 0.963) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Two landscapes. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-NAT-B",
 "iteration": 1,
 "kind": "adaptive_walk_sizes",
 "seed": 36101,
 "A": 4,
 "fracs": [
  0.14
 ],
 "max_basin_peaks": 0,
 "L_list": [
  9
 ],
 "reps": 2,
 "landscapes": [
  {
   "name": "rmf_s1",
   "model": "rmf",
   "sigma": 1.0
  }
 ],
 "hyps": [
  [
   "9 sites, RMF sigma 1: P14% between P85's sigma 0.5 and sigma 10 values (0.264 < P14% < 0.963)",
   "0.264 < o['by_L']['9']['rmf_s1']['P0.14'] < 0.963"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-1` (run from `Natural-Sciences/simulation/`)
