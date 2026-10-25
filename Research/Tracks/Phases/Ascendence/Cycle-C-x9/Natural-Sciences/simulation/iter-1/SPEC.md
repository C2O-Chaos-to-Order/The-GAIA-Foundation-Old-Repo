# SIM-AS-NAT-C - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
HoC: is the mean number of accessible paths 1 at every L (P94 Eq. 2)?

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
| H1 | hypothesis | HoC: mean number of accessible paths within 3 SE of 1 at L 4, 6, 8 (P94 Eq. 2: exactly 1 for all L) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
2000 landscapes per L; antipode of the global maximum as start. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-NAT-C",
 "iteration": 1,
 "kind": "accessible_paths",
 "seed": 37101,
 "L_list": [
  4,
  6,
  8
 ],
 "reps": 2000,
 "landscapes": [
  {
   "name": "hoc",
   "model": "hoc"
  }
 ],
 "hyps": [
  [
   "HoC: mean number of accessible paths within 3 SE of 1 at L 4, 6, 8 (P94 Eq. 2: exactly 1 for all L)",
   "all(abs(d['hoc']['mean_paths'] - 1) <= 3 * d['hoc']['se'] for d in o['by_L'].values())"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-1` (run from `Natural-Sciences/simulation/`)
