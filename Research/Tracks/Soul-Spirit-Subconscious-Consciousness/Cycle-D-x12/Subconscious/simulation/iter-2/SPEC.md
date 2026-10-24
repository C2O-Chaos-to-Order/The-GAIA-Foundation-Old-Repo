# SIM-SUBC-D - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Mind x Justice. K56 argues implicit race bias predicts behaviour while noting the attitude-behaviour link is marred by poor-quality studies. Can a small individual-level association still produce sizeable group disparities when applied at scale?

## Sources this run draws on
K56 (implicit bias, 'with or without awareness', control implies responsibility; attitude-behaviour link of uncertain size). Shift giving r of about 0.1 and top-10% selection are ILLUSTRATIVE.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | no shift: ratio 1 |
| H1 | hypothesis | ratio >= 1.2 |
| R1 | reporting | r, ratio |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
One decision per person; no accumulation over repeated decisions. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SUBC-D",
 "iteration": 2,
 "kind": "aggregate_disparity",
 "seed": 1302,
 "n": 1000000,
 "r_shift": 0.2,
 "top": 0.1,
 "h1": 1.2
}
```

## Command
`python sim_subc.py iter-2` (run from `Subconscious/simulation/`)
