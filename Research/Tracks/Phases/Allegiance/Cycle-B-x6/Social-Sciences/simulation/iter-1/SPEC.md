# SIM-AL-SOC-B - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Does P52's printed correlation table match its own raw OSF data, is Study 3's mismatch a transposition of the fusion and identification entries, and do P52's latent SEM paths imply the same ordering as the disattenuated raw correlations?

## Phase operationalization tested
SOC Allegiance = auditing a fusion study against its data.

## Sources this run draws on
P57 (P52's OSF project osf.io/huysb: Mplus output of Model 6 for Study 3, fetched as text and read in full; .sav data files downloaded and summarised by the agent's script build15/extract_osf_p52.py, sha256 prefixes {'Study1_Gaza': '0971bba463c48758', 'Study2_Turkiye_religion': 'f6d7b2bf45a86eda', 'Study3_football': '37c6c536a656ee38'}; no licence stated on OSF, data not redistributed). P52 (read in full in ALA): printed Tables 1-3.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | printed = raw within 0.02 in every study |
| H2 | hypothesis | Study 3: swapped printed = raw; others unswapped |
| H3 | hypothesis | Study 3: SEM-implied order and values within 0.05 of disattenuated raw |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Raw correlations are scale means of P52's items as used in its Mplus models (6 peaceful, 8 violent items in Study 3). Smoke foreknowledge: H1 not supported (Study 3 off by 0.10), H2 supported, H3 not supported (max difference 0.10).Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AL-SOC-B",
 "iteration": 1,
 "kind": "table_audit",
 "seed": 26301,
 "studies": {
  "Study1_Gaza": {
   "printed": {
    "FG": 0.71,
    "FP": -0.07,
    "FV": 0.36,
    "GP": 0.03,
    "GV": 0.24
   },
   "raw": {
    "FG": 0.713,
    "FP": -0.068,
    "FV": 0.356,
    "GP": 0.025,
    "GV": 0.244
   },
   "alpha_raw": {
    "F": 0.913,
    "G": 0.915,
    "P": 0.87,
    "V": 0.781
   }
  },
  "Study2_Turkiye_religion": {
   "printed": {
    "FG": 0.73,
    "FP": 0.47,
    "FV": 0.28,
    "GP": 0.49,
    "GV": 0.21
   },
   "raw": {
    "FG": 0.73,
    "FP": 0.468,
    "FV": 0.284,
    "GP": 0.489,
    "GV": 0.213
   },
   "alpha_raw": {
    "F": 0.913,
    "G": 0.916,
    "P": 0.899,
    "V": 0.837
   }
  },
  "Study3_football": {
   "printed": {
    "FG": 0.82,
    "FP": 0.6,
    "FV": 0.21,
    "GP": 0.59,
    "GV": 0.31
   },
   "raw": {
    "FG": 0.818,
    "FP": 0.591,
    "FV": 0.311,
    "GP": 0.596,
    "GV": 0.208
   },
   "alpha_raw": {
    "F": 0.957,
    "G": 0.948,
    "P": 0.878,
    "V": 0.945
   },
   "sem": {
    "F_V": 0.375,
    "G_V": -0.086,
    "F_P": 0.519,
    "G_P": 0.134,
    "r_FG": 0.8
   }
  }
 },
 "tol": 0.02,
 "audit_study": "Study3_football"
}
```

## Command
`python sim_soc.py iter-1` (run from `Social-Sciences/simulation/`)
