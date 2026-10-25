# SIM-TR-SOC-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P99's G*Power statements (.96, .96, .99, .92, .49): do they reproduce, and are the Universalism and Benevolence group means ordered prosocial > individualist > competitor?

## Phase operationalization tested
SOC Transcendence = self-transcendence values and prosocial orientation (P99).

## Sources this run draws on
P99 (Nezlek 2024, values and social value orientation, PLoS One, PMC11602047, CC BY; read in full in TR0): 1655 participants; SVO prosocial 1151, individualist 381, competitor 123; Portrait Values Questionnaire (self-transcendence = universalism + benevolence); Table 2 means; Table 3 group means, F(2, n - 3), eta^2, planned comparisons; participant flows in Method and Results.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | P99's five G*Power values (.96, .96, .99, .92, .49) reproduce from noncentral F / t within 0.01 |
| H2 | hypothesis | Universalism means are ordered prosocial > individualist > competitor (Table 3) |
| H3 | hypothesis | the same order holds for the first Benevolence measure |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Noncentral F (lambda = f^2 N) and noncentral t (delta = d sqrt(n1 n2/(n1 + n2))), two-sided alpha .05. Foreknowledge: the agent saw the Benevolence order while reading. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-SOC-A",
 "iteration": 3,
 "kind": "arith_audit",
 "seed": 40303,
 "items": [
  {
   "name": "pow_anova_f10",
   "expr": "ncf_pow(0.10**2*1655, 2, 1652)",
   "printed": 0.96
  },
  {
   "name": "pow_t_d20_pro_vs_self",
   "expr": "nct_pow2(0.2*sqrt(1151*504/1655), 1653)",
   "printed": 0.96
  },
  {
   "name": "pow_t_d50_ind_vs_comp",
   "expr": "nct_pow2(0.5*sqrt(381*123/504), 502)",
   "printed": 0.99
  },
  {
   "name": "pow_t_d35_ind_vs_comp",
   "expr": "nct_pow2(0.35*sqrt(381*123/504), 502)",
   "printed": 0.92
  },
  {
   "name": "pow_t_d20_ind_vs_comp",
   "expr": "nct_pow2(0.2*sqrt(381*123/504), 502)",
   "printed": 0.49
  },
  {
   "name": "univ_order",
   "expr": "(0.543 > 0.312) and (0.312 > 0.262)"
  },
  {
   "name": "bene_order",
   "expr": "(0.751 > 0.558) and (0.558 > 0.667)"
  },
  {
   "name": "beneG_order",
   "expr": "(0.854 > 0.693) and (0.693 > 0.692)"
  }
 ],
 "hyps": [
  [
   "P99's five G*Power values (.96, .96, .99, .92, .49) reproduce from noncentral F / t within 0.01",
   "all(abs(o['items'][k]['diff']) <= 0.01 for k in o['items'] if k.startswith('pow_'))"
  ],
  [
   "Universalism means are ordered prosocial > individualist > competitor (Table 3)",
   "o['items']['univ_order']['value'] == 1"
  ],
  [
   "the same order holds for the first Benevolence measure",
   "o['items']['bene_order']['value'] == 1"
  ]
 ]
}
```

## Command
`python sim_soc.py iter-3` (run from `Social-Sciences/simulation/`)
