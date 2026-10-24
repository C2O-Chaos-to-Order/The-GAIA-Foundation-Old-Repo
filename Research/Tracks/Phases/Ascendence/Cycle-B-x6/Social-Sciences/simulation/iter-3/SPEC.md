# SIM-AS-SOC-B - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P93's printed percentages: do they follow from its counts?

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
| H1 | hypothesis | P93's printed percentages follow from its counts within 0.6 points (whole-number rounding) |
| H2 | hypothesis | 68% of 40 men gives a whole number within 0.3 (27 mature male learners, consistent with '7 men (26%)') |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic audit; whole-number rounding tolerance 0.6. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-SOC-B",
 "iteration": 3,
 "kind": "arith_audit",
 "seed": 36303,
 "items": [
  {
   "name": "degree_holders_pct",
   "expr": "100*50/90",
   "printed": 56
  },
  {
   "name": "higher_ECC_of_degree",
   "expr": "100*24/50",
   "printed": 48
  },
  {
   "name": "higher_ECC_of_all",
   "expr": "100*24/90",
   "printed": 26
  },
  {
   "name": "mature_subjects_pct",
   "expr": "100*47/90",
   "printed": 52
  },
  {
   "name": "wives_more_qualified",
   "expr": "100*21/50",
   "printed": 42
  },
  {
   "name": "couples_unmatched",
   "expr": "100*24/90",
   "printed": 27
  },
  {
   "name": "daughters_higher",
   "expr": "100*16/24",
   "printed": 67
  },
  {
   "name": "mothers_public",
   "expr": "100*13/24",
   "printed": 54
  },
  {
   "name": "daughters_public",
   "expr": "100*18/24",
   "printed": 75
  },
  {
   "name": "women_vocational_of_mature",
   "expr": "100*27/47",
   "printed": 57
  },
  {
   "name": "women_HE_of_mature",
   "expr": "100*11/47",
   "printed": 23
  },
  {
   "name": "men_mature_n",
   "expr": "0.68*40"
  },
  {
   "name": "men_onjob_of_mature",
   "expr": "100*7/27",
   "printed": 26
  }
 ],
 "hyps": [
  [
   "P93's printed percentages follow from its counts within 0.6 points (whole-number rounding)",
   "all(abs(v['diff']) <= 0.6 for k, v in o['items'].items() if v['diff'] is not None)"
  ],
  [
   "68% of 40 men gives a whole number within 0.3 (27 mature male learners, consistent with '7 men (26%)')",
   "abs(o['items']['men_mature_n']['value'] - round(o['items']['men_mature_n']['value'])) <= 0.3"
  ]
 ]
}
```

## Command
`python sim_soc.py iter-3` (run from `Social-Sciences/simulation/`)
