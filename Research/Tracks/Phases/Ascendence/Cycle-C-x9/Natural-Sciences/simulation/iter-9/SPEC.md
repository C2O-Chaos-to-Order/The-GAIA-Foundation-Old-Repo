# SIM-AS-NAT-C - iteration 9 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Holey landscape p 0.5: mean connected shortest paths = L! p^(L-1)?

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
| H1 | hypothesis | holey landscape p 0.5 (endpoints viable): mean connected shortest paths within 3 SE of L! p^(L-1) (22.5 at L 6; 315 at L 8) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Endpoints constrained viable; P94 Eq. 5 form as read by the agent. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-NAT-C",
 "iteration": 9,
 "kind": "accessible_paths",
 "seed": 37109,
 "L_list": [
  6,
  8
 ],
 "reps": 2000,
 "landscapes": [
  {
   "name": "holey_p0.5",
   "model": "holey",
   "p": 0.5
  }
 ],
 "hyps": [
  [
   "holey landscape p 0.5 (endpoints viable): mean connected shortest paths within 3 SE of L! p^(L-1) (22.5 at L 6; 315 at L 8)",
   "abs(o['by_L']['6']['holey_p0.5']['mean_paths'] - 22.5) <= 3 * o['by_L']['6']['holey_p0.5']['se'] and abs(o['by_L']['8']['holey_p0.5']['mean_paths'] - 315) <= 3 * o['by_L']['8']['holey_p0.5']['se']"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-9` (run from `Natural-Sciences/simulation/`)
