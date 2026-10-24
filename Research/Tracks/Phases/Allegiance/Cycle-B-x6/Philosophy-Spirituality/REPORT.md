# Allegiance in the Philosophy Spirituality — Cycle-B-x6 (ALB)

Phase report: Allegiance (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x6: P59 sources when loyalty is forfeited; toys show loyalty's protection fragile under shocks.

## Claims (ledger: `claims/claims.csv`)
- **ALB-PHI-01** [PS] P51 treats loyalty as a practical disposition to persist in an intrinsically valued (though not necessarily valuable) associational attachment, an executive virtue whose value depends on its object; following Hirschman, loyalty keeps members in a declining institution while they use voice to bring it back on track rather than exiting, and medieval allegiance was an oath of fealty. *Operationalization:* PHI Allegiance = loyalty as a disposition to persist. *Sources:* P51. *Limits:* Interpretive; P51 discusses competing accounts (e.g. Fletcher, Royce) and whistle-blowing limits.
- **ALB-PHI-08** [PS] P59 treats loyalty as a practical disposition to persist in an intrinsically valued association, an executive virtue whose worth depends on its object. On Hirschman's account it should be given until it becomes clear that the institution cannot be recuperated, and loyalty to a particular object is forfeited when the object shows itself no longer worthy or capable of being a source of associational satisfaction or identity, though the breakpoint differs between people (P59's example of a spouse's infidelity). A loyal opposition stays within bounds compatible with the object's flourishing; whistle blowing should be a last resort, for serious wrongdoing, well grounded and likely to be effective. On religious roots P59 notes only that Old Testament writers framed fickleness as (un)faithfulness and that Confucian thought has long engaged loyalty. *Operationalization:* PHI Allegiance = when loyalty is forfeited. *Sources:* P59. *Limits:* Philosophical survey by one author; not a religious or spiritual-tradition source, so the gap on fidelity in a spiritual tradition remains. Slips: 'the one's who are loyal', 'self-maximation', a stray ';)' after 'Spencer, 2017'.
- **ALB-PHI-02** [H] In an exit-voice toy of a recoverable institution (decline 0.02, voice 0.1, threshold 0.5), members with no loyalty exited within 0.1 time units, nobody voiced and quality collapsed (0.002); with loyalty tolerances up to 0.2 or 0.6, members stayed, voiced, and quality recovered to the threshold (0.50). *Operationalization:* PHI Allegiance = loyalty buying time for voice. *Sources:* SIM-AL-PHI-0/iter-1#V1;SIM-AL-PHI-0/iter-1#H1. *Limits:* Agent's formalization of Hirschman as reported in P51; parameters arbitrary; recovery requires v(1 - theta) > d by construction.
- **ALB-PHI-03** [H] When decline outpaces what voice can repair (d = 0.06 > 0.05), quality collapses whatever the loyalty: loyalty only delays exit (all members gone after 0.06 time units without loyalty, after 8.0 with tolerances up to 0.2), and with high loyalty (up to 0.6) 16% of members remain in the collapsed institution. *Operationalization:* PHI Allegiance = loyalty to a failing institution. *Sources:* SIM-AL-PHI-A/iter-1#V1;SIM-AL-PHI-A/iter-1#H1. *Limits:* Agent's toy of Hirschman as reported in P51; P51 discusses when loyalty should be forfeited, which the toy does not model.
- **ALB-PHI-04** [H] With five times more noise, moderate loyalty (up to 0.2) no longer saved the institution (quality 0.04, everyone gone by 38 time units) and high loyalty (up to 0.6) only partly did (quality 0.42, 53% remaining), so the AL0 result is not supported under noise: random shocks push quality below members' tolerance before voice can act. *Operationalization:* PHI Allegiance = loyalty under shocks. *Sources:* SIM-AL-PHI-A/iter-2#V1;SIM-AL-PHI-A/iter-2#H1. *Limits:* Agent's toy; noise level arbitrary.
- **ALB-PHI-05** [H] With a higher standard (theta 0.7) there is a minimum loyalty: with tolerances up to 0.1 members left too early and the institution collapsed (quality 0.002, last exit at 66.9), while tolerances up to 0.3 kept 86% voicing and quality recovered to 0.69. *Operationalization:* PHI Allegiance = how much loyalty is enough. *Sources:* SIM-AL-PHI-A/iter-3#V1;SIM-AL-PHI-A/iter-3#H1. *Limits:* Agent's toy; the outcome was anticipated by reasoning before the run (disclosed).
- **ALB-PHI-06** [H] In the exit-voice toy the minimum loyalty at a high standard (theta 0.7) lies between tolerances 0.15 and 0.25 (quality 0.24, 0.51, 0.69); a small group (N 30) behaves as AL0; under intermediate noise (0.03) high loyalty still saves the institution (0.50) while moderate loyalty does not (0.03). *Operationalization:* PHI Allegiance = how much loyalty is enough. *Sources:* SIM-AL-PHI-B/iter-1#V1;SIM-AL-PHI-B/iter-1#H1;SIM-AL-PHI-B/iter-2#V1;SIM-AL-PHI-B/iter-2#H1;SIM-AL-PHI-B/iter-5#V1;SIM-AL-PHI-B/iter-5#H1. *Limits:* Agent's toy of Hirschman as reported in P51.
- **ALB-PHI-07** [H] Loyalty's protection is fragile: under noise 0.05 doubling voice's effect did not restore moderate loyalty's benefit (quality 0.12; not supported); a narrow margin (d 0.045) left even high loyalty short (0.42; not supported); and over T = 1000 under noise high loyalty fell to 0.23 (not supported), so in the toy loyalty delays decline under shocks rather than preventing it. *Operationalization:* PHI Allegiance = loyalty under shocks and narrow margins. *Sources:* SIM-AL-PHI-B/iter-3#V1;SIM-AL-PHI-B/iter-3#H1;SIM-AL-PHI-B/iter-4#V1;SIM-AL-PHI-B/iter-4#H1;SIM-AL-PHI-B/iter-6#V1;SIM-AL-PHI-B/iter-6#H1. *Limits:* Agent's toy; forfeiture of loyalty still not modelled and no spiritual-tradition source found.

