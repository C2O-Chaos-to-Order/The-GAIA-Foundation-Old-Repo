# Maps & Matrix — v1 (covers Cycles 0–1)

**Version:** v1 · **Covers:** Cycle 0 Baseline v2 (`Research/Cycles/Cycle-0-Baseline`, on `main`) and Cycle 1 x3 (`Research/Cycles/Cycle-1-x3`, branch `research/cycle-1-x3`) · **Date:** 2026-10-24 · **Tooling:** `Research/tools` (gaia_tools 0.1.0; data model 1.0.0)

| # | Deliverable | Files | Headline |
|---|---|---|---|
| 1 | Claim map | `claim_map/claim_map.csv`, `claim_map/README.md` | 242 rows = 100 Cycle-0 claims (65 E / 14 P / 19 PS / 2 H) + 142 Cycle-1 claims (91 E / 28 P / 21 PS / 2 H); label, sources, report, cycle, status and change vs the previous cycle |
| 2 | 625-intersection matrix | `matrix/` | All 625 cells listed. **0 claims can be placed exactly**, because Alchemy and Phase are undefined in the governing documents. In the Being × Lens projection, 11 of 25 cells are populated, 7 are under-researched and 7 are empty |
| 3 | Link graph | `graph/link_graph.json`, `graph/link_graph.mmd`, `graph/README.md` (rendered Mermaid) | GAIA at the centre plus 7 reports; 7 motherthread edges (PS) and 24 typed links |
| 4 | Cross-cycle change log | `changes/CROSS_CYCLE_CHANGELOG.md`, `changes/changes.csv` | Claims: 8 strengthened, 4 weakened, 0 dropped, 42 new. Links: 1 weakened (L20) and 0 dropped |
| 5 | Data model + validation | `data-model/` (5 JSON Schemas), `validation/` | 242 claims, 193 source rows, 48 links and 29 execution records validated: **0 errors**, 82 quality warnings. Reruns are byte-identical: C0 7/7 and C1 21/21 |
| — | Simulation index | `simulations/simulations_index.json` | 29 runs: 8 in C0 (incl. 1 archived) and 21 in C1 |

## Honest limits
- **Alchemy and Phase are undefined.** `Research/README.md` §9.3 names the five Alchemy modes and the five Phases but defines neither (§12 Q3–Q4 leave them open). No claim is assigned to an Alchemy mode or a Phase; assigning one would invent semantics. Every 625-cell row is therefore a projection of the Being × Lens placement, and its flag says so.
- **The Being axis** is assigned from the report (R1 Body … R5 Consciousness). Report 6 (Earth) and Report 7 (Unified) have no Being category. Their 38 claims are listed as outside the Being axis rather than forced into it.
- **Lens placement is a provisional keyword rule** (`matrix/lens_rules.json`, v1.0.1). It was written by a single coder, has not been validated and has had no inter-rater check. 69 of 142 Cycle-1 claims match no lens and are marked Unassigned. Known lexical false positives are kept and documented in `matrix/README.md`. After a 12-claim spot-check, one term ('practice') was removed before publication; this is disclosed as a post-hoc edit.
- **The data-model schemas were adjusted after the first validation run.** A schema bug (check IDs with underscores) was fixed. Four strictness rules became reported warnings rather than errors (see `data-model/README.md`) because the Cycle-0 files may not be modified. All of this is disclosed.
- Indeterminate is never Pass. The flags 'EMPTY' and 'UNDER-RESEARCHED' describe research coverage only; they say nothing about whether anything is true.

## Reproduce
```
cd Research/tools && pip install -r requirements.txt
python -m gaia_tools.maps .. ../Maps-and-Matrix/v1-cycles-0-1 --version-label "v1 - covers Cycles 0-1"
python -m gaia_tools.validate .. --out /tmp/schema_validation.json
python -m gaia_tools.claimsource .. C1
python -m gaia_tools.rerun .. C1      # ~1 min; C0 likewise
python -m pytest -q tests
```
`MANIFEST.sha256` lists the SHA-256 of every file in this version.
