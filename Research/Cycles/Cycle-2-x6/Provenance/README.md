# Provenance (Cycle 2)

- `SOURCE_REGISTER.csv` — 130 sources (15 added in Cycle 2: W01–W15; column `cycle_added`), with access mode, retrieval URL, date, HTTP status and SHA-256 of the fetched snapshot. Third-party text is not redistributed.
- `SEARCH_LOG.jsonl` — **new in Cycle 2:** 34 logged database queries (Europe PMC REST, OpenAlex) with UTC time, report, research pass, exact query, URL, hit count and top hits. Broad full-text queries were often very noisy (thousands of hits); title-restricted retries are logged too. Screening was of top-ranked hits only.
- `FETCH_LOG.jsonl` — every Cycle-2 retrieval (W01–W15), with HTTP status and SHA-256. W02 and W03 were available as abstracts only.
- `MANIFEST.sha256` — SHA-256 of every file in this cycle folder except itself.
