# Transcendence in the Humanities — Cycle-A-x3 (TRA)

Phase report: Transcendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x3: P101's Bayes factors reproduce (text prints a reciprocal); P103's changes graded by Bayes factor.

## Claims (ledger: `claims/claims.csv`)
- **TRA-HUM-02** [E] P101's Table 2 is internally consistent: Cohen's d = t/sqrt(50) and two-sided p from t(49) reproduce for all eight sublime dimensions (largest gaps 7e-5 and 0.0007), t has the sign of art minus nature throughout, and the printed means, SDs and t imply between-condition correlations of 0.09 to 0.55. One pre-registered check was not supported: Table 2's vastness BF01 is 0.968, so the text's 'strong evidence for H 1' for vastness and danger holds only for danger (BF01 4e-5). *Operationalization:* HUM Transcendence = auditing a sublime study. *Sources:* SIM-TR-HUM-0/iter-1#V1;SIM-TR-HUM-0/iter-1#H1;SIM-TR-HUM-0/iter-1#H2;SIM-TR-HUM-0/iter-1#H3;SIM-TR-HUM-0/iter-1#H4;SIM-TR-HUM-0/iter-1#H5. *Limits:* Audits printed numbers; the BF check compares wording with printed values, not a recomputed Bayes factor.
- **TRA-HUM-03** [E] Default JZS Bayes factors (Cauchy scale 0.707) recomputed from P101's t and n 50 reproduce all eight printed BF01 within 0.3% (vastness 0.968, danger 3.96e-5), so Table 2 is right and the text's 'BF 01 = 1.033' for vastness is its reciprocal (BF10). Vastness gives no evidence either way (BF01 0.78-1.71 for scales 0.5-1.414), while existential danger gives extreme evidence for a difference at every scale (BF01 below 5e-5). *Operationalization:* HUM Transcendence = recomputing sublime Bayes factors. *Sources:* SIM-TR-HUM-A/iter-1#V1;SIM-TR-HUM-A/iter-1#H1;SIM-TR-HUM-A/iter-1#H2;SIM-TR-HUM-A/iter-1#H3;SIM-TR-HUM-A/iter-2#V1;SIM-TR-HUM-A/iter-2#H1;SIM-TR-HUM-A/iter-2#H2. *Limits:* Assumes JASP's default prior (P101 does not state the scale).
- **TRA-HUM-04** [E] Applied to P103's paired changes (n 34), default JZS Bayes factors give extreme evidence for change in self-transcendence (BF01 3.5e-8), overall and existential spiritual well-being, depression and negative affect, strong evidence for positive affect (BF01 0.021), and no evidence for religious spiritual well-being (1.30) or life satisfaction (1.45) despite one-tailed p values near .04. *Operationalization:* HUM Transcendence = evidence strength in a self-transcendence intervention. *Sources:* SIM-TR-HUM-A/iter-3#V1;SIM-TR-HUM-A/iter-3#H1;SIM-TR-HUM-A/iter-3#H2. *Limits:* Two-sided default test; P103's design has no control group, so evidence for change is not evidence for an effect of the programme.
- **TRA-HUM-01** [P] In a within-subject virtual-reality study (n 50, 39 women), natural scenes elicited more perceived existential danger than artistic ones (22.34 vs 16.38; t(49) -5.72, d -0.81) and somewhat more vastness (29.4 vs 27.18, p 0.047), while self-transcendence, beauty and the overall feeling of the sublime did not differ (sublime BF10 0.164). P101 concludes that there was no significant difference in the capacity of art-based and nature-based stimuli to evoke the sublime. *Operationalization:* HUM Transcendence = the sublime and self-transcendence elicited by nature and art. *Sources:* P101. *Limits:* Small sample, one VR content set per condition. Slips: the text gives vastness BF01 = 1.033 while Table 2 prints 0.968, and calls vastness and danger 'strong evidence for H 1' although a BF01 near 1 is no evidence either way; the DFAS 'maximum of 15'; ITC-SOPI anchors printed 'strongly disagree' at both ends; an ecological-validity BF printed '100.128.094'.

## Simulations (SIM-TR-HUM-A; 3 iteration(s), spec-first; validation 3/3, hypotheses supported 7/7)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `0117a589` | Do default JZS Bayes factors (Cauchy 0.707) recomputed from P101's t and n 50 reproduce Table 2's BF01, and what do they say about vastness and danger? | V1 Pass; H1 Supported; H2 Supported; H3 Supported; R1 Reported |
| 2 | `0611b428` | Prior sensitivity: do the vastness and danger conclusions hold for Cauchy scales 0.5, 1 and 1.414? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |
| 3 | `156823fe` | Bayes factors for P103's paired changes (n 34): strong for self-transcendence, not for life satisfaction? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (3; details `research/PASSES.md`)
- Pass 1: TRA-HUM-03: P101's Table 2 BF01 reproduce; the text's 1.033 is the reciprocal.
- Pass 2: TRA-HUM-03 (prior sensitivity, iteration 2): vastness no evidence either way at every scale.
- Pass 3: TRA-HUM-04: P103's changes: extreme evidence for most, none for life satisfaction or religious well-being.

## Unresolved
- P101's prior scale assumed (JASP default).
- Non-VR studies of awe and self-transcendence not yet read.
