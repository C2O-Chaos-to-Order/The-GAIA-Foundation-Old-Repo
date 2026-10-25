# SIM-AS-APP-C - iteration 7 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P95 pooled prevalence vs simple and weighted means of Table 1

## Phase operationalization tested
APP Ascendence = ascent rate / protocol and AMS (P88, P91). ASC adds P95's meta-analysis.

## Sources this run draws on
P95 (Liu, Tan, Ren, Bai, Yong, Gao, Ba & Gongga 2026, 'Prevalence and risk factors for AMS: A systematic review and meta-analysis', PLoS One, PMC13068236, CC BY; read in full in ASC): 58 observational studies (stated n 2,705), pooled AMS prevalence 48.25% (95% CI 42.58-53.96), Table 1 study list, Table 2 GRADE risk ratios incl. rapid ascent (<6 h) RR 1.60 (1.44-1.78).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | the unweighted mean of Table 1 prevalences is within 5 points of P95's pooled 48.25% |
| H2 | hypothesis | the sample-size-weighted mean lies inside P95's 95% CI (42.58-53.96) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
P95 pools on the logit scale with random effects; simple means are the agent's check. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-APP-C",
 "iteration": 7,
 "kind": "arith_audit",
 "seed": 37407,
 "items": [
  {
   "name": "unweighted_mean_prev",
   "expr": "(73+26+63+70+60.46+38.89+62+28.57+11+32+40+40+43+83+81.18+66.7+41+35+43.4+68+69.2+67+67+45.1+50+20+52.4+35.5+60+43+62.2+55.8+60.8+5.5+74+40.4+45+63+84+66+36+23.1+21.9+58+47+50+56+52+20.3+81.8+72+69+28.6+17+34+51+47.1+58.3)/58"
  },
  {
   "name": "weighted_mean_prev",
   "expr": "(103*73+50*26+35*63+20*70+43*60.46+18*38.89+29*62+42*28.57+19*11+170*32+50*40+50*40+43*43+12*83+77*81.18+44*66.7+135*41+20*35+30*43.4+19*68+13*69.2+15*67+12*67+51*45.1+20*50+20*20+21*52.4+31*35.5+20*60+14*43+37*62.2+86*55.8+102*60.8+54*5.5+19*74+109*40.4+22*45+42*63+16*84+42*66+102*36+13*23.1+164*21.9+19*58+20*47+10*50+12*56+21*52+64*20.3+11*81.8+11*72+42*69+65*28.6+104*17+119*34+59*51+102*47.1+12*58.3)/(103+50+35+20+43+18+29+42+19+170+50+50+43+12+77+44+135+20+30+19+13+15+12+51+20+20+21+31+20+14+37+86+102+54+19+109+22+42+16+42+102+13+164+19+20+10+12+21+64+11+11+42+65+104+119+59+102+12)"
  }
 ],
 "hyps": [
  [
   "the unweighted mean of Table 1 prevalences is within 5 points of P95's pooled 48.25%",
   "abs(o['items']['unweighted_mean_prev']['value'] - 48.25) <= 5"
  ],
  [
   "the sample-size-weighted mean lies inside P95's 95% CI (42.58-53.96)",
   "42.58 <= o['items']['weighted_mean_prev']['value'] <= 53.96"
  ]
 ]
}
```

## Command
`python sim_app.py iter-7` (run from `Applied-Sciences/simulation/`)
