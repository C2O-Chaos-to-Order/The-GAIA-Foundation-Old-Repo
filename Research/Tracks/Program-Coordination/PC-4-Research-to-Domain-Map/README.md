# PC-4 Research-to-Domain Map

Work Queue item **PC-4** (Program Coordination) and gap check item **b7**. Status: **Proposed research output, not adopted.**
It maps Work Queue reports to the 45 domains of the owner-provided **GAIA Totality Suite v0.1.0** (Proposed, not adopted, and not filed in this repository; see `PLAN.md` §2).

- Method: `PLAN.md`
- Tool: `tools/pc4.py` (standard library; needs the owner's suite, checked by SHA-256)
- Agent judgments: `judgments/map_<cycle>.csv`, `judgments/clusters_<cycle>.csv`
- Cycles: `Cycle-0-Baseline/` (later cycles are added on stacked branches)

Rerun a cycle: `python3 tools/pc4.py run --cycle Cycle-0-Baseline --iter 1`; verify: `python3 tools/pc4.py verify --cycle Cycle-0-Baseline`.
