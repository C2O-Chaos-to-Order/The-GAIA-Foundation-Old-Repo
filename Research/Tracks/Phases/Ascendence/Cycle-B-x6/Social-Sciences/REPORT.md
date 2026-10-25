# Ascendence in the Social Sciences — Cycle-B-x6 (ASB)

Phase report: Ascendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x6: weaker inheritance (unidiff) nearly closes the mobility gap; P93: relative stability in women's education.

## Claims (ledger: `claims/claims.csv`)
- **ASB-SOC-02** [E] Most of P87's printed numbers reproduce (dissimilarity indices 0.117, 0.1615, 0.232 vs 0.12, 0.16, 0.23; 28%, 17%, 46%, 57%; mobile = up + down; 241 - 183 = 58), but two pre-registered checks were not supported: Table 5's quasi-perfect-mobility reduction is 1 - 6865/30992 = 77.8%, not the printed 78.8% (text: 79%); and Table 4's salariat sample size 7344 does not follow from Table 3 (its row percentages and sizes give 6234), although Table 4's percentages do (17.0% self-recruitment, as printed). P87 states that percentages are weighted while sample sizes are unweighted, which plausibly explains the second but not the first. *Operationalization:* SOC Ascendence = auditing a mobility study. *Sources:* SIM-AS-SOC-0/iter-1#V1;SIM-AS-SOC-0/iter-1#H1;SIM-AS-SOC-0/iter-1#H2;SIM-AS-SOC-0/iter-1#H3;SIM-AS-SOC-0/iter-1#H4;SIM-AS-SOC-0/iter-1#H5. *Limits:* Audits printed rounded numbers; the weighting explanation is the agent's inference, since the weights are not printed.
- **ASB-SOC-04** [E] P87's growth statements follow from Table 1: (67 - 52)/10 = 1.5 points per decade overall, 1.64 per decade 1901-1974 and 1.11 per decade 1974-2001 ('possibly slowing to 1 point per decade'); the unidiff parameters are 3.3 and 5.6 standard errors from zero. *Operationalization:* SOC Ascendence = growth of mobility. *Sources:* SIM-AS-SOC-A/iter-2#V1;SIM-AS-SOC-A/iter-2#H1;SIM-AS-SOC-A/iter-2#H2;SIM-AS-SOC-A/iter-2#H3. *Limits:* Rounded printed values; decade spans 7.3 and 2.7.
- **ASB-SOC-01** [P] P87 finds that male social mobility in Scotland was already extensive in 1901 (52% mobile, 30% upwardly) and grew over the twentieth century (64% and 42% in 1974; 67% and 45% in 2001; downward mobility 22% throughout), about 1.5 percentage points per decade, driven largely by structural change (the professional and managerial class rising to 46.9% of destinations in 2001); relative mobility also increased (unidiff parameters 0 in 1901, -0.24 in 1974, -0.48 in 2001). In 1901, 57% of the salariat came from manual origins. *Operationalization:* SOC Ascendence = upward intergenerational class mobility. *Sources:* P87. *Limits:* Men only; 1901 data are weighted linked records (11% of cases unclassifiable); comparisons over time use a five-class scheme. Arithmetic issues in AS0-SOC-02.
- **ASB-SOC-03** [P] Holding P87's 1901 class-inheritance parameters fixed and fitting each year's Table 2 margins, total mobility moves only from 57.5% (1901) to 62.0% (1974) and 59.4% (2001), so structural change alone does not reproduce Table 1's rise from 52% to 67%; all three pre-registered checks were not supported (rise of at least 5 points; 1901 within 5 points of 52%; half of the rise). On 2001 margins, total mobility falls from 76.4% (no inheritance) through 68.1, 59.4, 51.3 to 44.4% as inheritance is scaled 0.5-2, always above the 23.2% structural minimum. In this model, the rise in total mobility needs weaker inheritance as well, consistent with P87's unidiff estimates (-0.24, -0.48). *Operationalization:* SOC Ascendence = structural vs relative mobility. *Sources:* SIM-AS-SOC-A/iter-1#V1;SIM-AS-SOC-A/iter-1#H1;SIM-AS-SOC-A/iter-1#H2;SIM-AS-SOC-A/iter-1#H3;SIM-AS-SOC-A/iter-3#V1;SIM-AS-SOC-A/iter-3#H1;SIM-AS-SOC-A/iter-3#H2. *Limits:* P87's statement concerns upward mobility, which needs a class ranking and was not modelled; Table 1 may use a different class scheme; Table 6 is fitted to 1901 only.
- **ASB-SOC-05** [P] Weaker inheritance closes most of the gap that structural change leaves. Scaling the 1901 inheritance parameters by P87's unidiff factors raises total mobility from 62.0% to 65.6% on 1974 margins (exp(-0.24)) and from 59.4% to 66.0% on 2001 margins (exp(-0.48)), close to Table 1's 67%. On 1901 margins an inheritance scale of 1.2 gives 53.2% (Table 1: 52%), and on 1974 margins mobility falls monotonically with scale (76.7, 70.0, 62.0, 53.4% at 0, 0.5, 1, 1.5). *Operationalization:* SOC Ascendence = structural vs relative mobility. *Sources:* SIM-AS-SOC-B/iter-1#V1;SIM-AS-SOC-B/iter-1#H1;SIM-AS-SOC-B/iter-2#V1;SIM-AS-SOC-B/iter-2#H1;SIM-AS-SOC-B/iter-2#H2;SIM-AS-SOC-B/iter-4#V1;SIM-AS-SOC-B/iter-4#H1;SIM-AS-SOC-B/iter-6#V1;SIM-AS-SOC-B/iter-6#H1. *Limits:* Unidiff applied to QPM diagonal parameters is the agent's model, not P87's five-class layer model; total, not upward, mobility.
- **ASB-SOC-06** [P] For women's education, absolute expansion did not mean much relative ascent: P93 finds considerable intergenerational stability in education levels relative to each cohort (ECC) across three generations of 90 Oxford Biobank women, of whom 50 held degrees but only 24 had a higher ECC than their mothers; 47 (52%) obtained their highest qualification as mature students. Audit: P93's percentages follow from its counts except '26 per cent of all subjects' (24/90 = 26.7%, truncated rather than rounded; pre-registered check not supported). P87 Tables 3-4 rows and columns sum to 100 within rounding (99-101). *Operationalization:* SOC Ascendence = women's educational mobility. *Sources:* SIM-AS-SOC-B/iter-3#V1;SIM-AS-SOC-B/iter-3#H1;SIM-AS-SOC-B/iter-3#H2;SIM-AS-SOC-B/iter-5#V1;SIM-AS-SOC-B/iter-5#H1;P93. *Limits:* P93's own caveats: one regional cohort; ECC compares relative scarcity, not attainment; footnote 29 describes the 'midpoint' as max minus min (method wording unclear).

