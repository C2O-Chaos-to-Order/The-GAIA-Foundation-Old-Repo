# SIM-R4-C3 - iteration 6 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Many weak confounders instead of one strong one.

## Refinement from previous iteration
Multiplicative worst-case bias.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H6 | hypothesis | <= 5 weak confounders suffice |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic on published estimates (S12) with S14's formulas, plus synthetic cohorts; no individual data. E-values bound confounding by one binary-equivalent confounder; they neither prove nor exclude causation. Spiritual meaning is not measured.

## Command
`python sim_r4.py iter-6` (run from `Report-4-Spirit/simulation/`)
