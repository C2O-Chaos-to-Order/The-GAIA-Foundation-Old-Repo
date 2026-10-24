# Allegiance in the Applied Sciences — Cycle-A-x3 (ALA)

Phase report: Allegiance (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x3: P49's null stays weak under every variant: power 0.18-0.58 even with more heterogeneity, imbalance, or twice the studies.

## Claims (ledger: `claims/claims.csv`)
- **ALA-APP-01** [E] Researcher allegiance, 'a belief in the superiority of a treatment', was coded in 50 RCTs comparing humanistic with other psychotherapies; at end of treatment allegiance against humanistic therapy was not a significant moderator (beta = -0.183, SE 0.125, p = .144, N = 47), only 10% of studies showed allegiance in favour of humanistic therapy, and allegiance was significant in 2 of 5 comparisons; the authors conclude allegiance 'was not as relevant as expected' while noting absence of evidence is not evidence of absence. *Operationalization:* APP Allegiance = researcher allegiance in clinical trials. *Sources:* P49. *Limits:* One meta-analysis of one therapy family; allegiance coded from publications.
- **ALA-APP-02** [P] With P49's own estimate (beta = -0.183, SE = 0.125) the reported p was reproduced (0.143) and the two-sided power to detect a moderator of that size at alpha 0.05 was only 0.31; a simulated 47-study random-effects meta-regression gave SE 0.124 and power 0.33. P49's null for allegiance is therefore weak evidence of no effect, as P49 itself cautions; by chance alone, at least 2 of 5 independent null tests would be significant 2.3% of the time. *Operationalization:* APP Allegiance = power to detect allegiance effects. *Sources:* SIM-AL-APP-0/iter-1#V1;SIM-AL-APP-0/iter-1#H1;SIM-AL-APP-0/iter-1#H2. *Limits:* Simulated design (moderator share 0.3, tau 0.25, study SE 0.2-0.4) assumed; the five comparisons are not independent in P49.
- **ALA-APP-03** [P] With more heterogeneity (tau 0.4 instead of 0.25) the simulated 47-study meta-regression has SE 0.161 and power 0.22 for P49's moderator size, so the AL0 match to P49's SE 0.125 is not supported under this setting; P49's reported SE fits low-to-moderate heterogeneity in this design. *Operationalization:* APP Allegiance = power under heterogeneity. *Sources:* SIM-AL-APP-A/iter-1#V1;SIM-AL-APP-A/iter-1#H1;SIM-AL-APP-A/iter-1#H2. *Limits:* Design values (study SEs 0.2-0.4, moderator share 0.3) are the agent's.
- **ALA-APP-04** [P] Doubling the number of studies to K = 100 lowers the moderator SE to 0.085 and raises power to 0.58 (H2, designed for K = 47, not supported as expected): even a meta-analysis twice the size of P49's would miss a true allegiance effect of P49's estimated size about 4 times in 10. *Operationalization:* APP Allegiance = studies needed to detect allegiance. *Sources:* SIM-AL-APP-A/iter-2#V1;SIM-AL-APP-A/iter-2#H1;SIM-AL-APP-A/iter-2#H2. *Limits:* Simple scaling design; real meta-analyses have correlated moderators.
- **ALA-APP-05** [P] If only 10% of studies fall in the moderator category, the SE rises to 0.194 and power falls to 0.18 (H2 not supported): unbalanced allegiance coding, as P49's 10% figure suggests is common, makes allegiance effects even harder to detect. *Operationalization:* APP Allegiance = power with unbalanced allegiance. *Sources:* SIM-AL-APP-A/iter-3#V1;SIM-AL-APP-A/iter-3#H1;SIM-AL-APP-A/iter-3#H2. *Limits:* The mapping of P49's 10% to the moderator category is illustrative.

## Simulations (SIM-AL-APP-A; 3 iteration(s), spec-first; validation 3/3, hypotheses supported 3/6)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `ed30c381` | Sensitivity to heterogeneity: with tau = 0.4 instead of 0.25, does the simulated 47-study design still give a moderator SE near P49's 0.125 and power near the analytic 0.31? | V1 Pass; H1 Supported; H2 Not supported; R1 Reported |
| 2 | `6e31b8de` | How many studies would be needed? With K = 100 studies (otherwise as AL0), what SE and power would a meta-regression have for a moderator of P49's size? | V1 Pass; H1 Supported; H2 Not supported; R1 Reported |
| 3 | `ffd9d595` | Unbalanced moderator: if only 10% of studies fall in the allegiance category (P49: 'Only 10% of the studies showed allegiance in favour of HPT'), is the design's SE larger than P49's 0.125? | V1 Pass; H1 Supported; H2 Not supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (3; details `research/PASSES.md`)
- Pass 1: ALA-APP-03: with tau 0.4 the design's SE is 0.161 (match to P49 not supported).
- Pass 2: ALA-APP-04: K = 100 studies give power 0.58.
- Pass 3: ALA-APP-05: a 10% moderator share gives power 0.18.

## Unresolved
- No second meta-analysis of researcher allegiance read; design values assumed.
- Correlated moderators not modelled.
