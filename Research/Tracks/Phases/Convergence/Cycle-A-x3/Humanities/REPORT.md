# Convergence in the Humanities — Cycle-A-x3 (CVA)

Phase report: Convergence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x3: a minimal exemplar toy gives P71's main effects but not its task x frequency interaction; P71's remaining arithmetic is consistent.

## Claims (ledger: `claims/claims.csv`)
- **CVA-HUM-02** [E] P71's statistics are internally consistent: all ten BIC values equal AIC + df (ln 1138 - 2) within 0.01; every LR chi-square equals the AIC-implied value within 0.01; every z equals beta/SE within 0.03 and every printed p follows from its z within 0.0011; percentages and counts add up. The pre-registered p-tolerance (0.002) for the LR tests was not supported for M3 vs M2 (0.5839 vs 0.5797) and M5 vs M4 (0.5967 vs 0.6000): differences within the rounding of two-decimal AIC values, so this is a tolerance artefact, not an error in P71. *Operationalization:* HUM Convergence = auditing a convergence study. *Sources:* SIM-CV-HUM-0/iter-1#V1;SIM-CV-HUM-0/iter-1#H1;SIM-CV-HUM-0/iter-1#H2;SIM-CV-HUM-0/iter-1#H3;SIM-CV-HUM-0/iter-1#H4. *Limits:* Audits reported numbers only; the model fits themselves were not rerun (data not used).
- **CVA-HUM-04** [E] P71's Table 1 rows and totals and its questionnaire shares (82.1 + 14.8 + 3.1 = 100) add up, and the in-text chi-square p values recompute (0.63 on 1 df: 0.4274 vs 0.4277). The overall 82.1% implies subgroup weights 0.52 (frequency), 0.81 (P->F direction) and 0.69 (female); the P->F weight is 0.06 from Table 1's 46/61 session share (exploratory hypothesis not supported; questionnaire counts are not reported). *Operationalization:* HUM Convergence = auditing a convergence study. *Sources:* SIM-CV-HUM-A/iter-3#V1;SIM-CV-HUM-A/iter-3#H1;SIM-CV-HUM-A/iter-3#H2;SIM-CV-HUM-A/iter-3#H3;SIM-CV-HUM-A/iter-3#H4. *Limits:* Counts behind the questionnaire percentages are not given.
- **CVA-HUM-01** [P] In shadowing and interactive tasks with German speakers, phonetic accommodation of -ig toward a model talker's variant occurred in 53.5% of shadowing trials (301/563) and 27.3% of interaction trials (157/575); a binomial mixed model selected by likelihood-ratio tests (final M4) shows accommodation growing with exposure order and a task x frequency x gender interaction, with low-frequency words accommodating more in shadowing. *Operationalization:* HUM Convergence = phonetic convergence (accommodation). *Sources:* P71. *Limits:* One variable, one dialect pair; M9 had lower AIC and BIC but was rejected for separation instability; P71 discloses ChatGPT use for language editing.
- **CVA-HUM-03** [H] A minimal exemplar model of P71's entrenchment account (100 vs 10 stored exemplars; attention 1.0 vs 0.3) gives more accommodation for low-frequency words (0.244 vs 0.034 in shadowing), more in shadowing, and growth over exposure, but its logit-scale task x frequency interaction is about 0 (-0.06; 0.06 with decay), not > 0.5: not supported, so P71's positive task x frequency coefficient (1.68) needs more than proportional exemplar updating. *Operationalization:* HUM Convergence = phonetic convergence via exemplars. *Sources:* SIM-CV-HUM-A/iter-1#V1;SIM-CV-HUM-A/iter-1#H1;SIM-CV-HUM-A/iter-1#H2;SIM-CV-HUM-A/iter-1#H3;SIM-CV-HUM-A/iter-1#H4;SIM-CV-HUM-A/iter-2#V1;SIM-CV-HUM-A/iter-2#H1;SIM-CV-HUM-A/iter-2#H2. *Limits:* Toy; parameters arbitrary; foreknown from arithmetic (disclosed).

## Simulations (SIM-CV-HUM-A; 3 iteration(s), spec-first; validation 3/3, hypotheses supported 7/10)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `c6537a04` | P71's entrenchment account as an exemplar toy (N 100 vs 10 stored exemplars; attention 1.0 shadowing vs 0.3 interaction; 6 tokens per word): does it give more accommodation for low-frequency words and in shadowing, a positive task x frequency interaction on the logit scale (> 0.5, the sign of P71's beta 1.68), and an order effect? | V1 Pass; H1 Supported; H2 Supported; H3 Not supported; H4 Supported; R1 Reported |
| 2 | `0ffb19f3` | Exemplar toy with memory decay 0.3 per trial: does the frequency effect survive and does the logit task x frequency interaction exceed 0.5? | V1 Pass; H1 Supported; H2 Not supported; R1 Reported |
| 3 | `92ea5afd` | P71's Table 1 counts, questionnaire shares and in-text chi-squares: do they add up and recompute, and are the subgroup questionnaire percentages consistent with the overall 82.1%? | V1 Pass; H1 Supported; H2 Supported; H3 Supported; H4 Not supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (3; details `research/PASSES.md`)
- Pass 1: CVA-HUM-03: exemplar toy gives the main effects but not the logit interaction (not supported).
- Pass 2: Added nothing new: exemplar decay (CVA-HUM-03, iter-2) leaves the CVA iter-1 pattern unchanged.
- Pass 3: CVA-HUM-04: Table 1 and questionnaire arithmetic audited.

## Unresolved
- What produces P71's task x frequency interaction is open (attention thresholds? non-linear exemplar weighting?).
- Questionnaire counts not reported.
