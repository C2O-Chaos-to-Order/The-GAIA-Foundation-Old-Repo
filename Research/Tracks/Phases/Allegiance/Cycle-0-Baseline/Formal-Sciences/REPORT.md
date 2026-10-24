# Allegiance in the Formal Sciences — Cycle-0-Baseline (AL0)

Phase report: Allegiance (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
Baseline: allegiance as cooperation under five mechanisms (P47); printed thresholds reproduce exactly, the 1/3 rule's direction holds at N = 100, but its threshold is off by 6% (not supported).

## Claims (ledger: `claims/claims.csv`)
- **AL0-FOR-01** [E] P47 states five mechanisms under which natural selection can favour cooperation, each a benefit-to-cost threshold: kin selection r > c/b, direct reciprocity w > c/b, indirect reciprocity q > c/b, network reciprocity b/c > k, group selection b/c > 1 + n/m; for reciprocity, Table 1 adds stricter thresholds for risk-dominance and advantageousness, and the latter links to the '1/3 rule', which P47 says holds in the limit of weak selection. *Operationalization:* FOR Allegiance = cooperation stabilised by a mechanism. *Sources:* P47. *Limits:* Author manuscript of a short review; each rule is derived in a simplified model, and P47's 1/3 rule is stated only for weak selection.
- **AL0-FOR-02** [P] Numerically solving P47's Table 1 matrices (w = q = r = 0.5, k = 4, n = 10, m = 20) reproduced every printed threshold exactly (ESS/RD/AD b/c = 2, 3, 4 for reciprocity). In a Moran process (N = 100, selection 0.005) the fixation probability of tit-for-tat in always-defect was below 1/N at b/c = 3.5 (0.00947) and above at 4.5 (0.01019), as the 1/3 rule predicts, but the crossing was at b/c 4.23, not within 5% of 4: the finite-N prediction is not supported at N = 100 (expected from the smoke test). *Operationalization:* FOR Allegiance = cooperation thresholds. *Sources:* SIM-AL-FOR-0/iter-1#V1;SIM-AL-FOR-0/iter-1#V2;SIM-AL-FOR-0/iter-1#H1;SIM-AL-FOR-0/iter-1#H2. *Limits:* The 1/3 rule is a large-N weak-selection limit; finite-N correction not sourced. Stochastic check at N = 20 matched the exact formula (0.0531 vs 0.0515).

## Simulations (SIM-AL-FOR-0; 1 iteration(s), spec-first; validation 2/2, hypotheses supported 1/2)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `c6827516` | P47's five rules for the evolution of cooperation: do the ESS/RD/AD thresholds computed from Table 1's payoff matrices equal the printed rules, and does the '1/3 rule' (advantageous strategy => fixation probability above 1/N) hold for tit-for-tat vs always-defect in a Moran process (N = 100, weak selection 0.005, w = 0.5, AD threshold b/c = 4)? | V1 Pass; V2 Pass; H1 Supported; H2 Not supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: Five benefit-to-cost rules sourced (AL0-FOR-01); thresholds reproduced and the 1/3 rule checked at N = 100, finite-N crossing not supported (AL0-FOR-02).

## Unresolved
- Finite-N correction to the 1/3 rule unsourced; H2 not supported at N = 100.
- Only the reciprocity rules were checked by simulation.
