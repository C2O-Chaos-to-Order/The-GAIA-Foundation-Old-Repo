# SIM-AS-NAT-D - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
NK K 4 at L 8 (A. niger estimate)

## Phase operationalization tested
NAT Ascendence = adaptive walks climbing a fitness landscape (P85). ASC adds P94's accessibility of mutational pathways.

## Sources this run draws on
P94 (Franke, Kloezer, de Visser & Krug 2011, 'Evolutionary Accessibility of Mutational Pathways', PLoS Comput Biol 7:e1002134, PMC3158036, CC BY; read in full in ASC, supplementary figures not read): accessible (fitness-increasing shortest) paths from the antipodal genotype to the global maximum in HoC, RMF, LK (NK) and holey landscapes, and in subgraphs of an 8-locus Aspergillus niger landscape (Table 1).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | no landscape has more accessible paths than the L! shortest paths |
| H1 | hypothesis | binary NK K 4 at L 8 (P94's estimate for A. niger: each locus interacts with about half the others): mean accessible paths above 1 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's binary NK. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-NAT-D",
 "iteration": 6,
 "kind": "accessible_paths",
 "seed": 38106,
 "L_list": [
  8
 ],
 "reps": 500,
 "landscapes": [
  {
   "name": "nk_K4",
   "model": "nk",
   "K": 4
  }
 ],
 "hyps": [
  [
   "binary NK K 4 at L 8 (P94's estimate for A. niger: each locus interacts with about half the others): mean accessible paths above 1",
   "o['by_L']['8']['nk_K4']['mean_paths'] > 1"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-6` (run from `Natural-Sciences/simulation/`)
