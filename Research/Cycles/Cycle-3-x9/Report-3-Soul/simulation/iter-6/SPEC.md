# SIM-R3-C3 - iteration 6 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Sensitivity of coder C to window size.

## Refinement from previous iteration
300/600/1200 characters.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H6 | hypothesis | kappa range < 0.1 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Coder C is a lexicon rule designed by the same agent as coders A and B: a different-method check, not independent inter-rater reliability. Lexicon hits ignore negation and context. 15 conceptions; C07 has no window and C06 one (key terms rarely matched in those sources). Describes agreement about descriptions of doctrines only.

## Command
`python sim_r3.py iter-6` (run from `Report-3-Soul/simulation/`)
