"""Shared runner for the Soul/Spirit/Subconscious/Consciousness track (data model 1.4.0, 'track run layout').
Each run folder  <Topic>/simulation/iter-<k>/  holds two files:
  SPEC.md                written BEFORE execution; contains the run's parameters in one ```json block
  EXECUTION_RECORD.json  written by execution; embeds the results and the pre-registered checks
The record stores spec_sha256 (SPEC.md bytes at run time), params_sha256 (canonical JSON of the params block)
and results_sha256 (canonical JSON of the results), so a re-run can be compared byte-for-byte.
Usage from a topic script:  P, H, t0 = track_runner.start(sys.argv[1]); ...; track_runner.finish(H, P, results, checks, t0)"""
import json, os, re, sys, hashlib, platform, datetime
import numpy, scipy
RESULT = {"validation": ("Pass", "Fail"), "hypothesis": ("Supported", "Not supported"), "reporting": ("Reported", "Reported")}
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def clean(o):
    if isinstance(o, dict): return {str(k): clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)): return [clean(v) for v in o]
    if isinstance(o, numpy.bool_): return bool(o)
    if isinstance(o, numpy.integer): return int(o)
    if isinstance(o, (numpy.floating, float)): return round(float(o), 8)
    if isinstance(o, numpy.ndarray): return clean(o.tolist())
    return o
def canon(o): return json.dumps(clean(o), sort_keys=True, separators=(",", ":"))
def sha(b): return hashlib.sha256(b).hexdigest()
def params_from_spec(text):
    m = re.search(r"```json\n(.*?)\n```", text, re.S)
    if not m: raise SystemExit("SPEC.md has no ```json params block")
    return json.loads(m.group(1))
def start(iterdir):
    H = os.path.abspath(iterdir); spec = open(os.path.join(H, "SPEC.md"), "rb").read()
    P = params_from_spec(spec.decode("utf-8")); P["_spec_sha256"] = sha(spec)
    return P, H, now()
def chk(cid, expect, observed, ok, kind="validation"):
    """validation = code/analytic correctness (must Pass); hypothesis = pre-registered substantive test
    (Supported / Not supported - 'Not supported' is a finding); reporting = value recorded."""
    return dict(id=cid, kind=kind, expect=expect, observed=clean(observed), result=RESULT[kind][0 if ok else 1])
def finish(H, P, results, checks, t0):
    spec_sha = P.pop("_spec_sha256")
    rec = dict(sim_id=P["sim_id"], iteration=P["iteration"], status="executed", layout="track run layout (data model 1.4.0)",
               started_utc=t0, finished_utc=now(),
               environment=dict(python=sys.version.split()[0], platform=platform.platform(), numpy=numpy.__version__, scipy=scipy.__version__),
               command=f"python {os.path.basename(sys.argv[0])} {os.path.basename(H)}  (run from {os.path.basename(os.path.dirname(os.path.dirname(H)))}/simulation/)",
               spec_sha256=spec_sha, params_sha256=sha(canon(P).encode()), results_sha256=sha(canon(results).encode()),
               results=clean(results), pre_registered_checks=checks, n_checks=len(checks),
               n_validation=sum(c["kind"] == "validation" for c in checks), n_validation_pass=sum(c["result"] == "Pass" for c in checks),
               n_hypothesis=sum(c["kind"] == "hypothesis" for c in checks), n_supported=sum(c["result"] == "Supported" for c in checks),
               n_reporting=sum(c["kind"] == "reporting" for c in checks),
               all_validation_passed=all(c["result"] == "Pass" for c in checks if c["kind"] == "validation"))
    with open(os.path.join(H, "EXECUTION_RECORD.json"), "w", newline="\n") as f: json.dump(rec, f, indent=1, ensure_ascii=False); f.write("\n")
    print(P["sim_id"], P["iteration"], f"val {rec['n_validation_pass']}/{rec['n_validation']}", f"hyp {rec['n_supported']}/{rec['n_hypothesis']}")
    for c in checks:
        if c["result"] in ("Fail", "Not supported", "Reported"): print("  ", c["result"], c["id"], c["expect"], "->", str(c["observed"])[:160])
    return rec
