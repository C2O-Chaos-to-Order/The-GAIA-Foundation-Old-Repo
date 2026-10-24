# SIM-CV-HUM-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P71's entrenchment account as an exemplar toy (N 100 vs 10 stored exemplars; attention 1.0 shadowing vs 0.3 interaction; 6 tokens per word): does it give more accommodation for low-frequency words and in shadowing, a positive task x frequency interaction on the logit scale (> 0.5, the sign of P71's beta 1.68), and an order effect?

## Phase operationalization tested
HUM Convergence = phonetic convergence through exemplar updating (P71's account).

## Sources this run draws on
P71 (Sabev, Yuen, Andreeva & Moebius 2026, phonetic accommodation of German -ig, Front Psychol, PMC13585743, CC BY; read in full in CV0): 1138 trials after excluding 21 of 1159; Table 2 model selection (df, AIC, BIC, chi2, p for M0-M9); Table 3 final GLMM (beta, SE, z, p); 301/563 shadowing, 157/575 interaction.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | simulated rate matches its analytic mean within 4 SE |
| H1 | hypothesis | low-frequency words accommodate more than high-frequency words in both tasks |
| H2 | hypothesis | shadowing exceeds interaction for both frequencies |
| H3 | hypothesis | the logit-scale task x frequency interaction is positive and > 0.5 (sign of P71's beta 1.68) |
| H4 | hypothesis | order effect: second-half rate exceeds first-half rate in every cell |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy; all parameters are the agent's. Foreknowledge from arithmetic before writing: the logit interaction is expected to be near 0 (H3 expected not supported). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-HUM-A",
 "iteration": 1,
 "kind": "exemplar_shift",
 "seed": 30501,
 "speakers": 30,
 "tokens_per_word": 6,
 "N_high": 100,
 "N_low": 10,
 "a_shadow": 1.0,
 "a_inter": 0.3,
 "reps": 200,
 "hyps": [
  [
   "low-frequency words accommodate more than high-frequency words in both tasks",
   "all(o['cells'][f'{t}_low']['rate'] > o['cells'][f'{t}_high']['rate'] for t in ['shadowing', 'interaction'])"
  ],
  [
   "shadowing exceeds interaction for both frequencies",
   "all(o['cells'][f'shadowing_{q}']['rate'] > o['cells'][f'interaction_{q}']['rate'] for q in ['high', 'low'])"
  ],
  [
   "the logit-scale task x frequency interaction is positive and > 0.5 (sign of P71's beta 1.68)",
   "o['logit_task_x_freq'] > 0.5"
  ],
  [
   "order effect: second-half rate exceeds first-half rate in every cell",
   "all(v['second_half'] > v['first_half'] for v in o['cells'].values())"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-1` (run from `Humanities/simulation/`)
