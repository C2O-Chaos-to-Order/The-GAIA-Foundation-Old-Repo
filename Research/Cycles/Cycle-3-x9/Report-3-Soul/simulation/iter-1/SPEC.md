# SIM-R3-C3 - iteration 1 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Code check and coverage report for coder C.

## Refinement from previous iteration
New for carried item 'R3 independent coder': an independent human coder could not be obtained, so a different-method coder is used and disclosed.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | reproduces C2 kappa |
| V2 | validation | Fleiss ~ Cohen on test table |
| C0 | reporting | low-coverage conceptions |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Coder C is a lexicon rule designed by the same agent as coders A and B: a different-method check, not independent inter-rater reliability. Lexicon hits ignore negation and context. 15 conceptions; C07 has no window and C06 one (key terms rarely matched in those sources). Describes agreement about descriptions of doctrines only.

## Command
`python sim_r3.py iter-1` (run from `Report-3-Soul/simulation/`)
