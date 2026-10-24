# SIM-R2-C1 - iteration 3 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Refit the forgetting curves (S04 Table 3: Ebbinghaus 1885 and Murre & Dros 2015 savings) with leave-one-out CV and bootstrap, not AIC alone (C0 used AIC only).

## Refinement from previous iteration
Reads `../iter-2/outputs/results.json`.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| F1 | hypothesis | Ebbinghaus: exponential is not the best model by AIC or LOOCV |
| F3 | reporting | whether AIC and LOOCV agree per dataset |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Seven points per dataset; two-parameter forms only.

## Command
`python sim_r2.py iter-3` (run from `Report-2-Mind/simulation/`)
