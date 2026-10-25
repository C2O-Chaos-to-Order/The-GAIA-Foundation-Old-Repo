# x12 iteration 10: executed result

One initial execution andone same-authorisolated-copyreproduction;not independentreview. Specifications fixed beforefirstmodelrun. Originalpayloads retained,predecessors/implementations hashed.

## Results
```json
{
  "freshness_cases": 2688,
  "globally_revoked_lease_allows": 246,
  "globally_revoked_current_query_passes": 0,
  "active_offline_entries_blocked": 288,
  "nonce_traces": 2401,
  "nonce_event_steps": 9604,
  "unsafe_proper_commits": 0,
  "double_nonce_successes": 0,
  "cache_only_false_allows": 72,
  "replay_false_allows": 14,
  "checks": {
    "T1": "PASS",
    "T2": "PASS",
    "T3": "PASS",
    "T4": "PASS",
    "T5": "PASS",
    "T6": "PASS"
  },
  "hypotheses": {
    "H10": {
      "statement": "Local lease validity eliminates all globally revoked access",
      "result": "NOT SUPPORTED",
      "counterexample_grid_entries": 246
    }
  },
  "scope": "Finite synthetic or reconstructed-code checks;not independent,field,legal ordeploymentassurance"
}
```

## Meaning and limits
Finite/reconstructed code testonly;no realpermissions,reviewers,rightsoutcomes,sourceauthenticity orstandardsconformance. Synthetictransferfixture remainsunapproved. H10NOTSUPPORTED:246globallyrevokedleaseALLOWgrid entries. Querygiven currentansweroracle;localatomicityassumed,horizon4not unbounded. Availabilitycost288grid entries notempiricalrate.
