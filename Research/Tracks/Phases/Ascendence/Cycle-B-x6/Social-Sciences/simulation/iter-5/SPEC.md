# SIM-AS-SOC-B - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P87 Tables 3-4: do rows and columns sum to 100 within rounding?

## Phase operationalization tested
SOC Ascendence = upward and total intergenerational mobility (P87; P93 for women's educational mobility).

## Sources this run draws on
P87 (Paterson et al. 2025, social mobility in Scotland 1901-2001, Br J Sociol, PMC11890437, CC BY; read in full in AS0): Table 1 mobile/up/down; Table 2 origin and destination distributions (weighted in 1901 and 2001; sample sizes unweighted) and dissimilarity indices 0.12/0.16/0.23; Tables 3-4 outflow/inflow 1901 with sample sizes; Table 5 deviances 30,992/6865/1302 and printed reductions 78.8/95.8; text 'reduced by 79%', '17%', '46%', 'Fully 57%'.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | every Table 3 row and Table 4 column sums to 100 within 2 (rounding of seven whole percentages; '<0.1' as 0.05) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
'<0.1' entered as 0.05. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-SOC-B",
 "iteration": 5,
 "kind": "arith_audit",
 "seed": 36305,
 "items": [
  {
   "name": "T3_row_prof",
   "expr": "25+12+10+2+30+18+3",
   "printed": 100
  },
  {
   "name": "T3_row_routine",
   "expr": "16+17+12+2+30+19+3",
   "printed": 100
  },
  {
   "name": "T3_row_selfemp",
   "expr": "11+10+26+2+31+18+3",
   "printed": 100
  },
  {
   "name": "T3_row_selfagri",
   "expr": "7+4+6+31+16+13+22",
   "printed": 100
  },
  {
   "name": "T3_row_skilled",
   "expr": "6+4+7+1+60+18+3",
   "printed": 100
  },
  {
   "name": "T3_row_semi",
   "expr": "6+5+8+1+42+33+5",
   "printed": 100
  },
  {
   "name": "T3_row_agriw",
   "expr": "5+3+6+6+23+22+35",
   "printed": 100
  },
  {
   "name": "T4_col_salariat",
   "expr": "17+4+10+11+30+16+11",
   "printed": 100
  },
  {
   "name": "T4_col_routine",
   "expr": "11+5+12+10+33+19+10",
   "printed": 100
  },
  {
   "name": "T4_col_selfemp",
   "expr": "6+2+20+8+32+19+12",
   "printed": 100
  },
  {
   "name": "T4_col_selfagri",
   "expr": "2+1+2+66+8+5+17",
   "printed": 100
  },
  {
   "name": "T4_col_skilled",
   "expr": "4+1+5+4+56+21+9",
   "printed": 100
  },
  {
   "name": "T4_col_semi",
   "expr": "4+2+6+7+33+32+17",
   "printed": 100
  },
  {
   "name": "T4_col_agriw",
   "expr": "1+0.05+2+23+11+9+54",
   "printed": 100
  }
 ],
 "hyps": [
  [
   "every Table 3 row and Table 4 column sums to 100 within 2 (rounding of seven whole percentages; '<0.1' as 0.05)",
   "all(abs(v['diff']) <= 2 for v in o['items'].values())"
  ]
 ]
}
```

## Command
`python sim_soc.py iter-5` (run from `Social-Sciences/simulation/`)
