# SIM-SOUL-D - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K61 (the primary 24-country continuity study behind K01) reports continuity judgments for 16.1% of bodily and 47.4% of mental states, 61.0% judging at least one state to continue and 2.0% all six. Do these shares fit independent item responses, or do judgments cluster within persons?

## Sources this run draws on
K61 (Hoogeveen et al., preprint): 'Pattern of Continuity Judgments' paragraph (31.8%, 16.1%, 47.4%, 61.0%, 2.0%).

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | sim P(any) = analytic |
| H1 | hypothesis | independence over-predicts P(>=1) by >= .20 |
| H2 | hypothesis | two-class model under-predicts all-six by factor >= 2 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Item probabilities are sample averages across 24 countries; per-item rates within the bodily and mental sets are assumed equal. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SOUL-D",
 "iteration": 1,
 "kind": "continuity_dependence",
 "seed": 1101,
 "p_bodily": 0.161,
 "p_mental": 0.474,
 "n_items_each": 3,
 "share_any_reported": 0.61,
 "share_all_reported": 0.02,
 "h1_gap": 0.2,
 "n": 500000
}
```

## Command
`python sim_soul.py iter-1` (run from `Soul/simulation/`)
