"""Re-run path — RETIRED 2026-11-09 (owner Kyle Steen, card t44s607).

Historical behaviour (through the 2026-11-08 freshness repair on this
branch): copy the Cycles tree, delete cached EXECUTION_RECORD.json and
listed outputs, execute each script, and compare hashes. A no-op script
could previously compare the copied record with itself and report
"ALL IDENTICAL". The freshness repair stopped that cached-record pass,
but the owner then chose retirement over keeping the repair.

This module remains importable. run_cycle() and the CLI refuse with a
clear 'retired' error instead of executing or comparing anything.
"""
import argparse
import sys

from .retirement import RerunRetired, refuse_rerun


def run_cycle(research_dir, cycle_id, python=sys.executable, keep=False):
    refuse_rerun("gaia_tools.rerun")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("research_dir")
    ap.add_argument("cycle")
    ap.add_argument("--python", default=sys.executable)
    ap.add_argument("--out")
    # Parse so --help still works; then refuse without touching the tree.
    ap.parse_args(argv)
    try:
        run_cycle(None, None)
    except RerunRetired as exc:
        print(str(exc), file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    sys.exit(main())
