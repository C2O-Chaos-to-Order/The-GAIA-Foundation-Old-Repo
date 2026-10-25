# SIM-TR-SOC-C - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P107 Table 4 (India): as iter-2.

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
| H1 | hypothesis | P107 Table 4 (India): every OR is the geometric mean of its 95% CI within rounding (|ln OR - mean ln bounds| <= 0.05) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iter-2. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-SOC-C",
 "iteration": 3,
 "kind": "arith_audit",
 "seed": 42303,
 "items": [
  {
   "name": "max_logdev_India",
   "expr": "max(abs(log(r[0]) - (log(r[1]) + log(r[2]))/2) for d in {'RC': [(0.45, 0.32, 0.64, 1), (0.6, 0.43, 0.84, 1), (0.48, 0.33, 0.71, 1), (0.31, 0.12, 0.78, 1), (0.51, 0.22, 1.16, 0)], 'CP': [(0.62, 0.44, 0.87, 1), (0.68, 0.48, 0.95, 1), (0.67, 0.46, 0.97, 1), (0.73, 0.36, 1.49, 0), (1.06, 0.54, 2.1, 0)], 'UI': [(0.5, 0.36, 0.71, 1), (0.55, 0.4, 0.77, 1), (0.85, 0.59, 1.21, 0), (0.99, 0.53, 1.84, 0), (1.18, 0.62, 2.23, 0)], 'LOVE': [(0.4, 0.28, 0.56, 1), (0.41, 0.29, 0.57, 1), (0.38, 0.26, 0.57, 1), (0.46, 0.21, 0.99, 1), (0.44, 0.19, 1.0, 1)], 'ALT': [(0.28, 0.19, 0.4, 1), (0.38, 0.27, 0.53, 1), (0.28, 0.18, 0.43, 1), (0.21, 0.08, 0.59, 1), (0.31, 0.12, 0.79, 1)]}.values() for r in d)"
  }
 ],
 "hyps": [
  [
   "P107 Table 4 (India): every OR is the geometric mean of its 95% CI within rounding (|ln OR - mean ln bounds| <= 0.05)",
   "o['items']['max_logdev_India']['value'] <= 0.05"
  ]
 ]
}
```

## Command
`python sim_soc.py iter-3` (run from `Social-Sciences/simulation/`)
