# Allegiance in the Social Sciences — Cycle-0-Baseline (AL0)

Phase report: Allegiance (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
Baseline: allegiance as identity fusion (P48), with a proposed loop where condemnation deepens fusion to deviant groups; a Hypothetical toy shows a threshold at loop gain 1.

## Claims (ledger: `claims/claims.csv`)
- **AL0-SOC-01** [P] Identity fusion is a visceral, near-irrevocable sense of oneness in which personal and social identities overlap completely; it arises through shared biology or shared (often dysphoric) experiences and predicts willingness to fight and die for the group; P48 proposes, from labelling theory, a loop in which external condemnation amplifies fusion to a deviant group, which in turn leads to more deviant behaviour. *Operationalization:* SOC Allegiance = identity fusion with a group. *Sources:* P48. *Limits:* P48 is a conceptual proposal for criminology; the loop is a hypothesis it raises, and it notes research has yet to show how individuals de-fuse and that fusion to large groups has sometimes decreased (tension with 'irrevocable').
- **AL0-SOC-02** [H] Formalizing P48's labelling loop as dF/dt = a k D (1 - F) - d F, dD/dt = b F - g D gives a threshold at loop gain R = a k b/(g d) = 1: below it fusion dies out (R = 0.4: F = 0), above it a fused state F* = 1 - 1/R persists (R = 2: 0.50; R = 4: 0.75); lowering condemnation below the threshold dissolves it, and with condemnation removed fusion halves in ln2/d (13.9 time units). *Operationalization:* SOC Allegiance = self-reinforcing fusion under condemnation. *Sources:* SIM-AL-SOC-0/iter-1#V1;SIM-AL-SOC-0/iter-1#H1. *Limits:* The equations are the agent's formalization of a verbal hypothesis; parameters arbitrary.

## Simulations (SIM-AL-SOC-0; 1 iteration(s), spec-first; validation 1/1, hypotheses supported 1/1)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `a8ba1f04` | P48's labelling loop as a toy: if condemnation of deviance raises fusion with a deviant group and fusion raises deviance, is there a threshold (loop gain R = 1) above which a fused state 1 - 1/R persists, and does lowering stigma below it dissolve the state? | V1 Pass; H1 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: Identity fusion and the labelling loop sourced (AL0-SOC-01); Hypothetical toy of the loop (AL0-SOC-02).

## Unresolved
- The labelling loop is untested empirically; de-fusion mechanisms unknown (P48).
- Fusion vs other loyalty constructs (social identification) not compared.
