# SIM-AL-HUM-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P50's constant-rate language competition model (Eq. 4.4): with P50's reported prestige and transition rates for the four unequal-prestige cases, does the minority keep a positive equilibrium share, and is the prestige-weighted flow always minority-to-majority (even for Spanish-English, where P50 reports r12 < r21)? Comparator: P30's form, where the weaker group vanishes only if the exponent a >= 1.

## Phase operationalization tested
HUM Allegiance = language loyalty: speakers keeping (or shifting) their language under prestige pressure, with bilingualism as a buffer (P50).

## Sources this run draws on
P50 (Yang et al. 2025, Proc R Soc B 292:20251451, CC BY 4.0; read in full in AL0, SI not read): Eqs. 4.1-4.4, Table 1, reported s1, s2, r12, r21 per case. P30 (Abrams et al., read in full in INA): group-competition form with exponent a.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | minority equilibrium > 0.01 in every case |
| H2 | hypothesis | effective minority-to-majority rate larger |
| H3 | hypothesis | P30 form: coexistence for a < 1, extinction for a >= 1 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's simplification: P50's rates come from its model with bilinguals (Eq. 4.3) and are plugged into Eq. 4.4 without the bilingual group and with constant population; illustrative, not a re-fit. Smoke foreknowledge: equilibria 0.186 (Canada), 0.081 (USA); V1 failed at T = 500 because Scotland's rates are slow, so T was raised to 3000 (a numerical setting; no threshold changed). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AL-HUM-0",
 "iteration": 1,
 "kind": "language_markov",
 "seed": 24501,
 "dt": 0.01,
 "T": 3000,
 "T2": 2000,
 "cases": {
  "Canada": [
   0.177,
   0.5477,
   0.2343,
   0.1662
  ],
  "USA": [
   0.0691,
   1.2553,
   0.1067,
   0.1716
  ],
  "Wales": [
   0.013,
   0.1939,
   0.2137,
   0.0599
  ],
  "Scotland": [
   0.7911,
   0.9655,
   0.0113,
   0.0009
  ]
 },
 "u_x": 0.4,
 "a_values": [
  0.0,
  0.5,
  1.0,
  1.31
 ]
}
```

## Command
`python sim_hum.py iter-1` (run from `Humanities/simulation/`)
