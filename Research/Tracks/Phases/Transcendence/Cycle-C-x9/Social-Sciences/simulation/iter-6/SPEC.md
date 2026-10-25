# SIM-TR-SOC-C - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P107: do the text's correlation ranges match Table 2?

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
| H1 | hypothesis | P107's inter-factor correlation range (+0.28 to +0.56) and single-item range (+0.68 to +0.79) match Table 2 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-SOC-C",
 "iteration": 6,
 "kind": "arith_audit",
 "seed": 42306,
 "items": [
  {
   "name": "ifc_min",
   "expr": "min([0.55,0.55,0.36,0.48,0.28,0.52,0.50,0.36,0.37,0.56])",
   "printed": 0.28
  },
  {
   "name": "ifc_max",
   "expr": "max([0.55,0.55,0.36,0.48,0.28,0.52,0.50,0.36,0.37,0.56])",
   "printed": 0.56
  },
  {
   "name": "rc_single_min",
   "expr": "min(0.79,0.75,0.68)",
   "printed": 0.68
  },
  {
   "name": "rc_single_max",
   "expr": "max(0.79,0.75,0.68)",
   "printed": 0.79
  }
 ],
 "hyps": [
  [
   "P107's inter-factor correlation range (+0.28 to +0.56) and single-item range (+0.68 to +0.79) match Table 2",
   "all(abs(v['diff']) < 1e-9 for v in o['items'].values())"
  ]
 ]
}
```

## Command
`python sim_soc.py iter-6` (run from `Social-Sciences/simulation/`)
