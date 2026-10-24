# SIM-R7-C2 - iteration 1 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Apply the stricter Established-link rule pre-registered in Cycle 1 to the 24 links, using the Cycle-2 ledger; answer the Cycle-1 open question whether Report 2 keeps an Established link.

## Refinement from previous iteration
Cycle 1 retained L04, L08, L16 as Established with reasons and pre-registered this rule for Cycle 2. 'Essential' basis claims are not defined, so the strict reading (every basis claim) is applied.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| SR0 | validation | rule on toy cases |
| SR1 | reporting | downgrades |
| SR2 | hypothesis | R2 keeps >= 1 Established link |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Bookkeeping and graph checks only; they test the consistency of our own records, not any claim about the world.

## Command
`python sim_r7.py iter-1` (run from `Report-7-Unified/simulation/`)
