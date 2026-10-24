# SIM-R4-C2 - iteration 6 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Consolidation: replicate iterations 2 and 3 with a new seed.

## Refinement from previous iteration
Replication.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V2 | validation | as iteration 2 |
| H1 | hypothesis | as iteration 2 |
| V3 | validation | as iteration 3 |
| V3b | validation | as iteration 3 |
| H2 | hypothesis | as iteration 3 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Synthetic linear-Gaussian (and one logistic) data with known truth; illustrates estimator behaviour only. Does not re-analyse S12 or any cohort, and says nothing about whether religious practice causes health effects.

## Command
`python sim_r4.py iter-6` (run from `Report-4-Spirit/simulation/`)
