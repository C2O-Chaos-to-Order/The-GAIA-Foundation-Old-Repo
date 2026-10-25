# Transcendence in the Humanities — Cycle-B-x6 (TRB)

Phase report: Transcendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x6: small studies need t near 2.75 for moderate evidence; Pahnke's count difference is not significant two-sided.

## Claims (ledger: `claims/claims.csv`)
- **TRB-HUM-02** [E] P101's Table 2 is internally consistent: Cohen's d = t/sqrt(50) and two-sided p from t(49) reproduce for all eight sublime dimensions (largest gaps 7e-5 and 0.0007), t has the sign of art minus nature throughout, and the printed means, SDs and t imply between-condition correlations of 0.09 to 0.55. One pre-registered check was not supported: Table 2's vastness BF01 is 0.968, so the text's 'strong evidence for H 1' for vastness and danger holds only for danger (BF01 4e-5). *Operationalization:* HUM Transcendence = auditing a sublime study. *Sources:* SIM-TR-HUM-0/iter-1#V1;SIM-TR-HUM-0/iter-1#H1;SIM-TR-HUM-0/iter-1#H2;SIM-TR-HUM-0/iter-1#H3;SIM-TR-HUM-0/iter-1#H4;SIM-TR-HUM-0/iter-1#H5. *Limits:* Audits printed numbers; the BF check compares wording with printed values, not a recomputed Bayes factor.
- **TRB-HUM-03** [E] Default JZS Bayes factors (Cauchy scale 0.707) recomputed from P101's t and n 50 reproduce all eight printed BF01 within 0.3% (vastness 0.968, danger 3.96e-5), so Table 2 is right and the text's 'BF 01 = 1.033' for vastness is its reciprocal (BF10). Vastness gives no evidence either way (BF01 0.78-1.71 for scales 0.5-1.414), while existential danger gives extreme evidence for a difference at every scale (BF01 below 5e-5). *Operationalization:* HUM Transcendence = recomputing sublime Bayes factors. *Sources:* SIM-TR-HUM-A/iter-1#V1;SIM-TR-HUM-A/iter-1#H1;SIM-TR-HUM-A/iter-1#H2;SIM-TR-HUM-A/iter-1#H3;SIM-TR-HUM-A/iter-2#V1;SIM-TR-HUM-A/iter-2#H1;SIM-TR-HUM-A/iter-2#H2. *Limits:* Assumes JASP's default prior (P101 does not state the scale).
- **TRB-HUM-04** [E] Applied to P103's paired changes (n 34), default JZS Bayes factors give extreme evidence for change in self-transcendence (BF01 3.5e-8), overall and existential spiritual well-being, depression and negative affect, strong evidence for positive affect (BF01 0.021), and no evidence for religious spiritual well-being (1.30) or life satisfaction (1.45) despite one-tailed p values near .04. *Operationalization:* HUM Transcendence = evidence strength in a self-transcendence intervention. *Sources:* SIM-TR-HUM-A/iter-3#V1;SIM-TR-HUM-A/iter-3#H1;SIM-TR-HUM-A/iter-3#H2. *Limits:* Two-sided default test; P103's design has no control group, so evidence for change is not evidence for an effect of the programme.
- **TRB-HUM-05** [E] With default JZS priors a t near 2 (p about .05) gives no evidence either way at n 50 (BF01 1.04) or n 34 (0.93), and BF01 falls below 1/3 only near t 2.75 at both sizes; at n 10 even t 3.0 leaves BF01 at 0.22 and t 3.5 at 0.12. P103's evidence pattern is stable across prior scales 0.5 and 1 (self-transcendence BF01 below 1e-7; life satisfaction 1.16 to 1.88; religious well-being 1.05 to 1.69). *Operationalization:* HUM Transcendence = evidence thresholds for small self-transcendence studies. *Sources:* SIM-TR-HUM-B/iter-1#V1;SIM-TR-HUM-B/iter-1#H1;SIM-TR-HUM-B/iter-2#V1;SIM-TR-HUM-B/iter-2#H1;SIM-TR-HUM-B/iter-3#V1;SIM-TR-HUM-B/iter-3#H1;SIM-TR-HUM-B/iter-4#V1;SIM-TR-HUM-B/iter-4#H1;SIM-TR-HUM-B/iter-6#V1;SIM-TR-HUM-B/iter-6#H1. *Limits:* Default Cauchy priors only.
- **TRB-HUM-06** [E] The Pahnke result as P105 reports it, 4 of 10 psilocybin subjects vs 0 of 10 placebo subjects reaching a 'complete mystical experience', gives Fisher's exact p 0.087 two-sided (0.043 one-sided): on its own that count difference is not significant at the two-sided .05 level; P105 also reports that all psilocybin subjects scored significantly higher on all components, which this check does not test. *Operationalization:* HUM Transcendence = small-sample evidence for drug-induced mystical experience. *Sources:* SIM-TR-HUM-B/iter-5#V1;SIM-TR-HUM-B/iter-5#H1;SIM-TR-HUM-B/iter-5#H2. *Limits:* Counts only as P105 reports them; Pahnke's original analysis not read.
- **TRB-HUM-01** [P] In a within-subject virtual-reality study (n 50, 39 women), natural scenes elicited more perceived existential danger than artistic ones (22.34 vs 16.38; t(49) -5.72, d -0.81) and somewhat more vastness (29.4 vs 27.18, p 0.047), while self-transcendence, beauty and the overall feeling of the sublime did not differ (sublime BF10 0.164). P101 concludes that there was no significant difference in the capacity of art-based and nature-based stimuli to evoke the sublime. *Operationalization:* HUM Transcendence = the sublime and self-transcendence elicited by nature and art. *Sources:* P101. *Limits:* Small sample, one VR content set per condition. Slips: the text gives vastness BF01 = 1.033 while Table 2 prints 0.968, and calls vastness and danger 'strong evidence for H 1' although a BF01 near 1 is no evidence either way; the DFAS 'maximum of 15'; ITC-SOPI anchors printed 'strongly disagree' at both ends; an ecological-validity BF printed '100.128.094'.

