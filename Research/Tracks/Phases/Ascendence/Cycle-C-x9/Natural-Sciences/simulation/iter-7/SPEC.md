# SIM-AS-NAT-C - iteration 7 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P94 Table 1 and text arithmetic

## Phase operationalization tested
NAT Ascendence = adaptive walks climbing a fitness landscape (P85). ASC adds P94's accessibility of mutational pathways.

## Sources this run draws on
P94 (Franke, Kloezer, de Visser & Krug 2011, 'Evolutionary Accessibility of Mutational Pathways', PLoS Comput Biol 7:e1002134, PMC3158036, CC BY; read in full in ASC, supplementary figures not read): accessible (fitness-increasing shortest) paths from the antipodal genotype to the global maximum in HoC, RMF, LK (NK) and holey landscapes, and in subgraphs of an 8-locus Aspergillus niger landscape (Table 1).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | P94 Table 1: subgraph counts equal C(8, n); lethal-only path counts do not exceed n!; mean accessible paths do not exceed the lethal-only counts |
| H2 | hypothesis | '70 missing' = 256 - 186 and 'half of the 70 subgraphs' matches P_none 0.50 at n 4 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic audit (sim_nat copy of arith_audit). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-NAT-C",
 "iteration": 7,
 "kind": "arith_audit",
 "seed": 37107,
 "items": [
  {
   "name": "T1_nSG_2",
   "expr": "comb(8,2)",
   "printed": 28
  },
  {
   "name": "T1_nSG_3",
   "expr": "comb(8,3)",
   "printed": 56
  },
  {
   "name": "T1_nSG_4",
   "expr": "comb(8,4)",
   "printed": 70
  },
  {
   "name": "T1_nSG_5",
   "expr": "comb(8,5)",
   "printed": 56
  },
  {
   "name": "T1_nSG_6",
   "expr": "comb(8,6)",
   "printed": 28
  },
  {
   "name": "T1_lethalonly_le_fact_2",
   "expr": "1.61 <= factorial(2)"
  },
  {
   "name": "T1_lethalonly_le_fact_3",
   "expr": "4.05 <= factorial(3)"
  },
  {
   "name": "T1_lethalonly_le_fact_4",
   "expr": "12.53 <= factorial(4)"
  },
  {
   "name": "T1_lethalonly_le_fact_5",
   "expr": "55.32 <= factorial(5)"
  },
  {
   "name": "T1_lethalonly_le_fact_6",
   "expr": "246.0 <= factorial(6)"
  },
  {
   "name": "T1_mean_le_lethal_2",
   "expr": "0.82 <= 1.61"
  },
  {
   "name": "T1_mean_le_lethal_3",
   "expr": "1.34 <= 4.05"
  },
  {
   "name": "T1_mean_le_lethal_4",
   "expr": "2.01 <= 12.53"
  },
  {
   "name": "T1_mean_le_lethal_5",
   "expr": "3.16 <= 55.32"
  },
  {
   "name": "T1_mean_le_lethal_6",
   "expr": "6.07 <= 246.0"
  },
  {
   "name": "half_of_70_no_path",
   "expr": "0.50*70",
   "printed": 35
  },
  {
   "name": "missing_genotypes",
   "expr": "2**8-186",
   "printed": 70
  }
 ],
 "hyps": [
  [
   "P94 Table 1: subgraph counts equal C(8, n); lethal-only path counts do not exceed n!; mean accessible paths do not exceed the lethal-only counts",
   "all(o['items'][k]['diff'] == 0 for k in o['items'] if k.startswith('T1_nSG')) and all(o['items'][k]['value'] for k in o['items'] if k.startswith('T1_lethal') or k.startswith('T1_mean'))"
  ],
  [
   "'70 missing' = 256 - 186 and 'half of the 70 subgraphs' matches P_none 0.50 at n 4",
   "o['items']['missing_genotypes']['diff'] == 0 and o['items']['half_of_70_no_path']['diff'] == 0"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-7` (run from `Natural-Sciences/simulation/`)
