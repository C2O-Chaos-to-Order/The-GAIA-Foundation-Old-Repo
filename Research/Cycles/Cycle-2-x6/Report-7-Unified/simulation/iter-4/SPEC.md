# SIM-R7-C2 - iteration 4 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Audit the written Cycle-2 link register against the iteration-1 rule output and the executed checks.

## Refinement from previous iteration
Checks that the register was written from iteration 1 without hand edits to labels.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| RC1 | validation | labels match rule |
| RC2 | validation | c2_sim_checks resolve |
| RC3 | validation | claim ids exist |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Bookkeeping and graph checks only; they test the consistency of our own records, not any claim about the world.

## Command
`python sim_r7.py iter-4` (run from `Report-7-Unified/simulation/`)
