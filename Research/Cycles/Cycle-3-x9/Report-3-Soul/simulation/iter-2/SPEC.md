# SIM-R3-C3 - iteration 2 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Does a mechanical, blind coder agree with the Cycle-1 coding?

## Refinement from previous iteration
Coder C vs A on all 180 cells.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H2 | hypothesis | kappa >= 0.41 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Coder C is a lexicon rule designed by the same agent as coders A and B: a different-method check, not independent inter-rater reliability. Lexicon hits ignore negation and context. 15 conceptions; C07 has no window and C06 one (key terms rarely matched in those sources). Describes agreement about descriptions of doctrines only.

## Command
`python sim_r3.py iter-2` (run from `Report-3-Soul/simulation/`)