## Simulations (SIM-AS-SOC-B; 6 iteration(s), spec-first; validation 6/6, hypotheses supported 7/8)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `36b6869a` | 1974 margins: does scaling 1901 inheritance by exp(-0.24) (P87's unidiff estimate) raise % mobile by >= 3 points? | V1 Pass; H1 Supported; R1 Reported |
| 2 | `9aab9a90` | 2001 margins with exp(-0.48): >= 6 points over fixed inheritance, and >= 7.5 points above the 1901 fixed-inheritance value? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |
| 3 | `b5745d10` | P93's printed percentages: do they follow from its counts? | V1 Pass; H1 Not supported; H2 Supported; R1 Reported |
| 4 | `0503ddf3` | Which inheritance scale reproduces 1901's 52% mobile on Table 2 margins (1.2-1.8)? | V1 Pass; H1 Supported; R1 Reported |
| 5 | `d75ce554` | P87 Tables 3-4: do rows and columns sum to 100 within rounding? | V1 Pass; H1 Supported; R1 Reported |
| 6 | `d5e6e3c1` | 1974 margins: is % mobile monotone in inheritance scale (0, 0.5, 1, 1.5)? | V1 Pass; H1 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (6; details `research/PASSES.md`)
- Pass 1: ASB-SOC-05: unidiff scaling on 1974 margins (+3.6 points).
- Pass 2: ASB-SOC-05: unidiff scaling on 2001 margins (66.0%).
- Pass 3: Women's educational mobility sourced and audited (ASB-SOC-06).
- Pass 4: ASB-SOC-05: 1901 calibration at scale 1.2.
- Pass 5: ASB-SOC-06: P87 Tables 3-4 sum to 100 within rounding.
- Pass 6: ASB-SOC-05: monotone in inheritance scale.

## Unresolved
- Upward mobility needs a class ranking; not modelled.
- P87's weights not printed; 78.8% vs 77.8% unexplained.
