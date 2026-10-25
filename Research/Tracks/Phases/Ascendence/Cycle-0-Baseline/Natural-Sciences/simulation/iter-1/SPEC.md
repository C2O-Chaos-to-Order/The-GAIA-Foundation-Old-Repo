# SIM-AS-NAT-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P85's adaptive walks on small landscapes (6 four-state sites, 4096 genotypes; 10 landscapes per type): does the chance of reaching the top 14% of peaks fall as RMF ruggedness sigma rises, sit near 25% for HoC, fall with NK K, exceed 14% everywhere, and do peak height and basin size correlate positively?

## Phase operationalization tested
NAT Ascendence = adaptive walks climbing a fitness landscape to a peak (SSWM uphill steps; P85). Competing reading: anagenesis / increase in complexity (not used in AS0).

## Sources this run draws on
P85 (Li & Zhang 2025, 'On the Probability of Reaching High Peaks in Fitness Landscapes by Adaptive Walks', Mol Biol Evol, PMC11975533, CC BY-NC; read in full in AS0): SSWM adaptive walks; P14% (probability of reaching the top 14% of peaks); RMF F = -D(x, x*) + eta, eta ~ N(0.5, sigma); HoC; NK; RMF P14% 96.3% at sigma 0.5 to 26.4% at sigma 10; NK 100% at K 0 to 24.8% at K 8; HoC about 25%; R_ph-bs 0.69-0.97 across empirical landscapes.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | an additive RMF landscape (sigma 0) has one peak and every walk reaches it |
| H1 | hypothesis | RMF: P14% falls as sigma rises (0.5 > 2 > 10), as P85 reports for its RMF series |
| H2 | hypothesis | HoC: mean P14% between 0.15 and 0.35 (P85: 'always around 25%') |
| H3 | hypothesis | NK: mean P14% lower at K = 4 than at K = 1 |
| H4 | hypothesis | every landscape type: mean P14% above 0.14 (walks reach the top 14% of peaks more often than a uniform pick among peaks) |
| H5 | hypothesis | peak height and basin size positively correlated in every landscape with >= 3 peaks (minimum R_ph-bs > 0) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's implementation at a much smaller size than P85 (P85: 9 four-state sites; empirical landscapes not used). One walk from every genotype per landscape. 'Top 14%' = floor(0.14 n_peaks), at least 1, so landscapes with few peaks (NK K 1, about 11 peaks) test only the global peak: a granularity artefact. Basin search capped at 400 peaks per landscape.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so every outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-NAT-0",
 "iteration": 1,
 "kind": "adaptive_walk",
 "seed": 34101,
 "L": 6,
 "A": 4,
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
   "name": "rmf_s10",
   "model": "rmf",
   "sigma": 10.0
  },
  {
   "name": "hoc",
   "model": "hoc"
  },
  {
   "name": "nk_K1",
   "model": "nk",
   "K": 1
  },
  {
   "name": "nk_K4",
   "model": "nk",
   "K": 4
  }
 ],
 "hyps": [
  [
   "RMF: P14% falls as sigma rises (0.5 > 2 > 10), as P85 reports for its RMF series",
   "o['landscapes']['rmf_s0.5']['P0.14'] > o['landscapes']['rmf_s2']['P0.14'] > o['landscapes']['rmf_s10']['P0.14']"
  ],
  [
   "HoC: mean P14% between 0.15 and 0.35 (P85: 'always around 25%')",
   "0.15 <= o['landscapes']['hoc']['P0.14'] <= 0.35"
  ],
  [
   "NK: mean P14% lower at K = 4 than at K = 1",
   "o['landscapes']['nk_K4']['P0.14'] < o['landscapes']['nk_K1']['P0.14']"
  ],
  [
   "every landscape type: mean P14% above 0.14 (walks reach the top 14% of peaks more often than a uniform pick among peaks)",
   "all(v['P0.14'] > 0.14 for v in o['landscapes'].values() if 'P0.14' in v)"
  ],
  [
   "peak height and basin size positively correlated in every landscape with >= 3 peaks (minimum R_ph-bs > 0)",
   "all(v.get('R_ph_bs_min') is None or v['R_ph_bs_min'] > 0 for k, v in o['landscapes'].items() if k != 'V1_smooth')"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-1` (run from `Natural-Sciences/simulation/`)
