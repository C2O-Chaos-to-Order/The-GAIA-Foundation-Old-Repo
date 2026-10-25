# SIM-AS-SOC-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P87's printed mobility statistics: do the dissimilarity indices, Table 5's % reductions and the text's 28/17/46/57% follow from the printed tables, do Tables 3 and 4 behave as one unweighted table, and does % mobile = % up + % down?

## Phase operationalization tested
SOC Ascendence = upward intergenerational class mobility (P87).

## Sources this run draws on
P87 (Paterson et al. 2025, social mobility in Scotland 1901-2001, Br J Sociol, PMC11890437, CC BY; read in full in AS0): Table 1 mobile/up/down; Table 2 origin and destination distributions (weighted in 1901 and 2001; sample sizes unweighted) and dissimilarity indices 0.12/0.16/0.23; Tables 3-4 outflow/inflow 1901 with sample sizes; Table 5 deviances 30,992/6865/1302 and printed reductions 78.8/95.8; text 'reduced by 79%', '17%', '46%', 'Fully 57%'.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | the three dissimilarity indices reproduce from Table 2 to two decimals (|diff| <= 0.005; 2001 '<0.1' entered as 0.05) |
| H2 | hypothesis | Table 5's printed % reductions reproduce from its printed deviances within 0.1 points |
| H3 | hypothesis | the text's 28%, 17%, 46% and 57% follow from Tables 2 and 4 within 0.6 points |
| H4 | hypothesis | Tables 3 and 4 behave as one unweighted 7x7 table: the salariat destination total rebuilt from Table 3's row percentages and row sizes is within 2% of Table 4's 7344 |
| H5 | hypothesis | Table 1: % mobile = % up + % down in all three years |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic arithmetic audit of printed (rounded) numbers; 2001 destination '<0.1' entered as 0.05. P87 states percentages are weighted in 1901 and 2001 while sample sizes are unweighted, which can make percentages and sizes disagree. Foreknowledge: hand checks before running found the 77.8% vs printed 78.8% QPM reduction.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so every outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-SOC-0",
 "iteration": 1,
 "kind": "arith_audit",
 "seed": 34301,
 "items": [
  {
   "name": "DI_1901",
   "expr": "0.005*sum(abs(a-b) for a,b in zip([4.9, 1.7, 6.6, 11.4, 38.4, 20.3, 16.9],[7.3, 5.2, 8.7, 5.4, 41.1, 21.2, 11.1]))",
   "printed": 0.12
  },
  {
   "name": "DI_1974",
   "expr": "0.005*sum(abs(a-b) for a,b in zip([9.5, 6.4, 7.7, 2.6, 37.6, 30.9, 5.3],[23.9, 7.8, 8.0, 1.0, 31.4, 25.6, 2.2]))",
   "printed": 0.16
  },
  {
   "name": "DI_2001",
   "expr": "0.005*sum(abs(a-b) for a,b in zip([27.4, 17.1, 7.1, 1.5, 22.5, 22.9, 1.5],[46.9, 8.9, 4.8, 0.05, 26.3, 13.1, 0.1]))",
   "printed": 0.23
  },
  {
   "name": "T5_QPM_reduction_pct",
   "expr": "100*(1-6865/30992)",
   "printed": 78.8
  },
  {
   "name": "T5_QPM_plus_reduction_pct",
   "expr": "100*(1-1302/30992)",
   "printed": 95.8
  },
  {
   "name": "agri_origins_pct",
   "expr": "11.4+16.9",
   "printed": 28
  },
  {
   "name": "agri_dest_pct",
   "expr": "5.4+11.1",
   "printed": 17
  },
  {
   "name": "T4_salariat_nonagri_working_class",
   "expr": "30+16",
   "printed": 46
  },
  {
   "name": "T4_salariat_manual_origins",
   "expr": "30+16+11",
   "printed": 57
  },
  {
   "name": "T3_rows_total",
   "expr": "4245+1452+5616+10036+31859+16579+14270",
   "printed": 84057
  },
  {
   "name": "T4_cols_total",
   "expr": "7344+5169+8128+5560+33261+15446+9149",
   "printed": 84057
  },
  {
   "name": "T3_reconstructed_salariat_dest_n",
   "expr": "0.25*4245+0.16*1452+0.11*5616+0.07*10036+0.06*31859+0.06*16579+0.05*14270",
   "printed": 7344
  },
  {
   "name": "T3_reconstructed_salariat_self_recruit_pct",
   "expr": "100*0.25*4245/(0.25*4245+0.16*1452+0.11*5616+0.07*10036+0.06*31859+0.06*16579+0.05*14270)",
   "printed": 17
  },
  {
   "name": "T3_self_recruit_pct_using_T4_size",
   "expr": "100*0.25*4245/7344",
   "printed": 17
  },
  {
   "name": "T1_1901_mobile_eq_up_plus_down",
   "expr": "30+22",
   "printed": 52
  },
  {
   "name": "T1_1974",
   "expr": "42+22",
   "printed": 64
  },
  {
   "name": "T1_2001",
   "expr": "45+22",
   "printed": 67
  },
  {
   "name": "unidiff_dev_diff",
   "expr": "241-183",
   "printed": 58
  },
  {
   "name": "unidiff_p",
   "expr": "chi2_sf(58, 2)"
  },
  {
   "name": "T7_dev_diff",
   "expr": "2335-1885",
   "printed": null
  },
  {
   "name": "T7_p",
   "expr": "chi2_sf(2335-1885, 1152-1120)"
  }
 ],
 "hyps": [
  [
   "the three dissimilarity indices reproduce from Table 2 to two decimals (|diff| <= 0.005; 2001 '<0.1' entered as 0.05)",
   "all(abs(o['items'][k]['diff']) <= 0.005 for k in ['DI_1901','DI_1974','DI_2001'])"
  ],
  [
   "Table 5's printed % reductions reproduce from its printed deviances within 0.1 points",
   "all(abs(o['items'][k]['diff']) <= 0.1 for k in ['T5_QPM_reduction_pct','T5_QPM_plus_reduction_pct'])"
  ],
  [
   "the text's 28%, 17%, 46% and 57% follow from Tables 2 and 4 within 0.6 points",
   "all(abs(o['items'][k]['diff']) <= 0.6 for k in ['agri_origins_pct','agri_dest_pct','T4_salariat_nonagri_working_class','T4_salariat_manual_origins'])"
  ],
  [
   "Tables 3 and 4 behave as one unweighted 7x7 table: the salariat destination total rebuilt from Table 3's row percentages and row sizes is within 2% of Table 4's 7344",
   "abs(o['items']['T3_reconstructed_salariat_dest_n']['value'] - 7344) <= 0.02*7344"
  ],
  [
   "Table 1: % mobile = % up + % down in all three years",
   "all(o['items'][k]['diff'] == 0 for k in ['T1_1901_mobile_eq_up_plus_down','T1_1974','T1_2001'])"
  ]
 ]
}
```

## Command
`python sim_soc.py iter-1` (run from `Social-Sciences/simulation/`)
