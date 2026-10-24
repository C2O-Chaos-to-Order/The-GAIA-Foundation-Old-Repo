# Report-2-Mind — research pass 1 — logged systematic search (Cycle 2)

**Aim.** Run logged database searches (Europe PMC REST; OpenAlex where noted) for the report's Cycle-2 agenda; record every query with hit counts and top hits.

**Outcome.** 2 queries logged (latent inhibition models; Pearce–Hall associability).

## Sources consulted in this pass
No new external source in this pass (see Outcome).

## Logged queries (from `../../../Provenance/SEARCH_LOG.jsonl`)
| UTC | Database | Query | Hits |
|---|---|---|---|
| 2026-10-24T01:59:36+00:00 | Europe PMC REST search (sort: CITED desc) | `TITLE:"latent inhibition" AND (model OR "Pearce-Hall" OR "Rescorla-Wagner")` | 165 |
| 2026-10-24T02:01:58+00:00 | Europe PMC REST search (sort: CITED desc) | `("Pearce-Hall" OR "Pearce Hall") AND (attention OR associability) AND OPEN_ACCESS:y` | 138 |

## Honest note
Queries are logged with hit counts and top hits; screening was of the top-ranked hits only (sorted by citation count), not exhaustive. Which logged query surfaced a selected source is not recorded per source. Retrieval attempts are in `../../../Provenance/FETCH_LOG.jsonl`.
