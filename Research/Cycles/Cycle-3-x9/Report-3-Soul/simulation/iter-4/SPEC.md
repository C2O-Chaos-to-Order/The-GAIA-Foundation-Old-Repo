# SIM-R3-C3 - iteration 4 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Three-coder agreement on the sample.

## Refinement from previous iteration
Combines A, B, C.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H4 | hypothesis | Fleiss kappa >= 0.41 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Coder C is a lexicon rule designed by the same agent as coders A and B: a different-method check, not independent inter-rater reliability. Lexicon hits ignore negation and context. 15 conceptions; C07 has no window and C06 one (key terms rarely matched in those sources). Describes agreement about descriptions of doctrines only.

## Command
`python sim_r3.py iter-4` (run from `Report-3-Soul/simulation/`)
