# SIM-TR-SOC-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P99's printed statistics: do the SVO counts and percentages add up, do both participant flows reach 1655, do eta^2 and p follow from the printed F and df, and do Table 3's group means weight back to Table 2's means?

## Phase operationalization tested
SOC Transcendence = self-transcendence values (universalism + benevolence; Schwartz) and their link to prosocial social value orientation (P99).

## Sources this run draws on
P99 (Nezlek 2024, values and social value orientation, PLoS One, PMC11602047, CC BY; read in full in TR0): 1655 participants; SVO prosocial 1151, individualist 381, competitor 123; Portrait Values Questionnaire (self-transcendence = universalism + benevolence); Table 2 means; Table 3 group means, F(2, n - 3), eta^2, planned comparisons; participant flows in Method and Results.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | the three SVO groups add to 1655 and give the printed 69.5 / 23.0 / 7.4% within 0.05 |
| H2 | hypothesis | both participant flows printed (Method: 1903 - 226 - 22; Results: 1906 - 223 - 23) arrive at the analysed 1655 |
| H3 | hypothesis | every printed main-effect eta^2 reproduces from F and df (2, n - 3) within 0.0006 |
| H4 | hypothesis | every printed planned-comparison eta^2 reproduces from F and df (1, n - 3) within 0.0006 |
| H5 | hypothesis | every printed p reproduces from F within 0.002 (a printed .000 read as < 0.0005) |
| H6 | hypothesis | the n-weighted Table 3 group means reproduce Table 2's means within 0.005 for all 11 values |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic arithmetic audit of printed (rounded) numbers; error df taken as n - 3 from each row's n; eta^2 = df1 F/(df1 F + df2). Foreknowledge: the agent hand-checked several items while reading P99 (disclosed). Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so every outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-SOC-0",
 "iteration": 1,
 "kind": "arith_audit",
 "seed": 39301,
 "items": [
  {
   "name": "svo_total",
   "expr": "1151+381+123",
   "printed": 1655
  },
  {
   "name": "pct_prosocial",
   "expr": "100*1151/1655",
   "printed": 69.5
  },
  {
   "name": "pct_individualist",
   "expr": "100*381/1655",
   "printed": 23.0
  },
  {
   "name": "pct_competitor",
   "expr": "100*123/1655",
   "printed": 7.4
  },
  {
   "name": "pct_competitor_text",
   "expr": "100*123/1655",
   "printed": 7.3
  },
  {
   "name": "method_flow_classified",
   "expr": "1903-226",
   "printed": 1677
  },
  {
   "name": "method_flow_final",
   "expr": "1903-226-22",
   "printed": 1655
  },
  {
   "name": "results_flow_classified",
   "expr": "1906-223",
   "printed": 1683
  },
  {
   "name": "results_flow_final",
   "expr": "1906-223-23",
   "printed": 1655
  },
  {
   "name": "shared_variance_pct",
   "expr": "100*0.526**2",
   "printed": 28
  },
  {
   "name": "r_crit_05",
   "expr": "1.96/sqrt(1653)",
   "printed": 0.049
  },
  {
   "name": "r_crit_01",
   "expr": "2.576/sqrt(1653)",
   "printed": 0.064
  },
  {
   "name": "bene_competitor_text_vs_table",
   "expr": "0.667",
   "printed": 0.679
  },
  {
   "name": "wmean_Universalism",
   "expr": "(1151*(0.543)+381*(0.312)+123*(0.262))/1655",
   "printed": 0.469
  },
  {
   "name": "p_main_Universalism",
   "expr": "f_sf(31.71, 2, 1653-3)",
   "printed": 0.0
  },
  {
   "name": "eta2_main_Universalism",
   "expr": "2*31.71/(2*31.71+1653-3)",
   "printed": 0.037
  },
  {
   "name": "p_pc_Universalism",
   "expr": "f_sf(55.76, 1, 1653-3)",
   "printed": 0.0
  },
  {
   "name": "eta2_pc_Universalism",
   "expr": "55.76/(55.76+1653-3)",
   "printed": 0.033
  },
  {
   "name": "wmean_Benevolence",
   "expr": "(1151*(0.751)+381*(0.558)+123*(0.667))/1655",
   "printed": 0.7
  },
  {
   "name": "p_main_Benevolence",
   "expr": "f_sf(15.92, 2, 1649-3)",
   "printed": 0.0
  },
  {
   "name": "eta2_main_Benevolence",
   "expr": "2*15.92/(2*15.92+1649-3)",
   "printed": 0.019
  },
  {
   "name": "p_pc_Benevolence",
   "expr": "f_sf(15.95, 1, 1649-3)",
   "printed": 0.0
  },
  {
   "name": "eta2_pc_Benevolence",
   "expr": "15.95/(15.95+1649-3)",
   "printed": 0.01
  },
  {
   "name": "wmean_BeneGeneral",
   "expr": "(1151*(0.854)+381*(0.693)+123*(0.692))/1655",
   "printed": 0.805
  },
  {
   "name": "p_main_BeneGeneral",
   "expr": "f_sf(14.62, 2, 1647-3)",
   "printed": 0.0
  },
  {
   "name": "eta2_main_BeneGeneral",
   "expr": "2*14.62/(2*14.62+1647-3)",
   "printed": 0.017
  },
  {
   "name": "p_pc_BeneGeneral",
   "expr": "f_sf(23.48, 1, 1647-3)",
   "printed": 0.0
  },
  {
   "name": "eta2_pc_BeneGeneral",
   "expr": "23.48/(23.48+1647-3)",
   "printed": 0.014
  },
  {
   "name": "wmean_Conformity",
   "expr": "(1151*(-0.513)+381*(-0.692)+123*(-0.675))/1655",
   "printed": -0.567
  },
  {
   "name": "p_main_Conformity",
   "expr": "f_sf(6.6, 2, 1649-3)",
   "printed": 0.001
  },
  {
   "name": "eta2_main_Conformity",
   "expr": "2*6.6/(2*6.6+1649-3)",
   "printed": 0.008
  },
  {
   "name": "p_pc_Conformity",
   "expr": "f_sf(10.03, 1, 1649-3)",
   "printed": 0.002
  },
  {
   "name": "eta2_pc_Conformity",
   "expr": "10.03/(10.03+1649-3)",
   "printed": 0.006
  },
  {
   "name": "wmean_Tradition",
   "expr": "(1151*(-0.26)+381*(-0.314)+123*(-0.264))/1655",
   "printed": -0.273
  },
  {
   "name": "wmean_Security",
   "expr": "(1151*(-0.176)+381*(-0.08)+123*(-0.12))/1655",
   "printed": -0.15
  },
  {
   "name": "p_main_Security",
   "expr": "f_sf(2.27, 2, 1651-3)",
   "printed": 0.104
  },
  {
   "name": "eta2_main_Security",
   "expr": "2*2.27/(2*2.27+1651-3)",
   "printed": 0.003
  },
  {
   "name": "p_pc_Security",
   "expr": "f_sf(2.67, 1, 1651-3)",
   "printed": 0.103
  },
  {
   "name": "eta2_pc_Security",
   "expr": "2.67/(2.67+1651-3)",
   "printed": 0.002
  },
  {
   "name": "wmean_SelfDirection",
   "expr": "(1151*(-0.011)+381*(-0.018)+123*(0.003))/1655",
   "printed": -0.012
  },
  {
   "name": "wmean_Stimulation",
   "expr": "(1151*(-0.243)+381*(-0.171)+123*(-0.134))/1655",
   "printed": -0.218
  },
  {
   "name": "p_main_Stimulation",
   "expr": "f_sf(1.54, 2, 1657-3)",
   "printed": 0.214
  },
  {
   "name": "p_pc_Stimulation",
   "expr": "f_sf(2.92, 1, 1657-3)",
   "printed": 0.088
  },
  {
   "name": "eta2_pc_Stimulation",
   "expr": "2.92/(2.92+1657-3)",
   "printed": 0.002
  },
  {
   "name": "wmean_Hedonism",
   "expr": "(1151*(-0.253)+381*(-0.079)+123*(-0.116))/1655",
   "printed": -0.203
  },
  {
   "name": "p_main_Hedonism",
   "expr": "f_sf(7.49, 2, 1652-3)",
   "printed": 0.001
  },
  {
   "name": "eta2_main_Hedonism",
   "expr": "2*7.49/(2*7.49+1652-3)",
   "printed": 0.009
  },
  {
   "name": "p_pc_Hedonism",
   "expr": "f_sf(10.43, 1, 1652-3)",
   "printed": 0.001
  },
  {
   "name": "eta2_pc_Hedonism",
   "expr": "10.43/(10.43+1652-3)",
   "printed": 0.006
  },
  {
   "name": "wmean_Achievement",
   "expr": "(1151*(0.118)+381*(0.316)+123*(0.196))/1655",
   "printed": 0.17
  },
  {
   "name": "p_main_Achievement",
   "expr": "f_sf(9.82, 2, 1651-3)",
   "printed": 0.0
  },
  {
   "name": "eta2_main_Achievement",
   "expr": "2*9.82/(2*9.82+1651-3)",
   "printed": 0.012
  },
  {
   "name": "p_pc_Achievement",
   "expr": "f_sf(9.22, 1, 1651-3)",
   "printed": 0.002
  },
  {
   "name": "eta2_pc_Achievement",
   "expr": "9.22/(9.22+1651-3)",
   "printed": 0.006
  },
  {
   "name": "wmean_Power",
   "expr": "(1151*(-0.633)+381*(-0.287)+123*(-0.243))/1655",
   "printed": 0.469
  },
  {
   "name": "p_main_Power",
   "expr": "f_sf(34.43, 2, 1654-3)",
   "printed": 0.0
  },
  {
   "name": "eta2_main_Power",
   "expr": "2*34.43/(2*34.43+1654-3)",
   "printed": 0.04
  },
  {
   "name": "p_pc_Power",
   "expr": "f_sf(58.4, 1, 1654-3)",
   "printed": 0.0
  },
  {
   "name": "eta2_pc_Power",
   "expr": "58.4/(58.4+1654-3)",
   "printed": 0.034
  }
 ],
 "hyps": [
  [
   "the three SVO groups add to 1655 and give the printed 69.5 / 23.0 / 7.4% within 0.05",
   "o['items']['svo_total']['diff'] == 0 and all(abs(o['items'][k]['diff']) <= 0.05 for k in ['pct_prosocial','pct_individualist','pct_competitor'])"
  ],
  [
   "both participant flows printed (Method: 1903 - 226 - 22; Results: 1906 - 223 - 23) arrive at the analysed 1655",
   "o['items']['method_flow_final']['diff'] == 0 and o['items']['results_flow_final']['diff'] == 0"
  ],
  [
   "every printed main-effect eta^2 reproduces from F and df (2, n - 3) within 0.0006",
   "all(abs(v['diff']) <= 0.0006 for k, v in o['items'].items() if k.startswith('eta2_main_'))"
  ],
  [
   "every printed planned-comparison eta^2 reproduces from F and df (1, n - 3) within 0.0006",
   "all(abs(v['diff']) <= 0.0006 for k, v in o['items'].items() if k.startswith('eta2_pc_'))"
  ],
  [
   "every printed p reproduces from F within 0.002 (a printed .000 read as < 0.0005)",
   "all((v['value'] < 0.0005) if v['printed'] == 0 else abs(v['diff']) <= 0.002 for k, v in o['items'].items() if k.startswith('p_'))"
  ],
  [
   "the n-weighted Table 3 group means reproduce Table 2's means within 0.005 for all 11 values",
   "all(abs(v['diff']) <= 0.005 for k, v in o['items'].items() if k.startswith('wmean_'))"
  ]
 ]
}
```

## Command
`python sim_soc.py iter-1` (run from `Social-Sciences/simulation/`)
