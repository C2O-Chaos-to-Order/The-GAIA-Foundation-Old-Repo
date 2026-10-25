# SIM-TR-APP-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P103's printed statistics: do one-tailed p values follow from t(33), does overall spiritual well-being equal its subscales, do discontinuation reasons add to 6, do Table 2's percentages and the Discussion's per-item affect means follow, and is n 32 the right a priori size?

## Phase operationalization tested
APP Transcendence = self-transcendence measured and promoted in nursing (P100; P103 added in TRA).

## Sources this run draws on
P103 (Kim & Ahn 2021, 'Development and application of a self-transcendence enhancement program for the well-being of elderly women living alone in Korea', Korean J Women Health Nurs 27:128-140, PMC9334186, CC BY 4.0; read in full in TRA): single-group pre-post, 40 recruited, 34 completed; Reed's Self-Transcendence Scale; Table 2 characteristics (N 34); Table 3 pre/post means, SDs, paired t and one-tailed p; a priori n 32 (d .45, one-sided, power .80); reasons for discontinuation.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | one-tailed p from t(33) reproduces every printed p in P103's Table 3 within 0.005 (printed '<.001' read as < 0.001) |
| H2 | hypothesis | overall spiritual well-being equals religious + existential at pretest and posttest within 0.05 |
| H3 | hypothesis | the reasons given for discontinuation add up to the six who discontinued |
| H4 | hypothesis | Table 2's percentages reproduce from n/34 within 0.06 |
| H5 | hypothesis | the post-program per-item affect means in the Discussion (3.37, 3.10) equal Table 3's posttest sums divided by 9 and 11 items within 0.01 |
| H6 | hypothesis | the a priori sample size (one-sided paired t, d .45, alpha .05, power .80) is 32 as printed |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic audit of printed (rounded) numbers; df 33 from N 34; noncentral t for sample size. Foreknowledge: the agent noticed while reading that p .470 for t 1.72 and the pretest spiritual well-being total looked inconsistent. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-APP-A",
 "iteration": 1,
 "kind": "arith_audit",
 "seed": 40401,
 "items": [
  {
   "name": "p1_SelfTranscendence",
   "expr": "t_p1(abs(8.78), 33)",
   "printed": 0.0005
  },
  {
   "name": "p1_SpiritualWB",
   "expr": "t_p1(abs(8.3), 33)",
   "printed": 0.002
  },
  {
   "name": "p1_ReligiousSWB",
   "expr": "t_p1(abs(1.79), 33)",
   "printed": 0.04
  },
  {
   "name": "p1_ExistentialSWB",
   "expr": "t_p1(abs(6.75), 33)",
   "printed": 0.002
  },
  {
   "name": "p1_Depression",
   "expr": "t_p1(abs(-7.59), 33)",
   "printed": 0.0005
  },
  {
   "name": "p1_LifeSatisfaction",
   "expr": "t_p1(abs(1.72), 33)",
   "printed": 0.47
  },
  {
   "name": "p1_PositiveAffect",
   "expr": "t_p1(abs(3.77), 33)",
   "printed": 0.001
  },
  {
   "name": "p1_NegativeAffect",
   "expr": "t_p1(abs(-6.15), 33)",
   "printed": 0.0005
  },
  {
   "name": "swb_pre_sum",
   "expr": "27.76+29.55",
   "printed": 56.52
  },
  {
   "name": "swb_post_sum",
   "expr": "29.70+34.58",
   "printed": 64.29
  },
  {
   "name": "retention",
   "expr": "100*34/40",
   "printed": 85
  },
  {
   "name": "dropout_reasons_sum",
   "expr": "2+1+1",
   "printed": 6
  },
  {
   "name": "pct_age_75_80",
   "expr": "100*19/34",
   "printed": 55.9
  },
  {
   "name": "pct_alone_6_10",
   "expr": "100*19/34",
   "printed": 55.8
  },
  {
   "name": "pct_health_good",
   "expr": "100*9/34",
   "printed": 26.6
  },
  {
   "name": "pct_guardian_children",
   "expr": "100*28/34",
   "printed": 82.3
  },
  {
   "name": "pct_visit_week",
   "expr": "100*6/34",
   "printed": 17.7
  },
  {
   "name": "pct_no_hobby",
   "expr": "100*22/34",
   "printed": 64.7
  },
  {
   "name": "pa_post_per_item",
   "expr": "32.00/9",
   "printed": 3.37
  },
  {
   "name": "na_post_per_item",
   "expr": "30.26/11",
   "printed": 3.1
  },
  {
   "name": "n_required_d45",
   "expr": "min(n for n in range(5, 200) if nct_pow1(0.45*sqrt(n), n-1) >= 0.80)",
   "printed": 32
  },
  {
   "name": "dz_SelfTranscendence",
   "expr": "8.78/sqrt(34)"
  },
  {
   "name": "existential_vs_religious_gain",
   "expr": "(34.58-29.55)/(29.70-27.76)",
   "printed": 2
  }
 ],
 "hyps": [
  [
   "one-tailed p from t(33) reproduces every printed p in P103's Table 3 within 0.005 (printed '<.001' read as < 0.001)",
   "all((v['value'] < 0.001) if v['printed'] == 0.0005 else abs(v['diff']) <= 0.005 for k, v in o['items'].items() if k.startswith('p1_'))"
  ],
  [
   "overall spiritual well-being equals religious + existential at pretest and posttest within 0.05",
   "abs(o['items']['swb_pre_sum']['diff']) <= 0.05 and abs(o['items']['swb_post_sum']['diff']) <= 0.05"
  ],
  [
   "the reasons given for discontinuation add up to the six who discontinued",
   "o['items']['dropout_reasons_sum']['diff'] == 0"
  ],
  [
   "Table 2's percentages reproduce from n/34 within 0.06",
   "all(abs(o['items'][k]['diff']) <= 0.06 for k in o['items'] if k.startswith('pct_'))"
  ],
  [
   "the post-program per-item affect means in the Discussion (3.37, 3.10) equal Table 3's posttest sums divided by 9 and 11 items within 0.01",
   "abs(o['items']['pa_post_per_item']['diff']) <= 0.01 and abs(o['items']['na_post_per_item']['diff']) <= 0.01"
  ],
  [
   "the a priori sample size (one-sided paired t, d .45, alpha .05, power .80) is 32 as printed",
   "o['items']['n_required_d45']['diff'] == 0"
  ]
 ]
}
```

## Command
`python sim_app.py iter-1` (run from `Applied-Sciences/simulation/`)
