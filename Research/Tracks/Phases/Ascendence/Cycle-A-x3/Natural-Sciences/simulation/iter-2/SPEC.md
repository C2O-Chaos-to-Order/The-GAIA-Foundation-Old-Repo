# SIM-AS-NAT-A - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
The fragile AS0 NK comparison with 30 landscapes per K (6 sites): does P14% fall from K 2 to K 5, monotonically, and is K 0 single-peaked?

## Phase operationalization tested
NAT Ascendence = adaptive walks (P85's NK series).

## Sources this run draws on
P85 (Li & Zhang 2025, 'On the Probability of Reaching High Peaks in Fitness Landscapes by Adaptive Walks', Mol Biol Evol, PMC11975533, CC BY-NC; read in full in AS0): SSWM adaptive walks; P14% (probability of reaching the top 14% of peaks); RMF F = -D(x, x*) + eta, eta ~ N(0.5, sigma); HoC; NK; RMF P14% 96.3% at sigma 0.5 to 26.4% at sigma 10; NK 100% at K 0 to 24.8% at K 8; HoC about 25%; R_ph-bs 0.69-0.97 across empirical landscapes.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | an additive RMF landscape has one peak reached by every walk |
| H1 | hypothesis | NK, 30 landscapes per K: mean P14% at K 5 below K 2 |
| H2 | hypothesis | NK: mean P14% falls monotonically over K 2, 3, 4, 5 (P85: K 0-1 not fairly comparable) |
| H3 | hypothesis | NK K 0 (additive) has one peak in every landscape (P14% = 1) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
6 sites, not P85's 9; P85 warns that K 0-1 cannot be compared fairly (few peaks). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-NAT-A",
 "iteration": 2,
 "kind": "adaptive_walk",
 "seed": 35102,
 "L": 6,
 "A": 4,
 "reps": 30,
 "fracs": [
  0.14
 ],
 "max_basin_peaks": 0,
 "landscapes": [
  {
   "name": "nk_K0",
   "model": "nk",
   "K": 0
  },
  {
   "name": "nk_K1",
   "model": "nk",
   "K": 1
  },
  {
   "name": "nk_K2",
   "model": "nk",
   "K": 2
  },
  {
   "name": "nk_K3",
   "model": "nk",
   "K": 3
  },
  {
   "name": "nk_K4",
   "model": "nk",
   "K": 4
  },
  {
   "name": "nk_K5",
   "model": "nk",
   "K": 5
  }
 ],
 "hyps": [
  [
   "NK, 30 landscapes per K: mean P14% at K 5 below K 2",
   "o['landscapes']['nk_K5']['P0.14'] < o['landscapes']['nk_K2']['P0.14']"
  ],
  [
   "NK: mean P14% falls monotonically over K 2, 3, 4, 5 (P85: K 0-1 not fairly comparable)",
   "all(o['landscapes'][f'nk_K{k}']['P0.14'] > o['landscapes'][f'nk_K{k+1}']['P0.14'] for k in range(2, 5))"
  ],
  [
   "NK K 0 (additive) has one peak in every landscape (P14% = 1)",
   "o['landscapes']['nk_K0']['P0.14'] == 1.0 and o['landscapes']['nk_K0']['n_peaks'] == 1.0"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-2` (run from `Natural-Sciences/simulation/`)
