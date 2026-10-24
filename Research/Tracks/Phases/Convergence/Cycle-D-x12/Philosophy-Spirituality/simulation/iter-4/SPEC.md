# SIM-CV-PHI-D - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Does P83's regression Table 1 reproduce (t = B/SE, CIs)?

## Phase operationalization tested
PHI Convergence = convergence of traditions on a common core of mystical experience (P81, P83, P84).

## Sources this run draws on
P83 (Perry, Polito & Thompson 2021, Brain Sciences 11:101, PMC7828722, CC BY 4.0; read in full in CVD): online survey of 464 regular chanters from 33 countries; 60% met the MEQ30 criterion for a complete mystical experience; no association with tradition (chi2(8) = 12.573, p = 0.127; F(8,392) = 1.367, p = 0.209); absorption, altruism and religiosity higher in those with mystical states (t = 10.910, 3.889, 5.395); regression Table 1; authors read the cross-tradition similarity as in line with Stace's common core.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | two-sided normal-limit p at t = 1.96 equals 0.05 |
| H1 | hypothesis | P83 Table 1: every t = B/SE within 0.1 of the printed t |
| H2 | hypothesis | every 95% CI bound within 0.003 of the printed bound |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Recomputation from printed summaries only (P83's OSF data not downloaded). Group sizes 278/186 are the agent's derivation (60% of 464; P83 does not print them). Agent arithmetic before the run suggested most items reproduce and the 2 x 2 ANOVA df does not (disclosed). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds/options in CVD (stats_audit, instrument_core, levelling_voter bias_mode=selection) were smoke-tested once at trivial size (seed 99, temporary directory, nothing kept) with printed values suppressed; existing kinds were not smoke-tested. CVC results were known when these hypotheses were written (replications say so).

## Parameters
```json
{
 "sim_id": "SIM-CV-PHI-D",
 "iteration": 4,
 "kind": "stats_audit",
 "seed": 33604,
 "items": [
  {
   "name": "constant",
   "type": "coef",
   "B": 18.801,
   "SE": 7.675,
   "df": 460,
   "printed": {
    "t": 2.45,
    "lo": 3.719,
    "hi": 33.883
   }
  },
  {
   "name": "absorption",
   "type": "coef",
   "B": 0.542,
   "SE": 0.048,
   "df": 460,
   "printed": {
    "t": 11.35,
    "lo": 0.449,
    "hi": 0.636
   }
  },
  {
   "name": "altruism",
   "type": "coef",
   "B": 0.353,
   "SE": 0.133,
   "df": 460,
   "printed": {
    "t": 2.65,
    "lo": 0.091,
    "hi": 0.614
   }
  },
  {
   "name": "religiosity",
   "type": "coef",
   "B": 0.32,
   "SE": 0.066,
   "df": 460,
   "printed": {
    "t": 4.88,
    "lo": 0.191,
    "hi": 0.449
   }
  }
 ],
 "hyps": [
  [
   "P83 Table 1: every t = B/SE within 0.1 of the printed t",
   "all(abs(o['items'][k]['t'] - o['items'][k]['printed']['t']) < 0.1 for k in o['items'])"
  ],
  [
   "every 95% CI bound within 0.003 of the printed bound",
   "all(abs(o['items'][k]['lo'] - o['items'][k]['printed']['lo']) < 0.003 and abs(o['items'][k]['hi'] - o['items'][k]['printed']['hi']) < 0.003 for k in o['items'])"
  ]
 ]
}
```

## Command
`python sim_phi.py iter-4` (run from `Philosophy-Spirituality/simulation/`)
