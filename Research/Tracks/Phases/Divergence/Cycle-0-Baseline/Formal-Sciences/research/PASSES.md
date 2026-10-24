# Formal-Sciences — research passes, Divergence Cycle-0-Baseline

Queries are logged with timestamps in `../../Provenance/SEARCH_LOG.jsonl`; fetches in `../../Provenance/FETCH_LOG.jsonl`. A pass that added nothing is recorded as such.

## Pass 1
**Queries:** `ti:"Lyapunov exponents" AND ti:review (arXiv)`; `ti:"Kullback-Leibler divergence" AND (ti:tutorial OR ti:notes) (arXiv)`; `Lyapunov exponent chaos sensitive dependence initial conditions (PMC)`

**Read:** P09 SEP 'Chaos' (full text)

**Added:** P09 fixes the trajectory sense of divergence (Lyapunov exponent) and documents that chaos has no agreed definition. The arXiv API timed out for these queries (logged); PMC hits were applied EEG/heart-rate papers, not used. Other formal senses (divergent series, the divergence operator, statistical divergences such as Kullback-Leibler) are recorded in DEFINITIONS.md as not yet sourced.
