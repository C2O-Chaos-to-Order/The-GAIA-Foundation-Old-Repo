# SIM-R4-C3 - iteration 3 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Check the arithmetic in a synthetic S12-sized cohort with no true effect.

## Refinement from previous iteration
Simulation check of the iteration-2 bound.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H3 | hypothesis | observed RR within 5% of target |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic on published estimates (S12) with S14's formulas, plus synthetic cohorts; no individual data. E-values bound confounding by one binary-equivalent confounder; they neither prove nor exclude causation. Spiritual meaning is not measured.

## Command
`python sim_r4.py iter-3` (run from `Report-4-Spirit/simulation/`)
