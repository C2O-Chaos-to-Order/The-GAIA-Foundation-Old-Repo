# Ascendence in the Social Sciences — Cycle-0-Baseline (AS0)

Phase report: Ascendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
Baseline: upward class mobility in Scotland (P87); upward mobility rose from 30% to 45%; two printed numbers do not reproduce.

## Claims (ledger: `claims/claims.csv`)
- **AS0-SOC-02** [E] Most of P87's printed numbers reproduce (dissimilarity indices 0.117, 0.1615, 0.232 vs 0.12, 0.16, 0.23; 28%, 17%, 46%, 57%; mobile = up + down; 241 - 183 = 58), but two pre-registered checks were not supported: Table 5's quasi-perfect-mobility reduction is 1 - 6865/30992 = 77.8%, not the printed 78.8% (text: 79%); and Table 4's salariat sample size 7344 does not follow from Table 3 (its row percentages and sizes give 6234), although Table 4's percentages do (17.0% self-recruitment, as printed). P87 states that percentages are weighted while sample sizes are unweighted, which plausibly explains the second but not the first. *Operationalization:* SOC Ascendence = auditing a mobility study. *Sources:* SIM-AS-SOC-0/iter-1#V1;SIM-AS-SOC-0/iter-1#H1;SIM-AS-SOC-0/iter-1#H2;SIM-AS-SOC-0/iter-1#H3;SIM-AS-SOC-0/iter-1#H4;SIM-AS-SOC-0/iter-1#H5. *Limits:* Audits printed rounded numbers; the weighting explanation is the agent's inference, since the weights are not printed.
- **AS0-SOC-01** [P] P87 finds that male social mobility in Scotland was already extensive in 1901 (52% mobile, 30% upwardly) and grew over the twentieth century (64% and 42% in 1974; 67% and 45% in 2001; downward mobility 22% throughout), about 1.5 percentage points per decade, driven largely by structural change (the professional and managerial class rising to 46.9% of destinations in 2001); relative mobility also increased (unidiff parameters 0 in 1901, -0.24 in 1974, -0.48 in 2001). In 1901, 57% of the salariat came from manual origins. *Operationalization:* SOC Ascendence = upward intergenerational class mobility. *Sources:* P87. *Limits:* Men only; 1901 data are weighted linked records (11% of cases unclassifiable); comparisons over time use a five-class scheme. Arithmetic issues in AS0-SOC-02.

## Simulations (SIM-AS-SOC-0; 1 iteration(s), spec-first; validation 1/1, hypotheses supported 3/5)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `1a8a7873` | P87's printed mobility statistics: do the dissimilarity indices, Table 5's % reductions and the text's 28/17/46/57% follow from the printed tables, do Tables 3 and 4 behave as one unweighted table, and does % mobile = % up + % down? | V1 Pass; H1 Supported; H2 Not supported; H3 Supported; H4 Not supported; H5 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: Rising upward and relative mobility in Scotland 1901-2001 sourced (AS0-SOC-01); audit: most numbers reproduce, Table 5's 78.8% and Table 4's 7344 do not (AS0-SOC-02).

## Unresolved
- P87's weights are not printed, so the Table 3/4 size mismatch cannot be fully checked.
- The 78.8% vs 77.8% discrepancy is unexplained (possible typo in 6865 or 78.8).
