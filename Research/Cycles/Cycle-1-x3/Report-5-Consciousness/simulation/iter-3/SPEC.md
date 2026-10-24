# SIM-R5-C1 - iteration 3 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Two-area toy (local sensory area L with recurrence, global area G): does 'local recurrence without global ignition' (an RPT-like state, V19) occur for coupling > 0, and how does global ignition depend on coupling?

## Refinement from previous iteration
Reads `../iter-2/outputs/results.json`.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| A1 | hypothesis | a local-only regime exists for some coupling |
| A2 | validation | global ignition non-decreasing in coupling |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Shows the two signatures are dissociable in a toy; says nothing about which accompanies experience.

## Command
`python sim_r5.py iter-3` (run from `Report-5-Consciousness/simulation/`)
