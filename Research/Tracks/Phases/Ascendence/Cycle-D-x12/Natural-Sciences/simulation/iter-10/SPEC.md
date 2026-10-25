# SIM-AS-NAT-D - iteration 10 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P94 Table 1 trends

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
| H1 | hypothesis | P94 Table 1: P_none rises with subgraph size n 2-6 (P94: 'Up to n, the probability is found to increase') |
| H2 | hypothesis | P94 Table 1: mean accessible paths rise with n |
| H3 | hypothesis | the reduction by epistasis among viable genotypes (lethal-only / mean) exceeds 2 for every n >= 3 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic on printed values. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-NAT-D",
 "iteration": 10,
 "kind": "arith_audit",
 "seed": 38110,
 "items": [
  {
   "name": "T1_Pnone_2",
   "expr": "0.36"
  },
  {
   "name": "T1_Pnone_3",
   "expr": "0.39"
  },
  {
   "name": "T1_Pnone_4",
   "expr": "0.5"
  },
  {
   "name": "T1_Pnone_5",
   "expr": "0.63"
  },
  {
   "name": "T1_Pnone_6",
   "expr": "0.68"
  },
  {
   "name": "T1_mean_2",
   "expr": "0.82"
  },
  {
   "name": "T1_mean_3",
   "expr": "1.34"
  },
  {
   "name": "T1_mean_4",
   "expr": "2.01"
  },
  {
   "name": "T1_mean_5",
   "expr": "3.16"
  },
  {
   "name": "T1_mean_6",
   "expr": "6.07"
  },
  {
   "name": "T1_epistasis_factor_2",
   "expr": "1.61/0.82"
  },
  {
   "name": "T1_epistasis_factor_3",
   "expr": "4.05/1.34"
  },
  {
   "name": "T1_epistasis_factor_4",
   "expr": "12.53/2.01"
  },
  {
   "name": "T1_epistasis_factor_5",
   "expr": "55.32/3.16"
  },
  {
   "name": "T1_epistasis_factor_6",
   "expr": "246.0/6.07"
  }
 ],
 "hyps": [
  [
   "P94 Table 1: P_none rises with subgraph size n 2-6 (P94: 'Up to n, the probability is found to increase')",
   "all(o['items'][f'T1_Pnone_{n}']['value'] < o['items'][f'T1_Pnone_{n+1}']['value'] for n in range(2, 6))"
  ],
  [
   "P94 Table 1: mean accessible paths rise with n",
   "all(o['items'][f'T1_mean_{n}']['value'] < o['items'][f'T1_mean_{n+1}']['value'] for n in range(2, 6))"
  ],
  [
   "the reduction by epistasis among viable genotypes (lethal-only / mean) exceeds 2 for every n >= 3",
   "all(o['items'][f'T1_epistasis_factor_{n}']['value'] > 2 for n in range(3, 7))"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-10` (run from `Natural-Sciences/simulation/`)
