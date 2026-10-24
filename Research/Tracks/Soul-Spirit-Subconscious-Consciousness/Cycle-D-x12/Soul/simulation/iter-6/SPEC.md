# SIM-SOUL-D - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K54 says hidden-target studies of out-of-body perception have rarely produced testable cases; K53 builds a scale for spontaneous cases instead. How many cardiac arrests would a hidden-target study need?

## Sources this run draws on
K54 (difficulties of laboratory target paradigms), K53 (case evaluation). Stage probabilities ILLUSTRATIVE: survival to interview 0.10, interviewable 0.5, OBE/visual recall 0.10, event in a room with a target 0.2, target in the reported field of view 0.2.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | sim P = .8 at N |
| H1 | hypothesis | N >= 1000 |
| R1 | reporting | N |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Product of independent stages; every stage value is illustrative and not from the sources. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SOUL-D",
 "iteration": 6,
 "kind": "veridical_yield",
 "seed": 1106,
 "stages": [
  0.1,
  0.5,
  0.1,
  0.2,
  0.2
 ],
 "power": 0.8,
 "reps": 200000,
 "h1": 1000
}
```

## Command
`python sim_soul.py iter-6` (run from `Soul/simulation/`)
