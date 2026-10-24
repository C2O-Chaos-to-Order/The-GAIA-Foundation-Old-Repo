# Ascendence in the Social Sciences — Cycle-C-x9 (ASC)

Phase report: Ascendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x9: calibrated inheritance scales 1.25 (1901), > 0.8 (1974), 0.6 (2001); structure bounds mobility.

## Claims (ledger: `claims/claims.csv`)
- **ASC-SOC-02** [E] Most of P87's printed numbers reproduce (dissimilarity indices 0.117, 0.1615, 0.232 vs 0.12, 0.16, 0.23; 28%, 17%, 46%, 57%; mobile = up + down; 241 - 183 = 58), but two pre-registered checks were not supported: Table 5's quasi-perfect-mobility reduction is 1 - 6865/30992 = 77.8%, not the printed 78.8% (text: 79%); and Table 4's salariat sample size 7344 does not follow from Table 3 (its row percentages and sizes give 6234), although Table 4's percentages do (17.0% self-recruitment, as printed). P87 states that percentages are weighted while sample sizes are unweighted, which plausibly explains the second but not the first. *Operationalization:* SOC Ascendence = auditing a mobility study. *Sources:* SIM-AS-SOC-0/iter-1#V1;SIM-AS-SOC-0/iter-1#H1;SIM-AS-SOC-0/iter-1#H2;SIM-AS-SOC-0/iter-1#H3;SIM-AS-SOC-0/iter-1#H4;SIM-AS-SOC-0/iter-1#H5. *Limits:* Audits printed rounded numbers; the weighting explanation is the agent's inference, since the weights are not printed.
- **ASC-SOC-04** [E] P87's growth statements follow from Table 1: (67 - 52)/10 = 1.5 points per decade overall, 1.64 per decade 1901-1974 and 1.11 per decade 1974-2001 ('possibly slowing to 1 point per decade'); the unidiff parameters are 3.3 and 5.6 standard errors from zero. *Operationalization:* SOC Ascendence = growth of mobility. *Sources:* SIM-AS-SOC-A/iter-2#V1;SIM-AS-SOC-A/iter-2#H1;SIM-AS-SOC-A/iter-2#H2;SIM-AS-SOC-A/iter-2#H3. *Limits:* Rounded printed values; decade spans 7.3 and 2.7.
- **ASC-SOC-01** [P] P87 finds that male social mobility in Scotland was already extensive in 1901 (52% mobile, 30% upwardly) and grew over the twentieth century (64% and 42% in 1974; 67% and 45% in 2001; downward mobility 22% throughout), about 1.5 percentage points per decade, driven largely by structural change (the professional and managerial class rising to 46.9% of destinations in 2001); relative mobility also increased (unidiff parameters 0 in 1901, -0.24 in 1974, -0.48 in 2001). In 1901, 57% of the salariat came from manual origins. *Operationalization:* SOC Ascendence = upward intergenerational class mobility. *Sources:* P87. *Limits:* Men only; 1901 data are weighted linked records (11% of cases unclassifiable); comparisons over time use a five-class scheme. Arithmetic issues in AS0-SOC-02.
- **ASC-SOC-03** [P] Holding P87's 1901 class-inheritance parameters fixed and fitting each year's Table 2 margins, total mobility moves only from 57.5% (1901) to 62.0% (1974) and 59.4% (2001), so structural change alone does not reproduce Table 1's rise from 52% to 67%; all three pre-registered checks were not supported (rise of at least 5 points; 1901 within 5 points of 52%; half of the rise). On 2001 margins, total mobility falls from 76.4% (no inheritance) through 68.1, 59.4, 51.3 to 44.4% as inheritance is scaled 0.5-2, always above the 23.2% structural minimum. In this model, the rise in total mobility needs weaker inheritance as well, consistent with P87's unidiff estimates (-0.24, -0.48). *Operationalization:* SOC Ascendence = structural vs relative mobility. *Sources:* SIM-AS-SOC-A/iter-1#V1;SIM-AS-SOC-A/iter-1#H1;SIM-AS-SOC-A/iter-1#H2;SIM-AS-SOC-A/iter-1#H3;SIM-AS-SOC-A/iter-3#V1;SIM-AS-SOC-A/iter-3#H1;SIM-AS-SOC-A/iter-3#H2. *Limits:* P87's statement concerns upward mobility, which needs a class ranking and was not modelled; Table 1 may use a different class scheme; Table 6 is fitted to 1901 only.
- **ASC-SOC-05** [P] Weaker inheritance closes most of the gap that structural change leaves. Scaling the 1901 inheritance parameters by P87's unidiff factors raises total mobility from 62.0% to 65.6% on 1974 margins (exp(-0.24)) and from 59.4% to 66.0% on 2001 margins (exp(-0.48)), close to Table 1's 67%. On 1901 margins an inheritance scale of 1.2 gives 53.2% (Table 1: 52%), and on 1974 margins mobility falls monotonically with scale (76.7, 70.0, 62.0, 53.4% at 0, 0.5, 1, 1.5). *Operationalization:* SOC Ascendence = structural vs relative mobility. *Sources:* SIM-AS-SOC-B/iter-1#V1;SIM-AS-SOC-B/iter-1#H1;SIM-AS-SOC-B/iter-2#V1;SIM-AS-SOC-B/iter-2#H1;SIM-AS-SOC-B/iter-2#H2;SIM-AS-SOC-B/iter-4#V1;SIM-AS-SOC-B/iter-4#H1;SIM-AS-SOC-B/iter-6#V1;SIM-AS-SOC-B/iter-6#H1. *Limits:* Unidiff applied to QPM diagonal parameters is the agent's model, not P87's five-class layer model; total, not upward, mobility.
- **ASC-SOC-06** [P] For women's education, absolute expansion did not mean much relative ascent: P93 finds considerable intergenerational stability in education levels relative to each cohort (ECC) across three generations of 90 Oxford Biobank women, of whom 50 held degrees but only 24 had a higher ECC than their mothers; 47 (52%) obtained their highest qualification as mature students. Audit: P93's percentages follow from its counts except '26 per cent of all subjects' (24/90 = 26.7%, truncated rather than rounded; pre-registered check not supported). P87 Tables 3-4 rows and columns sum to 100 within rounding (99-101). *Operationalization:* SOC Ascendence = women's educational mobility. *Sources:* SIM-AS-SOC-B/iter-3#V1;SIM-AS-SOC-B/iter-3#H1;SIM-AS-SOC-B/iter-3#H2;SIM-AS-SOC-B/iter-5#V1;SIM-AS-SOC-B/iter-5#H1;P93. *Limits:* P93's own caveats: one regional cohort; ECC compares relative scarcity, not attainment; footnote 29 describes the 'midpoint' as max minus min (method wording unclear).
- **ASC-SOC-07** [P] Calibrating the agent's QPM inheritance scale to Table 1: 1901's 52% needs scale about 1.25 (52.2%), 2001's 67% about 0.6 (66.4%), but 1974's 64% is not reached within 0.5-0.8 (65.3% at 0.8; pre-registered check not supported), implying scale above 0.8 in 1974. 2001's unidiff scale on 1974 margins gives 68.2% vs 65.6% with 1974's own. *Operationalization:* SOC Ascendence = relative mobility. *Sources:* SIM-AS-SOC-C/iter-1#V1;SIM-AS-SOC-C/iter-1#H1;SIM-AS-SOC-C/iter-2#V1;SIM-AS-SOC-C/iter-2#H1;SIM-AS-SOC-C/iter-3#V1;SIM-AS-SOC-C/iter-3#H1;SIM-AS-SOC-C/iter-8#V1;SIM-AS-SOC-C/iter-8#H1. *Limits:* QPM diagonal scaling is not P87's layer model; Table 1 may use a different class scheme.
- **ASC-SOC-08** [P] Structure sets bounds that inheritance moves within: the structural minimum rises from 11.7% (1901 margins) to 23.2% (2001), and % mobile stays between it and independence (72.4, 59.4, 35.0% at scales 0.25, 1, 3 on 2001 margins; 21.5% at scale 4 on 1901 margins); on 1974 margins independence is 14.7 points above fixed 1901 inheritance. P93's contrast follows from its counts: full-time education at 16 rose 56 points (19% to 75%, 1951-1981) yet 26 of 50 degree-holders did not exceed their mothers' ECC. *Operationalization:* SOC Ascendence = structural bounds on mobility. *Sources:* SIM-AS-SOC-C/iter-4#V1;SIM-AS-SOC-C/iter-4#H1;SIM-AS-SOC-C/iter-5#V1;SIM-AS-SOC-C/iter-5#H1;SIM-AS-SOC-C/iter-6#V1;SIM-AS-SOC-C/iter-6#H1;SIM-AS-SOC-C/iter-7#V1;SIM-AS-SOC-C/iter-7#H1;SIM-AS-SOC-C/iter-7#H2;SIM-AS-SOC-C/iter-9#V1;SIM-AS-SOC-C/iter-9#H1. *Limits:* Agent's model; P93's sample is 90 women.

