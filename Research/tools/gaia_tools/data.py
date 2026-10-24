"""Loaders for the on-disk research corpus (Research/Cycles/Cycle-*/...).

Layouts supported:
  * Cycle 0 (baseline): Report-*/simulation/{SPEC.md, params.json, EXECUTION_RECORD.json, sim_*.py}
    (+ an archived run in Report-4-Spirit/simulation/archive_v1/).
  * Cycle >= 1: Report-*/simulation/iter-<k>/{SPEC.md, params.json, outputs/, EXECUTION_RECORD.json}
    with one script Report-*/simulation/sim_r<N>.py per report.
"""
import csv, glob, hashlib, json, os, re

LABELS = {"Established": "E", "Plausible": "P", "Philosophical/Spiritual": "PS", "Hypothetical": "H"}
REPORTS = {"R1": "Body", "R2": "Mind", "R3": "Soul", "R4": "Spirit", "R5": "Consciousness", "R6": "Earth", "R7": "Unified"}
REPORT_DIRS = {f"R{i}": f"Report-{i}-{n}" for i, n in enumerate(REPORTS.values(), 1)}
SIM_REF = re.compile(r"^(?P<c0>C0:)?(?P<sim>SIM-R[1-7]-C\d+)(?:/iter-(?P<it>\d+))?#(?P<chk>[A-Za-z0-9_]+)$")


def sha256_file(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def git_blob_sha(p):
    b = open(p, "rb").read()
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()


def read_csv(p):
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def split_ids(s):
    return [x.strip() for x in re.split(r"[;]", s or "") if x.strip()]


def cycles(research_dir):
    """Return [(cycle_id, path)] sorted by cycle number, e.g. ('C0', .../Cycle-0-Baseline)."""
    out = []
    for p in glob.glob(os.path.join(research_dir, "Cycles", "Cycle-*")):
        m = re.match(r"Cycle-(\d+)", os.path.basename(p))
        if m and os.path.isdir(p):
            out.append((f"C{int(m.group(1))}", p))
    return sorted(out, key=lambda t: int(t[0][1:]))


def claims(cycle_path):
    rows = []
    for rid, d in REPORT_DIRS.items():
        p = os.path.join(cycle_path, d, "claims", "claims.csv")
        if os.path.exists(p):
            for r in read_csv(p):
                r["_file"] = os.path.relpath(p, cycle_path)
                r["_report_dir"] = rid
                rows.append(r)
    return rows


def sources(cycle_path):
    return read_csv(os.path.join(cycle_path, "Provenance", "SOURCE_REGISTER.csv"))


def report_sources(cycle_path):
    out = {}
    for rid, d in REPORT_DIRS.items():
        p = os.path.join(cycle_path, d, "sources", "sources.csv")
        if os.path.exists(p):
            out[rid] = read_csv(p)
    return out


def links(cycle_path):
    p = os.path.join(cycle_path, "Report-7-Unified", "maps", "link_register.csv")
    return read_csv(p) if os.path.exists(p) else []


def simulations(cycle_path, cycle_id):
    """Index of every executed simulation run in a cycle (one entry per EXECUTION_RECORD.json)."""
    idx = []
    for rid, d in REPORT_DIRS.items():
        simdir = os.path.join(cycle_path, d, "simulation")
        for rec in sorted(glob.glob(os.path.join(simdir, "**", "EXECUTION_RECORD.json"), recursive=True)):
            rundir = os.path.dirname(rec)
            r = json.load(open(rec))
            m = re.match(r"iter-(\d+)$", os.path.basename(rundir))
            archived = "archive" in os.path.relpath(rundir, simdir)
            scripts = sorted(glob.glob(os.path.join(rundir if archived else simdir, "sim_*.py")))
            params = os.path.join(rundir, "params.json")
            spec = os.path.join(rundir, "SPEC.md")
            rel = lambda p: os.path.relpath(p, cycle_path) if p and os.path.exists(p) else None
            checks = r.get("pre_registered_checks", [])
            idx.append(dict(
                sim_id=r.get("sim_id"), cycle=cycle_id, report=rid,
                iteration=int(m.group(1)) if m else None, archived=archived,
                directory=os.path.relpath(rundir, cycle_path),
                script=rel(scripts[0]) if scripts else None, spec=rel(spec), params=rel(params),
                execution_record=os.path.relpath(rec, cycle_path),
                params_sha256=sha256_file(params) if os.path.exists(params) else None,
                n_checks=len(checks),
                results={k: sum(c.get("result") == k for c in checks)
                         for k in ("Pass", "Fail", "Supported", "Not supported", "Reported", "Indeterminate")}))
    return idx


def check_index(cycle_path, cycle_id):
    """Map 'SIM-Rn-Cm[/iter-k]#ID' -> check dict for one cycle (archived runs excluded)."""
    out = {}
    for s in simulations(cycle_path, cycle_id):
        if s["archived"]:
            continue
        rec = json.load(open(os.path.join(cycle_path, s["execution_record"])))
        key = s["sim_id"] + (f"/iter-{s['iteration']}" if s["iteration"] else "")
        for c in rec["pre_registered_checks"]:
            out[f"{key}#{c['id']}"] = c
    return out
