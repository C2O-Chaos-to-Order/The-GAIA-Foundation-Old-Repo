# Ascendence in the Humanities — Cycle-0-Baseline (AS0)

Phase report: Ascendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
Baseline: rising intonation in Liverpool (P89); internally consistent statistics, one contour-label slip.

## Claims (ledger: `claims/claims.csv`)
- **AS0-HUM-02** [E] P89's statistics are internally consistent: every LRT p reproduces from its chi-square and df within 0.009 (largest gap: City x Gender in the nuclear model, 0.699 vs printed 0.69, within the rounding of chi-square 0.15), all '<0.001' entries are below 0.001; F0 gender chi2(1) 2.82 gives p 0.093; Lawton's 1349% follows from 34,500 to 500,000 (1349.3%); the rise-plateau-slump percentages imply about 47 tokens per male and 46 per female Liverpool speaker; the F0 means imply about 71 female of 138 values. *Operationalization:* HUM Ascendence = auditing an intonation study. *Sources:* SIM-AS-HUM-0/iter-1#V1;SIM-AS-HUM-0/iter-1#H1;SIM-AS-HUM-0/iter-1#H2;SIM-AS-HUM-0/iter-1#H3;SIM-AS-HUM-0/iter-1#H4. *Limits:* Audits printed numbers only; the GLMMs were not refitted (data not used); equal token contribution per speaker is the agent's assumption.
- **AS0-HUM-01** [P] P89 finds that Liverpool English is characterised by low and rising contours: the most common phrase-final contour in Liverpool is L* L-H% (Knowles' 'rise'; 54% of tokens vs 7% in Manchester), with rise-plateau-slump used more by men (145 tokens, 34%) than women (48, 13%); Manchester uses mainly falls (H* L-L%), and very high final rises (possible HRT) were only six of 495 declaratives, all in Manchester. P89 argues the Liverpool rise came from new-dialect formation after rapid nineteenth-century growth (Lawton: 1349% in 1773-1871) with Irish input, a case where a minority variant was favoured. *Operationalization:* HUM Ascendence = rising intonation in Liverpool English. *Sources:* P89. *Limits:* Read speech only; the historical account is argued, not tested. Slip: the text labels the Liverpool 'rise' L* H-H% in the results summary and in the Fig. 3 caption, although it defines L* H-H% as the 'rise-plateau' and tests L* L-H% as the most common Liverpool contour.

## Simulations (SIM-AS-HUM-0; 1 iteration(s), spec-first; validation 1/1, hypotheses supported 4/4)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `f019988b` | P89's statistics: do the printed LRT chi-squares and df give the printed p-values, does Lawton's 1349% follow from 34,500 to 500,000, and are the gendered rise-plateau-slump percentages and the F0-excursion means internally consistent? | V1 Pass; H1 Supported; H2 Supported; H3 Supported; H4 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: Liverpool rising contours and their new-dialect origin sourced, with a contour-label slip (AS0-HUM-01); statistics internally consistent (AS0-HUM-02).

## Unresolved
- GLMMs not refitted; token totals per speaker assumed equal.
- Other readings of ascent in language and culture (e.g. pitch in music, social ascent in narrative) not covered.
