# SIM-R7-C0 — Categorical index generation, matrix arithmetic, and cross-report consistency check (specification, written before execution)

**Status:** Specified before execution. Class: Mathematical/computational (enumeration, arithmetic, data validation). Correct output demonstrates only correct enumeration/arithmetic/bookkeeping — **not** that the categories represent Body, Mind, Soul, Spirit, Consciousness or Earth (Plan §6).

## Parts
1. **Enumeration.** Axes (names exactly as in Research/README.md §9.3–9.4): Alchemy {Body, Mind, Soul, Spirit, Consciousness Alchemy}; Being {Body, Mind, Soul, Spirit, Consciousness}; Phase {Divergence, Insurgence, Allegiance, Convergence, Ascendence}; Lens {Truth, Integrity, Love, Justice, Wisdom}. Produce 125 triality IDs, 625 four-axis IDs (format `X-A#-B#-P#-L#`), 25 Alchemy×Being and 25 Alchemy×Phase map rows, all with status "Proposed — category only".
2. **Matrix arithmetic.** M = a⊗b + 1, a=(0,1,3,5,0), b=(3,6,9,12), compared cell-by-cell against the README §10 table (transcribed in params.json). Later pattern: A⊙B⊙C·D·E with A=(0,1,2,3,0), B=(1,3,5,7,0), C=(3,6,9,12,0), D=1, E=0.
3. **Consistency check** over the 7 `claims/claims.csv` files + Provenance/SOURCE_REGISTER.csv + simulation EXECUTION_RECORDs.

## Expected outputs / pass criteria
- E1: 125 and 625 IDs, all unique; every ID decodes back to exactly one category tuple.
- E2: 25 + 25 map rows.
- E3: M equals the README table (20/20 cells).
- E4: later-pattern product = (0,0,0,0,0).
- E5: all claim rows have non-empty required fields; class and status in the allowed vocabularies; claim IDs unique.
- E6: every source ID resolves to the register or to an executed SIM with an EXECUTION_RECORD.json.
- E7: every SIM-based claim with status "Supported" points to a SIM whose record exists (a failed check must not back a Supported claim unless the claim is about a passing part — flagged for manual review).
- E8 (warning, not pass/fail): list "Supported" claims whose only literature support is abstract-only access.
**Failure criteria:** any of E1–E7 not met → Fail.

## Baseline v2 changes (specified 2026-10-24 before the v2 run)
- **Vocabulary:** every claim row now carries a framework label (Established / Plausible / Philosophical/Spiritual / Hypothetical) *and* a repository status; E5 additionally checks the label vocabulary and that the pair is allowed by the mapping in `FRAMEWORK.md` (appendix; transcribed in params.json `label_status_map`).
- **E7 refined (per-check citation):** SIM sources are cited per check (`SIM-Rn-C0#Ek`). E7 now requires that (a) every cited check exists in that simulation's EXECUTION_RECORD and (b) no claim labelled Established cites a check whose result is Fail. A bare SIM citation (no `#check`) on an Established claim is itself a failure. This replaces the v1 rule, which failed on C0-R4-05 and needed manual review.
- **E9 (new):** the GAIA-motherthread link register `maps/link_register.csv` — every link has a non-empty statement, a framework label from the vocabulary, a basis whose claim IDs all exist in the ledgers, a test, a rejection criterion and a `gaia_thread` trace; all seven link types the framework names for Report 7 (relationship, distinction, dependency, feedback loop, competing interpretation, unresolved question, humans within Earth) occur at least once; every report R1–R6 appears in at least one link.
- **E10 (new):** no claim labelled Established cites only G03 (the framework/motherthread document) — the metaphor may not back an Established claim.
- `maps/cross_domain_map.csv` (v1 path) is regenerated from the link register for continuity.
