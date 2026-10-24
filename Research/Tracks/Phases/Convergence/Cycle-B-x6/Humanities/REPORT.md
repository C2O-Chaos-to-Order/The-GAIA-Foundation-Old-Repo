# Convergence in the Humanities — Cycle-B-x6 (CVB)

Phase report: Convergence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x6: an exemplar-independent floor in the interaction task gives the toy the sign of P71's interaction; without it the interaction stays near zero.

## Claims (ledger: `claims/claims.csv`)
- **CVB-HUM-02** [E] P71's statistics are internally consistent: all ten BIC values equal AIC + df (ln 1138 - 2) within 0.01; every LR chi-square equals the AIC-implied value within 0.01; every z equals beta/SE within 0.03 and every printed p follows from its z within 0.0011; percentages and counts add up. The pre-registered p-tolerance (0.002) for the LR tests was not supported for M3 vs M2 (0.5839 vs 0.5797) and M5 vs M4 (0.5967 vs 0.6000): differences within the rounding of two-decimal AIC values, so this is a tolerance artefact, not an error in P71. *Operationalization:* HUM Convergence = auditing a convergence study. *Sources:* SIM-CV-HUM-0/iter-1#V1;SIM-CV-HUM-0/iter-1#H1;SIM-CV-HUM-0/iter-1#H2;SIM-CV-HUM-0/iter-1#H3;SIM-CV-HUM-0/iter-1#H4. *Limits:* Audits reported numbers only; the model fits themselves were not rerun (data not used).
- **CVB-HUM-04** [E] P71's Table 1 rows and totals and its questionnaire shares (82.1 + 14.8 + 3.1 = 100) add up, and the in-text chi-square p values recompute (0.63 on 1 df: 0.4274 vs 0.4277). The overall 82.1% implies subgroup weights 0.52 (frequency), 0.81 (P->F direction) and 0.69 (female); the P->F weight is 0.06 from Table 1's 46/61 session share (exploratory hypothesis not supported; questionnaire counts are not reported). *Operationalization:* HUM Convergence = auditing a convergence study. *Sources:* SIM-CV-HUM-A/iter-3#V1;SIM-CV-HUM-A/iter-3#H1;SIM-CV-HUM-A/iter-3#H2;SIM-CV-HUM-A/iter-3#H3;SIM-CV-HUM-A/iter-3#H4. *Limits:* Counts behind the questionnaire percentages are not given.
- **CVB-HUM-01** [P] In shadowing and interactive tasks with German speakers, phonetic accommodation of -ig toward a model talker's variant occurred in 53.5% of shadowing trials (301/563) and 27.3% of interaction trials (157/575); a binomial mixed model selected by likelihood-ratio tests (final M4) shows accommodation growing with exposure order and a task x frequency x gender interaction, with low-frequency words accommodating more in shadowing. *Operationalization:* HUM Convergence = phonetic convergence (accommodation). *Sources:* P71. *Limits:* One variable, one dialect pair; M9 had lower AIC and BIC but was rejected for separation instability; P71 discloses ChatGPT use for language editing.
- **CVB-HUM-03** [H] A minimal exemplar model of P71's entrenchment account (100 vs 10 stored exemplars; attention 1.0 vs 0.3) gives more accommodation for low-frequency words (0.244 vs 0.034 in shadowing), more in shadowing, and growth over exposure, but its logit-scale task x frequency interaction is about 0 (-0.06; 0.06 with decay), not > 0.5: not supported, so P71's positive task x frequency coefficient (1.68) needs more than proportional exemplar updating. *Operationalization:* HUM Convergence = phonetic convergence via exemplars. *Sources:* SIM-CV-HUM-A/iter-1#V1;SIM-CV-HUM-A/iter-1#H1;SIM-CV-HUM-A/iter-1#H2;SIM-CV-HUM-A/iter-1#H3;SIM-CV-HUM-A/iter-1#H4;SIM-CV-HUM-A/iter-2#V1;SIM-CV-HUM-A/iter-2#H1;SIM-CV-HUM-A/iter-2#H2. *Limits:* Toy; parameters arbitrary; foreknown from arithmetic (disclosed).
- **CVB-HUM-05** [H] In the exemplar toy of P71's entrenchment account, an exemplar-independent floor of accommodation in the interaction task (0.2 or 0.05) produced a positive logit task x frequency interaction (1.92 and 1.37), the sign of P71's 1.68; the same floor in both tasks reduced it to 0.46; without floors it stayed small (-0.18 at interaction attention 0.1, 0.003 with 1000 high-frequency exemplars, -0.09 with 20 tokens per word). Low-frequency words accommodated more in every run, and later tokens more than earlier ones. Two hypotheses were not supported (the -0.18 is not 'near zero'; 0.46 is below the pre-set 0.5). *Operationalization:* HUM Convergence = phonetic convergence via exemplars. *Sources:* SIM-CV-HUM-B/iter-1#V1;SIM-CV-HUM-B/iter-1#H1;SIM-CV-HUM-B/iter-1#H2;SIM-CV-HUM-B/iter-2#V1;SIM-CV-HUM-B/iter-2#H1;SIM-CV-HUM-B/iter-2#H2;SIM-CV-HUM-B/iter-3#V1;SIM-CV-HUM-B/iter-3#H1;SIM-CV-HUM-B/iter-3#H2;SIM-CV-HUM-B/iter-4#V1;SIM-CV-HUM-B/iter-4#H1;SIM-CV-HUM-B/iter-4#H2;SIM-CV-HUM-B/iter-5#V1;SIM-CV-HUM-B/iter-5#H1;SIM-CV-HUM-B/iter-5#H2;SIM-CV-HUM-B/iter-6#V1;SIM-CV-HUM-B/iter-6#H1;SIM-CV-HUM-B/iter-6#H2;SIM-CV-HUM-B/iter-6#H3. *Limits:* Toy; parameters arbitrary; one mechanism among several that could produce the interaction. Two of thirteen hypotheses not supported (iter-1 H2, iter-5 H2).

