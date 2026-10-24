# SIM-R3-C3 - iteration 5 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Which attributes can a lexicon capture at all?

## Refinement from previous iteration
Per-attribute A vs C.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H5 | hypothesis | >= 6 of 12 attributes with kappa >= 0.2 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Coder C is a lexicon rule designed by the same agent as coders A and B: a different-method check, not independent inter-rater reliability. Lexicon hits ignore negation and context. 15 conceptions; C07 has no window and C06 one (key terms rarely matched in those sources). Describes agreement about descriptions of doctrines only.

## Command
`python sim_r3.py iter-5` (run from `Report-3-Soul/simulation/`)
