# PLAN — GAIA Five Phase Reports track (build15)

Owner request (2026-10-24): five phase reports — **Divergence, Insurgence, Allegiance, Convergence, Ascendence** — each covering **all major fields of knowledge**, each with Baseline + verification, then x3, x6, x9, x12 cycles (N research passes and N simulation iterations per field, spec-first, one verification per cycle), mapped against ALL existing work (Cycles 0-4, Master Report, Track A-D, and earlier phase cycles) in new Maps versions (earlier versions unchanged), then one phase synthesis report. Governing rules: `Research/README.md`, `Research/RESEARCH_PLAN_EXTENSION.md`, `GOVERNANCE/UNIVERSAL_REGULATION.md` (seven laws; Proposed), Seven-Report framework rules (four labels; Indeterminate is never Pass; no invented sources or results; failures and empty passes reported).

## 1. Fields (the six "major fields of knowledge"; owner choice t80s253)
| code | folder | scope used here |
|---|---|---|
| NAT | Natural-Sciences | physics, chemistry, biology, earth science |
| FOR | Formal-Sciences | mathematics, logic, statistics, computation theory |
| SOC | Social-Sciences | psychology (social), sociology, economics, political science |
| APP | Applied-Sciences | medicine, engineering, computing practice |
| HUM | Humanities | history (incl. history of science), languages and linguistics, literature, arts |
| PHI | Philosophy-Spirituality | philosophy, theology, comparative religion, spiritual traditions |
The six-field list is a convention, not a natural kind (overlaps disclosed per claim; e.g. historical linguistics is filed under HUM, opinion dynamics under SOC).

## 2. Phases and codes
| phase | code | folder |
|---|---|---|
| Divergence | DV | `Research/Tracks/Phases/Divergence/` |
| Insurgence | IN | `.../Insurgence/` |
| Allegiance | AL | `.../Allegiance/` |
| Convergence | CV | `.../Convergence/` |
| Ascendence | AS | `.../Ascendence/` |
Each phase is **operationalized per field** (e.g. Divergence = branching, differentiation, variation, separation of trajectories) and its **competing definitions** are recorded in the phase `DEFINITIONS.md`. The README §12 Q4 question (fixed sequence vs recurring states) stays open; no ordering is assumed by the reports.

## 3. Cycles (per phase)
| cycle | folder | passes per field | sim iterations per field | runs per cycle |
|---|---|---|---|---|
| 0 Baseline | `Cycle-0-Baseline` | 1 | 1 | 6 |
| A x3 | `Cycle-A-x3` | 3 | 3 | 18 |
| B x6 | `Cycle-B-x6` | 6 | 6 | 36 |
| C x9 | `Cycle-C-x9` | 9 | 9 | 54 |
| D x12 | `Cycle-D-x12` | 12 | 12 | 72 |
Per phase: 31 passes and 31 iterations per field (186 runs per phase; 930 for five phases).

## 4. Identifiers
- Sources: **P01, P02, ...** (one register for the whole Phases track; never reused; cycle_added records where first used). Main-cycle (G/S/T/U/V/W/X/Y/Z) and SSC-track (K) sources may be reused by ID.
- Claims: `<PH><L>-<FIELD>-nn` e.g. `DV0-NAT-01`, `DVA-SOC-04`. Carried claims are renamed per cycle with `change` = "carried from <id> unchanged" or "revised: ...".
- Simulations: `SIM-<PH>-<FIELD>-<L>`; citation `SIM-DV-NAT-0/iter-1#V1`.
- Links: `PL-nn` (endpoints: fields, phases, R1-R7, MR, SSC topics, GAIA).

