# Phases track — six phase reports across all fields of knowledge

Owner request (2026-10-24): five phase reports — **Divergence, Insurgence, Allegiance, Convergence, Ascendence** — each covering all major fields of knowledge, each with a Baseline and x3, x6, x9, x12 cycles, mapped against all existing work, then a synthesis. Owner update (2026-10-25): **Transcendence** added as the sixth phase (`PLAN.md` §9; the earlier five-phase plan is kept as `PLAN_v1_five_phases.md`). The canonical matrix stays at 625 cells; the 625 -> 750 re-dimension is a pending owner-approved update. The phase names are the GAIA Phase axis (Research/README.md §9.3; RESEARCH_PLAN_EXTENSION.md §3.1). Governing rules: Research/README.md, RESEARCH_PLAN_EXTENSION.md, GOVERNANCE/UNIVERSAL_REGULATION.md (Proposed).

| phase | folder | status |
|---|---|---|
| Divergence | `Divergence/` | complete: Baseline–x12 verified; merged to `main` (PRs #11, #13) |
| Insurgence | `Insurgence/` | complete: Baseline–x12 verified; merged to `main` (PR #14) |
| Allegiance | `Allegiance/` | complete: Baseline–x12 verified; merged to `main` (PRs #15, #16) |
| Convergence | `Convergence/` | complete: Baseline–x12 verified; merged to `main` (PR #24; x12 @ `bbf85f11`) |
| Ascendence | `Ascendence/` | complete: Baseline–x12 verified; merged to `main` (PR #25; x12 @ `54d6f083`) |
| Transcendence | `Transcendence/` | complete: Baseline–x12 verified; merged to `main` (PR #26; x12 @ `3ae9bf57`) |
| Synthesis | `SYNTHESIS.md` | written 2026-10-25 (six phases; Proposed); method and checks in `Synthesis/`; merged to `main` (PR #27; @ `84b382bf`) |

Status updated 2026-10-25. "Complete" means all cycles were run and verified by the agent; every gate stays **INDETERMINATE** (independent review pending).

## Fields
NAT Natural-Sciences · FOR Formal-Sciences · SOC Social-Sciences · APP Applied-Sciences · HUM Humanities · PHI Philosophy-Spirituality. The six-field list is a convention (owner choice), not a natural kind.

## Identifiers
Claims `<PH><L>-<FIELD>-nn` (PH = DV, IN, AL, CV, AS, TR; L = 0 Baseline, A x3, B x6, C x9, D x12); simulations `SIM-<PH>-<FIELD>-<L>/iter-k#check`; sources `P01…` (one register for the track); links `PL-nn`.

## Honest scope
- A phase is operationalized separately in each field, and competing definitions are recorded (`<Phase>/Cycle-*/DEFINITIONS.md`). That one word applies in several fields does not show a shared mechanism.
- Phase-track claims are placed on the matrix's Phase axis by report scope (organisational placement, not evidence that a claim "is" a phase). They sit on the Being axis only when a claim is explicitly about a Being domain.
- Order of phases (fixed sequence vs recurring states, README §12 Q4) is not assumed.
- Tooling: `Research/tools` gaia_tools 0.6.0 (`python -m gaia_tools.phases`). Research tooling only.
