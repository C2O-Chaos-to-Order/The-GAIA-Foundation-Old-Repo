# Report-5-Consciousness — research pass 1 — logged systematic search (Cycle 2)

**Aim.** Run logged database searches (Europe PMC REST; OpenAlex where noted) for the report's Cycle-2 agenda; record every query with hit counts and top hits.

**Outcome.** GNW/IIT query logged; W12 (Cogitate protocol) selected (C2-R5-03).

## Sources consulted in this pass
| Source | Access | Used by claims |
|---|---|---|
| W12: Melloni L, Mudrik L, Pitts M, Bendtz K, Ferrante O, Gorska U, Hirschhorn R, Khalaf A, Kozma C, Lepauvre A, Liu L, Mazumder D, Richter D, Zhou H, Blumenfeld H, Boly M, Chalmers DJ, Devore S, Fallon F, de Lange FP, Jensen O, Kreiman G, Luo H, Panagiotaropoulos TI, Dehaene S, Koch C, Tononi G (2023). An adversarial collaboration protocol for testing contrasting predictions of global neuronal workspace and integrated information theory. PloS one 18:e0268577. doi:10.1371/journal.pone.0268577 | full text (Europe PMC PMC9916582) | C2-R5-03 |

## Logged queries (from `../../../Provenance/SEARCH_LOG.jsonl`)
| UTC | Database | Query | Hits |
|---|---|---|---|
| 2026-10-24T01:59:45+00:00 | Europe PMC REST search (sort: CITED desc) | `("global neuronal workspace" OR "global workspace") AND ("integrated information") AND (adversarial OR preregistered OR "pre-registered")` | 85 |
| 2026-10-24T02:02:01+00:00 | Europe PMC REST search (sort: CITED desc) | `("perturbational complexity" OR "Lempel-Ziv") AND consciousness AND OPEN_ACCESS:y` | 510 |

## Honest note
Queries are logged with hit counts and top hits; screening was of the top-ranked hits only (sorted by citation count), not exhaustive. Which logged query surfaced a selected source is not recorded per source. Retrieval attempts are in `../../../Provenance/FETCH_LOG.jsonl`.
