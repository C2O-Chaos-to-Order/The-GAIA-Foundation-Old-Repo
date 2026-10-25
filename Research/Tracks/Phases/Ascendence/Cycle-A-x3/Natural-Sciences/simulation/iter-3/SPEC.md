# SIM-AS-NAT-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P85's statement that HoC P14% is 'always around 25%' whatever the number of sites: is mean P14% between 0.15 and 0.35 at 5, 6, 7 and 8 four-state sites, with a range below 0.08?

## Phase operationalization tested
NAT Ascendence = adaptive walks on maximally rugged (HoC) landscapes (P85).

## Sources this run draws on
P85 (Li & Zhang 2025, 'On the Probability of Reaching High Peaks in Fitness Landscapes by Adaptive Walks', Mol Biol Evol, PMC11975533, CC BY-NC; read in full in AS0): SSWM adaptive walks; P14% (probability of reaching the top 14% of peaks); RMF F = -D(x, x*) + eta, eta ~ N(0.5, sigma); HoC; NK; RMF P14% 96.3% at sigma 0.5 to 26.4% at sigma 10; NK 100% at K 0 to 24.8% at K 8; HoC about 25%; R_ph-bs 0.69-0.97 across empirical landscapes.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | for every L an additive landscape has one peak reached by every walk |
| H1 | hypothesis | HoC: mean P14% between 0.15 and 0.35 at every size 5-8 sites |
| H2 | hypothesis | HoC: the range of mean P14% across sizes is below 0.08 (P85: 'minimal impacts') |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
5 landscapes per size; P85 used 5-10 sites (its supplementary fig. S6 not read). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-NAT-A",
 "iteration": 3,
 "kind": "adaptive_walk_sizes",
 "seed": 35103,
 "L_list": [
  5,
  6,
  7,
  8
 ],
 "A": 4,
 "reps": 5,
 "fracs": [
  0.14
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
   "HoC: mean P14% between 0.15 and 0.35 at every size 5-8 sites",
   "all(0.15 <= v['hoc']['P0.14'] <= 0.35 for v in o['by_L'].values())"
  ],
  [
   "HoC: the range of mean P14% across sizes is below 0.08 (P85: 'minimal impacts')",
   "max(v['hoc']['P0.14'] for v in o['by_L'].values()) - min(v['hoc']['P0.14'] for v in o['by_L'].values()) < 0.08"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-3` (run from `Natural-Sciences/simulation/`)
