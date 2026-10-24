# SIM-R7-C2 - iteration 3 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Structural parallel behind L01 (body - Earth regulation analogy): do the Cycle-2 body and Daisyworld toys show the same qualitative pattern (unbounded adaptation of the reference degrades regulation; bounded adaptation preserves it)?

## Refinement from previous iteration
Reads outputs of SIM-R1-C2 iteration 4 and SIM-R6-C2 iterations 1 and 6.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| PA1 | hypothesis | both patterns concordant |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Bookkeeping and graph checks only; they test the consistency of our own records, not any claim about the world. The R1 iteration was designed as an analogue of R6, so concordance is partly built in; the R1 bounded result is trivial (effector saturation).

## Command
`python sim_r7.py iter-3` (run from `Report-7-Unified/simulation/`)
