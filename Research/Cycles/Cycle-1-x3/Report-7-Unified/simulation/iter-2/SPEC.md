# SIM-R7-C1 - iteration 2 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Robustness of the cross-report argument: does the R1-R7 link graph stay connected when weaker links are removed?

## Refinement from previous iteration
Reads `../iter-1/outputs/results.json`.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| N1 | validation | connected with all links |
| N2 | hypothesis | connected without Philosophical/Spiritual and Hypothetical links |
| N3 | hypothesis | connected using only links whose basis is all Established |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Connectivity is a structural property only.

## Command
`python sim_r7.py iter-2` (run from `Report-7-Unified/simulation/`)
