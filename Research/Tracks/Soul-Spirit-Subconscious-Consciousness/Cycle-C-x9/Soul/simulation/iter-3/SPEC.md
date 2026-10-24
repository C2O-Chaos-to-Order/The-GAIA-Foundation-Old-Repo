# SIM-SOUL-C - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K46 found Chinese cultural motifs in 4 of 23 NDE narratives and 1 of 25 NDE-like narratives. Could a design of this size detect such a difference?

## Sources this run draws on
K46 (Xue et al. 2026): 4/23 vs 1/25; 63 participants, online convenience sample, self-report classification.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | Fisher identity |
| H1 | hypothesis | power < .5 |
| R1 | reporting | observed p; power by n |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Treats the observed proportions as true. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SOUL-C",
 "iteration": 3,
 "kind": "fisher_small",
 "seed": 613,
 "g1": [
  4,
  23
 ],
 "g2": [
  1,
  25
 ],
 "alpha": 0.05,
 "reps": 4000,
 "n_grid": [
  50,
  100,
  200
 ]
}
```

## Command
`python sim_soul.py iter-3` (run from `Soul/simulation/`)
