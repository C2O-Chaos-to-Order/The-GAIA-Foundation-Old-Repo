# SIM-CV-PHI-D - iteration 9 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Null control for the instrument toy.

## Phase operationalization tested
PHI Convergence = convergence of traditions on a common core of mystical experience (P81, P83, P84).

## Sources this run draws on
P84 (Mosurinjohn, Roseman & Girn 2023, Frontiers in Psychiatry 14:1077311, PMC10171200, CC BY 4.0; read in full in CVD): the MEQ descends from Pahnke's typology built on Stace's perennialist 'common core' and imports its assumptions; Taves' item-level validation found mysticism-scale items inconsistently interpreted across US and Indian samples.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | instrument false-positive rate near 0.05 when measured dimensions do not differ |
| H1 | hypothesis | no differences anywhere: unmeasured dimensions significant in at most 10% of studies |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds/options in CVD (stats_audit, instrument_core, levelling_voter bias_mode=selection) were smoke-tested once at trivial size (seed 99, temporary directory, nothing kept) with printed values suppressed; existing kinds were not smoke-tested. CVC results were known when these hypotheses were written (replications say so).

## Parameters
```json
{
 "sim_id": "SIM-CV-PHI-D",
 "iteration": 9,
 "kind": "instrument_core",
 "seed": 33609,
 "T": 9,
 "D": 6,
 "m": 3,
 "n": 45,
 "reps": 300,
 "delta": 0.0,
 "hyps": [
  [
   "no differences anywhere: unmeasured dimensions significant in at most 10% of studies",
   "o['frac_sig_unmeasured'] <= 0.1"
  ]
 ]
}
```

## Command
`python sim_phi.py iter-9` (run from `Philosophy-Spirituality/simulation/`)
