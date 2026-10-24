# SIM-R7-C2 - iteration 5 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Cycle-1 -> Cycle-2 ledger transition, including a diminishing-returns probe (share of carried claims whose label or status changed).

## Refinement from previous iteration
Ledger-level summary after iterations 1-4.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| T0 | validation | no claim lost |
| T1 | hypothesis | <= 5% of carried claims changed |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Bookkeeping and graph checks only; they test the consistency of our own records, not any claim about the world.

## Command
`python sim_r7.py iter-5` (run from `Report-7-Unified/simulation/`)
