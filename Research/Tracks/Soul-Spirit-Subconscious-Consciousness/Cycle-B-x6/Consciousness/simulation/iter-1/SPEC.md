# SIM-CONS-B - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
If up to one in four patients diagnosed with unresponsive wakefulness have covert consciousness (K30) and tests are imperfect, how likely is consciousness after a NEGATIVE test? (Bears on K30's 'presumption of consciousness'.)

## Sources this run draws on
K30 (Hawkins 2026): 'up to one in four'; K26 (Laigaard et al. 2026): detection varies by etiology and modality. Sensitivity grid and specificity (.95) are ILLUSTRATIVE.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | simulated = analytic |
| H1 | hypothesis | P(conscious|neg) >= .10 |
| R1 | reporting | by sensitivity |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Bayes' rule with assumed test characteristics; CMD is not identical to consciousness. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-CONS-B",
 "iteration": 1,
 "kind": "cmd_bayes",
 "seed": 411,
 "prevalence": 0.25,
 "specificity": 0.95,
 "sens_grid": [
  0.3,
  0.5,
  0.7,
  0.9
 ],
 "sens_test": 0.5,
 "N": 2000000
}
```

## Command
`python sim_cons.py iter-1` (run from `Consciousness/simulation/`)
