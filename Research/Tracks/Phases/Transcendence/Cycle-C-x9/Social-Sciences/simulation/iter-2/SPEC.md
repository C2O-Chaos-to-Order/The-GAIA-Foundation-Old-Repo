# SIM-TR-SOC-C - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P107 Table 4 (China): is every OR the geometric mean of its CI?

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
| H1 | hypothesis | P107 Table 4 (China): every OR is the geometric mean of its 95% CI within rounding (|ln OR - mean ln bounds| <= 0.05) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic; logistic-regression CIs are symmetric on the log scale. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-SOC-C",
 "iteration": 2,
 "kind": "arith_audit",
 "seed": 42302,
 "items": [
  {
   "name": "max_logdev_China",
   "expr": "max(abs(log(r[0]) - (log(r[1]) + log(r[2]))/2) for d in {'RC': [(1.31, 1.1, 1.55, 1), (1.38, 1.16, 1.63, 1), (1.55, 1.27, 1.89, 1), (2.53, 1.86, 3.45, 1), (3.37, 2.27, 5.01, 1)], 'CP': [(1.06, 0.89, 1.26, 0), (1.07, 0.9, 1.27, 0), (0.98, 0.8, 1.21, 0), (2.18, 1.6, 2.98, 1), (2.19, 1.46, 3.27, 1)], 'UI': [(0.81, 0.67, 0.96, 1), (0.56, 0.47, 0.67, 1), (0.78, 0.63, 0.97, 1), (0.42, 0.26, 0.66, 1), (0.16, 0.07, 0.4, 1)], 'LOVE': [(0.81, 0.67, 0.96, 1), (0.65, 0.54, 0.77, 1), (0.77, 0.62, 0.96, 1), (0.48, 0.31, 0.75, 1), (0.2, 0.09, 0.45, 1)], 'ALT': [(0.63, 0.53, 0.76, 1), (0.53, 0.44, 0.64, 1), (0.7, 0.56, 0.87, 1), (0.51, 0.33, 0.78, 1), (0.4, 0.22, 0.73, 1)]}.values() for r in d)"
  }
 ],
 "hyps": [
  [
   "P107 Table 4 (China): every OR is the geometric mean of its 95% CI within rounding (|ln OR - mean ln bounds| <= 0.05)",
   "o['items']['max_logdev_China']['value'] <= 0.05"
  ]
 ]
}
```

## Command
`python sim_soc.py iter-2` (run from `Social-Sciences/simulation/`)
