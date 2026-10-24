# Report-7-Unified — research pass 1 — logged systematic search (Cycle 3)

**Aim.** Run logged database searches (Europe PMC REST; OpenAlex where noted) for the report's Cycle-3 agenda; record every query with hit counts and top hits.

**Outcome.** Social-support/mortality query logged (33,806 hits; top hits screened); X08 selected for Report 1.

## Sources consulted in this pass
| Source | Access | Used by claims |
|---|---|---|
| X08: Holt-Lunstad J, Smith TB, Layton JB (2010). Social relationships and mortality risk: a meta-analytic review. PLoS medicine 7:e1000316. doi:10.1371/journal.pmed.1000316 | full text (Europe PMC PMC2910600) | — |

## Logged queries (from `../../../Provenance/SEARCH_LOG.jsonl`)
| UTC | Database | Query | Hits |
|---|---|---|---|
| 2026-10-24T02:53:44+00:00 | Europe PMC REST search (sort: CITED desc) | `(oxytocin OR "social support" OR "loneliness") AND (physiology OR mortality) AND (meta-analysis)` | 33806 |

## Honest note
Queries are logged with hit counts and top hits; screening was of the top-ranked hits only (sorted by citation count), not exhaustive. The log does not link selected sources to queries; where the Outcome names the query that surfaced a source, that is our account, not a logged fact. Retrieval attempts are in `../../../Provenance/FETCH_LOG.jsonl`.
