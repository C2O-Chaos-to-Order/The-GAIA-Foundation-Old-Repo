# SIM-TR-APP-B - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
6 raters (a common panel size): Monte Carlo vs formula and kappa at 4 and 5 agreeing?

## Phase operationalization tested
APP Transcendence = self-transcendence measured and promoted in nursing (P100; P103 added in TRA).

## Sources this run draws on
P100 (Pena-Gayo, Gonzalez-Chorda, Cervera-Gasch, Mena-Tudela 2018, Spanish Reed Self-Transcendence Scale, Rev Lat Am Enfermagem, PMC6293607, CC BY 4.0; read in full in TR0): 19 experts; I-CVI, Pc, modified kappa, S-CVI; N 116 (138 recruited, 22 incomplete); EFA (Bartlett, KMO) and CFA (chi-square, df, RMSEA, SRMR) of 1-4 factor models; Table 2 sociodemographics.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | binomial probabilities sum to 1 |
| H1 | hypothesis | 6 raters: Monte Carlo within 4 SE of the formula |
| H2 | hypothesis | with 6 raters, 5 agreeing (I-CVI 0.83) still gives kappa above 0.74 but 4 agreeing (0.67) does not |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
400,000 replicates. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-APP-B",
 "iteration": 5,
 "kind": "cvi_chance_mc",
 "seed": 41405,
 "N": 6,
 "A_list": [
  4,
  5,
  6
 ],
 "reps": 400000,
 "hyps": [
  [
   "6 raters: Monte Carlo within 4 SE of the formula",
   "all(abs(v['freq'] - v['pc']) <= 4 * v['se'] + 1e-12 for v in o['by_A'].values())"
  ],
  [
   "with 6 raters, 5 agreeing (I-CVI 0.83) still gives kappa above 0.74 but 4 agreeing (0.67) does not",
   "o['by_A']['5']['kappa'] > 0.74 and o['by_A']['4']['kappa'] < 0.74"
  ]
 ]
}
```

## Command
`python sim_app.py iter-5` (run from `Applied-Sciences/simulation/`)
