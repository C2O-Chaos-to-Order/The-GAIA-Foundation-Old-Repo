# SIM-TR-HUM-B - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P105's report of Pahnke (4/10 vs 0/10 'complete mystical experience'): significant by Fisher's exact test?

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
| H1 | hypothesis | P105's report of Pahnke: 4 of 10 psilocybin vs 0 of 10 placebo subjects reaching a 'complete mystical experience' is not significant two-sided by Fisher's exact test (p > .05) |
| H2 | hypothesis | one-sided it is (p < .05) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypergeometric arithmetic; P105 does not report this test. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-HUM-B",
 "iteration": 5,
 "kind": "arith_audit",
 "seed": 41505,
 "items": [
  {
   "name": "fisher_one_sided_4of10_vs_0of10",
   "expr": "comb(10,4)*comb(10,0)/comb(20,4)"
  },
  {
   "name": "fisher_two_sided",
   "expr": "2*comb(10,4)*comb(10,0)/comb(20,4)"
  },
  {
   "name": "pct_complete_psilocybin",
   "expr": "100*4/10"
  }
 ],
 "hyps": [
  [
   "P105's report of Pahnke: 4 of 10 psilocybin vs 0 of 10 placebo subjects reaching a 'complete mystical experience' is not significant two-sided by Fisher's exact test (p > .05)",
   "o['items']['fisher_two_sided']['value'] > 0.05"
  ],
  [
   "one-sided it is (p < .05)",
   "o['items']['fisher_one_sided_4of10_vs_0of10']['value'] < 0.05"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-5` (run from `Humanities/simulation/`)
