# SIM-CV-HUM-A - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Exemplar toy with memory decay 0.3 per trial: does the frequency effect survive and does the logit task x frequency interaction exceed 0.5?

## Phase operationalization tested
HUM Convergence = phonetic convergence through exemplar updating.

## Sources this run draws on
P71 (Sabev, Yuen, Andreeva & Moebius 2026, phonetic accommodation of German -ig, Front Psychol, PMC13585743, CC BY; read in full in CV0): 1138 trials after excluding 21 of 1159; Table 2 model selection (df, AIC, BIC, chi2, p for M0-M9); Table 3 final GLMM (beta, SE, z, p); 301/563 shadowing, 157/575 interaction.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | simulated rate matches its analytic mean within 4 SE (n/a with decay: Pass by construction) |
| H1 | hypothesis | with exemplar decay 0.3 low-frequency words still accommodate more in both tasks |
| H2 | hypothesis | with decay the logit task x frequency interaction is > 0.5 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy; decay is the agent's. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-HUM-A",
 "iteration": 2,
 "kind": "exemplar_shift",
 "seed": 30502,
 "speakers": 30,
 "tokens_per_word": 6,
 "N_high": 100,
 "N_low": 10,
 "a_shadow": 1.0,
 "a_inter": 0.3,
 "reps": 200,
 "decay": 0.3,
 "hyps": [
  [
   "with exemplar decay 0.3 low-frequency words still accommodate more in both tasks",
   "all(o['cells'][f'{t}_low']['rate'] > o['cells'][f'{t}_high']['rate'] for t in ['shadowing', 'interaction'])"
  ],
  [
   "with decay the logit task x frequency interaction is > 0.5",
   "o['logit_task_x_freq'] > 0.5"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-2` (run from `Humanities/simulation/`)
