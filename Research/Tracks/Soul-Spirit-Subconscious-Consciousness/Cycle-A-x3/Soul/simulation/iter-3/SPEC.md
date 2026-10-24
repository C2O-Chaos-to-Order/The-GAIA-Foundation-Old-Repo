# SIM-SOUL-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K02 coded open answers about what happens after death and reports 96% agreement with kappa .79. What prevalence and coder error does that pair imply, and how would kappa move at other prevalences (kappa paradox; links to R3's coding-reliability work)?

## Sources this run draws on
K02 (Haimila & Muraja 2023): 96% agreement, Cohen's kappa = .79 on 25% of the data; W07 (McHugh 2012, kappa interpretation) carried from the main cycles.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | implied chance agreement computed |
| V2 | validation | simulated kappa within 0.02 of .79 |
| H1 | hypothesis | same coders at prevalence 0.5: kappa > 0.90 |
| R1 | reporting | implied percent agreement at the fit |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Treats K02's multi-category coding as one binary category with equal coder error (a simplification; K02's category structure is richer). Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SOUL-A",
 "iteration": 3,
 "kind": "kappa_prevalence",
 "seed": 203,
 "p_o": 0.96,
 "kappa": 0.79,
 "n_units": 2000,
 "reps": 2000,
 "pi_grid": [
  0.05,
  0.1,
  0.2,
  0.3,
  0.5
 ]
}
```

## Command
`python sim_soul.py iter-3` (run from `Soul/simulation/`)
