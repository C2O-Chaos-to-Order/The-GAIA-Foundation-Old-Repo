# SIM-R7-C1 - iteration 3 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Mechanical rejection screen: for every link, do its Cycle-1 simulation tests or contested basis claims trigger its rejection criterion?

## Refinement from previous iteration
Reads `../iter-2/outputs/results.json`.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| J1 | validation | every Plausible/Hypothetical link names a rejection criterion and a Cycle-1 test |
| J2 | reporting | links under pressure |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
A screen, not a judgement; flagged links are discussed in REPORT.md.

## Command
`python sim_r7.py iter-3` (run from `Report-7-Unified/simulation/`)
