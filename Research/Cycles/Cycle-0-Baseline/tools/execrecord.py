"""Shared execution-record helper for Cycle-0 baseline simulations."""
import json, hashlib, platform, sys, datetime, os
def sha(p): return hashlib.sha256(open(p,'rb').read()).hexdigest()
def write(simdir, sim_id, params, outputs, checks, started):
    import numpy, scipy
    rec = dict(sim_id=sim_id, status="executed", started_utc=started,
        finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        environment=dict(python=sys.version.split()[0], platform=platform.platform(),
                         numpy=numpy.__version__, scipy=scipy.__version__),
        command=" ".join(sys.argv), params=params,
        outputs={os.path.relpath(p, simdir): sha(p) for p in outputs},
        pre_registered_checks=checks,
        all_checks_passed=all(c["result"]=="Pass" for c in checks))
    json.dump(rec, open(os.path.join(simdir,"EXECUTION_RECORD.json"),"w"), indent=2)
    print(json.dumps({k:rec[k] for k in ("sim_id","all_checks_passed")}))
    for c in checks: print(c["id"], c["result"], c.get("observed"))
    return rec
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
