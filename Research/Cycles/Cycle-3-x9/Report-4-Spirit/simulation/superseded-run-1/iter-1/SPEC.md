# SIM-R4-C3 - iteration 1 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Code check: reproduce S12's own E-values and the bound's defining properties.

## Refinement from previous iteration
New simulation for carried item 'R4 sensitivity analysis calibrated to S12'.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | reproduces 2.35 / 2.16 |
| V2 | validation | B(E,E) = RR |
| V3 | validation | binary bias attains bound |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic on published estimates (S12) with S14's formulas, plus synthetic cohorts; no individual data. E-values bound confounding by one binary-equivalent confounder; they neither prove nor exclude causation. Spiritual meaning is not measured.

## Command
`python sim_r4.py iter-1` (run from `Report-4-Spirit/simulation/`)
