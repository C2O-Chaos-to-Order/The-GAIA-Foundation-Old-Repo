# SIM-R7-C4 - iteration 6 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Carried item 'Body x Justice cell'.

## Refinement from previous iteration
Maps v3 matrix as baseline; no source targeted it successfully this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H6 | hypothesis | Body x Justice populated |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Bookkeeping and graph checks on our own records; they test consistency, not any claim about the world. Lens placement is a keyword rule by the same agent. Report 7's own C4 claims are excluded from inputs.

## Command
`python sim_r7.py iter-6` (run from `Report-7-Unified/simulation/`)
