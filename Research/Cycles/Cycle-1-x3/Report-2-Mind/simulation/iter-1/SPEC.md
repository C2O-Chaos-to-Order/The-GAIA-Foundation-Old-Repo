# SIM-R2-C1 - iteration 1 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Rescorla-Wagner blocking over learning rate x pretraining amount: where does blocking (ratio < 0.1) fail?

## Refinement from previous iteration
First iteration of this cycle (builds on the Cycle-0 baseline simulation).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| W1 | validation | blocking ratio monotone non-increasing in n_pre at every alpha |
| W2 | hypothesis | blocking is not universal: it fails for weak pretraining |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Standard RW; one compound cue.

## Command
`python sim_r2.py iter-1` (run from `Report-2-Mind/simulation/`)
