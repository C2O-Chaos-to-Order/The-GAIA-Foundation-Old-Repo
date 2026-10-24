# SIM-R6-C2 - iteration 2 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Test the Lenton & Lovelock 2000 (W03) / 2001 (W01 sec. 6.3) design claim: bounds on adaptation plus growth limitation near the bounds recover regulation.

## Refinement from previous iteration
Uses the worst (most regulation-destroying) rate found in iteration 1 (`worst_rate`), so the constraint is tested where unconstrained adaptation does most damage.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| LL1 | hypothesis | every bounded+costed setting keeps >= 0.8x non-adapting band |
| LL2 | hypothesis | Spearman rho(bound, width) < 0 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Our own re-implementation of the published designs from their verbal descriptions (W01 full text; W02, W03 abstracts only). Parable model; no claim about the real Earth.

## Command
`python sim_r6.py iter-2` (run from `Report-6-Earth/simulation/`)
