# SIM-TR-HUM-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P101's Table 2: do Cohen's d and p follow from t(49), does t's sign match art minus nature, are means, SDs and t mutually consistent (implied correlation in [-1, 1]), and do the BF01 values support the text's 'strong evidence' wording?

## Phase operationalization tested
HUM Transcendence = the sublime and self-transcendence elicited by nature versus art (VR study; P101).

## Sources this run draws on
P101 (Chirico, Clewis, Yaden & Gaggioli 2021, 'Nature versus art as elicitors of the sublime: A virtual reality study', PLoS One, PMC7984734, CC BY 4.0; read in full in TR0): within-subject VR, n 50 (39 women); eight sublime dimensions (incl. self-transcendence, vastness, existential danger); Table 2 means, SDs, t(49), p, Cohen's d, BF01; text calls vastness and danger 'strong evidence for H 1'.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | Cohen's d equals t/sqrt(50) within 0.001 for all eight sublime dimensions |
| H2 | hypothesis | two-sided p from t with 49 df reproduces the printed p within 0.005 for all eight (danger's '.000' read as < 0.0005) |
| H3 | hypothesis | t has the sign of (art mean - nature mean) for all eight dimensions |
| H4 | hypothesis | printed means, SDs and t imply a between-condition correlation within [-1, 1] for every dimension |
| H5 | hypothesis | Table 2's BF01 for vastness and for existential danger are both below 1/3, as the text's 'strong evidence for H 1' for both requires |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic arithmetic audit; d = t/sqrt(n) for paired designs; implied correlation from the paired-difference SD. Foreknowledge: hand checks while reading (disclosed). Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so every outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-HUM-0",
 "iteration": 1,
 "kind": "arith_audit",
 "seed": 39501,
 "items": [
  {
   "name": "d_Rarity",
   "expr": "0.253/sqrt(50)",
   "printed": 0.0358
  },
  {
   "name": "p_Rarity",
   "expr": "t_p2(0.253, 49)",
   "printed": 0.801
  },
  {
   "name": "sign_Rarity",
   "expr": "((25.9)-(25.72))*(0.253)"
  },
  {
   "name": "r_implied_Rarity",
   "expr": "(5.5997**2+4.8741**2-(abs(25.9-25.72)*sqrt(50)/abs(0.253))**2)/(2*5.5997*4.8741)"
  },
  {
   "name": "d_BeautyPerception",
   "expr": "-0.03/sqrt(50)",
   "printed": -0.0042
  },
  {
   "name": "p_BeautyPerception",
   "expr": "t_p2(-0.03, 49)",
   "printed": 0.976
  },
  {
   "name": "sign_BeautyPerception",
   "expr": "((26.18)-(26.22))*(-0.03)"
  },
  {
   "name": "r_implied_BeautyPerception",
   "expr": "(7.1105**2+6.864**2-(abs(26.18-26.22)*sqrt(50)/abs(-0.03))**2)/(2*7.1105*6.864)"
  },
  {
   "name": "d_SelfTranscendence",
   "expr": "-0.355/sqrt(50)",
   "printed": -0.0502
  },
  {
   "name": "p_SelfTranscendence",
   "expr": "t_p2(-0.355, 49)",
   "printed": 0.724
  },
  {
   "name": "sign_SelfTranscendence",
   "expr": "((26.32)-(26.68))*(-0.355)"
  },
  {
   "name": "r_implied_SelfTranscendence",
   "expr": "(5.6657**2+5.7016**2-(abs(26.32-26.68)*sqrt(50)/abs(-0.355))**2)/(2*5.6657*5.7016)"
  },
  {
   "name": "d_ConceptualComplexity",
   "expr": "-1.932/sqrt(50)",
   "printed": -0.2732
  },
  {
   "name": "p_ConceptualComplexity",
   "expr": "t_p2(-1.932, 49)",
   "printed": 0.059
  },
  {
   "name": "sign_ConceptualComplexity",
   "expr": "((19.6)-(21.58))*(-1.932)"
  },
  {
   "name": "r_implied_ConceptualComplexity",
   "expr": "(6.1246**2+6.6856**2-(abs(19.6-21.58)*sqrt(50)/abs(-1.932))**2)/(2*6.1246*6.6856)"
  },
  {
   "name": "d_ExistentialDanger",
   "expr": "-5.72/sqrt(50)",
   "printed": -0.809
  },
  {
   "name": "p_ExistentialDanger",
   "expr": "t_p2(-5.72, 49)",
   "printed": 0.0
  },
  {
   "name": "sign_ExistentialDanger",
   "expr": "((16.38)-(22.34))*(-5.72)"
  },
  {
   "name": "r_implied_ExistentialDanger",
   "expr": "(5.721**2+7.6894**2-(abs(16.38-22.34)*sqrt(50)/abs(-5.72))**2)/(2*5.721*7.6894)"
  },
  {
   "name": "d_Vastness",
   "expr": "-2.041/sqrt(50)",
   "printed": -0.2886
  },
  {
   "name": "p_Vastness",
   "expr": "t_p2(-2.041, 49)",
   "printed": 0.047
  },
  {
   "name": "sign_Vastness",
   "expr": "((27.18)-(29.4))*(-2.041)"
  },
  {
   "name": "r_implied_Vastness",
   "expr": "(8.1858**2+7.2787**2-(abs(27.18-29.4)*sqrt(50)/abs(-2.041))**2)/(2*8.1858*7.2787)"
  },
  {
   "name": "d_NeedToShare",
   "expr": "-1.821/sqrt(50)",
   "printed": -0.2575
  },
  {
   "name": "p_NeedToShare",
   "expr": "t_p2(-1.821, 49)",
   "printed": 0.075
  },
  {
   "name": "sign_NeedToShare",
   "expr": "((26.66)-(28))*(-1.821)"
  },
  {
   "name": "r_implied_NeedToShare",
   "expr": "(5.0127**2+4.8234**2-(abs(26.66-28)*sqrt(50)/abs(-1.821))**2)/(2*5.0127*4.8234)"
  },
  {
   "name": "d_ExistentialSafety",
   "expr": "1.948/sqrt(50)",
   "printed": 0.2755
  },
  {
   "name": "p_ExistentialSafety",
   "expr": "t_p2(1.948, 49)",
   "printed": 0.057
  },
  {
   "name": "sign_ExistentialSafety",
   "expr": "((22.18)-(20.5))*(1.948)"
  },
  {
   "name": "r_implied_ExistentialSafety",
   "expr": "(5.271**2+5.8771**2-(abs(22.18-20.5)*sqrt(50)/abs(1.948))**2)/(2*5.271*5.8771)"
  },
  {
   "name": "BF01_vastness_table",
   "expr": "0.968",
   "printed": 1.033
  },
  {
   "name": "BF01_danger_table",
   "expr": "3.961e-5"
  },
  {
   "name": "pct_female",
   "expr": "100*39/50"
  }
 ],
 "hyps": [
  [
   "Cohen's d equals t/sqrt(50) within 0.001 for all eight sublime dimensions",
   "all(abs(v['diff']) <= 0.001 for k, v in o['items'].items() if k.startswith('d_'))"
  ],
  [
   "two-sided p from t with 49 df reproduces the printed p within 0.005 for all eight (danger's '.000' read as < 0.0005)",
   "all((v['value'] < 0.0005) if v['printed'] == 0 else abs(v['diff']) <= 0.005 for k, v in o['items'].items() if k.startswith('p_'))"
  ],
  [
   "t has the sign of (art mean - nature mean) for all eight dimensions",
   "all(v['value'] > 0 for k, v in o['items'].items() if k.startswith('sign_'))"
  ],
  [
   "printed means, SDs and t imply a between-condition correlation within [-1, 1] for every dimension",
   "all(-1 <= v['value'] <= 1 for k, v in o['items'].items() if k.startswith('r_implied_'))"
  ],
  [
   "Table 2's BF01 for vastness and for existential danger are both below 1/3, as the text's 'strong evidence for H 1' for both requires",
   "o['items']['BF01_vastness_table']['value'] < 1/3 and o['items']['BF01_danger_table']['value'] < 1/3"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-1` (run from `Humanities/simulation/`)
