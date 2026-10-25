# SIM-TR-HUM-B - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
n 10 (Pahnke's group size): can t 3.0 give BF01 below 1/10?

## Phase operationalization tested
HUM Transcendence = the sublime and self-transcendence from nature vs art (P101).

## Sources this run draws on
P105 (Mosurinjohn, Roseman & Girn 2023, 'Psychedelic-induced mystical experiences: An interdisciplinary discussion and critique', Front Psychiatry 14:1077311, PMC10171200, CC BY 4.0; read in full in TRB): MEQ lineage from Stace and Pahnke's Mystical Consciousness Typology; perennialist and Christian bias; Pahnke: 4 of 10 psilocybin subjects vs no placebo subjects reached a 'complete mystical experience'; Taves's INOE and psychometric meta-data (US and India); Table 1 factor structures.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | the JZS mixing density integrates to 1 |
| H1 | hypothesis | n 10: even t 3.0 gives BF01 above 1/10 (small samples cannot give strong evidence at moderate t) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
JZS. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-HUM-B",
 "iteration": 6,
 "kind": "jzs_bf_audit",
 "seed": 41506,
 "items": [
  {
   "name": "t2.0",
   "t": 2.0,
   "n": 10
  },
  {
   "name": "t2.25",
   "t": 2.25,
   "n": 10
  },
  {
   "name": "t2.5",
   "t": 2.5,
   "n": 10
  },
  {
   "name": "t2.75",
   "t": 2.75,
   "n": 10
  },
  {
   "name": "t3.0",
   "t": 3.0,
   "n": 10
  },
  {
   "name": "t3.5",
   "t": 3.5,
   "n": 10
  }
 ],
 "scales": [
  0.707
 ],
 "hyps": [
  [
   "n 10: even t 3.0 gives BF01 above 1/10 (small samples cannot give strong evidence at moderate t)",
   "o['items']['t3.0']['0.707']['BF01'] > 0.1"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-6` (run from `Humanities/simulation/`)
