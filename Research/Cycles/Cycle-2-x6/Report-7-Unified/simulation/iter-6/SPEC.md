# SIM-R7-C2 - iteration 6 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Whole-ledger audit for Cycle 2.

## Refinement from previous iteration
Final consistency gate.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| AU1 | validation | references resolve |
| AU2 | validation | 'not supported' wording |
| AU3 | validation | full-text rule |
| AU4 | validation | no empty limits |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Bookkeeping and graph checks only; they test the consistency of our own records, not any claim about the world.

## Command
`python sim_r7.py iter-6` (run from `Report-7-Unified/simulation/`)
