# SIM-R7-C4 - iteration 3 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Carried item 'a causal design that could give Report 2 an Established link': does Y06 do it?

## Refinement from previous iteration
New link L28 (Plausible, basis C4-R2-01).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H3 | hypothesis | R2 has an E link to another report |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Bookkeeping and graph checks on our own records; they test consistency, not any claim about the world. Lens placement is a keyword rule by the same agent. Report 7's own C4 claims are excluded from inputs.

## Command
`python sim_r7.py iter-3` (run from `Report-7-Unified/simulation/`)
