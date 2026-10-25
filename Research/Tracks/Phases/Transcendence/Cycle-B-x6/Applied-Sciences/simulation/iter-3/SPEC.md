# SIM-TR-APP-B - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P100: universal-agreement S-CVI vs the printed average, and minimum I-CVI?

## Phase operationalization tested
APP Transcendence = self-transcendence measured and promoted in nursing (P100; P103 added in TRA).

## Sources this run draws on
P100 (Pena-Gayo, Gonzalez-Chorda, Cervera-Gasch, Mena-Tudela 2018, Spanish Reed Self-Transcendence Scale, Rev Lat Am Enfermagem, PMC6293607, CC BY 4.0; read in full in TR0): 19 experts; I-CVI, Pc, modified kappa, S-CVI; N 116 (138 recruited, 22 incomplete); EFA (Bartlett, KMO) and CFA (chi-square, df, RMSEA, SRMR) of 1-4 factor models; Table 2 sociodemographics.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | P100's universal-agreement S-CVI (share of items all experts rate relevant) is below 0.80, unlike its S-CVI/Ave 0.92 (P100 reports only the average) |
| H2 | hypothesis | every printed I-CVI is at least 0.78 (Polit et al.'s item threshold) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic on Table 1's I-CVIs. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-APP-B",
 "iteration": 3,
 "kind": "arith_audit",
 "seed": 41403,
 "items": [
  {
   "name": "scvi_ua",
   "expr": "sum(1 for x in [0.9473, 1, 0.8947, 0.9473, 1, 0.8947, 0.9473, 1, 0.8947, 0.8421, 1, 0.8421, 0.9473, 0.8421, 0.8333] if x == 1)/15"
  },
  {
   "name": "scvi_ave",
   "expr": "sum([0.9473, 1, 0.8947, 0.9473, 1, 0.8947, 0.9473, 1, 0.8947, 0.8421, 1, 0.8421, 0.9473, 0.8421, 0.8333])/15",
   "printed": 0.92
  },
  {
   "name": "min_icvi",
   "expr": "min([0.9473, 1, 0.8947, 0.9473, 1, 0.8947, 0.9473, 1, 0.8947, 0.8421, 1, 0.8421, 0.9473, 0.8421, 0.8333])"
  }
 ],
 "hyps": [
  [
   "P100's universal-agreement S-CVI (share of items all experts rate relevant) is below 0.80, unlike its S-CVI/Ave 0.92 (P100 reports only the average)",
   "o['items']['scvi_ua']['value'] < 0.80"
  ],
  [
   "every printed I-CVI is at least 0.78 (Polit et al.'s item threshold)",
   "o['items']['min_icvi']['value'] >= 0.78"
  ]
 ]
}
```

## Command
`python sim_app.py iter-3` (run from `Applied-Sciences/simulation/`)
