# Ascendence in the Social Sciences — Cycle-A-x3 (ASA)

Phase report: Ascendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x3: with fixed 1901 inheritance, margins alone do not raise total mobility; P87's per-decade growth figures follow from Table 1.

## Claims (ledger: `claims/claims.csv`)
- **ASA-SOC-02** [E] Most of P87's printed numbers reproduce (dissimilarity indices 0.117, 0.1615, 0.232 vs 0.12, 0.16, 0.23; 28%, 17%, 46%, 57%; mobile = up + down; 241 - 183 = 58), but two pre-registered checks were not supported: Table 5's quasi-perfect-mobility reduction is 1 - 6865/30992 = 77.8%, not the printed 78.8% (text: 79%); and Table 4's salariat sample size 7344 does not follow from Table 3 (its row percentages and sizes give 6234), although Table 4's percentages do (17.0% self-recruitment, as printed). P87 states that percentages are weighted while sample sizes are unweighted, which plausibly explains the second but not the first. *Operationalization:* SOC Ascendence = auditing a mobility study. *Sources:* SIM-AS-SOC-0/iter-1#V1;SIM-AS-SOC-0/iter-1#H1;SIM-AS-SOC-0/iter-1#H2;SIM-AS-SOC-0/iter-1#H3;SIM-AS-SOC-0/iter-1#H4;SIM-AS-SOC-0/iter-1#H5. *Limits:* Audits printed rounded numbers; the weighting explanation is the agent's inference, since the weights are not printed.
- **ASA-SOC-04** [E] P87's growth statements follow from Table 1: (67 - 52)/10 = 1.5 points per decade overall, 1.64 per decade 1901-1974 and 1.11 per decade 1974-2001 ('possibly slowing to 1 point per decade'); the unidiff parameters are 3.3 and 5.6 standard errors from zero. *Operationalization:* SOC Ascendence = growth of mobility. *Sources:* SIM-AS-SOC-A/iter-2#V1;SIM-AS-SOC-A/iter-2#H1;SIM-AS-SOC-A/iter-2#H2;SIM-AS-SOC-A/iter-2#H3. *Limits:* Rounded printed values; decade spans 7.3 and 2.7.
- **ASA-SOC-01** [P] P87 finds that male social mobility in Scotland was already extensive in 1901 (52% mobile, 30% upwardly) and grew over the twentieth century (64% and 42% in 1974; 67% and 45% in 2001; downward mobility 22% throughout), about 1.5 percentage points per decade, driven largely by structural change (the professional and managerial class rising to 46.9% of destinations in 2001); relative mobility also increased (unidiff parameters 0 in 1901, -0.24 in 1974, -0.48 in 2001). In 1901, 57% of the salariat came from manual origins. *Operationalization:* SOC Ascendence = upward intergenerational class mobility. *Sources:* P87. *Limits:* Men only; 1901 data are weighted linked records (11% of cases unclassifiable); comparisons over time use a five-class scheme. Arithmetic issues in AS0-SOC-02.
- **ASA-SOC-03** [P] Holding P87's 1901 class-inheritance parameters fixed and fitting each year's Table 2 margins, total mobility moves only from 57.5% (1901) to 62.0% (1974) and 59.4% (2001), so structural change alone does not reproduce Table 1's rise from 52% to 67%; all three pre-registered checks were not supported (rise of at least 5 points; 1901 within 5 points of 52%; half of the rise). On 2001 margins, total mobility falls from 76.4% (no inheritance) through 68.1, 59.4, 51.3 to 44.4% as inheritance is scaled 0.5-2, always above the 23.2% structural minimum. In this model, the rise in total mobility needs weaker inheritance as well, consistent with P87's unidiff estimates (-0.24, -0.48). *Operationalization:* SOC Ascendence = structural vs relative mobility. *Sources:* SIM-AS-SOC-A/iter-1#V1;SIM-AS-SOC-A/iter-1#H1;SIM-AS-SOC-A/iter-1#H2;SIM-AS-SOC-A/iter-1#H3;SIM-AS-SOC-A/iter-3#V1;SIM-AS-SOC-A/iter-3#H1;SIM-AS-SOC-A/iter-3#H2. *Limits:* P87's statement concerns upward mobility, which needs a class ranking and was not modelled; Table 1 may use a different class scheme; Table 6 is fitted to 1901 only.

## Simulations (SIM-AS-SOC-A; 3 iteration(s), spec-first; validation 3/3, hypotheses supported 5/8)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `734d7921` | Structural vs relative mobility with P87's quasi-perfect-mobility form: holding 1901 class inheritance (Table 6) fixed and fitting each year's Table 2 margins by IPF, does % mobile rise by at least 5 points 1901 to 2001, is 1901 within 5 points of Table 1's 52%, and does structural change alone account for half of the 15-point rise? | V1 Pass; H1 Not supported; H2 Not supported; H3 Not supported; R1 Reported |
| 2 | `158d8896` | P87's growth statements: does 'about 1.5 percentage points per decade' follow from Table 1, did growth slow after 1974, and are both unidiff parameters more than 3 SE from zero? | V1 Pass; H1 Supported; H2 Supported; H3 Supported; R1 Reported |
| 3 | `66732749` | Sensitivity of total mobility to inheritance on 2001 margins: does % mobile fall monotonically as Table 6's inheritance is scaled 0, 0.5, 1, 1.5, 2, and never below the dissimilarity-index bound? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (3; details `research/PASSES.md`)
- Pass 1: ASA-SOC-03: fixed 1901 inheritance does not reproduce the rise in total mobility.
- Pass 2: ASA-SOC-04: P87's growth-per-decade statements follow from Table 1.
- Pass 3: ASA-SOC-03 (sensitivity to inheritance, iteration 3).

## Unresolved
- Upward mobility needs a class ranking; not modelled.
- P87's weights are not printed; the 78.8% vs 77.8% discrepancy is unexplained.
