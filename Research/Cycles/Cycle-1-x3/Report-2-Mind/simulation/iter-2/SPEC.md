# SIM-R2-C1 - iteration 2 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Challenge pass: a known failure of Rescorla-Wagner is latent inhibition (pre-exposure slows later learning). Compare RW with a Pearce-Hall-type associability model.

## Refinement from previous iteration
Reads `../iter-1/outputs/results.json`.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| L1 | validation | RW predicts no latent inhibition (acquisition ratio exactly 1) |
| L2 | hypothesis | Pearce-Hall-type associability decay gives latent inhibition (ratio < 0.9) |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Our simplified Pearce-Hall variant (associability decays with |prediction error|); not a fit to data.

## Command
`python sim_r2.py iter-2` (run from `Report-2-Mind/simulation/`)
