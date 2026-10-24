# SIM-R7-C3 - iteration 1 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Code checks: strict rule reproduces Cycle 2; essential-claim definition on toy links.

## Refinement from previous iteration
Carried item 'define essential basis claims' (definition pre-registered in the script docstring and this SPEC: a basis claim is essential if it is the only one from its endpoint report, or the only one of the link).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | reproduces C2 downgrades |
| V2 | validation | essential definition on toys |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Bookkeeping and graph checks on our own records; they test consistency, not any claim about the world. Lens hand coding is by the same agent that wrote the keyword rule.

## Command
`python sim_r7.py iter-1` (run from `Report-7-Unified/simulation/`)