## Simulations (SIM-AL-PHI-B; 6 iteration(s), spec-first; validation 6/6, hypotheses supported 3/6)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `d34fce67` | Locating the minimum loyalty at theta 0.7: lam_max 0.15, 0.2, 0.25. | V1 Pass; H1 Supported; R1 Reported |
| 2 | `d055a224` | Small group (N = 30): does the AL0 result hold? | V1 Pass; H1 Supported; R1 Reported |
| 3 | `61968571` | Stronger voice (v 0.2) under the noisy setting of ALA iter-2 (noise 0.05): does more effective voice restore the benefit of moderate loyalty? | V1 Pass; H1 Not supported; R1 Reported |
| 4 | `b06dcf0b` | Narrow margin (d 0.045 vs v(1 - theta) 0.05): does loyalty still save the institution? | V1 Pass; H1 Not supported; R1 Reported |
| 5 | `5e19ebcf` | Intermediate noise (0.03). | V1 Pass; H1 Supported; R1 Reported |
| 6 | `d41e9975` | Long horizon (T 1000) under noise 0.05: does high loyalty survive in the long run? | V1 Pass; H1 Not supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (6; details `research/PASSES.md`)
- Pass 1: ALB-PHI-08 (when loyalty is forfeited; loyal opposition; limits) and ALB-PHI-06 (minimum loyalty at theta 0.7 between 0.15 and 0.25).
- Pass 2: Added nothing: a small group (N 30) reproduces AL0.
- Pass 3: ALB-PHI-07: stronger voice does not restore moderate loyalty's benefit under noise.
- Pass 4: ALB-PHI-07: a narrow margin leaves even high loyalty short (0.42).
- Pass 5: Added nothing: intermediate noise (0.03) lies between AL0 and ALA iter-2 as expected.
- Pass 6: ALB-PHI-07: over T = 1000 under noise high loyalty falls to 0.23.

## Unresolved
- No religious or spiritual-tradition source on fidelity (P59 is a philosophical survey).
- Forfeiture now sourced (P59) but not modelled in the toy.
