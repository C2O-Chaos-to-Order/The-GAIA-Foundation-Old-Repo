# SIM-SOUL-B - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Could a mortality-salience x norm interaction of g = .34 (K18, uncorrected) arise from a true mean of zero plus selective publication?

## Sources this run draws on
K18 (Schindler et al. 2023): g = 0.34 and bias-adjusted estimates that in several cases reach nonsignificance.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | no selection recovers truth |
| H1 | hypothesis | naive >= .30 |
| R1 | reporting | SD |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Main-effect two-group studies (K18 meta-analysed interactions); illustrative. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SOUL-B",
 "iteration": 6,
 "kind": "selection_meta",
 "seed": 216,
 "g_true": 0.0,
 "tau": 0.1,
 "n_lo": 15,
 "n_hi": 40,
 "p_pub_ns": 0.15,
 "k_published": 64,
 "reps": 300,
 "h1_threshold": 0.3
}
```

## Command
`python sim_soul.py iter-6` (run from `Soul/simulation/`)
