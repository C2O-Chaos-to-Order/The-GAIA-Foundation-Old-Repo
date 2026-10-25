# SIM-TR-HUM-C - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Pahnke-sized groups: how many of 10 are needed for two-sided Fisher p < .05?

## Phase operationalization tested
HUM Transcendence = the sublime and self-transcendence from nature vs art (P101). Cross-field: P105 (PHI).

## Sources this run draws on
P105 (Mosurinjohn, Roseman & Girn 2023, 'Psychedelic-induced mystical experiences: An interdisciplinary discussion and critique', Front Psychiatry 14:1077311, PMC10171200, CC BY 4.0; read in full in TRB): MEQ lineage from Stace and Pahnke's Mystical Consciousness Typology; perennialist and Christian bias; Pahnke: 4 of 10 psilocybin subjects vs no placebo subjects reached a 'complete mystical experience'; Taves's INOE and psychometric meta-data (US and India); Table 1 factor structures.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | Pahnke-sized groups (10 vs 10, none in placebo): at least 5 of 10 are needed for two-sided Fisher p < .05 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypergeometric arithmetic. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-HUM-C",
 "iteration": 6,
 "kind": "arith_audit",
 "seed": 42506,
 "items": [
  {
   "name": "fisher2_3of10_vs_0of10",
   "expr": "min(1, 2*comb(10,3)/comb(20,3))"
  },
  {
   "name": "fisher2_4of10_vs_0of10",
   "expr": "min(1, 2*comb(10,4)/comb(20,4))"
  },
  {
   "name": "fisher2_5of10_vs_0of10",
   "expr": "min(1, 2*comb(10,5)/comb(20,5))"
  },
  {
   "name": "fisher2_6of10_vs_0of10",
   "expr": "min(1, 2*comb(10,6)/comb(20,6))"
  },
  {
   "name": "fisher2_7of10_vs_0of10",
   "expr": "min(1, 2*comb(10,7)/comb(20,7))"
  }
 ],
 "hyps": [
  [
   "Pahnke-sized groups (10 vs 10, none in placebo): at least 5 of 10 are needed for two-sided Fisher p < .05",
   "o['items']['fisher2_4of10_vs_0of10']['value'] > 0.05 and o['items']['fisher2_5of10_vs_0of10']['value'] < 0.05"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-6` (run from `Humanities/simulation/`)
