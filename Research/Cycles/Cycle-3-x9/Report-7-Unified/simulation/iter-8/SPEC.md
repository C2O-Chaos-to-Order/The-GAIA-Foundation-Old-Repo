# SIM-R7-C3 - iteration 8 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
GAIA motherthread separability audit.

## Refinement from previous iteration
Audit.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H8 | hypothesis | no E link on PS/H claims |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Bookkeeping and graph checks on our own records; they test consistency, not any claim about the world. Lens hand coding is by the same agent that wrote the keyword rule.

## Command
`python sim_r7.py iter-8` (run from `Report-7-Unified/simulation/`)
