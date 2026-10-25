# Convergence in the Social Sciences — Cycle-0-Baseline (CV0)

Phase report: Convergence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
Baseline: convergence of estimates into a collective one (P69); centralization helps with overestimation or high dispersion and hurts with low-dispersion underestimation, as P69 states.

## Claims (ledger: `claims/claims.csv`)
- **CV0-SOC-01** [P] P69 shows that whether a centralized influence network (one agent's estimate weighted by omega) improves the collective estimate over the plain mean depends on the distribution of initial estimates: it helps under overestimation bias or large dispersion and is reversed under low dispersion with underestimation; in a reanalysis of four experiments (2885 participants, 99 groups, 54 tasks, 687 collective estimates) the probability of improvement was explained by its heavy-tail measure (z = 4.16). *Operationalization:* SOC Convergence = estimates converging into a collective estimate. *Sources:* P69. *Limits:* Slips: '678 observations' vs 582 + 105 = 687 collective estimates; a logistic model is written with a Gaussian error term; the distributional parametrisation is in the SI (not read).
- **CV0-SOC-02** [P] With n 50, omega 1/3, theta 2 and a = theta exp(mu + sigma Z), the probability that the centralized estimate beats the mean was 0.681 under overestimation (mu 0.5, sigma 1), 0.7535 under large dispersion (mu 0, sigma 1.5) and 0.440 under low-dispersion underestimation (mu -0.3, sigma 0.3), reproducing P69's three qualitative regimes; unbiased low dispersion (mu 0, sigma 0.3) gave 0.340. *Operationalization:* SOC Convergence = wisdom of crowds under centralization. *Sources:* SIM-CV-SOC-0/iter-1#V1;SIM-CV-SOC-0/iter-1#H1;SIM-CV-SOC-0/iter-1#H2;SIM-CV-SOC-0/iter-1#H3. *Limits:* The log-normal parametrisation is the agent's, not P69's SI.

## Simulations (SIM-CV-SOC-0; 1 iteration(s), spec-first; validation 1/1, hypotheses supported 3/3)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `4c5a2a15` | P69's centralization model: with n 50, omega 1/3, theta 2 and log-normal estimates a = theta exp(mu + sigma Z), is Omega > 0.5 under overestimation (mu 0.5, sigma 1) and large dispersion (mu 0, sigma 1.5) and < 0.5 under low-dispersion underestimation (mu -0.3, sigma 0.3)? | V1 Pass; H1 Supported; H2 Supported; H3 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: Centralization and the distribution of initial estimates sourced (CV0-SOC-01); P69's three regimes reproduced (CV0-SOC-02).

## Unresolved
- P69's SI parametrisation not read; the agent's log-normal form may differ.
- The empirical reanalysis (z = 4.16) was not reproduced (data not used).
