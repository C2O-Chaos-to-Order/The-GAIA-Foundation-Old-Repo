# Report-6-Earth — research pass 1 — logged systematic search (Cycle 2)

**Aim.** Run logged database searches (Europe PMC REST; OpenAlex where noted) for the report's Cycle-2 agenda; record every query with hit counts and top hits.

**Outcome.** Europe PMC and OpenAlex Daisyworld queries logged (22, 327 and 95 hits).

## Sources consulted in this pass
No new external source in this pass (see Outcome).

## Logged queries (from `../../../Provenance/SEARCH_LOG.jsonl`)
| UTC | Database | Query | Hits |
|---|---|---|---|
| 2026-10-24T01:59:26+00:00 | Europe PMC REST search (sort: CITED desc) | `(TITLE:"daisyworld" OR ABSTRACT:"daisyworld") AND (adaptation OR evolution OR mutation)` | 22 |
| 2026-10-24T01:59:57+00:00 | OpenAlex works search (sort: cited_by_count desc) | `Daisyworld review` | 327 |
| 2026-10-24T02:00:09+00:00 | OpenAlex works search (sort: cited_by_count desc) | `title:daisyworld` | 95 |

## Honest note
Queries are logged with hit counts and top hits; screening was of the top-ranked hits only (sorted by citation count), not exhaustive. Which logged query surfaced a selected source is not recorded per source. Retrieval attempts are in `../../../Provenance/FETCH_LOG.jsonl`.
