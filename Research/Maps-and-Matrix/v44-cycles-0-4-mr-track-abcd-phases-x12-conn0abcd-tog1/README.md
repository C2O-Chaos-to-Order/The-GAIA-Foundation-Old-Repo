# Maps & Matrix — v44 (adds ToG 1: Constitutional Commitments, Baseline–x12, to v43)

**Tooling:** `Research/Tracks/Totality-of-Governance/tools/build_maps_v44.py` (Grok Bot, 2026-10-25). It copies v43 unchanged and adds the ToG 1 overlay below. Earlier versions (v1 to v43) are kept unchanged.

**Source:** the owner-supplied ToG 1 package filed at `Research/Tracks/Totality-of-Governance/ToG-1-Constitutional-Commitments/` (five cycles). The package states it was prepared by Perplexity (AI assistant) for the owner, KyleAlexanderSteen; its gate is **INDETERMINATE** in every cycle, with no independent or ethics review. See that folder's `INTAKE_RECORD.md`.

## What changed
- All v43 files are copied byte-identical (140 files), except the three extended below. The base is **not** regenerated (v43 regenerated its base with `phases maps`; v44 does not need to, since no base input changed).
- `matrix/tog1_claims_all_cycles.csv`: all 296 ToG 1 claims (Baseline 45, x3 41, x6 54, x9 71, x12 85), with label, status and sources exactly as the package states.
- `matrix/tog1_label_x_cycle.csv` and `matrix/tog1_clause_x_cycle.csv`: claim counts by label and by clause (§4.1–§4.11 and cross-cutting) for each cycle.
- `matrix/tog1_clause_domain_map.csv` and `matrix/tog1_clause_x_domain_x12.csv`: the package's DOMAIN_MAP files joined across cycles (46 clause–domain pairs; 39 in x12 across 26 TOT domains). All are labelled Plausible with approval NOT RECORDED in the package; the package notes the primary Totality Suite was not inspected.
- `matrix/tog1_clause_crosswalk_x12.csv`: the x12 CLAUSE_CROSSWALK, verbatim, with its source path.
- `matrix/tog1_links_x12.csv`: the 29 x12 links, with the graph node each resolves to. 9 resolve (R1–R7, Master Report, the SSSC track's four topic nodes); 20 have no node in the v43 graph and are **not** added (listed in `validation/tog1_intake.json`).
- `matrix/intersections_625.csv` gains three columns: `tog1_x12_local_cell_id`, `tog1_x12_status`, `tog1_x12_canonical_id_as_stated`. Each of the package's 625 local tuples matched exactly one intersection by its four category names. The package records every tuple as **UNPLACED** with canonical ID **UNRESOLVED**, and that is what is recorded here: this is a name correspondence, not a placement.
- `graph/link_graph.json` and `.mmd` gain one node `TOG1` and 12 `TG1-*` edges (all Plausible, as the package labels them).
- `changes/tog1_changes.csv`: every claim with its cycle and the continuity note the package gives. The package states earlier ledgers were not imported between cycles, so IDs are cycle-local.
- `validation/tog1_intake.json`: 7 overlay checks (all PASS), each cycle's manifest result and the SHA-256 of every input file.

## Honest limits
- Grok Bot's checks here are self-checks of the overlay, not independent review. The ToG 1 gate stays **INDETERMINATE**; x9's external-input validator reuse gate and x12's specification-count check (A1: declared 5346 vs actual 1782) stay **FAIL** as recorded.
- No ToG 1 claim is placed on the Alchemy, Being, Phase or Lens axes; the package says no justified four-axis mapping exists yet.
- The Charter (GAIA-GOV-TOG-001) remains Proposed; nothing here adopts it.

## Reproduce
```
python3 Research/Tracks/Totality-of-Governance/tools/build_maps_v44.py
```
