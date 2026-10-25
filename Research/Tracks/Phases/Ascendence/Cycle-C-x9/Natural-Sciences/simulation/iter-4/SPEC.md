# SIM-AS-NAT-C - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
RMF theta 1: does the mean number of accessible paths grow with L?

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
| H1 | hypothesis | RMF theta 1: mean number of accessible paths rises with L over 4, 6, 8, 10 (P94: grows without bound) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's RMF: -theta d + N(0, 1), d to a random reference genotype. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-NAT-C",
 "iteration": 4,
 "kind": "accessible_paths",
 "seed": 37104,
 "L_list": [
  4,
  6,
  8,
  10
 ],
 "reps": 1000,
 "landscapes": [
  {
   "name": "rmf",
   "model": "rmf",
   "theta": 1.0
  }
 ],
 "hyps": [
  [
   "RMF theta 1: mean number of accessible paths rises with L over 4, 6, 8, 10 (P94: grows without bound)",
   "(lambda d: d['4']['rmf']['mean_paths'] < d['6']['rmf']['mean_paths'] < d['8']['rmf']['mean_paths'] < d['10']['rmf']['mean_paths'])(o['by_L'])"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-4` (run from `Natural-Sciences/simulation/`)
