# SIM-TR-SOC-C - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P107: do significance markers agree with the CIs, and the text's ranges with Table 4?

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
| H1 | hypothesis | P107 Table 4: every OR marked significant has a 95% CI excluding 1 and every unmarked one includes 1 |
| H2 | hypothesis | P107's text ranges of reduced odds for altruism and love match Table 4 (within 0.5 points) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic; a CI touching 1.00 at two decimals counts as including 1. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-SOC-C",
 "iteration": 5,
 "kind": "arith_audit",
 "seed": 42305,
 "items": [
  {
   "name": "sig_marker_mismatches",
   "expr": "sum(1 for c in {'China': {'RC': [(1.31, 1.1, 1.55, 1), (1.38, 1.16, 1.63, 1), (1.55, 1.27, 1.89, 1), (2.53, 1.86, 3.45, 1), (3.37, 2.27, 5.01, 1)], 'CP': [(1.06, 0.89, 1.26, 0), (1.07, 0.9, 1.27, 0), (0.98, 0.8, 1.21, 0), (2.18, 1.6, 2.98, 1), (2.19, 1.46, 3.27, 1)], 'UI': [(0.81, 0.67, 0.96, 1), (0.56, 0.47, 0.67, 1), (0.78, 0.63, 0.97, 1), (0.42, 0.26, 0.66, 1), (0.16, 0.07, 0.4, 1)], 'LOVE': [(0.81, 0.67, 0.96, 1), (0.65, 0.54, 0.77, 1), (0.77, 0.62, 0.96, 1), (0.48, 0.31, 0.75, 1), (0.2, 0.09, 0.45, 1)], 'ALT': [(0.63, 0.53, 0.76, 1), (0.53, 0.44, 0.64, 1), (0.7, 0.56, 0.87, 1), (0.51, 0.33, 0.78, 1), (0.4, 0.22, 0.73, 1)]}, 'India': {'RC': [(0.45, 0.32, 0.64, 1), (0.6, 0.43, 0.84, 1), (0.48, 0.33, 0.71, 1), (0.31, 0.12, 0.78, 1), (0.51, 0.22, 1.16, 0)], 'CP': [(0.62, 0.44, 0.87, 1), (0.68, 0.48, 0.95, 1), (0.67, 0.46, 0.97, 1), (0.73, 0.36, 1.49, 0), (1.06, 0.54, 2.1, 0)], 'UI': [(0.5, 0.36, 0.71, 1), (0.55, 0.4, 0.77, 1), (0.85, 0.59, 1.21, 0), (0.99, 0.53, 1.84, 0), (1.18, 0.62, 2.23, 0)], 'LOVE': [(0.4, 0.28, 0.56, 1), (0.41, 0.29, 0.57, 1), (0.38, 0.26, 0.57, 1), (0.46, 0.21, 0.99, 1), (0.44, 0.19, 1.0, 1)], 'ALT': [(0.28, 0.19, 0.4, 1), (0.38, 0.27, 0.53, 1), (0.28, 0.18, 0.43, 1), (0.21, 0.08, 0.59, 1), (0.31, 0.12, 0.79, 1)]}, 'US': {'RC': [(0.44, 0.32, 0.61, 1), (0.54, 0.38, 0.78, 1), (0.6, 0.42, 0.85, 1), (0.28, 0.12, 0.65, 1), (0.54, 0.31, 0.94, 1)], 'CP': [(0.83, 0.62, 1.11, 0), (1.01, 0.74, 1.38, 0), (0.95, 0.69, 1.3, 0), (0.68, 0.38, 1.21, 0), (1.06, 0.68, 1.67, 0)], 'UI': [(0.64, 0.48, 0.87, 1), (0.62, 0.44, 0.88, 1), (0.82, 0.59, 1.14, 0), (0.65, 0.36, 1.19, 0), (1.08, 0.69, 1.68, 0)], 'LOVE': [(0.42, 0.3, 0.57, 1), (0.53, 0.37, 0.75, 1), (0.67, 0.48, 0.93, 1), (0.72, 0.41, 1.27, 0), (0.89, 0.56, 1.4, 0)], 'ALT': [(0.5, 0.36, 0.68, 1), (0.48, 0.33, 0.7, 1), (0.69, 0.49, 0.97, 1), (0.53, 0.27, 1.01, 1), (0.83, 0.51, 1.34, 0)]}}.values() for d in c.values() for r in d if r[3] != int(r[2] < 1 or r[1] > 1))"
  },
  {
   "name": "alt_MDD_lo",
   "expr": "100*(1-.63)",
   "printed": 37
  },
  {
   "name": "alt_MDD_hi",
   "expr": "100*(1-.28)",
   "printed": 72
  },
  {
   "name": "alt_SI_lo",
   "expr": "100*(1-.53)",
   "printed": 47
  },
  {
   "name": "alt_SI_hi",
   "expr": "100*(1-.38)",
   "printed": 62
  },
  {
   "name": "alt_GAD_lo",
   "expr": "100*(1-.70)",
   "printed": 30
  },
  {
   "name": "alt_GAD_hi",
   "expr": "100*(1-.28)",
   "printed": 72
  },
  {
   "name": "alt_ALC_lo",
   "expr": "100*(1-.53)",
   "printed": 47
  },
  {
   "name": "alt_ALC_hi",
   "expr": "100*(1-.21)",
   "printed": 79
  },
  {
   "name": "love_MDD_lo",
   "expr": "100*(1-.81)",
   "printed": 19
  },
  {
   "name": "love_MDD_hi",
   "expr": "100*(1-.40)",
   "printed": 60
  },
  {
   "name": "love_SI_lo",
   "expr": "100*(1-.65)",
   "printed": 35
  },
  {
   "name": "love_SI_hi",
   "expr": "100*(1-.41)",
   "printed": 49
  },
  {
   "name": "love_GAD_lo",
   "expr": "100*(1-.77)",
   "printed": 23
  },
  {
   "name": "love_GAD_hi",
   "expr": "100*(1-.38)",
   "printed": 62
  }
 ],
 "hyps": [
  [
   "P107 Table 4: every OR marked significant has a 95% CI excluding 1 and every unmarked one includes 1",
   "o['items']['sig_marker_mismatches']['value'] == 0"
  ],
  [
   "P107's text ranges of reduced odds for altruism and love match Table 4 (within 0.5 points)",
   "all(abs(v['diff']) <= 0.5 for k, v in o['items'].items() if k.startswith(('alt_','love_')))"
  ]
 ]
}
```

## Command
`python sim_soc.py iter-5` (run from `Social-Sciences/simulation/`)
