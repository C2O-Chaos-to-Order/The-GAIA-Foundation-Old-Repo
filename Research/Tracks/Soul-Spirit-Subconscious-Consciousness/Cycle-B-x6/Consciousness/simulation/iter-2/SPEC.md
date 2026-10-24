# SIM-CONS-B - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K26 reports odds ratios for CMD detection by etiology and diagnosis. What do they mean as detection rates and risk ratios at plausible baselines?

## Sources this run draws on
K26: OR anoxic 0.35, cerebrovascular 0.51, MCS- vs UWS 1.50 (multivariable). Baselines ILLUSTRATIVE.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | back-conversion |
| H1 | hypothesis | RR differs from OR by > .05 |
| R1 | reporting | rates |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Applies multivariable ORs to a single baseline (ignores covariate mix).

## Parameters
```json
{
 "sim_id": "SIM-CONS-B",
 "iteration": 2,
 "kind": "or_to_rates",
 "seed": 412,
 "odds_ratios": {
  "anoxic": 0.35,
  "cerebrovascular": 0.51,
  "mcs_minus": 1.5
 },
 "baseline_grid": [
  0.1,
  0.25,
  0.4
 ],
 "baseline_test": 0.25
}
```

## Command
`python sim_cons.py iter-2` (run from `Consciousness/simulation/`)
