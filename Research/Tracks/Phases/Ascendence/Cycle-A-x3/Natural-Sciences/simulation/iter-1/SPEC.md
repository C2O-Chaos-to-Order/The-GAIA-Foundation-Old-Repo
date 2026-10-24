# SIM-AS-NAT-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P85 at its own size: with 9 four-state sites (262,144 genotypes; 2 landscapes per type, one walk from every genotype), is P14% within 0.10 of P85's printed 96.3% (RMF sigma 0.5) and 26.4% (sigma 10), and between 0.15 and 0.35 for HoC?

## Phase operationalization tested
NAT Ascendence = adaptive walks climbing a fitness landscape (P85).

## Sources this run draws on
P85 (Li & Zhang 2025, 'On the Probability of Reaching High Peaks in Fitness Landscapes by Adaptive Walks', Mol Biol Evol, PMC11975533, CC BY-NC; read in full in AS0): SSWM adaptive walks; P14% (probability of reaching the top 14% of peaks); RMF F = -D(x, x*) + eta, eta ~ N(0.5, sigma); HoC; NK; RMF P14% 96.3% at sigma 0.5 to 26.4% at sigma 10; NK 100% at K 0 to 24.8% at K 8; HoC about 25%; R_ph-bs 0.69-0.97 across empirical landscapes.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | for every L an additive landscape has one peak reached by every walk |
| H1 | hypothesis | at P85's size (9 four-state sites) RMF sigma 0.5: mean P14% within 0.10 of P85's 96.3% |
| H2 | hypothesis | RMF sigma 10: mean P14% within 0.10 of P85's 26.4% |
| H3 | hypothesis | HoC at 9 sites: mean P14% between 0.15 and 0.35 (P85: about 25%) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Two landscapes per type only; no basin sizes at this size (too many peaks). Smoke-test and earlier AS0 results gave foreknowledge of the direction. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-NAT-A",
 "iteration": 1,
 "kind": "adaptive_walk_sizes",
 "seed": 35101,
 "L_list": [
  9
 ],
 "A": 4,
 "reps": 2,
 "fracs": [
  0.14
 ],
 "max_basin_peaks": 0,
 "landscapes": [
  {
   "name": "rmf_s0.5",
   "model": "rmf",
   "sigma": 0.5
  },
  {
   "name": "rmf_s10",
   "model": "rmf",
   "sigma": 10.0
  },
  {
   "name": "hoc",
   "model": "hoc"
  }
 ],
 "hyps": [
  [
   "at P85's size (9 four-state sites) RMF sigma 0.5: mean P14% within 0.10 of P85's 96.3%",
   "abs(o['by_L']['9']['rmf_s0.5']['P0.14'] - 0.963) <= 0.10"
  ],
  [
   "RMF sigma 10: mean P14% within 0.10 of P85's 26.4%",
   "abs(o['by_L']['9']['rmf_s10']['P0.14'] - 0.264) <= 0.10"
  ],
  [
   "HoC at 9 sites: mean P14% between 0.15 and 0.35 (P85: about 25%)",
   "0.15 <= o['by_L']['9']['hoc']['P0.14'] <= 0.35"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-1` (run from `Natural-Sciences/simulation/`)
