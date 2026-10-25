# The Connection: Soul, Spirit, Subconscious and Consciousness — plan

**Work Queue item:** §E "The Connection: Soul, Spirit, Subconscious and Consciousness — shared factors, differences, and unity". Work Queue §L adds that the existing track "has links to the main reports but none among the four topics (handled by the Connection report in §E)", and item b21 asks for those links to be re-checked.

**Status:** Proposed. Gate INDETERMINATE until independent review. Nothing here edits `WORK_QUEUE.md`, `Research/README.md`, the Soul-Spirit-Subconscious-Consciousness (SSSC) track or the Phases track; proposed edits appear as options only.

## 1. Question
How do the four topics of the SSSC track relate to each other?
1. **Shared factors:** what they have in common, in evidence, method, subject matter and tradition.
2. **Differences:** what each can and cannot study, and where they diverge.
3. **Unity:** in what sense, if any, they form one whole. The criterion is `Research/README.md` §9.5: unity "should preserve meaningful distinctions, explain relationships, and improve understanding without turning analogy into unsupported fact".

The relation vocabulary is `Research/README.md` §9.2: interaction, dependence, contrast, feedback, conflict, common cause, or absence of a demonstrated connection. Connection is not proof of identity, causation or physical quantum entanglement (§9.2, §7).

## 2. Inputs (never edited)
- SSSC track, Cycle-D-x12: the four `claims/claims.csv` ledgers (139 claims), the four `REPORT.md`, `SUMMARY.md`, `Links/link_register.csv` (TL-01 to TL-35), `Provenance/SOURCE_REGISTER.csv`; and `FRAMEWORK.md`.
- Phases track: `SYNTHESIS.md`, the six phases' Cycle-D-x12 claim ledgers, link registers (PL-*) and source registers (P-IDs).
- Main reports (Cycle-4-x12) and the Master Report, read in x6 and x9 for traditions and science on the four topics.
- `Research/README.md` §6, §7, §9 and Work Queue §E, §G, §L (owner wording).

## 3. Labels
Every claim and link carries one label: **Established**, **Plausible**, **Philosophical/Spiritual** or **Hypothetical**.
- A description of what a tradition teaches can be Established as a description (it says that the tradition holds X, not that X is true); the teaching itself is Philosophical/Spiritual.
- A claim or link may not carry a label stronger than its weakest evidential basis (rank Established > Plausible > Hypothetical). Philosophical/Spiritual items must name their basis but are not ranked.
- **Owner claims** (Kyle Steen's) are recorded as the owner's, labelled Hypothetical or Philosophical/Spiritual, and never as findings. GAIA as motherthread is a Philosophical/Spiritual framing (G03), kept apart from the science.

## 4. Method (each cycle)
1. **Specification first.** `SPEC.md` and `config.json`, with the pre-registered checks, are committed and pushed before the run. A failed check stays failed; nothing is re-thresholded. Any knowledge from a dry run is disclosed in the SPEC.
2. **Pass 1, agent judgment** (`judgments/`):
   - `factors_<c>.csv`: factor × topic incidence. Each row names basis claim IDs from that topic's own ledger.
   - `claims_<c>.csv`: the Connection claims (CN<c>-nn), each with label, topics, basis IDs and source IDs.
   - `links_<c>.csv`: topic-to-topic links (CL-nn) in the §9.2 vocabulary.
3. **Pass 2, tool** (`tools/conn.py run`): resolves every basis ID and source ID against the existing ledgers and registers (never invents a source), applies the label rules, computes the objective censuses (topic-to-topic links already in the track, sources shared between topics, cross-citations between topics, duplicate source registrations), and the judged summaries (factors shared by two, three or four topics; pairwise overlap). It writes `iter-k/EXECUTION_RECORD.json` with input and output hashes, and runs the boundary scan against the Totality Suite.
4. **Iterations** are rule variants declared in `config.json` (for example `strict` counts only factor rows with an Established or Plausible basis). New metrics go behind config keys so earlier records stay byte-identical.
5. **Maps & Matrix:** a new version per cycle (v39 Baseline to v43 x12), built by `tools/conn.py maps`: the unchanged `gaia_tools.phases maps` base plus a connection overlay. Earlier versions are never modified. The 625 matrix stays canonical; the Subconscious sits on the Mind row as in the SSSC track.
6. **Verification:** every iteration of this and every earlier cycle is re-run and must give an identical EXECUTION_RECORD, both in the worktree and in a fresh clone; then manifests, `gaia_tools.phases validate` and pytest.

## 5. Cycles
| Cycle | Branch | Reading added (in full) | Iterations |
|---|---|---|---|
| Baseline | research/connection-c0 | the four SSSC x12 reports, SUMMARY, FRAMEWORK, link register, `Phases/SYNTHESIS.md`, README §6–§9, Work Queue §E, §G, §L | 1 |
| x3 | research/connection-x3 | the four SSSC x12 claim ledgers (all columns) and the Convergence and Transcendence x12 philosophy and application reports | 3 |
| x6 | research/connection-x6 | the SSSC source register; main Reports 3, 4 and 5 (Cycle-4-x12) for traditions and science | 6 |
| x9 | research/connection-x9 | adversarial review of every claim and link; the Master Report | 9 |
| x12 | research/connection-x12 | consolidation in `CONNECTION.md`; diminishing returns | 12 |

Branches are stacked: each starts from the previous cycle's head; Baseline starts from research/crosswalk-x12 (58044d58). Small pushes; no force-push; no pull request unless asked.

## 6. Out of scope
- Whether souls or spirits exist, or what consciousness is. The SSSC track already records that no cycle settles these (TD-SOUL-10, TD-CONS-07).
- The owner's other §E items (Electromagnetic Spectrum, Geomagnetic Spectrum, GAIA as Soul and Spirit of the Universe) and §G Quantum items. Where they bear on the four topics, they are recorded as the owner's claims only.
