# SIM-CV-PHI-D - iteration 7 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
How large a tradition difference could P83's null test detect (power)?

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
| H1 | hypothesis | P83's one-way ANOVA across 9 traditions (N 401) had >= 80% power only for effects f >= 0.15 (a null result does not exclude small differences) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Standard noncentral-F power; Cohen's f. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds/options in CVD (stats_audit, instrument_core, levelling_voter bias_mode=selection) were smoke-tested once at trivial size (seed 99, temporary directory, nothing kept) with printed values suppressed; existing kinds were not smoke-tested. CVC results were known when these hypotheses were written (replications say so).

## Parameters
```json
{
 "sim_id": "SIM-CV-PHI-D",
 "iteration": 7,
 "kind": "stats_audit",
 "seed": 33607,
 "items": [
  {
   "name": "power_traditions",
   "type": "power_anova",
   "k": 9,
   "N": 401,
   "f_values": [
    0.1,
    0.15,
    0.25
   ]
  }
 ],
 "hyps": [
  [
   "P83's one-way ANOVA across 9 traditions (N 401) had >= 80% power only for effects f >= 0.15 (a null result does not exclude small differences)",
   "o['items']['power_traditions']['f80'] >= 0.15"
  ]
 ]
}
```

## Command
`python sim_phi.py iter-7` (run from `Philosophy-Spirituality/simulation/`)
