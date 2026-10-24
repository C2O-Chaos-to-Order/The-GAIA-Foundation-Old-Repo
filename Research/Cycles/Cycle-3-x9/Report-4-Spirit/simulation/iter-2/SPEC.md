# SIM-R4-C3 - iteration 2 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
S12 has 18% cumulative mortality; S14 advises an approximation for common outcomes. How much does the E-value change?

## Refinement from previous iteration
Applies S14's HR approximation.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H2 | hypothesis | E-value still >= 1.5 |
| H2r | reporting | drop |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic on published estimates (S12) with S14's formulas, plus synthetic cohorts; no individual data. E-values bound confounding by one binary-equivalent confounder; they neither prove nor exclude causation. Spiritual meaning is not measured.

## Command
`python sim_r4.py iter-2` (run from `Report-4-Spirit/simulation/`)
