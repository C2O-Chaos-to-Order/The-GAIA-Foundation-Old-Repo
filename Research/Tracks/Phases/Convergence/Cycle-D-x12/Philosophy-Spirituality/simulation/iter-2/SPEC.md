# SIM-CV-PHI-D - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Does P83's Welch religiosity test reproduce?

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
| H1 | hypothesis | P83's Welch religiosity t (5.395) recomputed within 0.1 |
| H2 | hypothesis | Welch df within 10 of the printed 327 |
| H3 | hypothesis | d (0.52) within 0.02 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Recomputation from printed summaries only (P83's OSF data not downloaded). Group sizes 278/186 are the agent's derivation (60% of 464; P83 does not print them). Agent arithmetic before the run suggested most items reproduce and the 2 x 2 ANOVA df does not (disclosed). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds/options in CVD (stats_audit, instrument_core, levelling_voter bias_mode=selection) were smoke-tested once at trivial size (seed 99, temporary directory, nothing kept) with printed values suppressed; existing kinds were not smoke-tested. CVC results were known when these hypotheses were written (replications say so).

## Parameters
```json
{
 "sim_id": "SIM-CV-PHI-D",
 "iteration": 2,
 "kind": "stats_audit",
 "seed": 33602,
 "items": [
  {
   "name": "religiosity_welch",
   "type": "t_welch",
   "n1": 278,
   "n2": 186,
   "m1": 79.24,
   "m2": 70.97,
   "s1": 17.91,
   "s2": 13.63,
   "printed": {
    "t": 5.395,
    "df": 327
   }
  },
  {
   "name": "religiosity_pooled",
   "type": "t_pooled",
   "n1": 278,
   "n2": 186,
   "m1": 79.24,
   "m2": 70.97,
   "s1": 17.91,
   "s2": 13.63,
   "printed": {
    "d": 0.52
   }
  }
 ],
 "hyps": [
  [
   "P83's Welch religiosity t (5.395) recomputed within 0.1",
   "abs(o['items']['religiosity_welch']['t'] - 5.395) < 0.1"
  ],
  [
   "Welch df within 10 of the printed 327",
   "abs(o['items']['religiosity_welch']['df'] - 327) < 10"
  ],
  [
   "d (0.52) within 0.02",
   "abs(o['items']['religiosity_pooled']['d'] - 0.52) < 0.02"
  ]
 ]
}
```

## Command
`python sim_phi.py iter-2` (run from `Philosophy-Spirituality/simulation/`)
