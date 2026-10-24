"""Re-run a cycle's simulations from a fresh copy and compare with the stored execution records.

Usage:  python -m gaia_tools.rerun <Research dir> <cycle id, e.g. C1> [--python PATH] [--out report.json]
The whole Research/Cycles tree is copied to a temporary directory (so Cycle>=1 scripts can resolve
'C0:' citations against the sibling Cycle-0 folder), every non-archived run of the chosen cycle is
executed in report order (iterations in order), and for each run we compare:
  outputs_identical  - output SHA-256 map equal to the stored record
  checks_identical   - list of (check id, result) equal to the stored record
  params_identical   - params SHA-256 equal (iteration records only)
Exit code 0 only if every run exits 0 and all comparisons hold. Archived runs are not re-executed."""
import argparse, json, os, shutil, subprocess, sys, tempfile
from . import data as D


def run_cycle(research_dir, cycle_id, python=sys.executable, keep=False):
    cyc = dict(D.cycles(research_dir))
    if cycle_id not in cyc:
        raise SystemExit(f"unknown cycle {cycle_id}; have {sorted(cyc)}")
    src_cycles = os.path.join(research_dir, "Cycles")
    tmp = tempfile.mkdtemp(prefix="gaia-rerun-")
    dst_cycles = os.path.join(tmp, "Cycles")
    shutil.copytree(src_cycles, dst_cycles, ignore=shutil.ignore_patterns("__pycache__"))
    cp_orig = cyc[cycle_id]; cp_tmp = os.path.join(dst_cycles, os.path.basename(cp_orig))
    runs = [s for s in D.simulations(cp_orig, cycle_id) if not s["archived"]]
    runs.sort(key=lambda s: (s["report"], s["iteration"] or 0))
    rep = []
    for s in runs:
        old = json.load(open(os.path.join(cp_orig, s["execution_record"])))
        script = os.path.join(cp_tmp, s["script"])
        if s["iteration"]:
            cmd, cwd = [python, os.path.basename(script), f"iter-{s['iteration']}"], os.path.dirname(script)
        else:
            cmd, cwd = [python, s["script"]], cp_tmp
        p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
        new = json.load(open(os.path.join(cp_tmp, s["execution_record"])))
        row = dict(sim_id=s["sim_id"], iteration=s["iteration"], exit=p.returncode,
                   outputs_identical=old["outputs"] == new["outputs"],
                   checks_identical=[(c["id"], c["result"]) for c in old["pre_registered_checks"]] ==
                                    [(c["id"], c["result"]) for c in new["pre_registered_checks"]],
                   params_identical=(old.get("params_sha256") == new.get("params_sha256")) if "params_sha256" in old
                                    else old.get("params") == new.get("params"))
        if p.returncode:
            row["stderr_tail"] = p.stderr[-500:]
        rep.append(row)
    if not keep:
        shutil.rmtree(tmp, ignore_errors=True)
    ok = all(r["exit"] == 0 and r["outputs_identical"] and r["checks_identical"] and r["params_identical"] for r in rep)
    return dict(cycle=cycle_id, n_runs=len(rep), all_identical=ok, runs=rep)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("research_dir"); ap.add_argument("cycle")
    ap.add_argument("--python", default=sys.executable); ap.add_argument("--out")
    a = ap.parse_args(argv)
    r = run_cycle(a.research_dir, a.cycle, a.python)
    if a.out:
        open(a.out, "w").write(json.dumps(r, indent=1) + "\n")
    for x in r["runs"]:
        print(x["sim_id"], x["iteration"], "exit", x["exit"], "outputs", x["outputs_identical"], "checks", x["checks_identical"], "params", x["params_identical"])
    print("ALL IDENTICAL" if r["all_identical"] else "DIFFERENCES FOUND", f"({r['n_runs']} runs)")
    return 0 if r["all_identical"] else 1


if __name__ == "__main__":
    sys.exit(main())
