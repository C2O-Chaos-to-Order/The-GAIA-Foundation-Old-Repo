# SIM-CV-PHI-D - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Do P83's p-values (traditions, interaction, vocalisation) follow from its printed statistics?

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
| H1 | hypothesis | P83's p-values (0.127, 0.209, 0.009, 0.637) recomputed within 0.002 from the printed statistics and df |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Recomputation from printed summaries only (P83's OSF data not downloaded). Group sizes 278/186 are the agent's derivation (60% of 464; P83 does not print them). Agent arithmetic before the run suggested most items reproduce and the 2 x 2 ANOVA df does not (disclosed). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds/options in CVD (stats_audit, instrument_core, levelling_voter bias_mode=selection) were smoke-tested once at trivial size (seed 99, temporary directory, nothing kept) with printed values suppressed; existing kinds were not smoke-tested. CVC results were known when these hypotheses were written (replications say so).

## Parameters
```json
{
 "sim_id": "SIM-CV-PHI-D",
 "iteration": 3,
 "kind": "stats_audit",
 "seed": 33603,
 "items": [
  {
   "name": "chi2_traditions",
   "type": "p_chi2",
   "chi2": 12.573,
   "df": 8,
   "printed": 0.127
  },
  {
   "name": "F_traditions",
   "type": "p_F",
   "F": 1.367,
   "df1": 8,
   "df2": 392,
   "printed": 0.209
  },
  {
   "name": "F_interaction",
   "type": "p_F",
   "F": 1.828,
   "df1": 24,
   "df2": 1176,
   "printed": 0.009
  },
  {
   "name": "F_vocal",
   "type": "p_F",
   "F": 0.222,
   "df1": 1,
   "df2": 463,
   "printed": 0.637
  }
 ],
 "hyps": [
  [
   "P83's p-values (0.127, 0.209, 0.009, 0.637) recomputed within 0.002 from the printed statistics and df",
   "all(abs(o['items'][k]['p'] - o['items'][k]['printed']) < 0.002 for k in ['chi2_traditions', 'F_traditions', 'F_interaction', 'F_vocal'])"
  ]
 ]
}
```

## Command
`python sim_phi.py iter-3` (run from `Philosophy-Spirituality/simulation/`)
