# SIM-AS-HUM-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P89's statistics: do the printed LRT chi-squares and df give the printed p-values, does Lawton's 1349% follow from 34,500 to 500,000, and are the gendered rise-plateau-slump percentages and the F0-excursion means internally consistent?

## Phase operationalization tested
HUM Ascendence = rising intonation (pitch ascent at the phrase end) in Liverpool English, a minority variant selected in new-dialect formation (P89).

## Sources this run draws on
P89 (Nance et al. 2022, rising intonation in Liverpool English, Lang Speech, PMC9669732, CC BY-NC; read in full in AS0): 17 Liverpool and 15 Manchester speakers; L* L-H% = Knowles' 'rise', L* H-H% = 'rise-plateau'; Tables 1-2 LRT chi-squares; rise-plateau-slump counts by gender; F0 excursion 18 Hz, chi2(1) 2.82, p 0.09; Lawton's 1349% population increase 1773-1871.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | every LRT p-value printed as a number is reproduced within 0.01, and every '<0.001' is below 0.001 |
| H2 | hypothesis | Lawton's 1349% follows from 34,500 to 500,000 within 1 point |
| H3 | hypothesis | the printed rise-plateau-slump percentages imply token totals per Liverpool speaker within 10% for males (145, 34%, 9 speakers) and females (48, 13%, 8 speakers) |
| H4 | hypothesis | the F0-excursion means (overall 18, female 23.0, male 12.7, 138 values) imply a female count between 0 and 138 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic arithmetic audit; inputs rounded to 2 decimals so recomputed p values carry rounding error; per-speaker token totals assume all 9 male and 8 female Liverpool speakers contribute equally (agent's assumption). Foreknowledge: hand checks before running.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so every outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-HUM-0",
 "iteration": 1,
 "kind": "arith_audit",
 "seed": 34501,
 "items": [
  {
   "name": "T1_city_p",
   "expr": "chi2_sf(128.64, 6)",
   "printed": 0.001
  },
  {
   "name": "T1_task_p",
   "expr": "chi2_sf(113.11, 8)",
   "printed": 0.001
  },
  {
   "name": "T1_gender_p",
   "expr": "chi2_sf(7.46, 2)",
   "printed": 0.02
  },
  {
   "name": "T1_cityxgender_p",
   "expr": "chi2_sf(6.18, 1)",
   "printed": 0.01
  },
  {
   "name": "T1_cityxtask_p",
   "expr": "chi2_sf(100.16, 4)",
   "printed": 0.001
  },
  {
   "name": "T2_city_p",
   "expr": "chi2_sf(48.39, 6)",
   "printed": 0.001
  },
  {
   "name": "T2_task_p",
   "expr": "chi2_sf(63.94, 8)",
   "printed": 0.001
  },
  {
   "name": "T2_gender_p",
   "expr": "chi2_sf(2.91, 2)",
   "printed": 0.23
  },
  {
   "name": "T2_cityxgender_p",
   "expr": "chi2_sf(0.15, 1)",
   "printed": 0.69
  },
  {
   "name": "T2_cityxtask_p",
   "expr": "chi2_sf(11.59, 4)",
   "printed": 0.02
  },
  {
   "name": "F0_gender_p",
   "expr": "chi2_sf(2.82, 1)",
   "printed": 0.09
  },
  {
   "name": "Lawton_increase_pct",
   "expr": "100*(500000/34500-1)",
   "printed": 1349
  },
  {
   "name": "Cruttenden_sum",
   "expr": "26.5+16.7",
   "printed": 43.2
  },
  {
   "name": "tokens_per_male_RPS",
   "expr": "145/0.34/9"
  },
  {
   "name": "tokens_per_female_RPS",
   "expr": "48/0.13/8"
  },
  {
   "name": "F0_implied_female_n",
   "expr": "138*(18-12.7)/(23.0-12.7)"
  }
 ],
 "hyps": [
  [
   "every LRT p-value printed as a number is reproduced within 0.01, and every '<0.001' is below 0.001",
   "all((o['items'][k]['value'] < 0.001) if o['items'][k]['printed'] == 0.001 else abs(o['items'][k]['diff']) <= 0.01 for k in o['items'] if k.endswith('_p'))"
  ],
  [
   "Lawton's 1349% follows from 34,500 to 500,000 within 1 point",
   "abs(o['items']['Lawton_increase_pct']['diff']) <= 1"
  ],
  [
   "the printed rise-plateau-slump percentages imply token totals per Liverpool speaker within 10% for males (145, 34%, 9 speakers) and females (48, 13%, 8 speakers)",
   "abs(o['items']['tokens_per_male_RPS']['value']/o['items']['tokens_per_female_RPS']['value'] - 1) <= 0.10"
  ],
  [
   "the F0-excursion means (overall 18, female 23.0, male 12.7, 138 values) imply a female count between 0 and 138",
   "0 < o['items']['F0_implied_female_n']['value'] < 138"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-1` (run from `Humanities/simulation/`)
