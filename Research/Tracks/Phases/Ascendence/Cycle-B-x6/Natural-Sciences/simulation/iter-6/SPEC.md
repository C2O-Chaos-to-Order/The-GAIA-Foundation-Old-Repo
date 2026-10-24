# SIM-AS-NAT-B - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Peak-basin correlation at 7 sites (16,384 genotypes) for RMF sigma 1 and HoC: positive in every landscape, higher for RMF?

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
| H1 | hypothesis | 7 sites: peak height and basin size positively correlated in every landscape (minimum r > 0) |
| H2 | hypothesis | 7 sites: the correlation is higher for RMF sigma 1 than for HoC (mean r) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
3 landscapes per type; basins found for up to 1000 peaks. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-NAT-B",
 "iteration": 6,
 "kind": "adaptive_walk",
 "seed": 36106,
 "L": 7,
 "A": 4,
 "reps": 3,
 "fracs": [
  0.14
 ],
 "max_basin_peaks": 1000,
 "landscapes": [
  {
   "name": "rmf_s1",
   "model": "rmf",
   "sigma": 1.0
  },
  {
   "name": "hoc",
   "model": "hoc"
  }
 ],
 "hyps": [
  [
   "7 sites: peak height and basin size positively correlated in every landscape (minimum r > 0)",
   "all(v['R_ph_bs_min'] is not None and v['R_ph_bs_min'] > 0 for k, v in o['landscapes'].items() if k != 'V1_smooth')"
  ],
  [
   "7 sites: the correlation is higher for RMF sigma 1 than for HoC (mean r)",
   "o['landscapes']['rmf_s1']['R_ph_bs'] > o['landscapes']['hoc']['R_ph_bs']"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-6` (run from `Natural-Sciences/simulation/`)
