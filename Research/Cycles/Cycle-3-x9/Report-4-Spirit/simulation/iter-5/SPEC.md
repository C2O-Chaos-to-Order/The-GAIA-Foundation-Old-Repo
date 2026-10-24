# SIM-R4-C3 - iteration 5 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Challenge: could residual 'healthy attender' selection (people in poor health attend less and die more) alone produce S12's estimate?

## Refinement from previous iteration
Pre-declared scenarios of residual poor-health prevalence and risk.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H5 | hypothesis | some scenario explains it away |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic on published estimates (S12) with S14's formulas, plus synthetic cohorts; no individual data. E-values bound confounding by one binary-equivalent confounder; they neither prove nor exclude causation. Spiritual meaning is not measured.

## Command
`python sim_r4.py iter-5` (run from `Report-4-Spirit/simulation/`)
