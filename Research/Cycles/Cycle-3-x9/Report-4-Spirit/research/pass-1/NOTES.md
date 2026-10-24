# Report-4-Spirit — research pass 1 — logged systematic search (Cycle 3)

**Aim.** Run logged database searches (Europe PMC REST; OpenAlex where noted) for the report's Cycle-3 agenda; record every query with hit counts and top hits.

**Outcome.** Three queries logged (one title-restricted query returned 0 hits).

## Sources consulted in this pass
No new external source in this pass (see Outcome).

## Logged queries (from `../../../Provenance/SEARCH_LOG.jsonl`)
| UTC | Database | Query | Hits |
|---|---|---|---|
| 2026-10-24T02:53:44+00:00 | Europe PMC REST search (sort: CITED desc) | `("E-value" OR "sensitivity analysis") AND (religious OR spirituality OR "service attendance") AND mortality` | 2836 |
| 2026-10-24T02:55:09+00:00 | Europe PMC REST search (sort: CITED desc) | `(TITLE:"E-value" OR TITLE:"unmeasured confounding") AND (ABSTRACT:religio* OR ABSTRACT:spiritual*)` | 0 |
| 2026-10-24T02:56:14+00:00 | Europe PMC REST search (sort: CITED desc) | `(TITLE:"religious service attendance" OR TITLE:religiosity OR TITLE:spirituality) AND TITLE:mortality AND (TITLE:cohort OR TITLE:"meta-analysis" OR TITLE:prospective)` | 4 |

## Honest note
Queries are logged with hit counts and top hits; screening was of the top-ranked hits only (sorted by citation count), not exhaustive. The log does not link selected sources to queries; where the Outcome names the query that surfaced a source, that is our account, not a logged fact. Retrieval attempts are in `../../../Provenance/FETCH_LOG.jsonl`.
