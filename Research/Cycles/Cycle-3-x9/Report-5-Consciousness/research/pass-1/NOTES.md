# Report-5-Consciousness — research pass 1 — logged systematic search (Cycle 3)

**Aim.** Run logged database searches (Europe PMC REST; OpenAlex where noted) for the report's Cycle-3 agenda; record every query with hit counts and top hits.

**Outcome.** Two PCI queries logged; X12, X13, X14 selected.

## Sources consulted in this pass
| Source | Access | Used by claims |
|---|---|---|
| X12: Maschke C, O'Byrne J, Colombo MA, Boly M, Gosseries O, Laureys S, Rosanova M, Jerbi K, Blain-Moraes S (2024). Critical dynamics in spontaneous EEG predict anesthetic-induced loss of consciousness and perturbational complexity. Communications biology 7:946. doi:10.1038/s42003-024-06613-8 | full text (Europe PMC PMC11300875) | C3-R5-01 |
| X13: Farisco M, Changeux JP (2023). About the compatibility between the perturbational complexity index and the global neuronal workspace theory of consciousness. Neuroscience of consciousness 2023:niad016. doi:10.1093/nc/niad016 | full text (Europe PMC PMC10279414) | C3-R5-02 |
| X14: Cavelli ML, Mao R, Findlay G, Driessen K, Bugnon T, Tononi G, Cirelli C (2023). Sleep/wake changes in perturbational complexity in rats and mice. iScience 26:106186. doi:10.1016/j.isci.2023.106186 | full text (Europe PMC PMC9988678) | C3-R5-03 |

## Logged queries (from `../../../Provenance/SEARCH_LOG.jsonl`)
| UTC | Database | Query | Hits |
|---|---|---|---|
| 2026-10-24T02:53:43+00:00 | Europe PMC REST search (sort: CITED desc) | `"perturbational complexity index" AND (validation OR benchmark OR TMS)` | 243 |
| 2026-10-24T02:55:09+00:00 | Europe PMC REST search (sort: CITED desc) | `(TITLE:"perturbational complexity" OR TITLE:"PCI") AND (TITLE:consciousness OR TITLE:anesthesia OR TITLE:sleep)` | 13 |

## Honest note
Queries are logged with hit counts and top hits; screening was of the top-ranked hits only (sorted by citation count), not exhaustive. The log does not link selected sources to queries; where the Outcome names the query that surfaced a source, that is our account, not a logged fact. Retrieval attempts are in `../../../Provenance/FETCH_LOG.jsonl`.
