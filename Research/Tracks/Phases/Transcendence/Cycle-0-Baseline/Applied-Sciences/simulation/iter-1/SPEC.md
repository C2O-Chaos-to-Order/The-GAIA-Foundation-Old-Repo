# SIM-TR-APP-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P100's content-validity and factor-analysis statistics: do I-CVIs, chance agreement Pc, modified kappa and S-CVI follow from the expert counts, do RMSEA and chi-square p follow from chi-square, df and N, and is Bartlett's df right for 15 items?

## Phase operationalization tested
APP Transcendence = self-transcendence as a measured construct in nursing (Reed's Self-Transcendence Scale; P100).

## Sources this run draws on
P100 (Pena-Gayo, Gonzalez-Chorda, Cervera-Gasch, Mena-Tudela 2018, Spanish Reed Self-Transcendence Scale, Rev Lat Am Enfermagem, PMC6293607, CC BY 4.0; read in full in TR0): 19 experts; I-CVI, Pc, modified kappa, S-CVI; N 116 (138 recruited, 22 incomplete); EFA (Bartlett, KMO) and CFA (chi-square, df, RMSEA, SRMR) of 1-4 factor models; Table 2 sociodemographics.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | the printed I-CVIs equal the share of agreeing raters (18/19, 17/19, 16/19, 15/18) within 0.0001 |
| H2 | hypothesis | the printed chance-agreement probabilities Pc equal the binomial C(N, A) 0.5^N within 5% (relative) for all five rating patterns |
| H3 | hypothesis | the printed modified kappas follow from the printed I-CVI and Pc as (I-CVI - Pc)/(1 - Pc) within 0.0005 |
| H4 | hypothesis | S-CVI (mean of the 15 printed I-CVIs) is within 0.005 of the printed 0.92 |
| H5 | hypothesis | RMSEA reproduces from chi-square, df and N 116 within 0.001 for all four factor models, and their chi-square p within 0.002 (1-factor '<0.001' read as < 0.001) |
| H6 | hypothesis | Bartlett's sphericity df equals p(p - 1)/2 = 105 for 15 items, as printed ('df = 1,050') |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic arithmetic audit; Pc formula C(N, A) 0.5^N (Polit et al.); RMSEA = sqrt(max(chi2 - df, 0)/(df (N - 1))) with N 116. Foreknowledge: hand checks while reading (disclosed). Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so every outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-APP-0",
 "iteration": 1,
 "kind": "arith_audit",
 "seed": 39401,
 "items": [
  {
   "name": "icvi_18_19",
   "expr": "18/19",
   "printed": 0.9473
  },
  {
   "name": "icvi_17_19",
   "expr": "17/19",
   "printed": 0.8947
  },
  {
   "name": "icvi_16_19",
   "expr": "16/19",
   "printed": 0.8421
  },
  {
   "name": "icvi_15_18",
   "expr": "15/18",
   "printed": 0.8333
  },
  {
   "name": "pc_19_19",
   "expr": "comb(19,19)*0.5**19",
   "printed": 1.90735e-06
  },
  {
   "name": "pc_18_19",
   "expr": "comb(19,18)*0.5**19",
   "printed": 3.62396e-05
  },
  {
   "name": "pc_17_19",
   "expr": "comb(19,17)*0.5**19",
   "printed": 0.0013
  },
  {
   "name": "pc_16_19",
   "expr": "comb(19,16)*0.5**19",
   "printed": 0.0665
  },
  {
   "name": "pc_15_18",
   "expr": "comb(18,15)*0.5**18",
   "printed": 0.112
  },
  {
   "name": "kappa_17_19",
   "expr": "(0.8947-0.0013)/(1-0.0013)",
   "printed": 0.8945
  },
  {
   "name": "kappa_16_19",
   "expr": "(0.8421-0.0665)/(1-0.0665)",
   "printed": 0.8308
  },
  {
   "name": "kappa_15_18",
   "expr": "(0.8333-0.1120)/(1-0.1120)",
   "printed": 0.8122
  },
  {
   "name": "scvi_mean",
   "expr": "sum([0.9473, 1, 0.8947, 0.9473, 1, 0.8947, 0.9473, 1, 0.8947, 0.8421, 1, 0.8421, 0.9473, 0.8421, 0.8333])/15",
   "printed": 0.92
  },
  {
   "name": "rmsea_4f",
   "expr": "sqrt(max(111.537-84,0)/(84*115))",
   "printed": 0.053
  },
  {
   "name": "rmsea_3f",
   "expr": "sqrt(max(111.673-87,0)/(87*115))",
   "printed": 0.049
  },
  {
   "name": "rmsea_2f",
   "expr": "sqrt(max(117.577-89,0)/(89*115))",
   "printed": 0.053
  },
  {
   "name": "rmsea_1f",
   "expr": "sqrt(max(152.377-90,0)/(90*115))",
   "printed": 0.077
  },
  {
   "name": "p_4f",
   "expr": "chi2_sf(111.537, 84)",
   "printed": 0.023
  },
  {
   "name": "p_3f",
   "expr": "chi2_sf(111.673, 87)",
   "printed": 0.038
  },
  {
   "name": "p_2f",
   "expr": "chi2_sf(117.577, 89)",
   "printed": 0.022
  },
  {
   "name": "p_1f",
   "expr": "chi2_sf(152.377, 90)",
   "printed": 0.001
  },
  {
   "name": "bartlett_df_15_items",
   "expr": "15*14/2",
   "printed": 1050
  },
  {
   "name": "pct_women",
   "expr": "100*90/116",
   "printed": 77.59
  },
  {
   "name": "pct_noncomplete",
   "expr": "100*22/138",
   "printed": 15.94
  },
  {
   "name": "marital_total",
   "expr": "39+14+11+49+3",
   "printed": 116
  },
  {
   "name": "children0_total",
   "expr": "11+50",
   "printed": 16
  }
 ],
 "hyps": [
  [
   "the printed I-CVIs equal the share of agreeing raters (18/19, 17/19, 16/19, 15/18) within 0.0001",
   "all(abs(o['items'][k]['diff']) <= 0.0001 for k in ['icvi_18_19','icvi_17_19','icvi_16_19','icvi_15_18'])"
  ],
  [
   "the printed chance-agreement probabilities Pc equal the binomial C(N, A) 0.5^N within 5% (relative) for all five rating patterns",
   "all(abs(o['items'][k]['value']/o['items'][k]['printed'] - 1) <= 0.05 for k in ['pc_19_19','pc_18_19','pc_17_19','pc_16_19','pc_15_18'])"
  ],
  [
   "the printed modified kappas follow from the printed I-CVI and Pc as (I-CVI - Pc)/(1 - Pc) within 0.0005",
   "all(abs(o['items'][k]['diff']) <= 0.0005 for k in ['kappa_17_19','kappa_16_19','kappa_15_18'])"
  ],
  [
   "S-CVI (mean of the 15 printed I-CVIs) is within 0.005 of the printed 0.92",
   "abs(o['items']['scvi_mean']['diff']) <= 0.005"
  ],
  [
   "RMSEA reproduces from chi-square, df and N 116 within 0.001 for all four factor models, and their chi-square p within 0.002 (1-factor '<0.001' read as < 0.001)",
   "all(abs(o['items'][k]['diff']) <= 0.001 for k in ['rmsea_4f','rmsea_3f','rmsea_2f','rmsea_1f']) and all(abs(o['items'][k]['diff']) <= 0.002 for k in ['p_4f','p_3f','p_2f']) and o['items']['p_1f']['value'] < 0.001"
  ],
  [
   "Bartlett's sphericity df equals p(p - 1)/2 = 105 for 15 items, as printed ('df = 1,050')",
   "o['items']['bartlett_df_15_items']['diff'] == 0"
  ]
 ]
}
```

## Command
`python sim_app.py iter-1` (run from `Applied-Sciences/simulation/`)
