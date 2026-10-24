# Report-3-Soul — research pass 1 — logged systematic search (Cycle 2)

**Aim.** Run logged database searches (Europe PMC REST; OpenAlex where noted) for the report's Cycle-2 agenda; record every query with hit counts and top hits.

**Outcome.** 3 queries logged (Europe PMC ×2; OpenAlex ×1) on cross-cultural soul coding and inter-rater reliability.

## Sources consulted in this pass
No new external source in this pass (see Outcome).

## Logged queries (from `../../../Provenance/SEARCH_LOG.jsonl`)
| UTC | Database | Query | Hits |
|---|---|---|---|
| 2026-10-24T01:59:44+00:00 | Europe PMC REST search (sort: CITED desc) | `(soul OR afterlife) AND (cross-cultural OR "cross cultural") AND (coding OR "inter-rater" OR database OR Seshat OR Pulotu)` | 1548 |
| 2026-10-24T01:59:56+00:00 | OpenAlex works search (sort: cited_by_count desc) | `cross-cultural concepts of soul afterlife ethnographic coding` | 1706 |
| 2026-10-24T02:01:59+00:00 | Europe PMC REST search (sort: CITED desc) | `TITLE:("interrater reliability" OR "inter-rater reliability") AND kappa AND OPEN_ACCESS:y` | 267 |

## Honest note
Queries are logged with hit counts and top hits; screening was of the top-ranked hits only (sorted by citation count), not exhaustive. Which logged query surfaced a selected source is not recorded per source. Retrieval attempts are in `../../../Provenance/FETCH_LOG.jsonl`.
