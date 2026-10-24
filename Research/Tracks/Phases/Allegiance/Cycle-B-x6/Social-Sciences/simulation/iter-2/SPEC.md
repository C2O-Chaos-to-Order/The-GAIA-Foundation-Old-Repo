# SIM-AL-SOC-B - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Re-run of ALA's sign check using correlations computed from P52's raw data instead of the printed tables: does fusion -> violent now have the SEM's sign in all three studies?

## Phase operationalization tested
SOC Allegiance = fusion versus identification from raw data.

## Sources this run draws on
P57 (P52's OSF project osf.io/huysb: Mplus output of Model 6 for Study 3, fetched as text and read in full; .sav data files downloaded and summarised by the agent's script build15/extract_osf_p52.py, sha256 prefixes {'Study1_Gaza': '0971bba463c48758', 'Study2_Turkiye_religion': 'f6d7b2bf45a86eda', 'Study3_football': '37c6c536a656ee38'}; no licence stated on OSF, data not redistributed). P52 (read in full in ALA): printed Tables 1-3.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | fusion -> violent sign matches SEM in all studies |
| H2 | hypothesis | identification -> peaceful sign matches SEM |
| H3 | hypothesis | disattenuation changes no sign |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Foreknowledge by hand arithmetic on the raw correlations before the run: H1 expected supported (Study 3 about +0.43); Study 2's near-zero identification -> violent coefficient may again flip under disattenuation.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Existing kind; no new smoke test.

## Parameters
```json
{
 "sim_id": "SIM-AL-SOC-B",
 "iteration": 2,
 "kind": "corr_regress",
 "seed": 26302,
 "studies": {
  "Study1_Gaza": {
   "N": 333,
   "alpha": {
    "F": 0.913,
    "G": 0.915,
    "P": 0.87,
    "V": 0.781
   },
   "r": {
    "FG": 0.713,
    "FP": -0.068,
    "FV": 0.356,
    "GP": 0.025,
    "GV": 0.244
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
    "F": 0.913,
    "G": 0.916,
    "P": 0.899,
    "V": 0.837
   },
   "r": {
    "FG": 0.73,
    "FP": 0.468,
    "FV": 0.284,
    "GP": 0.489,
    "GV": 0.213
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
    "F": 0.957,
    "G": 0.948,
    "P": 0.878,
    "V": 0.945
   },
   "r": {
    "FG": 0.818,
    "FP": 0.591,
    "FV": 0.311,
    "GP": 0.596,
    "GV": 0.208
   },
   "sem": {
    "F_V": 0.375,
    "F_P": 0.519,
    "G_P": 0.134,
    "G_V": 0
   }
  }
 }
}
```

## Command
`python sim_soc.py iter-2` (run from `Social-Sciences/simulation/`)
