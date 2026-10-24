"""Draw the pre-registered 40-claim sample for lens hand-coding (seed 20261025) from the Cycle-3 ledger; writes data/lens_sample.json.
Sampling frame: every Cycle-3 claim except the C3-R7-* claims, which report this analysis and were written after the hand coding
(the frame was the 212-claim ledger when the sample was first drawn; this exclusion keeps it identical after C3-R7-* were added)."""
import csv, glob, json, os, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); C3 = os.path.join(HERE, "..", "..")
ids = sorted(r["claim_id"] for f in glob.glob(os.path.join(C3, "Report-*", "claims", "claims.csv")) for r in csv.DictReader(open(f, encoding="utf-8")) if not r["claim_id"].startswith("C3-R7-"))
rng = np.random.default_rng(20261025); pick = sorted(rng.choice(len(ids), 40, replace=False).tolist())
json.dump([ids[i] for i in pick], open(os.path.join(HERE, "data", "lens_sample.json"), "w", newline="\n"), indent=1); print(len(ids))
