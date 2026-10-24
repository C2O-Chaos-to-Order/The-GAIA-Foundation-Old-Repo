# SIM-SPIRIT-D - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K62: a transformative religious/spiritual experience in late adolescence predicted volunteering in early adulthood (RR 1.21 [1.12, 1.30]; E-value 1.71, limit 1.48). Check the E-values and what they mean.

## Sources this run draws on
K62 Results: RR = 1.21 [1.12, 1.30], E-value = 1.71, E-limit = 1.48.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | worked example |
| V2 | validation | bias factor |
| V3 | validation | match reported |
| H1 | hypothesis | E < 2 |
| R1 | reporting | E-values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic only. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SPIRIT-D",
 "iteration": 3,
 "kind": "evalue_harmful",
 "seed": 1203,
 "rr": 1.21,
 "ci_lower": 1.12,
 "reported": [
  1.71,
  1.48
 ]
}
```

## Command
`python sim_spirit.py iter-3` (run from `Spirit/simulation/`)
