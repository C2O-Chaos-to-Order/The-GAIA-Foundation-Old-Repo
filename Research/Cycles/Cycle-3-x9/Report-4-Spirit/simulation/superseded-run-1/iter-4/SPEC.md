# SIM-R4-C3 - iteration 4 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Tipping-point curve: which combinations of confounder strengths would explain the association away?

## Refinement from previous iteration
Full curve instead of the single E-value.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H4 | hypothesis | RR_EU 1.5 needs RR_UD >= 3 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic on published estimates (S12) with S14's formulas, plus synthetic cohorts; no individual data. E-values bound confounding by one binary-equivalent confounder; they neither prove nor exclude causation. Spiritual meaning is not measured.

## Command
`python sim_r4.py iter-4` (run from `Report-4-Spirit/simulation/`)
