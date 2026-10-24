# Ascendence in the Humanities — Cycle-A-x3 (ASA)

Phase report: Ascendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x3: in a toy, majority-amplifying copying removes a 15% variant even with selection 0.3 (Hypothetical).

## Claims (ledger: `claims/claims.csv`)
- **ASA-HUM-02** [E] P89's statistics are internally consistent: every LRT p reproduces from its chi-square and df within 0.009 (largest gap: City x Gender in the nuclear model, 0.699 vs printed 0.69, within the rounding of chi-square 0.15), all '<0.001' entries are below 0.001; F0 gender chi2(1) 2.82 gives p 0.093; Lawton's 1349% follows from 34,500 to 500,000 (1349.3%); the rise-plateau-slump percentages imply about 47 tokens per male and 46 per female Liverpool speaker; the F0 means imply about 71 female of 138 values. *Operationalization:* HUM Ascendence = auditing an intonation study. *Sources:* SIM-AS-HUM-0/iter-1#V1;SIM-AS-HUM-0/iter-1#H1;SIM-AS-HUM-0/iter-1#H2;SIM-AS-HUM-0/iter-1#H3;SIM-AS-HUM-0/iter-1#H4. *Limits:* Audits printed numbers only; the GLMMs were not refitted (data not used); equal token contribution per speaker is the agent's assumption.
- **ASA-HUM-01** [P] P89 finds that Liverpool English is characterised by low and rising contours: the most common phrase-final contour in Liverpool is L* L-H% (Knowles' 'rise'; 54% of tokens vs 7% in Manchester), with rise-plateau-slump used more by men (145 tokens, 34%) than women (48, 13%); Manchester uses mainly falls (H* L-L%), and very high final rises (possible HRT) were only six of 495 declaratives, all in Manchester. P89 argues the Liverpool rise came from new-dialect formation after rapid nineteenth-century growth (Lawton: 1349% in 1773-1871) with Irish input, a case where a minority variant was favoured. *Operationalization:* HUM Ascendence = rising intonation in Liverpool English. *Sources:* P89. *Limits:* Read speech only; the historical account is argued, not tested. Slip: the text labels the Liverpool 'rise' L* H-H% in the results summary and in the Fig. 3 caption, although it defines L* H-H% as the 'rise-plateau' and tests L* L-H% as the most common Liverpool contour.
- **ASA-HUM-03** [H] In a 200-speaker copying toy, majority-amplifying copying (c 1.5, a stand-in for Trudgill's majority rule) eliminated a variant starting at 15% (P89's Irish share in 1871) or 30% in every run within about 3-5 generations, and selection b 0.3 for the variant did not rescue it (fixation 0 from 15%, 0.019 from 30%; both pre-registered rescue checks not supported); under neutral copying a 15% variant fixed in 15.4% of runs. In this toy a minority rise such as Liverpool's needs either much stronger selection or a copying rule without majority amplification. *Operationalization:* HUM Ascendence = selection of a minority variant. *Sources:* SIM-AS-HUM-A/iter-1#V1;SIM-AS-HUM-A/iter-1#H1;SIM-AS-HUM-A/iter-1#H2;SIM-AS-HUM-A/iter-2#V1;SIM-AS-HUM-A/iter-2#H1;SIM-AS-HUM-A/iter-2#H2;SIM-AS-HUM-A/iter-3#V1;SIM-AS-HUM-A/iter-3#H1. *Limits:* Toy; N, c, b and the start share are the agent's choices; P89's account involves many features, social networks and Irish input over decades.

## Simulations (SIM-AS-HUM-A; 3 iteration(s), spec-first; validation 3/3, hypotheses supported 3/5)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `56e1d25a` | P89's minority-variant argument as a toy: under majority-amplifying copying (c 1.5; a stand-in for Trudgill's majority rule) in a community of 200 speakers, is a variant at 15% (P89's Irish share of Liverpool in 1871) or 30% lost in at least 99% / 95% of runs? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |
| 2 | `f4f9a95e` | Can selection for a minority variant (b 0.3, as for functional load; P89 citing Hickey) overcome majority-amplifying copying (c 1.5) from 15% and 30%? | V1 Pass; H1 Not supported; H2 Not supported; R1 Reported |
| 3 | `056c4420` | Neutral baseline: does a 15% variant fix with probability 0.15 (Wright-Fisher, N 200)? | V1 Pass; H1 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (3; details `research/PASSES.md`)
- Pass 1: Search logged; 3 hits (P89 itself, toad zoonyms in Greece, Cypriot Greek writing), none read. ASA-HUM-03: majority-amplifying copying eliminates a 15% variant.
- Pass 2: ASA-HUM-03 (selection b 0.3 does not rescue it, iteration 2).
- Pass 3: ASA-HUM-03 (neutral baseline, iteration 3).

## Unresolved
- No second source on rising intonation or new-dialect formation read.
- The toy omits networks, multiple features and continued Irish immigration.
