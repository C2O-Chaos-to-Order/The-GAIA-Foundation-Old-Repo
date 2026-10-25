# SIM-TR-PHI-C - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Fully templated instrument (a 1): advantage > 1 SD?

## Phase operationalization tested
PHI Transcendence = mystical experience: common core vs construction (P102). TRB adds P105's critique of mystical-experience measures.

## Sources this run draws on
P105 (Mosurinjohn, Roseman & Girn 2023, 'Psychedelic-induced mystical experiences: An interdisciplinary discussion and critique', Front Psychiatry 14:1077311, PMC10171200, CC BY 4.0; read in full in TRB): MEQ lineage from Stace and Pahnke's Mystical Consciousness Typology; perennialist and Christian bias; Pahnke: 4 of 10 psilocybin subjects vs no placebo subjects reached a 'complete mystical experience'; Taves's INOE and psychometric meta-data (US and India); Table 1 factor structures.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | w = 1 and no noise give template advantage 0 |
| H1 | hypothesis | a fully templated instrument (a 1) gives template advantage > 1 SD under constructivism |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-PHI-C",
 "iteration": 2,
 "kind": "instrument_bias",
 "seed": 42602,
 "T": 6,
 "M": 20,
 "F": 40,
 "K": 30,
 "reps": 200,
 "scenarios": {
  "a10": {
   "w": 0,
   "h": 0,
   "d": 0,
   "a": 1.0,
   "sigma": 1.0
  }
 },
 "hyps": [
  [
   "a fully templated instrument (a 1) gives template advantage > 1 SD under constructivism",
   "o['template_advantage']['a10'] > 1"
  ]
 ]
}
```

## Command
`python sim_phi.py iter-2` (run from `Philosophy-Spirituality/simulation/`)
