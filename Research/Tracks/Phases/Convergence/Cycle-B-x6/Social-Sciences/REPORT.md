# Convergence in the Social Sciences — Cycle-B-x6 (CVB)

Phase report: Convergence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x6: centralization helps exactly when the mean is biased, more so in larger groups, and hurts more in larger groups when it is not; CVA's value replicates.

## Claims (ledger: `claims/claims.csv`)
- **CVB-SOC-01** [P] P69 shows that whether a centralized influence network (one agent's estimate weighted by omega) improves the collective estimate over the plain mean depends on the distribution of initial estimates: it helps under overestimation bias or large dispersion and is reversed under low dispersion with underestimation; in a reanalysis of four experiments (2885 participants, 99 groups, 54 tasks, 687 collective estimates) the probability of improvement was explained by its heavy-tail measure (z = 4.16). *Operationalization:* SOC Convergence = estimates converging into a collective estimate. *Sources:* P69. *Limits:* Slips: '678 observations' vs 582 + 105 = 687 collective estimates; a logistic model is written with a Gaussian error term; the distributional parametrisation is in the SI (not read).
- **CVB-SOC-02** [P] With n 50, omega 1/3, theta 2 and a = theta exp(mu + sigma Z), the probability that the centralized estimate beats the mean was 0.681 under overestimation (mu 0.5, sigma 1), 0.7535 under large dispersion (mu 0, sigma 1.5) and 0.440 under low-dispersion underestimation (mu -0.3, sigma 0.3), reproducing P69's three qualitative regimes; unbiased low dispersion (mu 0, sigma 0.3) gave 0.340. *Operationalization:* SOC Convergence = wisdom of crowds under centralization. *Sources:* SIM-CV-SOC-0/iter-1#V1;SIM-CV-SOC-0/iter-1#H1;SIM-CV-SOC-0/iter-1#H2;SIM-CV-SOC-0/iter-1#H3. *Limits:* The log-normal parametrisation is the agent's, not P69's SI.
- **CVB-SOC-03** [P] Under overestimation (mu 0.5, sigma 1) centralization beat the plain mean with probability 0.596, 0.645, 0.683 and 0.690 for groups of 5, 10, 50 and 200: always above one half and rising with group size, as the mean's bias dominates its noise in larger groups. *Operationalization:* SOC Convergence = collective estimation and group size. *Sources:* SIM-CV-SOC-A/iter-1#V1;SIM-CV-SOC-A/iter-1#H1;SIM-CV-SOC-A/iter-1#H2. *Limits:* Agent's log-normal parametrisation.
- **CVB-SOC-04** [P] Under large dispersion (mu 0, sigma 1.5) Omega stayed at 0.755, 0.751 and 0.744 for centralization weights 0.1, 0.5 and 0.9: the advantage barely depends on how strongly the central estimate is weighted. *Operationalization:* SOC Convergence = centralization weight. *Sources:* SIM-CV-SOC-A/iter-2#V1;SIM-CV-SOC-A/iter-2#H1. *Limits:* Agent's parametrisation; one context.
- **CVB-SOC-05** [P] If the log-normal is mean-unbiased (mu = -sigma^2/2) centralization hurts: Omega 0.233 at sigma 0.3 and 0.283 at sigma 1.0, so in this model centralization helps only by countering a bias of the mean, consistent with P69's account. *Operationalization:* SOC Convergence = when centralization helps. *Sources:* SIM-CV-SOC-A/iter-3#V1;SIM-CV-SOC-A/iter-3#H1. *Limits:* Context is the agent's, not one of P69's.
- **CVB-SOC-06** [P] Whenever the plain mean was biased upward, centralization beat it: Omega 0.571, 0.652, 0.756 and 0.773 for groups of 5, 10, 50 and 200 at mu 0, sigma 1.5; 0.680, 0.682 and 0.687 for weights 0.1, 0.5 and 0.9 at mu 0.5, sigma 1; and 0.597 at mu 1, sigma 0.5. CVA's 0.683 (mu 0.5, sigma 1, n 50) replicated on a new seed (0.681). *Operationalization:* SOC Convergence = collective estimation under centralization. *Sources:* SIM-CV-SOC-B/iter-1#V1;SIM-CV-SOC-B/iter-1#H1;SIM-CV-SOC-B/iter-2#V1;SIM-CV-SOC-B/iter-2#H1;SIM-CV-SOC-B/iter-5#V1;SIM-CV-SOC-B/iter-5#H1;SIM-CV-SOC-B/iter-6#V1;SIM-CV-SOC-B/iter-6#H1. *Limits:* Agent's log-normal parametrisation (P69's SI not read).
- **CVB-SOC-07** [P] With a mean-unbiased log-normal, centralization hurt at both small and large dispersion (Omega 0.232 at sigma 0.1, 0.314 at sigma 2.0), and its disadvantage grew with group size: 0.422, 0.379, 0.283 and 0.173 for n = 5, 10, 50 and 200 (mu -0.5, sigma 1). *Operationalization:* SOC Convergence = when centralization hurts. *Sources:* SIM-CV-SOC-B/iter-3#V1;SIM-CV-SOC-B/iter-3#H1;SIM-CV-SOC-B/iter-4#V1;SIM-CV-SOC-B/iter-4#H1. *Limits:* Contexts are the agent's, not P69's.

## Simulations (SIM-CV-SOC-B; 6 iteration(s), spec-first; validation 6/6, hypotheses supported 6/6)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `9fc92ab8` | P69 with large dispersion (mu 0, sigma 1.5): is Omega > 0.5 for groups of 5, 10, 50 and 200? | V1 Pass; H1 Supported; R1 Reported |
| 2 | `796f860f` | P69 under overestimation: is Omega > 0.5 for omega 0.1, 0.5, 0.9 (replication of CVA iter-2 in a different context)? | V1 Pass; H1 Supported; R1 Reported |
| 3 | `7e68f5c8` | Mean-unbiased contexts at small (0.1) and large (2.0) sigma: does centralization hurt (Omega < 0.5)? | V1 Pass; H1 Supported; R1 Reported |
| 4 | `36e2beef` | Mean-unbiased (mu -0.5, sigma 1) by group size: is Omega < 0.5 for n = 5-200? | V1 Pass; H1 Supported; R1 Reported |
| 5 | `8d5d0637` | Strong overestimation with low dispersion (mu 1, sigma 0.5): is Omega > 0.5? | V1 Pass; H1 Supported; R1 Reported |
| 6 | `b8f087a3` | Replication of CVA's overestimation context (mu 0.5, sigma 1, n 50) with a new seed: within 0.02 of 0.683? | V1 Pass; H1 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (6; details `research/PASSES.md`)
- Pass 1: CVB-SOC-06: under large dispersion the centralization advantage grows with group size; no new search (disclosed).
- Pass 2: Added nothing new: the weight sweep in a second context repeats CVA-SOC-04 (Omega insensitive to omega).
- Pass 3: CVB-SOC-07: centralization hurts at small and large dispersion when the mean is unbiased.
- Pass 4: CVB-SOC-07: the disadvantage grows with group size.
- Pass 5: CVB-SOC-06: strong overestimation with low dispersion still favours centralization.
- Pass 6: Added nothing new: replication of CVA's 0.683 on a new seed (0.681) confirms it.

## Unresolved
- P69's SI parametrisation still not read.
- P69's empirical reanalysis not reproduced.