## Simulations (SIM-TR-HUM-B; 6 iteration(s), spec-first; validation 6/6, hypotheses supported 7/7)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `3a3ad821` | P103 with Cauchy scale 1: do life satisfaction and religious well-being still give BF01 > 1/3? | V1 Pass; H1 Supported; R1 Reported |
| 2 | `cf4c4783` | P103 with Cauchy scale 0.5: does self-transcendence still give BF01 < 1/100? | V1 Pass; H1 Supported; R1 Reported |
| 3 | `8783eca5` | n 50 (P101's size): what t is needed for BF01 < 1/3? | V1 Pass; H1 Supported; R1 Reported |
| 4 | `ec23da9c` | n 34 (P103's size): does t 2.0 give BF01 > 1/3? | V1 Pass; H1 Supported; R1 Reported |
| 5 | `ed3576e3` | P105's report of Pahnke (4/10 vs 0/10 'complete mystical experience'): significant by Fisher's exact test? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |
| 6 | `d9f00f93` | n 10 (Pahnke's group size): can t 3.0 give BF01 below 1/10? | V1 Pass; H1 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (6; details `research/PASSES.md`)
- Pass 1: TRB-HUM-05: P103's evidence pattern at prior scale 1.
- Pass 2: TRB-HUM-05 (scale 0.5, iteration 2): pattern unchanged.
- Pass 3: TRB-HUM-05 (n 50, iteration 3): BF01 < 1/3 needs t about 2.75.
- Pass 4: TRB-HUM-05 (n 34, iteration 4): t 2.0 gives BF01 0.93.
- Pass 5: TRB-HUM-06: Pahnke's 4/10 vs 0/10 (as P105 reports it): Fisher two-sided p 0.087.
- Pass 6: TRB-HUM-05 (n 10, iteration 6): t 3.0 gives BF01 0.22.

## Unresolved
- Pahnke's original report (1966) not read; P105's counts used.
- Non-VR studies of awe not yet read.