## Simulations (SIM-AS-SOC-C; 9 iteration(s), spec-first; validation 9/9, hypotheses supported 9/10)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `a8d176a3` | 1974: which inheritance scale (0.5-0.8) matches Table 1's 64%? | V1 Pass; H1 Not supported; R1 Reported |
| 2 | `2e1f1837` | 2001: which scale (0.4-0.6) matches 67%? | V1 Pass; H1 Supported; R1 Reported |
| 3 | `6bb15dc4` | 1901: finer calibration (1.1-1.25) to 52% | V1 Pass; H1 Supported; R1 Reported |
| 4 | `0d8de395` | 2001: bounds for scales 0.25, 1, 3 | V1 Pass; H1 Supported; R1 Reported |
| 5 | `e2b39eea` | 1974: independence vs fixed 1901 inheritance | V1 Pass; H1 Supported; R1 Reported |
| 6 | `11dc671c` | Structural minimum 1901 vs 2001 | V1 Pass; H1 Supported; R1 Reported |
| 7 | `970519c1` | P93 expansion vs relative stability arithmetic | V1 Pass; H1 Supported; H2 Supported; R1 Reported |
| 8 | `d7adfcfb` | 1974 margins with 2001's unidiff scale | V1 Pass; H1 Supported; R1 Reported |
| 9 | `facbf6d6` | 1901 margins at inheritance scale 4 | V1 Pass; H1 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (9; details `research/PASSES.md`)
- Pass 1: ASC-SOC-07 (iteration 1).
- Pass 2: ASC-SOC-07 (iteration 2).
- Pass 3: ASC-SOC-07 (iteration 3).
- Pass 4: ASC-SOC-08 (iteration 4).
- Pass 5: ASC-SOC-08 (iteration 5).
- Pass 6: ASC-SOC-08 (iteration 6).
- Pass 7: ASC-SOC-08 (iteration 7).
- Pass 8: ASC-SOC-07 (iteration 8).
- Pass 9: ASC-SOC-08 (iteration 9).

## Unresolved
- Upward mobility needs a class ranking; not modelled.
- P87's weights not printed; 78.8% vs 77.8% unexplained.
