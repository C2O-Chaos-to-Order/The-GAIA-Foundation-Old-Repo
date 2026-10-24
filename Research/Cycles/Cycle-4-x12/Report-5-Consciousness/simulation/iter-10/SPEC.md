# SIM-R5-C4 - iteration 10 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Translate m into an autocorrelation time, the quantity Y01 reports for cortex (100-2000 ms).

## Refinement from previous iteration
Analytic check only.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V3 | validation | m 0.984, 4 ms -> ~248 ms |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic; the 4 ms bin is an assumption for illustration.

## Command
`python sim_r5.py iter-10` (run from `Report-5-Consciousness/simulation/`)
