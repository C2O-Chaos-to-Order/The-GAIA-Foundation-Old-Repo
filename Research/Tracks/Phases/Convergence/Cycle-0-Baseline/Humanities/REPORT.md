# Convergence in the Humanities — Cycle-0-Baseline (CV0)

Phase report: Convergence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
Baseline: phonetic convergence (P71); its model-selection and coefficient tables are internally consistent.

## Claims (ledger: `claims/claims.csv`)
- **CV0-HUM-02** [E] P71's statistics are internally consistent: all ten BIC values equal AIC + df (ln 1138 - 2) within 0.01; every LR chi-square equals the AIC-implied value within 0.01; every z equals beta/SE within 0.03 and every printed p follows from its z within 0.0011; percentages and counts add up. The pre-registered p-tolerance (0.002) for the LR tests was not supported for M3 vs M2 (0.5839 vs 0.5797) and M5 vs M4 (0.5967 vs 0.6000): differences within the rounding of two-decimal AIC values, so this is a tolerance artefact, not an error in P71. *Operationalization:* HUM Convergence = auditing a convergence study. *Sources:* SIM-CV-HUM-0/iter-1#V1;SIM-CV-HUM-0/iter-1#H1;SIM-CV-HUM-0/iter-1#H2;SIM-CV-HUM-0/iter-1#H3;SIM-CV-HUM-0/iter-1#H4. *Limits:* Audits reported numbers only; the model fits themselves were not rerun (data not used).
- **CV0-HUM-01** [P] In shadowing and interactive tasks with German speakers, phonetic accommodation of -ig toward a model talker's variant occurred in 53.5% of shadowing trials (301/563) and 27.3% of interaction trials (157/575); a binomial mixed model selected by likelihood-ratio tests (final M4) shows accommodation growing with exposure order and a task x frequency x gender interaction, with low-frequency words accommodating more in shadowing. *Operationalization:* HUM Convergence = phonetic convergence (accommodation). *Sources:* P71. *Limits:* One variable, one dialect pair; M9 had lower AIC and BIC but was rejected for separation instability; P71 discloses ChatGPT use for language editing.

## Simulations (SIM-CV-HUM-0; 1 iteration(s), spec-first; validation 1/1, hypotheses supported 3/4)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `66aa0e78` | P71's statistics: do Table 2's BIC values follow from AIC and df (n 1138), do its LR chi-squares and p values follow from AIC differences, do Table 3's z and p follow from beta/SE, and do the printed percentages and counts add up? | V1 Pass; H1 Supported; H2 Not supported; H3 Supported; H4 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: Task-dependent phonetic accommodation sourced (CV0-HUM-01); Tables 2-3 audited, internally consistent; one p-tolerance hypothesis not supported by rounding (CV0-HUM-02).

## Unresolved
- The GLMM fit itself not rerun; only reported numbers audited.
- Other kinds of convergence in language (dialect levelling) not covered.
