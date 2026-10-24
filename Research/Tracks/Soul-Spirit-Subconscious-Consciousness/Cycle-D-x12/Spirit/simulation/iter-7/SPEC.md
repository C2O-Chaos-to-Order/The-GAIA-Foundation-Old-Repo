# SIM-SPIRIT-D - iteration 7 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
All K52 meta-analysed studies were within-subject pre-post designs without a control arm. How large an apparent reduction can regression to the mean produce if participants are selected for high death anxiety?

## Sources this run draws on
K52: 'All studies included in the meta-analysis employed within-subject, pre-post designs.' Test-retest r 0.7 and top-30% selection ILLUSTRATIVE.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | no selection: 0 |
| H1 | hypothesis | apparent d >= .3 |
| R1 | reporting | d |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Selection is on the observed baseline score; no treatment, practice or expectancy effects. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SPIRIT-D",
 "iteration": 7,
 "kind": "prepost_rtm",
 "seed": 1207,
 "n": 400000,
 "r": 0.7,
 "q": 0.3,
 "h1": 0.3
}
```

## Command
`python sim_spirit.py iter-7` (run from `Spirit/simulation/`)
