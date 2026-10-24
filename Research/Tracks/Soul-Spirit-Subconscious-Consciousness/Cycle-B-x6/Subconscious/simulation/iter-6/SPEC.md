# SIM-SUBC-B - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Could K23's pooled g = .32 for subliminal-to-brief affective priming arise from a much smaller true effect plus selective publication? (Counter-evidence check, not a claim that it did.)

## Sources this run draws on
K23 (g = 0.32; K23 reports its own publication-bias assessment, which this toy does not replicate); K08/K09 (replication and power problems in priming).

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | no selection recovers truth |
| H1 | hypothesis | selection yields naive >= .30 |
| R1 | reporting | SD |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Two-group designs (many priming studies are within-subject); selection rule illustrative. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SUBC-B",
 "iteration": 6,
 "kind": "selection_meta",
 "seed": 116,
 "g_true": 0.1,
 "tau": 0.1,
 "n_lo": 15,
 "n_hi": 40,
 "p_pub_ns": 0.15,
 "k_published": 60,
 "reps": 300,
 "h1_threshold": 0.3
}
```

## Command
`python sim_subc.py iter-6` (run from `Subconscious/simulation/`)
