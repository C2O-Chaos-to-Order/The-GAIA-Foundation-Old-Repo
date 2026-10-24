# SIM-AL-SOC-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P52 reports that, controlling for group identification, identity fusion predicts violent pro-group action and identification predicts peaceful action in all three studies (latent SEM). Do two-predictor regressions computed from P52's printed correlation tables give the same signs, and does disattenuation with the printed alphas change any sign?

## Phase operationalization tested
SOC Allegiance = identity fusion versus group identification as two forms of group bonding (P52).

## Sources this run draws on
P52 (Ozkan, El-Astal & Cakal 2025, Br J Soc Psychol 64:e70002, CC BY-NC; read in full in ALA): Tables 1-3 correlations, alphas, N; SEM Model 2 paths (Figures 2, 4, 6 as reported in the text).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | fusion -> violent sign matches SEM in all studies |
| H2 | hypothesis | identification -> peaceful sign matches SEM in all studies |
| H3 | hypothesis | disattenuation changes no sign |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Manifest regression on printed correlations is not P52's latent SEM; non-significant SEM paths are coded 0 and not compared. Foreknowledge: while reading Table 3 the agent computed by hand that fusion -> violent comes out negative from the printed correlations; the smoke (seed 99) confirmed H1 and H3 not supported. Thresholds unchanged.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AL-SOC-A",
 "iteration": 1,
 "kind": "corr_regress",
 "seed": 25301,
 "studies": {
  "Study1_Gaza": {
   "N": 333,
   "alpha": {
    "F": 0.91,
    "G": 0.91,
    "P": 0.87,
    "V": 0.78
   },
   "r": {
    "FG": 0.71,
    "FP": -0.07,
    "FV": 0.36,
    "GP": 0.03,
    "GV": 0.24
   },
   "sem": {
    "F_V": 0.5,
    "F_P": -0.29,
    "G_P": 0.25,
    "G_V": 0
   }
  },
  "Study2_Turkiye_religion": {
   "N": 382,
   "alpha": {
    "F": 0.95,
    "G": 0.92,
    "P": 0.93,
    "V": 0.85
   },
   "r": {
    "FG": 0.73,
    "FP": 0.47,
    "FV": 0.28,
    "GP": 0.49,
    "GV": 0.21
   },
   "sem": {
    "F_V": 0.31,
    "F_P": 0,
    "G_P": 0.4,
    "G_V": 0
   }
  },
  "Study3_football": {
   "N": 413,
   "alpha": {
    "F": 0.96,
    "G": 0.95,
    "P": 0.87,
    "V": 0.95
   },
   "r": {
    "FG": 0.82,
    "FP": 0.6,
    "FV": 0.21,
    "GP": 0.59,
    "GV": 0.31
   },
   "sem": {
    "F_V": 0.38,
    "F_P": 0.52,
    "G_P": 0.13,
    "G_V": 0
   }
  }
 }
}
```

## Command
`python sim_soc.py iter-1` (run from `Social-Sciences/simulation/`)
