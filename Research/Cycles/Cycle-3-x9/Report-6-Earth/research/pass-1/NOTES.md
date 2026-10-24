# Report-6-Earth — research pass 1 — logged systematic search (Cycle 3)

**Aim.** Run logged database searches (Europe PMC REST; OpenAlex where noted) for the report's Cycle-3 agenda; record every query with hit counts and top hits.

**Outcome.** Two Daisyworld/Gaia queries logged; X15 selected.

## Sources consulted in this pass
| Source | Access | Used by claims |
|---|---|---|
| X15: Lenton TM (2025). The evolution of Gaia(s). Philosophical transactions of the Royal Society of London. Series B, Biological sciences 380:rstb20240095. doi:10.1098/rstb.2024.0095 | full text (Europe PMC PMC12329439) | C3-R6-01 |

## Logged queries (from `../../../Provenance/SEARCH_LOG.jsonl`)
| UTC | Database | Query | Hits |
|---|---|---|---|
| 2026-10-24T02:53:44+00:00 | Europe PMC REST search (sort: CITED desc) | `(daisyworld OR "Gaia hypothesis") AND (regulation OR feedback) AND (model OR review)` | 117 |
| 2026-10-24T02:55:10+00:00 | Europe PMC REST search (sort: CITED desc) | `(TITLE:daisyworld OR TITLE:gaia) AND (TITLE:selection OR TITLE:regulation OR TITLE:evolution OR TITLE:feedback)` | 21 |

## Honest note
Queries are logged with hit counts and top hits; screening was of the top-ranked hits only (sorted by citation count), not exhaustive. The log does not link selected sources to queries; where the Outcome names the query that surfaced a source, that is our account, not a logged fact. Retrieval attempts are in `../../../Provenance/FETCH_LOG.jsonl`.
