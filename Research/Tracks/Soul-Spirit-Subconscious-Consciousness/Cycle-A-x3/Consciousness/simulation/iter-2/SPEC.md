# SIM-CONS-A - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Context for K14's 12-factor solution (92 items, 1,403 respondents): how many factors would common retention rules return if the items had NO structure?

## Sources this run draws on
K14 (Gamma & Metzinger 2021): 92 items, 1,403 usable responses, 12 factors explaining 44% of variance. K14's own retention procedure is not re-run (raw data not used).

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | parallel analysis retains 0 factors in >= 90% of null replications |
| H1 | hypothesis | Kaiser rule retains >= 10 spurious factors |
| R1 | reporting | Marchenko-Pastur edge |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Normal items, Pearson correlations, principal components. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-CONS-A",
 "iteration": 2,
 "kind": "kaiser_null",
 "seed": 402,
 "p": 92,
 "n": 1403,
 "reps": 20,
 "n_null": 20,
 "q": 0.95
}
```

## Command
`python sim_cons.py iter-2` (run from `Consciousness/simulation/`)
