# SIM-AS-NAT-B - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
NK K 8 at 9 sites: is P14% within 0.10 of P85's 24.8%?

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
| H1 | hypothesis | NK K 8 at 9 sites (maximally rugged): P14% within 0.10 of P85's 24.8% |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Two landscapes; random interaction sets. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-NAT-B",
 "iteration": 5,
 "kind": "adaptive_walk_sizes",
 "seed": 36105,
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
   "name": "nk_K8",
   "model": "nk",
   "K": 8
  }
 ],
 "hyps": [
  [
   "NK K 8 at 9 sites (maximally rugged): P14% within 0.10 of P85's 24.8%",
   "abs(o['by_L']['9']['nk_K8']['P0.14'] - 0.248) <= 0.10"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-5` (run from `Natural-Sciences/simulation/`)
