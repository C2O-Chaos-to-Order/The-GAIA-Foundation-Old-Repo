# Insurgence in the Humanities — Cycle-0-Baseline (IN0)

Phase report: Insurgence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
Baseline: insurgence as a rare style rising to dominance (rap-enriched style in P21); a toy shows most new styles vanish and winners rise in an S-curve.

## Claims (ledger: `claims/claims.csv`)
- **IN0-HUM-01** [E] In P21's analysis of US Billboard Hot 100 songs 1960-2010, a style enriched for rap-related tags was very rare before the mid-1980s and then rapidly expanded to become the single largest style; P21 links this rise to the 1991 stylistic revolution. *Operationalization:* HUM Insurgence = a rare style rising rapidly to dominance. *Sources:* P21. *Limits:* Styles are clusters inferred from audio features and listener tags; chart songs only.
- **IN0-HUM-02** [P] In a Wright-Fisher toy (1,000 songs, advantage 5%), a new style entering as a single copy took over in only 9.9% of 4,000 runs (Kimura 9.5%); the successful takeovers were S-shaped, with 10%-90% times of 90.9 generations against the logistic 90.1. Rare insurgent styles usually vanish, and the ones that win rise fast. *Operationalization:* HUM Insurgence = establishment and logistic takeover of a rare style. *Sources:* SIM-IN-HUM-0/iter-1#V1;SIM-IN-HUM-0/iter-1#H1;SIM-IN-HUM-0/iter-1#H2. *Limits:* Agent's toy; P21 gives frequencies, not a mechanism.

## Simulations (SIM-IN-HUM-0; 1 iteration(s), spec-first; validation 1/1, hypotheses supported 2/2)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `185ac0c8` | P21 reports a rap-enriched style that 'is very rare before the mid-1980s but then rapidly expands'. In a Wright-Fisher toy (N = 1000 songs, advantage s = 0.05), how often does a new style entering at one copy take over, and is a successful takeover S-shaped? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: Insurgence operationalized for HUM as the rise of a rare style (IN0-HUM-01) using a source already read; no new search (disclosed).

## Unresolved
- Literary or artistic insurgence beyond popular music unsourced; mechanism of style rise unknown.
