# SIM-SPIRIT-C - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K43 reports high internal consistency for the mystical subscales (alpha/omega > .90) but only acceptable consistency (.70) for visual experience. How much does that alone lower correlations involving the visual scale?

## Sources this run draws on
K43 (Stocker et al. 2026): MEQ40 subscales alpha/omega > .90 (five of six); visual experience .70. True correlation .5 ILLUSTRATIVE. K45's r = .198 (spirituality-mindfulness) disattenuated with ASSUMED reliabilities .8.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | sim = analytic |
| H1 | hypothesis | loss >= .05 |
| R1 | reporting | disattenuated |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Classical test theory; alpha treated as reliability. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SPIRIT-C",
 "iteration": 3,
 "kind": "attenuation",
 "seed": 713,
 "N": 200000,
 "cases": {
  "visual_vs_mystical": [
   0.5,
   0.7,
   0.9
  ],
  "mystical_vs_mystical": [
   0.5,
   0.9,
   0.9
  ]
 },
 "test_case": "visual_vs_mystical",
 "observed": {
  "K45_spirituality_mindfulness": [
   0.198,
   0.8,
   0.8
  ]
 }
}
```

## Command
`python sim_spirit.py iter-3` (run from `Spirit/simulation/`)
