# SIM-R4-C2 - iteration 4 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Scale dependence: S12 computed PM on the risk-difference scale. How far does a PM from the odds-ratio difference method depart when the outcome is common vs rare?

## Refinement from previous iteration
Moves from continuous (iterations 1-3) to binary outcomes.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H3 | hypothesis | common outcome: |gap| >= 0.05 |
| H3b | hypothesis | rare outcome: |gap| <= 0.05 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Synthetic linear-Gaussian (and one logistic) data with known truth; illustrates estimator behaviour only. Does not re-analyse S12 or any cohort, and says nothing about whether religious practice causes health effects.

## Command
`python sim_r4.py iter-4` (run from `Report-4-Spirit/simulation/`)
