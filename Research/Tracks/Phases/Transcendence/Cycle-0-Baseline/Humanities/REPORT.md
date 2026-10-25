# Transcendence in the Humanities — Cycle-0-Baseline (TR0)

Phase report: Transcendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
Baseline: the sublime from nature vs art in VR (P101); statistics consistent, one Bayes-factor wording not supported.

## Claims (ledger: `claims/claims.csv`)
- **TR0-HUM-02** [E] P101's Table 2 is internally consistent: Cohen's d = t/sqrt(50) and two-sided p from t(49) reproduce for all eight sublime dimensions (largest gaps 7e-5 and 0.0007), t has the sign of art minus nature throughout, and the printed means, SDs and t imply between-condition correlations of 0.09 to 0.55. One pre-registered check was not supported: Table 2's vastness BF01 is 0.968, so the text's 'strong evidence for H 1' for vastness and danger holds only for danger (BF01 4e-5). *Operationalization:* HUM Transcendence = auditing a sublime study. *Sources:* SIM-TR-HUM-0/iter-1#V1;SIM-TR-HUM-0/iter-1#H1;SIM-TR-HUM-0/iter-1#H2;SIM-TR-HUM-0/iter-1#H3;SIM-TR-HUM-0/iter-1#H4;SIM-TR-HUM-0/iter-1#H5. *Limits:* Audits printed numbers; the BF check compares wording with printed values, not a recomputed Bayes factor.
- **TR0-HUM-01** [P] In a within-subject virtual-reality study (n 50, 39 women), natural scenes elicited more perceived existential danger than artistic ones (22.34 vs 16.38; t(49) -5.72, d -0.81) and somewhat more vastness (29.4 vs 27.18, p 0.047), while self-transcendence, beauty and the overall feeling of the sublime did not differ (sublime BF10 0.164). P101 concludes that there was no significant difference in the capacity of art-based and nature-based stimuli to evoke the sublime. *Operationalization:* HUM Transcendence = the sublime and self-transcendence elicited by nature and art. *Sources:* P101. *Limits:* Small sample, one VR content set per condition. Slips: the text gives vastness BF01 = 1.033 while Table 2 prints 0.968, and calls vastness and danger 'strong evidence for H 1' although a BF01 near 1 is no evidence either way; the DFAS 'maximum of 15'; ITC-SOPI anchors printed 'strongly disagree' at both ends; an ecological-validity BF printed '100.128.094'.

## Simulations (SIM-TR-HUM-0; 1 iteration(s), spec-first; validation 1/1, hypotheses supported 4/5)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `3f3ae95e` | P101's Table 2: do Cohen's d and p follow from t(49), does t's sign match art minus nature, are means, SDs and t mutually consistent (implied correlation in [-1, 1]), and do the BF01 values support the text's 'strong evidence' wording? | V1 Pass; H1 Supported; H2 Supported; H3 Supported; H4 Supported; H5 Not supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: Nature vs art sublime VR study sourced (TR0-HUM-01); audit: d and p reproduce for all eight dimensions; the vastness 'strong evidence' wording is not supported by Table 2's BF01 (TR0-HUM-02).

## Unresolved
- BF01 vastness 1.033 (text) vs 0.968 (table) unresolved; Bayes factors not recomputed (raw data not used).
- Non-VR studies of awe and self-transcendence not yet read.
