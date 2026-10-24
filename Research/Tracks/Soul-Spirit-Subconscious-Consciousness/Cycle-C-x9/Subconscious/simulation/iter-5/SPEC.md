# SIM-SUBC-C - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Mind x Justice. K35's within-country association of free will belief with everyday punitiveness is highly significant (b = 0.11 per SD). How large is it for individuals?

## Sources this run draws on
K35: b = 0.11 [0.09, 0.13] per SD of free will belief; punitiveness SD 1.12 (Table 1).

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | MC = analytic |
| H1 | hypothesis | concordance < .60 |
| R1 | reporting | r, r^2 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Approximates the standardized slope as a correlation and ignores covariates and clustering.

## Parameters
```json
{
 "sim_id": "SIM-SUBC-C",
 "iteration": 5,
 "kind": "cles",
 "seed": 515,
 "b": 0.11,
 "sd_y": 1.12,
 "pairs": 2000000
}
```

## Command
`python sim_subc.py iter-5` (run from `Subconscious/simulation/`)
