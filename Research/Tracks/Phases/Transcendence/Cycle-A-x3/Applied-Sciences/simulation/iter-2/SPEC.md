# SIM-TR-APP-A - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Chance agreement among 19 raters: does Monte Carlo agree with C(19, A) 0.5^19 for A 15-19, and is kappa with that Pc >= 0.74 throughout?

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
| H1 | hypothesis | simulated frequencies of exactly A of 19 raters agreeing by chance are within 4 SE of C(19, A) 0.5^19 for A = 15..19 |
| H2 | hypothesis | with the formula Pc, modified kappa is at least 0.74 ('excellent') for every A >= 15 of 19 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
400,000 simulated rating sets; Polit et al.'s formula as cited by P100. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-APP-A",
 "iteration": 2,
 "kind": "cvi_chance_mc",
 "seed": 40402,
 "N": 19,
 "A_list": [
  15,
  16,
  17,
  18,
  19
 ],
 "reps": 400000,
 "hyps": [
  [
   "simulated frequencies of exactly A of 19 raters agreeing by chance are within 4 SE of C(19, A) 0.5^19 for A = 15..19",
   "all(abs(v['freq'] - v['pc']) <= 4 * v['se'] + 1e-12 for v in o['by_A'].values())"
  ],
  [
   "with the formula Pc, modified kappa is at least 0.74 ('excellent') for every A >= 15 of 19",
   "all(v['kappa'] >= 0.74 for v in o['by_A'].values())"
  ]
 ]
}
```

## Command
`python sim_app.py iter-2` (run from `Applied-Sciences/simulation/`)
