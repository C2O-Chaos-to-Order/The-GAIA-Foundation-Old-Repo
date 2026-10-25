# N-A Level-Name Crosswalk: plan

**Item:** Work Queue §N, N-A. **Owner:** Kyle Alexander Steen. **Agent:** Grok Bot. **Status:** proposed → researched, cycle by cycle.
**Scope:** map the level, phase and dimension vocabularies of `KyleAlexanderSteen/GAIA-Documentation` (GD) and The GAIA Foundation. Record the six conflicts listed in Work Queue §N, and give options for Kyle for each one. **Nothing here is a decision.** Reports 2, 3 and 7 depend on this item.

## Boundaries
- GD is **read-only**. It is read through the `get_file_contents` connector, or through the local copy after a blob-SHA check. Nothing is written to it, and no issue or PR is opened there.
- GD files are **not copied** here. The ledger (`ledger/`) records each file's path, git blob SHA and size. `ledger/listing.csv` is the full file listing of the GD default branch, taken 2026-10-24/25 through the connector. The connector does not expose a commit SHA, so each file is pinned by its blob SHA.
- GD material is cited as prior work, not as Foundation evidence. Each claim is labelled Established, Plausible, Philosophical/Spiritual or Hypothetical.
  - A statement of what a document *says* is labelled Established (a documentary fact).
  - A mapping between senses is usually Plausible.
  - The owner's phase-level pattern is Hypothetical.
- The Totality Suite (owner-provided v0.1.0) stays external. No 80-character span of the suite or of any GD file appears in this folder. This is checked on every run.
- No Foundation file outside this folder is edited. Edits proposed for the Work Queue or the README are listed as options only.

## Method (each cycle)
1. Write SPEC.md and config.json, and push them **before** the run. Checks are pre-registered, and a failed check stays failed.
2. Pass 1, the agent's judgment: `judgments/*_<cycle>.csv`.
   - schemes: each vocabulary with its ordered terms
   - crosswalk: term-to-term rows with a relation and a label
   - conflicts: the six Work Queue conflicts with a verdict (confirmed, refined or corrected)
   - options: at least two per conflict, one of which is "defer"; every decision is "open (Kyle)"
3. Pass 2, the tool (`tools/na.py run`).
   - Verifies every mirrored GD file against its blob SHA.
   - Re-extracts each scheme from its source and compares it with the judged list.
   - Checks crosswalk coverage and integrity.
   - Recomputes the phase census of the 32 reports, the tablet sealing census (discrepancy types D1–D9) and a vocabulary census over all 333 listed files.
   - Compares the Foundation's two ladders.
   - Runs the boundary scan.
   - Writes `iter-N/EXECUTION_RECORD.json` and `iter-N/data/*.csv`.
4. Verify: rerun every cycle with the current tool and require identical records, then repeat this from a fresh clone. Write a MANIFEST.sha256 for each cycle.
5. REPORT.md: findings, options, the sources read in full, and honest diminishing returns.

## Cycle plan
| Cycle | Branch | Adds |
|---|---|---|
| Baseline | `research/crosswalk-c0` | the schemes, crosswalk, conflicts, options and censuses; core sources, the Tablets INDEX and the 3 matrices read in full; the 22 tablets and 32 reports read as a census only |
| x3 | `research/crosswalk-x3` | read the 4 drafts and the 6 source-sealed or consistent tablets in full; a sensitivity variant (strict relation rule); fixes found by re-reading |
| x6 | `research/crosswalk-x6` | read the remaining 12 tablets in full; a sense comparison of the phase names (Tablets glosses vs the Foundation phase reports); a Meta-sense census |
| x9 | `research/crosswalk-x9` | an adversarial review of every option; the Foundation ripple (files each option would touch); a re-read of the conflicts |
| x12 | `research/crosswalk-x12` | consolidated CROSSWALK.md, final options register, statement of diminishing returns |

Each cycle is stacked on the previous one. The Baseline is stacked on `research/pc1-x12` (`e7c6419f`).
