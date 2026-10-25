# PC-4 Research-to-Domain Map

Work Queue item **PC-4** (Program Coordination) and gap check item **b7**. Status: **Proposed research output, not adopted.**
It maps Work Queue reports to the 45 domains of the owner-provided **GAIA Totality Suite v0.1.0** (Proposed, not adopted, and not filed in this repository; see `PLAN.md` §2).

**Result: `MAP.md`**: coverage lists, the 12 single-home proposals, owner decisions and the full item → domain map.

| Cycle | Folder | Branch | Checks |
|---|---|---|---|
| Baseline | `Cycle-0-Baseline/` | `research/pc4-c0` | 7/7 PASS |
| x3 | `Cycle-x3/` | `research/pc4-x3` | X3-3 FAIL (check design flaw), others PASS |
| x6 | `Cycle-x6/` | `research/pc4-x6` | 11/11 PASS |
| x9 | `Cycle-x9/` | `research/pc4-x9` | 8/8 PASS |
| x12 | `Cycle-x12/` | `research/pc4-x12` | X12-7 FAIL (one quotation over the window), others PASS |

- Method: `PLAN.md`. Tool: `tools/pc4.py` (standard library; needs the owner's suite, checked by SHA-256). Exploratory helper: `tools/compare_maps.py`.
- Agent judgments: `judgments/map_<cycle>.csv`, `clusters_<cycle>.csv`, `nonreport_<cycle>.csv`, `tog24_<cycle>.csv`, `review_x3.csv`, `scan_proposals_x9.csv`.
- Rerun: `python3 tools/pc4.py run --cycle Cycle-x12 --iter 2`. Verify every cycle: `for c in Cycle-*; do python3 tools/pc4.py verify --cycle $c; done`. Boundary scan: `python3 tools/pc4.py boundary`.
