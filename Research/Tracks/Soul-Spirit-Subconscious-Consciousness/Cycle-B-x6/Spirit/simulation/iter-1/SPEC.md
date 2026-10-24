# SIM-SPIRIT-B - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K19 reports a 13% protective association (RR 0.87) between spirituality and harmful drug use from longitudinal observational studies. How strong would an unmeasured confounder have to be to explain it away?

## Sources this run draws on
K19 (Koh et al. 2026, JAMA Psychiatry): 55 studies, RR 0.87 (95% CI 0.84-0.91).

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | worked example |
| V2 | validation | bias factor identity |
| H1 | hypothesis | E-value < 2 |
| R1 | reporting | CI E-value |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
E-value is a sensitivity summary, not evidence that confounding exists; treats RR as approximately a risk ratio.

## Parameters
```json
{
 "sim_id": "SIM-SPIRIT-B",
 "iteration": 1,
 "kind": "evalue",
 "seed": 311,
 "rr": 0.87,
 "ci_upper": 0.91
}
```

## Command
`python sim_spirit.py iter-1` (run from `Spirit/simulation/`)
