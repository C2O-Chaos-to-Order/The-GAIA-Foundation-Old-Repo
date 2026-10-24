# Allegiance in the Humanities — Cycle-0-Baseline (AL0)

Phase report: Allegiance (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
Baseline: language loyalty under prestige (P50); with P50's rates minorities keep a positive share, while P30's exponent form predicts extinction for a >= 1.

## Claims (ledger: `claims/claims.csv`)
- **AL0-HUM-01** [P] P50 fits language-competition models with prestige and bilingualism to public population data for six bilingual cases (e.g. Gaelic-English 1891-1971, Welsh-English 1901-2001); Bayes factors favour the model with bilingualism, which decelerates the shift from minority to majority language, and in the four unequal-prestige cases the majority language has higher prestige (e.g. Spanish-English in the USA, s2 = 1.2553 > s1 = 0.0691). *Operationalization:* HUM Allegiance = language loyalty under prestige pressure. *Sources:* P50. *Limits:* Six cases; model rates are estimates; P50 has small slips (cites figure 1a for results in figure 2; 'minority Catalonia').
- **AL0-HUM-02** [P] Plugging P50's reported rates into its constant-rate Eq. 4.4 gives positive minority equilibria in all four unequal-prestige cases (Canada 0.186, USA 0.081, Wales 0.018, Scotland 0.061), and the prestige-weighted flow runs minority-to-majority in each (USA 0.134 vs 0.012, although r12 < r21); by contrast, in P30's exponent form the weaker group survives only for a < 1 (0.31 at a = 0.5, 0 at a = 1 and 1.31). *Operationalization:* HUM Allegiance = persistence of a minority language. *Sources:* SIM-AL-HUM-0/iter-1#V1;SIM-AL-HUM-0/iter-1#H1;SIM-AL-HUM-0/iter-1#H2;SIM-AL-HUM-0/iter-1#H3. *Limits:* Agent's simplification: rates estimated in P50's bilingual model are used in a model without bilinguals; not a re-fit.

## Simulations (SIM-AL-HUM-0; 1 iteration(s), spec-first; validation 1/1, hypotheses supported 3/3)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `ced403b3` | P50's constant-rate language competition model (Eq. 4.4): with P50's reported prestige and transition rates for the four unequal-prestige cases, does the minority keep a positive equilibrium share, and is the prestige-weighted flow always minority-to-majority (even for Spanish-English, where P50 reports r12 < r21)? Comparator: P30's form, where the weaker group vanishes only if the exponent a >= 1. | V1 Pass; H1 Supported; H2 Supported; H3 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: Prestige and bilingualism in language competition sourced (AL0-HUM-01); equilibria from reported rates (AL0-HUM-02).

## Unresolved
- Rates from the bilingual model used without bilinguals; P50's SI not read.
- Literary or historical senses of allegiance not covered.
