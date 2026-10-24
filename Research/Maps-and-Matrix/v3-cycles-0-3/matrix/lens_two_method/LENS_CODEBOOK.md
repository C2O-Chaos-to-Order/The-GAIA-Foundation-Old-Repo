# Hand-coding codebook for lens placement (coder H, Cycle 3) — written before the sample was drawn

Coder H reads only the claim **wording** (not the keyword rule's output, not the label) and marks each lens that the claim is
substantively *about* (0, 1 or several). Source of the axis: G01 Research/README.md §9.4 (Truth, Integrity, Love, Justice, Wisdom are
"foreground lenses, not a complete moral theory").

| lens | mark 1 when the claim is mainly about … |
|---|---|
| Truth | evidence, measurement, verification, replication, bias/confounding, whether something is so |
| Integrity | coherence or wholeness of a system or person: regulation, homeostasis, identity, integration, consistency |
| Love | care, relationships, social bonds, compassion, kindness, connection between beings |
| Justice | fairness, harm, rights, moral standing or duties, distribution of goods or burdens |
| Wisdom | meaning, purpose, judgement or decision under uncertainty, reflection, contemplation |

Limits: coder H is the same research agent that wrote the keyword rule (v1.0.1), so this is a two-method comparison, not independent
inter-rater reliability. The sample (40 claims) is drawn by `draw_lens_sample.py` with seed 20261025 from the Cycle-3 ledger.
