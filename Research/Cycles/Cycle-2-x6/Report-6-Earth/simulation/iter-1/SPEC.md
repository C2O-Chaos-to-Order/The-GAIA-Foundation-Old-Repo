# SIM-R6-C2 - iteration 1 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Replicate the Cycle-1 toy exactly, then test the Robertson & Robinson 1998 (W02) design claim over a finer grid of adaptation rates: unconstrained adaptation of optimum temperature erodes regulation.

## Refinement from previous iteration
First iteration of Cycle 2. Carries the Cycle-1 finding A1 'Not supported' (unbounded width 0.19 vs 0.82) as the expected replication target.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| R0 | validation | widths equal Cycle-1 values [0.82, 0.19] |
| U1 | hypothesis | every positive rate gives band < 0.8x non-adapting |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Our own re-implementation of the published designs from their verbal descriptions (W01 full text; W02, W03 abstracts only). Parable model; no claim about the real Earth.

## Command
`python sim_r6.py iter-1` (run from `Report-6-Earth/simulation/`)
