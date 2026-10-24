# SIM-R4-C3 - iteration 8 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Sensitivity of the E-value to how 'common' the outcome is, using an exact proportional-hazards conversion.

## Refinement from previous iteration
Compares rare formula, S14 approximation and exact conversion.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H8 | hypothesis | exact within 0.1 of approximation at p0 ~ 0.2 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic on published estimates (S12) with S14's formulas, plus synthetic cohorts; no individual data. E-values bound confounding by one binary-equivalent confounder; they neither prove nor exclude causation. Spiritual meaning is not measured.

## Command
`python sim_r4.py iter-8` (run from `Report-4-Spirit/simulation/`)