## Simulations (SIM-CV-HUM-B; 6 iteration(s), spec-first; validation 6/6, hypotheses supported 11/13)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `b194af77` | Exemplar toy with weak interaction attention (0.1): is the logit task x frequency interaction near zero (|x| < 0.15)? | V1 Pass; H1 Supported; H2 Not supported; R1 Reported |
| 2 | `89d56f31` | Exemplar toy with a 100-fold frequency contrast (N 1000 vs 10): is the interaction still near zero? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |
| 3 | `61f679ad` | Candidate mechanism for P71's positive interaction: a word-independent accommodation floor of 0.2 in interaction only. Does it give a logit interaction > 0.5? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |
| 4 | `6ccd5fec` | Same with a floor of 0.05: is a small global component enough for an interaction > 0.5? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |
| 5 | `91631a70` | Same floor (0.2) in both tasks: is the interaction still > 0.5? | V1 Pass; H1 Supported; H2 Not supported; R1 Reported |
| 6 | `db74c92a` | Longer exposure (20 tokens per word): interaction near zero and order effect in every cell? | V1 Pass; H1 Supported; H2 Supported; H3 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (6; details `research/PASSES.md`)
- Pass 1: CVB-HUM-05: lower interaction attention gives a slightly negative interaction (not supported as 'near zero').
- Pass 2: Added nothing new: 1000 high-frequency exemplars leave the interaction at about 0 (as CVA).
- Pass 3: CVB-HUM-05: an exemplar-independent floor in the interaction task gives a positive interaction (1.92).
- Pass 4: CVB-HUM-05: a smaller floor (0.05) still gives 1.37.
- Pass 5: CVB-HUM-05: floors in both tasks reduce it to 0.46 (not supported).
- Pass 6: Added nothing new: 20 tokens per word repeat the null interaction and the order effect already seen in CVA.

## Unresolved
- Whether speakers show an exemplar-independent accommodation floor (the toy's mechanism for P71's interaction) is untested against data.
- Questionnaire counts not reported in P71.
