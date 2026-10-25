# Convergence in the Social Sciences — Cycle-A-x3 (CVA)

Phase report: Convergence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x3: centralization's advantage under overestimation grows with group size, barely depends on the weight, and reverses without a bias of the mean.

## Claims (ledger: `claims/claims.csv`)
- **CVA-SOC-01** [P] P69 shows that whether a centralized influence network (one agent's estimate weighted by omega) improves the collective estimate over the plain mean depends on the distribution of initial estimates: it helps under overestimation bias or large dispersion and is reversed under low dispersion with underestimation; in a reanalysis of four experiments (2885 participants, 99 groups, 54 tasks, 687 collective estimates) the probability of improvement was explained by its heavy-tail measure (z = 4.16). *Operationalization:* SOC Convergence = estimates converging into a collective estimate. *Sources:* P69. *Limits:* Slips: '678 observations' vs 582 + 105 = 687 collective estimates; a logistic model is written with a Gaussian error term; the distributional parametrisation is in the SI (not read).
- **CVA-SOC-02** [P] With n 50, omega 1/3, theta 2 and a = theta exp(mu + sigma Z), the probability that the centralized estimate beats the mean was 0.681 under overestimation (mu 0.5, sigma 1), 0.7535 under large dispersion (mu 0, sigma 1.5) and 0.440 under low-dispersion underestimation (mu -0.3, sigma 0.3), reproducing P69's three qualitative regimes; unbiased low dispersion (mu 0, sigma 0.3) gave 0.340. *Operationalization:* SOC Convergence = wisdom of crowds under centralization. *Sources:* SIM-CV-SOC-0/iter-1#V1;SIM-CV-SOC-0/iter-1#H1;SIM-CV-SOC-0/iter-1#H2;SIM-CV-SOC-0/iter-1#H3. *Limits:* The log-normal parametrisation is the agent's, not P69's SI.
- **CVA-SOC-03** [P] Under overestimation (mu 0.5, sigma 1) centralization beat the plain mean with probability 0.596, 0.645, 0.683 and 0.690 for groups of 5, 10, 50 and 200: always above one half and rising with group size, as the mean's bias dominates its noise in larger groups. *Operationalization:* SOC Convergence = collective estimation and group size. *Sources:* SIM-CV-SOC-A/iter-1#V1;SIM-CV-SOC-A/iter-1#H1;SIM-CV-SOC-A/iter-1#H2. *Limits:* Agent's log-normal parametrisation.
- **CVA-SOC-04** [P] Under large dispersion (mu 0, sigma 1.5) Omega stayed at 0.755, 0.751 and 0.744 for centralization weights 0.1, 0.5 and 0.9: the advantage barely depends on how strongly the central estimate is weighted. *Operationalization:* SOC Convergence = centralization weight. *Sources:* SIM-CV-SOC-A/iter-2#V1;SIM-CV-SOC-A/iter-2#H1. *Limits:* Agent's parametrisation; one context.
- **CVA-SOC-05** [P] If the log-normal is mean-unbiased (mu = -sigma^2/2) centralization hurts: Omega 0.233 at sigma 0.3 and 0.283 at sigma 1.0, so in this model centralization helps only by countering a bias of the mean, consistent with P69's account. *Operationalization:* SOC Convergence = when centralization helps. *Sources:* SIM-CV-SOC-A/iter-3#V1;SIM-CV-SOC-A/iter-3#H1. *Limits:* Context is the agent's, not one of P69's.

## Simulations (SIM-CV-SOC-A; 3 iteration(s), spec-first; validation 3/3, hypotheses supported 4/4)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `cec8e20b` | P69 under overestimation (mu 0.5, sigma 1): is Omega > 0.5 for groups of 5, 10, 50 and 200, and does it grow with group size? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |
| 2 | `1dfa24b0` | P69 under large dispersion (mu 0, sigma 1.5): is Omega > 0.5 for centralization weights 0.1, 0.5 and 0.9? | V1 Pass; H1 Supported; R1 Reported |
| 3 | `7c4cd79a` | P69's logic without bias: if the log-normal is mean-unbiased (mu = -sigma^2/2), does centralization hurt (Omega < 0.5) at sigma 0.3 and 1.0? | V1 Pass; H1 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (3; details `research/PASSES.md`)
- Pass 1: CVA-SOC-03: centralization advantage grows with group size under overestimation; no new search (disclosed).
- Pass 2: Added nothing new of substance: the weight sweep (CVA-SOC-04) only shows the CV0 result is insensitive to omega.
- Pass 3: CVA-SOC-05: without a bias of the mean, centralization hurts.

## Unresolved
- P69's SI parametrisation still not read.
- P69's empirical reanalysis not reproduced.
