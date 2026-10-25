# SIM-CV-SOC-C - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
A crowd not centred on the truth through underestimation with low dispersion (mu -1, -0.5; sigma 0.3): Omega > 0.5?

## Phase operationalization tested
SOC Convergence = collective estimation (P69).

## Sources this run draws on
P69 (Almaatouq, Rahimian, Burton & Alhajri 2022, 'The distribution of initial estimates moderates the effect of social influence on the wisdom of the crowd', Sci Rep 12:16546, PMC9530231, CC BY; read in full in CV0, SI not read): a_n(omega) = omega a_1 + (1 - omega) mean; Omega_n; Fig. 2 (n 50, theta 2, omega 1/3, log-normal): centralization helps under overestimation or large dispersion, hurts under low-dispersion underestimation.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | omega = 0 gives Omega exactly 0 |
| H1 | hypothesis | a crowd not centred on the truth (underestimation, mu -1 or -0.5, sigma 0.3): Omega > 0.5 (P69's 'not initially centered' argument) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Tests P69's 'not initially centered' argument for underestimation, which P69's Fig. 2 contexts in CVA/CVB did not cover. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds in CVC (kuramoto_lyap, kuramoto_fss, crowd_bound, trap_simpson, levelling_voter, common_core) were smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before the SPECs; printed values were suppressed except one kuramoto_lyap smoke (N = 3 and 4, K = 1, 3 settings, T 400) whose maxima (both slightly negative) were seen (disclosed). Thresholds were not informed by smoke values. Existing kinds were not smoke-tested.

## Parameters
```json
{
 "sim_id": "SIM-CV-SOC-C",
 "iteration": 6,
 "kind": "crowd_centralization",
 "seed": 32306,
 "n": 50,
 "omega": 0.3333333333333333,
 "theta": 2.0,
 "reps": 20000,
 "contexts": [
  [
   -1.0,
   0.3
  ],
  [
   -0.5,
   0.3
  ]
 ],
 "hyps": [
  [
   "a crowd not centred on the truth (underestimation, mu -1 or -0.5, sigma 0.3): Omega > 0.5 (P69's 'not initially centered' argument)",
   "all(v > 0.5 for v in o['Omega'].values())"
  ]
 ]
}
```

## Command
`python sim_soc.py iter-6` (run from `Social-Sciences/simulation/`)
