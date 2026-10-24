# SIM-R1-C1 - iteration 3 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Core/shell thermal toy: a skin (shell) signal used as feedforward for core regulation, the structure OpenStax describes (V06: hypothalamic thermostat, skin and core). Robustness to +/-50% parameter perturbation.

## Refinement from previous iteration
Reads `../iter-2/outputs/results.json`.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| T1 | hypothesis | skin-signal feedforward lowers peak core deviation vs feedback only |
| T2 | validation | integral action returns core to set point while P-only leaves a residual |
| T3 | hypothesis | feedforward benefit robust to +/-50% parameter perturbation (peak ratio < 1 in >= 95% of draws) |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Two-compartment toy with arbitrary units; not a physiological thermoregulation model.

## Command
`python sim_r1.py iter-3` (run from `Report-1-Body/simulation/`)
