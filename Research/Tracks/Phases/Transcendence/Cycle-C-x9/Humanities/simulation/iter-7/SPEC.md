# SIM-TR-HUM-C - iteration 7 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Pahnke with one placebo case (4/10 vs 1/10): one-sided Fisher p above .05?

## Phase operationalization tested
HUM Transcendence = the sublime and self-transcendence from nature vs art (P101).

## Sources this run draws on
P105 (Mosurinjohn, Roseman & Girn 2023, 'Psychedelic-induced mystical experiences: An interdisciplinary discussion and critique', Front Psychiatry 14:1077311, PMC10171200, CC BY 4.0; read in full in TRB): MEQ lineage from Stace and Pahnke's Mystical Consciousness Typology; perennialist and Christian bias; Pahnke: 4 of 10 psilocybin subjects vs no placebo subjects reached a 'complete mystical experience'; Taves's INOE and psychometric meta-data (US and India); Table 1 factor structures.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | if one placebo subject had qualified (4/10 vs 1/10), one-sided Fisher p would exceed .05 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Counterfactual arithmetic. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-HUM-C",
 "iteration": 7,
 "kind": "arith_audit",
 "seed": 42507,
 "items": [
  {
   "name": "fisher1_4of10_vs_1of10",
   "expr": "sum(comb(10,k)*comb(10,5-k) for k in range(4,6))/comb(20,5)"
  },
  {
   "name": "fisher1_6of10_vs_1of10",
   "expr": "sum(comb(10,k)*comb(10,7-k) for k in range(6,8))/comb(20,7)"
  }
 ],
 "hyps": [
  [
   "if one placebo subject had qualified (4/10 vs 1/10), one-sided Fisher p would exceed .05",
   "o['items']['fisher1_4of10_vs_1of10']['value'] > 0.05"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-7` (run from `Humanities/simulation/`)
