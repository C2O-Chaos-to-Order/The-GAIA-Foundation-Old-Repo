# SIM-TR-PHI-D - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Template a 0.05: advantage > 0.5 SD?

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
| H1 | hypothesis | a slight template (a 0.05) already gives a template advantage > 0.5 SD (TRC saturation) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-PHI-D",
 "iteration": 1,
 "kind": "instrument_bias",
 "seed": 43601,
 "T": 6,
 "M": 20,
 "F": 40,
 "K": 30,
 "reps": 200,
 "scenarios": {
  "a05": {
   "w": 0,
   "h": 0,
   "d": 0,
   "a": 0.05,
   "sigma": 1.0
  },
  "a0": {
   "w": 0,
   "h": 0,
   "d": 0,
   "a": 0.0,
   "sigma": 1.0
  }
 },
 "hyps": [
  [
   "a slight template (a 0.05) already gives a template advantage > 0.5 SD (TRC saturation)",
   "o['template_advantage']['a05'] > 0.5"
  ]
 ]
}
```

## Command
`python sim_phi.py iter-1` (run from `Philosophy-Spirituality/simulation/`)
