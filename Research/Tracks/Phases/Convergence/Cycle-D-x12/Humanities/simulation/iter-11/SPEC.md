# SIM-CV-HUM-D - iteration 11 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Exemplar toy, interaction attention 0.6, no floor.

## Phase operationalization tested
HUM Convergence = convergence of dialects by levelling (P82).

## Sources this run draws on
P71 (Sabev, Yuen, Andreeva & Moebius 2026, phonetic accommodation of German -ig, Front Psychol, PMC13585743, CC BY; read in full in CV0): 1138 trials after excluding 21 of 1159; Table 2 model selection (df, AIC, BIC, chi2, p for M0-M9); Table 3 final GLMM (beta, SE, z, p); 301/563 shadowing, 157/575 interaction.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | simulated rate matches its analytic mean within 4 SE |
| H1 | hypothesis | low-frequency words accommodate more in both tasks |
| H2 | hypothesis | without a floor, stronger interaction attention (0.6) keeps |interaction| < 0.15 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Replication-extension. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds/options in CVD (stats_audit, instrument_core, levelling_voter bias_mode=selection) were smoke-tested once at trivial size (seed 99, temporary directory, nothing kept) with printed values suppressed; existing kinds were not smoke-tested. CVC results were known when these hypotheses were written (replications say so).

## Parameters
```json
{
 "sim_id": "SIM-CV-HUM-D",
 "iteration": 11,
 "kind": "exemplar_shift",
 "seed": 33511,
 "speakers": 30,
 "tokens_per_word": 6,
 "N_high": 100,
 "N_low": 10,
 "a_shadow": 1.0,
 "a_inter": 0.6,
 "reps": 200,
 "hyps": [
  [
   "low-frequency words accommodate more in both tasks",
   "all(o['cells'][f'{t}_low']['rate'] > o['cells'][f'{t}_high']['rate'] for t in ['shadowing', 'interaction'])"
  ],
  [
   "without a floor, stronger interaction attention (0.6) keeps |interaction| < 0.15",
   "abs(o['logit_task_x_freq']) < 0.15"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-11` (run from `Humanities/simulation/`)
