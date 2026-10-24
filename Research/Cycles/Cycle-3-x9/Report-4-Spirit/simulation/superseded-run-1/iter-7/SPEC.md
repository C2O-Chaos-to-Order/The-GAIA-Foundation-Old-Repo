# SIM-R4-C3 - iteration 7 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
X11 (Sweden) found the association disappeared after adjusting for social participation. Does that show confounding?

## Refinement from previous iteration
Two synthetic DAGs.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H7 | hypothesis | attenuation >= 80% under both DAGs |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic on published estimates (S12) with S14's formulas, plus synthetic cohorts; no individual data. E-values bound confounding by one binary-equivalent confounder; they neither prove nor exclude causation. Spiritual meaning is not measured.

## Command
`python sim_r4.py iter-7` (run from `Report-4-Spirit/simulation/`)
