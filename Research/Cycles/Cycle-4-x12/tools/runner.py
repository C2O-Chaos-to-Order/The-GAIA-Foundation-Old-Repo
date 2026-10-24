"""Shared runner for iterated simulations (Cycle 1+).
Usage from a report script:  P, prev, H = runner.start(sys.argv[1]);  ...;  runner.finish(H, P, results, checks, t0)
Each iteration folder holds params.json (written before execution, with SPEC.md), outputs/results.json and EXECUTION_RECORD.json."""
import json, os, sys, hashlib, platform, datetime
import numpy, scipy
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def _clean(o):
    if isinstance(o, dict): return {str(k): _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)): return [_clean(v) for v in o]
    if isinstance(o, (numpy.integer,)): return int(o)
    if isinstance(o, (numpy.floating,)): return round(float(o), 10)
    if isinstance(o, float): return round(o, 10)
    if isinstance(o, numpy.ndarray): return _clean(o.tolist())
    if isinstance(o, (numpy.bool_,)): return bool(o)
    return o
def start(iterdir):
    H = os.path.abspath(iterdir); P = json.load(open(os.path.join(H, "params.json")))
    prev = None
    if P.get("prev"):
        prev = json.load(open(os.path.join(H, P["prev"], "outputs", "results.json")))
    os.makedirs(os.path.join(H, "outputs"), exist_ok=True)
    return P, prev, H
RESULT = {"validation": ("Pass", "Fail"), "hypothesis": ("Supported", "Not supported"), "reporting": ("Reported", "Reported")}
def chk(cid, expect, observed, ok, kind="validation"):
    """kind: 'validation' = code/analytic correctness (must Pass); 'hypothesis' = pre-registered substantive test whose outcome
    may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); 'reporting' = value recorded."""
    return dict(id=cid, kind=kind, expect=expect, observed=_clean(observed), result=RESULT[kind][0 if ok else 1])
def finish(H, P, results, checks, t0, extra_outputs=()):
    out = os.path.join(H, "outputs", "results.json")
    with open(out, "w", newline="\n") as f: json.dump(_clean(results), f, indent=1, sort_keys=True); f.write("\n")
    outs = [out] + [os.path.join(H, "outputs", e) for e in extra_outputs]
    rec = dict(sim_id=P["sim_id"], iteration=P["iteration"], status="executed", started_utc=t0, finished_utc=now(),
               environment=dict(python=sys.version.split()[0], platform=platform.platform(), numpy=numpy.__version__, scipy=scipy.__version__),
               command="python " + " ".join(os.path.relpath(a, os.path.dirname(os.path.dirname(H))) if os.path.exists(a) else a for a in sys.argv),
               params_sha256=hashlib.sha256(open(os.path.join(H, "params.json"), "rb").read()).hexdigest(),
               outputs={os.path.relpath(p, H): hashlib.sha256(open(p, "rb").read()).hexdigest() for p in outs},
               pre_registered_checks=checks, n_checks=len(checks),
               n_validation=sum(c["kind"] == "validation" for c in checks), n_validation_pass=sum(c["result"] == "Pass" for c in checks),
               n_hypothesis=sum(c["kind"] == "hypothesis" for c in checks), n_supported=sum(c["result"] == "Supported" for c in checks),
               n_reporting=sum(c["kind"] == "reporting" for c in checks),
               all_validation_passed=all(c["result"] == "Pass" for c in checks if c["kind"] == "validation"))
    with open(os.path.join(H, "EXECUTION_RECORD.json"), "w", newline="\n") as f: json.dump(rec, f, indent=1); f.write("\n")
    print(P["sim_id"], P["iteration"], f"validation {rec['n_validation_pass']}/{rec['n_validation']}", f"hypotheses supported {rec['n_supported']}/{rec['n_hypothesis']}")
    for c in checks:
        if c["result"] in ("Fail", "Not supported"): print("  ", c["result"], c["id"], c["expect"], str(c["observed"])[:200])
    return rec
