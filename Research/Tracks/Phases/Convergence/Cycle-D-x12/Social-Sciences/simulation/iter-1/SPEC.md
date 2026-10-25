# SIM-CV-SOC-D - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P69's bound at sigma 2.5 up to n = 10^5: does it peak at intermediate n?

## Phase operationalization tested
SOC Convergence = collective estimation (P69).

## Sources this run draws on
P69 (Almaatouq, Rahimian, Burton & Alhajri 2022, 'The distribution of initial estimates moderates the effect of social influence on the wisdom of the crowd', Sci Rep 12:16546, PMC9530231, CC BY; read in full in CV0, SI not read): a_n(omega) = omega a_1 + (1 - omega) mean; Omega_n; Fig. 2 (n 50, theta 2, omega 1/3, log-normal): centralization helps under overestimation or large dispersion, hurts under low-dispersion underestimation.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | log-normal CDF at the truth with mu = 0 is exactly 1/2 |
| H1 | hypothesis | P69's bound never exceeds Monte Carlo Omega_n (3 SE) in any case |
| H2 | hypothesis | sigma 2.5: the bound peaks at an intermediate n (not at n 10 or 10^5) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent arithmetic (CVC pattern) suggested a peak. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds/options in CVD (stats_audit, instrument_core, levelling_voter bias_mode=selection) were smoke-tested once at trivial size (seed 99, temporary directory, nothing kept) with printed values suppressed; existing kinds were not smoke-tested. CVC results were known when these hypotheses were written (replications say so).

## Parameters
```json
{
 "sim_id": "SIM-CV-SOC-D",
 "iteration": 1,
 "kind": "crowd_bound",
 "seed": 33301,
 "theta": 2.0,
 "omega": 0.3333333333333333,
 "reps": 500,
 "contexts": [
  [
   0.0,
   2.5
  ]
 ],
 "n_values": [
  10,
  100,
  1000,
  10000,
  100000
 ],
 "hyps": [
  [
   "P69's bound never exceeds Monte Carlo Omega_n (3 SE) in any case",
   "all(v['bound_le_mc_plus_3se'] for v in o['by_case'].values())"
  ],
  [
   "sigma 2.5: the bound peaks at an intermediate n (not at n 10 or 10^5)",
   "max(o['by_case'], key=lambda k: o['by_case'][k]['bound']) not in ['mu0.0_s2.5_n10', 'mu0.0_s2.5_n100000']"
  ]
 ]
}
```

## Command
`python sim_soc.py iter-1` (run from `Social-Sciences/simulation/`)
