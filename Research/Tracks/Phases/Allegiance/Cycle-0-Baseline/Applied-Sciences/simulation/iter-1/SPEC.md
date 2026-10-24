# SIM-AL-APP-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P49 found allegiance a significant moderator in only 2 of 5 comparisons and concluded it was 'not as relevant ... as expected'. With P49's own primary estimate (beta = -0.183, SE = 0.125), what was the power to detect a moderator of that size, and does a simulated 47-study meta-regression reproduce that SE and power?

## Phase operationalization tested
APP Allegiance = researcher allegiance: a belief in the superiority of a treatment that can bias comparative trials (P49, quoting Leykin & DeRubeis).

## Sources this run draws on
P49 (Schuenemann, Jansen, Willutzki & Heinrichs 2025, Clin Psychol Eur 7(1):e9709, CC BY 4.0; read in full in AL0, supplement not read): Table 1A row 'no or unclear allegiance against HPT', beta -.183, SE 0.125, p .144, N = 47.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | analytic power < 0.5 |
| H2 | hypothesis | simulated SE within 20% of 0.125 and power within 0.1 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Normal approximation for power; simulated design (moderator share 0.3, within-study SE 0.2-0.4, tau 0.25) is the agent's assumption, chosen before the smoke test, which gave power 0.31 and SE 0.124. P49 itself notes 'no evidence of the moderators' impact does not mean that this is evidence of no difference'. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AL-APP-0",
 "iteration": 1,
 "kind": "meta_power",
 "seed": 24401,
 "beta_rep": -0.183,
 "se_rep": 0.125,
 "p_rep": 0.144,
 "K": 47,
 "pi": 0.3,
 "tau": 0.25,
 "beta_true": -0.183,
 "b0": 0.3,
 "s_lo": 0.2,
 "s_hi": 0.4,
 "reps": 4000
}
```

## Command
`python sim_app.py iter-1` (run from `Applied-Sciences/simulation/`)
