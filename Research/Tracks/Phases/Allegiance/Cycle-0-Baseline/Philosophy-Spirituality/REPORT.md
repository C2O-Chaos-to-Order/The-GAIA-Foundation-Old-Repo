# Allegiance in the Philosophy Spirituality — Cycle-0-Baseline (AL0)

Phase report: Allegiance (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
Baseline: loyalty as a disposition to persist (P51); in a Hypothetical Hirschman toy loyalty buys time for voice and recovery.

## Claims (ledger: `claims/claims.csv`)
- **AL0-PHI-01** [PS] P51 treats loyalty as a practical disposition to persist in an intrinsically valued (though not necessarily valuable) associational attachment, an executive virtue whose value depends on its object; following Hirschman, loyalty keeps members in a declining institution while they use voice to bring it back on track rather than exiting, and medieval allegiance was an oath of fealty. *Operationalization:* PHI Allegiance = loyalty as a disposition to persist. *Sources:* P51. *Limits:* Interpretive; P51 discusses competing accounts (e.g. Fletcher, Royce) and whistle-blowing limits.
- **AL0-PHI-02** [H] In an exit-voice toy of a recoverable institution (decline 0.02, voice 0.1, threshold 0.5), members with no loyalty exited within 0.1 time units, nobody voiced and quality collapsed (0.002); with loyalty tolerances up to 0.2 or 0.6, members stayed, voiced, and quality recovered to the threshold (0.50). *Operationalization:* PHI Allegiance = loyalty buying time for voice. *Sources:* SIM-AL-PHI-0/iter-1#V1;SIM-AL-PHI-0/iter-1#H1. *Limits:* Agent's formalization of Hirschman as reported in P51; parameters arbitrary; recovery requires v(1 - theta) > d by construction.

## Simulations (SIM-AL-PHI-0; 1 iteration(s), spec-first; validation 1/1, hypotheses supported 1/1)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `0ac3504a` | Hirschman's account of loyalty as reported in P51: in a declining but recoverable institution, do members without loyalty exit at once so that nobody voices and the institution collapses, while moderate loyalty keeps members voicing long enough for recovery? | V1 Pass; H1 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: Loyalty as a virtue and Hirschman's exit/voice sourced (AL0-PHI-01, PS); Hypothetical exit-voice toy (AL0-PHI-02).

## Unresolved
- No theological or spiritual-tradition source on fidelity or covenant read.
- The exit-voice toy is a formal stand-in, not an argument.
