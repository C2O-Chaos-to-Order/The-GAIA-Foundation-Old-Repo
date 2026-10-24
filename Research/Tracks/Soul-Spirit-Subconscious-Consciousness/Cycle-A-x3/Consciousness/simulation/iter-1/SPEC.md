# SIM-CONS-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K13 argues that no-report paradigms remove report-related late PFC activity but that PFC activity on visible trials may still cross a reportability threshold, so no-report data need not refute cognitive theories. Check the logic in a minimal threshold toy.

## Sources this run draws on
K13 (Whyte, Hohwy & Smith 2022). This toy is NOT K13's active-inference model; it only tests whether the qualitative pattern follows from 'gating + report demand'.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | g = 0, no report: contrast ~ 0 |
| H1 | hypothesis | no-report reduces contrast >= 50% |
| H2 | hypothesis | no-report: >= 80% of visible trials above tau |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
The outcome follows from the assumed g, r and tau; this shows logical compatibility, not evidence about brains. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-CONS-A",
 "iteration": 1,
 "kind": "report_confound",
 "seed": 401,
 "trials": 20000,
 "stim": 0.0,
 "theta": 0.0,
 "g": 1.0,
 "r": 1.5,
 "noise": 0.5,
 "tau": 0.5
}
```

## Command
`python sim_cons.py iter-1` (run from `Consciousness/simulation/`)
