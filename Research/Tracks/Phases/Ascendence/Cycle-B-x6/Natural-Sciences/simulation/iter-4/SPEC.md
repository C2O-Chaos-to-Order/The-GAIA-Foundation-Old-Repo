# SIM-AS-NAT-B - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Binary sites (12 two-state sites, 4096 genotypes): does P14% fall from RMF sigma 0.5 to 2 to HoC, with positive peak-basin correlation?

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
| H1 | hypothesis | binary sites (12 two-state sites): P14% falls from RMF sigma 0.5 to sigma 2 to HoC |
| H2 | hypothesis | binary sites: peak height and basin size positively correlated in every landscape with >= 3 peaks |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's extension to two-state sites (P85 uses four-state sites). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-NAT-B",
 "iteration": 4,
 "kind": "adaptive_walk",
 "seed": 36104,
 "L": 12,
 "A": 2,
 "reps": 10,
 "fracs": [
  0.14
 ],
 "max_basin_peaks": 400,
 "landscapes": [
  {
   "name": "rmf_s0.5",
   "model": "rmf",
   "sigma": 0.5
  },
  {
   "name": "rmf_s2",
   "model": "rmf",
   "sigma": 2.0
  },
  {
   "name": "hoc",
   "model": "hoc"
  }
 ],
 "hyps": [
  [
   "binary sites (12 two-state sites): P14% falls from RMF sigma 0.5 to sigma 2 to HoC",
   "o['landscapes']['rmf_s0.5']['P0.14'] > o['landscapes']['rmf_s2']['P0.14'] > o['landscapes']['hoc']['P0.14']"
  ],
  [
   "binary sites: peak height and basin size positively correlated in every landscape with >= 3 peaks",
   "all(v.get('R_ph_bs_min') is None or v['R_ph_bs_min'] > 0 for k, v in o['landscapes'].items() if k != 'V1_smooth')"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-4` (run from `Natural-Sciences/simulation/`)
