# Allegiance in the Philosophy Spirituality — Cycle-A-x3 (ALA)

Phase report: Allegiance (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x3: loyalty helps only when decline is recoverable, noise is modest and loyalty exceeds a minimum (Hypothetical toys).

## Claims (ledger: `claims/claims.csv`)
- **ALA-PHI-01** [PS] P51 treats loyalty as a practical disposition to persist in an intrinsically valued (though not necessarily valuable) associational attachment, an executive virtue whose value depends on its object; following Hirschman, loyalty keeps members in a declining institution while they use voice to bring it back on track rather than exiting, and medieval allegiance was an oath of fealty. *Operationalization:* PHI Allegiance = loyalty as a disposition to persist. *Sources:* P51. *Limits:* Interpretive; P51 discusses competing accounts (e.g. Fletcher, Royce) and whistle-blowing limits.
- **ALA-PHI-02** [H] In an exit-voice toy of a recoverable institution (decline 0.02, voice 0.1, threshold 0.5), members with no loyalty exited within 0.1 time units, nobody voiced and quality collapsed (0.002); with loyalty tolerances up to 0.2 or 0.6, members stayed, voiced, and quality recovered to the threshold (0.50). *Operationalization:* PHI Allegiance = loyalty buying time for voice. *Sources:* SIM-AL-PHI-0/iter-1#V1;SIM-AL-PHI-0/iter-1#H1. *Limits:* Agent's formalization of Hirschman as reported in P51; parameters arbitrary; recovery requires v(1 - theta) > d by construction.
- **ALA-PHI-03** [H] When decline outpaces what voice can repair (d = 0.06 > 0.05), quality collapses whatever the loyalty: loyalty only delays exit (all members gone after 0.06 time units without loyalty, after 8.0 with tolerances up to 0.2), and with high loyalty (up to 0.6) 16% of members remain in the collapsed institution. *Operationalization:* PHI Allegiance = loyalty to a failing institution. *Sources:* SIM-AL-PHI-A/iter-1#V1;SIM-AL-PHI-A/iter-1#H1. *Limits:* Agent's toy of Hirschman as reported in P51; P51 discusses when loyalty should be forfeited, which the toy does not model.
- **ALA-PHI-04** [H] With five times more noise, moderate loyalty (up to 0.2) no longer saved the institution (quality 0.04, everyone gone by 38 time units) and high loyalty (up to 0.6) only partly did (quality 0.42, 53% remaining), so the AL0 result is not supported under noise: random shocks push quality below members' tolerance before voice can act. *Operationalization:* PHI Allegiance = loyalty under shocks. *Sources:* SIM-AL-PHI-A/iter-2#V1;SIM-AL-PHI-A/iter-2#H1. *Limits:* Agent's toy; noise level arbitrary.
- **ALA-PHI-05** [H] With a higher standard (theta 0.7) there is a minimum loyalty: with tolerances up to 0.1 members left too early and the institution collapsed (quality 0.002, last exit at 66.9), while tolerances up to 0.3 kept 86% voicing and quality recovered to 0.69. *Operationalization:* PHI Allegiance = how much loyalty is enough. *Sources:* SIM-AL-PHI-A/iter-3#V1;SIM-AL-PHI-A/iter-3#H1. *Limits:* Agent's toy; the outcome was anticipated by reasoning before the run (disclosed).

## Simulations (SIM-AL-PHI-A; 3 iteration(s), spec-first; validation 3/3, hypotheses supported 2/3)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `6df610f6` | Unrecoverable decline (d = 0.06 > v(1 - theta) = 0.05): does loyalty only delay collapse, so that quality collapses at every loyalty level? | V1 Pass; H1 Supported; R1 Reported |
| 2 | `51f402f2` | Noisier institution (noise 0.05): does moderate loyalty still allow recovery to near the threshold while no loyalty means collapse? | V1 Pass; H1 Not supported; R1 Reported |
| 3 | `9feb5841` | Higher standard (theta 0.7, voice margin v(1 - theta) = 0.03 vs decline 0.02): is there a minimum loyalty below which members leave too early for voice to save the institution? | V1 Pass; H1 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (3; details `research/PASSES.md`)
- Pass 1: ALA-PHI-03: with unrecoverable decline loyalty only delays exit (Hypothetical).
- Pass 2: ALA-PHI-04: under noise moderate loyalty no longer saves the institution (Hypothetical).
- Pass 3: ALA-PHI-05: a minimum loyalty is needed when the standard is high (Hypothetical).

## Unresolved
- No theological or spiritual-tradition source on fidelity found by the Europe PMC search.
- Forfeiture of loyalty (P51) not modelled.
