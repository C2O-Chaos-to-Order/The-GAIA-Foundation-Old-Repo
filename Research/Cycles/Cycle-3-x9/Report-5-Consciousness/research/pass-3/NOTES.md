# Report-5-Consciousness — research pass 3 — widen (adjacent literature, open-access full-text upgrades) (Cycle 3)

**Aim.** Widen to adjacent literature; look up open-access full texts for sources previously read as abstracts.

**Outcome.** OpenAlex: T10 → X05 (C3-R5-04), U21 → X02, U20 → X03; S20 (X06) failed. Five lens-targeted queries logged; X23, X24, X26 read (C3-R5-07 to -09).

## Sources consulted in this pass
| Source | Access | Used by claims |
|---|---|---|
| X05: Casali AG, Gosseries O, Rosanova M, Boly M, Sarasso S, Casali KR, Casarotto S, Bruno MA, Laureys S, Tononi G, Massimini M (2013). A theoretically based index of consciousness independent of sensory processing and behavior. Science translational medicine 5:198ra105. doi:10.1126/scitranslmed.3006294 | full text (submitted version PDF, ORBi repository via OpenAlex) | C3-R5-04 |
| X02: Carhart-Harris RL, Leech R, Hellyer PJ, Shanahan M, Feilding A, Tagliazucchi E, Chialvo DR, Nutt D (2014). The entropic brain: a theory of conscious states informed by neuroimaging research with psychedelic drugs. Frontiers in human neuroscience 8:20. doi:10.3389/fnhum.2014.00020 | full text (Europe PMC PMC3909994) | C0v2-R5-07 |
| X03: Petersen SE, Posner MI (2012). The attention system of the human brain: 20 years after. Annual review of neuroscience 35:73-89. doi:10.1146/annurev-neuro-062111-150525 | full text (PMC OAI-PMH PMC3413263) | C0v2-R5-02 |
| X23: Lutz A, Brefczynski-Lewis J, Johnstone T, Davidson RJ (2008). Regulation of the neural circuitry of emotion by compassion meditation: effects of meditative expertise. PloS one 3:e1897. doi:10.1371/journal.pone.0001897 | full text (Europe PMC PMC2267490) | C3-R5-07 |
| X24: Peterson A, Young MJ, Fins JJ (2022). Ethics and the 2018 Practice Guideline on Disorders of Consciousness: A Framework for Responsible Implementation. Neurology 98:712-718. doi:10.1212/wnl.0000000000200301 | full text (Europe PMC PMC9071367) | C3-R5-08 |
| X26: Fleming SM, Dolan RJ, Frith CD (2012). Metacognition: computation, biology and function. Philosophical transactions of the Royal Society of London. Series B, Biological sciences 367:1280-1286. doi:10.1098/rstb.2012.0021 | full text (Europe PMC PMC3318771) | C3-R5-09 |

## Logged queries (from `../../../Provenance/SEARCH_LOG.jsonl`)
| UTC | Database | Query | Hits |
|---|---|---|---|
| 2026-10-24T02:54:12+00:00 | OpenAlex works API (OA location lookup) | `T10 doi:10.1126/scitranslmed.3006294` | 1 |
| 2026-10-24T02:54:12+00:00 | OpenAlex works API (OA location lookup) | `T11 doi:10.1038/nrn.2016.22` | 1 |
| 2026-10-24T02:54:13+00:00 | OpenAlex works API (OA location lookup) | `S20 doi:10.1016/j.neuron.2011.03.018` | 1 |
| 2026-10-24T02:54:13+00:00 | OpenAlex works API (OA location lookup) | `U21 doi:10.3389/fnhum.2014.00020` | 1 |
| 2026-10-24T03:12:28+00:00 | Europe PMC REST search (sort: CITED desc) | `(TITLE:"disorders of consciousness") AND (TITLE:ethic* OR TITLE:"moral") AND OPEN_ACCESS:y` | 9 |
| 2026-10-24T03:12:28+00:00 | Europe PMC REST search (sort: CITED desc) | `(TITLE:metacognition) AND (TITLE:consciousness OR TITLE:awareness) AND (TITLE:review OR TITLE:neural) AND OPEN_ACCESS:y` | 0 |
| 2026-10-24T03:12:28+00:00 | Europe PMC REST search (sort: CITED desc) | `(TITLE:"loving-kindness" OR TITLE:"compassion meditation") AND (TITLE:brain OR TITLE:neural OR TITLE:EEG OR TITLE:fMRI) AND OPEN_ACCESS:y` | 5 |
| 2026-10-24T03:12:36+00:00 | Europe PMC REST search (sort: CITED desc) | `(TITLE:metacognit*) AND (ABSTRACT:consciousness OR ABSTRACT:awareness) AND OPEN_ACCESS:y` | 221 |

## Honest note
Queries are logged with hit counts and top hits; screening was of the top-ranked hits only (sorted by citation count), not exhaustive. The log does not link selected sources to queries; where the Outcome names the query that surfaced a source, that is our account, not a logged fact. Retrieval attempts are in `../../../Provenance/FETCH_LOG.jsonl`.
