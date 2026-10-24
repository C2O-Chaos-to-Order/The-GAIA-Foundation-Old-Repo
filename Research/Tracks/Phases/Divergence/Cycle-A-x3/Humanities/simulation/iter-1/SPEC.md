# SIM-DV-HUM-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
How much does the size of a meaning list limit cognate-based divergence estimates? Reproduce P12's list-size formula and simulate T_hat spread by list size.

## Phase operationalization tested
HUM Divergence = lexical divergence measured on a finite basic-vocabulary list (P12: lexicostatistics, Swadesh 100/200 lists).

## Sources this run draws on
P12 (Zhang & Gong 2016, read in full): Eq. 8 and Table 1 (356.750; 66.526), range [67, 357].

## Refinement from previous iteration
DV0's lexical_divergence assumed M = 200 meanings without sampling-size analysis; this iteration adds P12's list-size principle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | Eq. 8 reproduces Table 1 within 0.01 |
| V2 | validation | mean C within 4 SE |
| H1 | hypothesis | 100-meaning list: 95% range within +/-25% of T |
| R1 | reporting | ranges by size |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Rate r = 0.07 per millennium is still illustrative (P12 gives no retention rate); binomial sampling only, no borrowing or coding error. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-HUM-A",
 "iteration": 1,
 "kind": "list_size",
 "seed": 15501,
 "r": 0.07,
 "T": 3.0,
 "list_sizes": [
  40,
  100,
  200
 ],
 "reps": 20000,
 "tol_se": 4,
 "h1": 0.25
}
```

## Command
`python sim_hum.py iter-1` (run from `Humanities/simulation/`)
