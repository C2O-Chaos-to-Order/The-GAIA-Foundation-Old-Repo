# SIM-SUBC-B - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Redo of SIM-SUBC-A iteration 2 with the design flaw fixed: latent conscious knowledge is non-negative (zero = no knowledge), so 'below chance' on the awareness test can only arise from measurement error. Does a post-hoc 'unaware' subgroup still show priming that is entirely carried by conscious knowledge?

## Sources this run draws on
K09 (awareness tests are insensitive); K25 (Jimenez et al. 2025: objective vs subjective awareness measures, regression-based approaches to post-hoc selection). The selection mechanism is regression to the mean, modelled here.

## Refinement from previous iteration
Cycle A iteration 2 let knowledge be negative, so the 'below chance' subgroup had below-average knowledge (design artefact, disclosed). Knowledge is now Gamma(2, mu/2) >= 0.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | knowledge non-negative |
| V2 | validation | b = 0 rate <= 0.08 |
| H1 | hypothesis | b = 0.4: selected 'unaware' subgroup significant in >= 50% |
| R1 | reporting | true knowledge of the selected subgroup |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Gamma-distributed knowledge, linear priming, one awareness measure with normal error. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SUBC-B",
 "iteration": 1,
 "kind": "posthoc_unaware_nonneg",
 "seed": 111,
 "mu": 0.5,
 "shape": 2.0,
 "reliability": 0.5,
 "N": 100,
 "cut": 0.0,
 "b_list": [
  0.0,
  0.2,
  0.4
 ],
 "alpha": 0.05,
 "reps": 4000
}
```

## Command
`python sim_subc.py iter-1` (run from `Subconscious/simulation/`)
