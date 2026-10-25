# SIM-AS-SOC-C - iteration 7 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P93 expansion vs relative stability arithmetic

## Phase operationalization tested
SOC Ascendence = upward and total intergenerational mobility (P87; P93 for women's educational mobility).

## Sources this run draws on
P93 (de Bellaigue, Worth, Bennett, Eli & Ulijaszek 2022, 'Women, Mobility, and Education in Twentieth-century England and Wales: A New Analytical Approach', Twentieth Century British History 33:345-368, PMC10652814, CC BY; read in full in ASB): Educational Cohort Code (ECC) for 90 Oxford Biobank women, their mothers and grandmothers; counts and percentages of upward educational mobility, mature study and spouse comparisons.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | P93: full-time education at 16 rose by more than 50 points between 1951 and 1981 (19% to 75%) |
| H2 | hypothesis | P93: most degree-holders (26 of 50) did not exceed their mothers' ECC |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic audit. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-SOC-C",
 "iteration": 7,
 "kind": "arith_audit",
 "seed": 37307,
 "items": [
  {
   "name": "P93_rise_1951_1981",
   "expr": "75-19"
  },
  {
   "name": "P93_ratio_1951_1981",
   "expr": "75/19"
  },
  {
   "name": "P93_other_mature",
   "expr": "47-27-11"
  },
  {
   "name": "P93_other_mature_pct",
   "expr": "100*(47-27-11)/47"
  },
  {
   "name": "P93_nondegree",
   "expr": "90-50"
  },
  {
   "name": "P93_degree_not_higher",
   "expr": "50-24"
  },
  {
   "name": "P93_higher_nonmature",
   "expr": "24-16"
  }
 ],
 "hyps": [
  [
   "P93: full-time education at 16 rose by more than 50 points between 1951 and 1981 (19% to 75%)",
   "o['items']['P93_rise_1951_1981']['value'] > 50"
  ],
  [
   "P93: most degree-holders (26 of 50) did not exceed their mothers' ECC",
   "o['items']['P93_degree_not_higher']['value'] > 25"
  ]
 ]
}
```

## Command
`python sim_soc.py iter-7` (run from `Social-Sciences/simulation/`)