## 5. Per-cycle steps (successors: follow in order)
1. STATUS line "start". Branch: `research/phase-<phase>-<c0|x3|x6|x9|x12>` from the previous head (first: from `research/governance-universal-regulation` @7dded25).
2. Research: N passes per field. Searches with `build15/ncbi_search.py`, `build15/arxiv_search.py` (logged to `build15/SEARCH_LOG_PH.jsonl`); fetch full text with `build15/fetch_ncbi.py Pnn=PMCxxxx` or `build15/fetch_url.py Pnn=<url>` (logged to `build15/FETCH_LOG_PH.jsonl`, text in `/workspace/gaia/ph-sources/`, copy to `/workspace/gaia/snap_ph/`). Check phrases with `build15/kw2.py`. A pass that adds nothing starts "Added nothing:".
3. Simulations: add kinds to `build15/sims/sim_<field>.py`; write `build15/specs_<PH><L>.py`; run `/workspace/gaia/.venv/bin/python build15/specs_<PH><L>.py` (SPEC.md written before execution; never re-run an existing record).
4. `build15/claims_<PH><L>.py` and `build15/passes_<PH><L>.py`.
5. `python3 build15/build.py <PH> <L>` (ledgers, registers, reports) → `python3 build15/verify.py <PH> <L>` (validate, claimsource with snapshots, rerun, live phrase check) → `python3 build15/maps.py <PH> <L>` (new Maps version) → MANIFEST.
6. Push files changed since the previous verify file, at most 4 per `push_files` call, contents written directly (never a whole-batch `$file`), strictly sequential; then compare subtree SHAs (`build13/tree.py`) with the remote tree; save `build15/verify_<PH><L>.json`; STATUS line.
7. No PRs, no writes to main, no merges. Gate INDETERMINATE (independent review pending).

## 6. Maps versions
v9 = Divergence Baseline; v10 = DV x3; v11 = DV x6; v12 = DV x9; v13 = DV x12; then +5 per phase. Each version = `gaia_tools.maps_all` over all earlier work + the phase overlay (`gaia_tools.phases maps`), which places phase-track claims on the **Phase axis** (by report scope: a claim in the Divergence report is placed on Phase = Divergence — an organisational placement, not evidence that the claim instantiates a "phase") and on Being only where the claim is explicitly about a Being domain.

## 7. Synthesis
After Ascendence x12: `Research/Tracks/Phases/SYNTHESIS.md` — cross-phase, cross-field comparison, competing definitions, what the Phase axis adds to the 625 grid (README §12 Q4, Q6), and the owner's matrix hypothesis (README §10) tested only as arithmetic vs. unresolved semantics.

## 8. Governance (UNIVERSAL_REGULATION.md, Proposed)
Laws 1-3 apply directly (labels, sources read, specs before runs, reruns). Law 4/6: no human-subject data; public open-access texts only; licences recorded. Law 5/7: every commit is by the agent on research branches; the owner merges. Responsibility-ladder level: Power (research documents only).

## 9. Amendment v2 (2026-10-25): sixth phase Transcendence
Sections 1-8 above are the v1 five-phase plan, kept unchanged (frozen copy: `PLAN_v1_five_phases.md`). This amendment adds to them; where it differs, it takes precedence.
- **Owner update (2026-10-25):** Transcendence is the owner's new **sixth phase**. Code `TR`, folder `Research/Tracks/Phases/Transcendence/`, cycles as in §3 (Baseline, x3, x6, x9, x12; 186 runs; 1,116 runs for six phases). Claims `TR<L>-<FIELD>-nn`, simulations `SIM-TR-<FIELD>-<L>`. Branches `research/phase-transcendence-<c0|x3|x6|x9|x12>`, the first from `research/phase-ascendence-x12` @54d6f083.
- **Owner context (Hypothetical):** in the owner's pattern (Base = Divergence, Meta = Insurgence, Super = Allegiance, Hyper = Convergence, Ultra = Ascendence), **Magic = Transcendence**. Recorded as the owner's Hypothetical claim; not tested; no ledger claim depends on it; methods unchanged.
- **Maps versions:** v34 = Transcendence Baseline; v35 = TR x3; v36 = TR x6; v37 = TR x9; v38 = TR x12.
- **Matrix, pending owner-approved update 625 -> 750.** Adding a sixth value to the Phase axis would make the four-axis matrix 5 x 5 x 6 x 5 = 750 cells. This re-dimension is **pending owner approval** and is **not** applied: `maps.AXES`, `intersections_625.csv`, `phase_x_field_30.csv` and `phase_x_lens_25.csv` keep the five canonical phases. Transcendence claims are placed (Phase = Transcendence) in `claim_placement.csv` and recorded only in phases-track overlay files in each Maps version: `matrix/phase_track_transcendence_x_field_6.csv`, `matrix/phase_track_transcendence_x_lens_5.csv`, `matrix/phase_track_transcendence_cells_125.csv` (the 125 Alchemy x Being x Lens cells that a 750 grid would add; each row marked "pending").
- **Synthesis (§7):** moves to after Transcendence x12 and becomes a six-phase synthesis. **Not yet written** (owner: do not write it yet).
- Tooling: `gaia_tools.phases` registers `TR` and writes the overlay files; `build15/sims/sim_app.py` `ordlogit_mc` takes an optional `v1_label` (the default text is unchanged so earlier records reproduce).
