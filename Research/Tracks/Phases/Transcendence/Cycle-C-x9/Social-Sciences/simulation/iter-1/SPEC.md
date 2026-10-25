# SIM-TR-SOC-C - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P107: do sample sizes and affiliation percentages add up?

## Phase operationalization tested
SOC Transcendence = self-transcendence values and prosocial orientation (P99). TRC adds P107's cross-cultural dimensions of spirituality.

## Sources this run draws on
P107 (McClintock, Lau & Miller 2016, 'Phenotypic Dimensions of Spirituality: Implications for Mental Health in China, India, and the United States', Front Psychol 7:1600, PMC5082226, CC BY 4.0; read in full in TRC): N = 5512 (China 3150, India 863, US 1499); EFA in two subsamples and ESEM in two further subsamples derive five dimensions (reflection and commitment, contemplative practice, unifying interconnectedness, love, altruism); multi-group ESEM tests configural invariance (CFI about 0.90); Table 4 odds ratios of psychiatric conditions for the top quartile of each dimension.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 with 1 df equals 0.05 within 1e-9 |
| H1 | hypothesis | P107's sample sizes add up (countries and four subsamples to 5512; S1 + S2 = 1838) |
| H2 | hypothesis | P107's whole-sample religious-affiliation percentages add to 100 (within 1) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-SOC-C",
 "iteration": 1,
 "kind": "arith_audit",
 "seed": 42301,
 "items": [
  {
   "name": "N_countries",
   "expr": "3150+863+1499",
   "printed": 5512
  },
  {
   "name": "N_subsamples",
   "expr": "919+919+1837+1837",
   "printed": 5512
  },
  {
   "name": "N_S1S2",
   "expr": "919+919",
   "printed": 1838
  },
  {
   "name": "religion_pct_sum",
   "expr": "20+21+11+2+26+9"
  },
  {
   "name": "measures_after_S1",
   "expr": "40-6",
   "printed": 34
  },
  {
   "name": "measures_after_S2",
   "expr": "40-10",
   "printed": 30
  }
 ],
 "hyps": [
  [
   "P107's sample sizes add up (countries and four subsamples to 5512; S1 + S2 = 1838)",
   "all(abs(o['items'][k]['diff']) < 1e-9 for k in ['N_countries','N_subsamples','N_S1S2'])"
  ],
  [
   "P107's whole-sample religious-affiliation percentages add to 100 (within 1)",
   "abs(o['items']['religion_pct_sum']['value'] - 100) <= 1"
  ]
 ]
}
```

## Command
`python sim_soc.py iter-1` (run from `Social-Sciences/simulation/`)
