# Allegiance in the Applied Sciences — Cycle-0-Baseline (AL0)

Phase report: Allegiance (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
Baseline: researcher allegiance (P49) was not a significant moderator, but P49's own estimate implies only 31% power, so the null is weak.

## Claims (ledger: `claims/claims.csv`)
- **AL0-APP-01** [E] Researcher allegiance, 'a belief in the superiority of a treatment', was coded in 50 RCTs comparing humanistic with other psychotherapies; at end of treatment allegiance against humanistic therapy was not a significant moderator (beta = -0.183, SE 0.125, p = .144, N = 47), only 10% of studies showed allegiance in favour of humanistic therapy, and allegiance was significant in 2 of 5 comparisons; the authors conclude allegiance 'was not as relevant as expected' while noting absence of evidence is not evidence of absence. *Operationalization:* APP Allegiance = researcher allegiance in clinical trials. *Sources:* P49. *Limits:* One meta-analysis of one therapy family; allegiance coded from publications.
- **AL0-APP-02** [P] With P49's own estimate (beta = -0.183, SE = 0.125) the reported p was reproduced (0.143) and the two-sided power to detect a moderator of that size at alpha 0.05 was only 0.31; a simulated 47-study random-effects meta-regression gave SE 0.124 and power 0.33. P49's null for allegiance is therefore weak evidence of no effect, as P49 itself cautions; by chance alone, at least 2 of 5 independent null tests would be significant 2.3% of the time. *Operationalization:* APP Allegiance = power to detect allegiance effects. *Sources:* SIM-AL-APP-0/iter-1#V1;SIM-AL-APP-0/iter-1#H1;SIM-AL-APP-0/iter-1#H2. *Limits:* Simulated design (moderator share 0.3, tau 0.25, study SE 0.2-0.4) assumed; the five comparisons are not independent in P49.

## Simulations (SIM-AL-APP-0; 1 iteration(s), spec-first; validation 1/1, hypotheses supported 2/2)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `1e635995` | P49 found allegiance a significant moderator in only 2 of 5 comparisons and concluded it was 'not as relevant ... as expected'. With P49's own primary estimate (beta = -0.183, SE = 0.125), what was the power to detect a moderator of that size, and does a simulated 47-study meta-regression reproduce that SE and power? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: Researcher allegiance as a moderator sourced (AL0-APP-01); power of P49's test computed (AL0-APP-02).

## Unresolved
- Allegiance effects in other therapy families and in drug trials unsourced.
- Power analysis assumes independent studies.
