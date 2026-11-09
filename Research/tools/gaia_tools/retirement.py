"""Retirement of GAIA re-run paths (Wave 1 N24).

Owner decision: Kyle Steen, card t44s607, 2026-11-09 14:13 CT — RETIRE the
no-op re-run code instead of keeping the 2026-11-08 freshness repair.
Invoking a retired path raises RerunRetired with a message that includes
the word "retired". The modules remain importable so callers get an
explicit refusal instead of an ImportError (less destructive than deletion).
"""

RETIRED_ON = "2026-11-09"
RETIRED_CARD = "t44s607"
RETIRED_OWNER = "Kyle Steen"


class RerunRetired(RuntimeError):
    """Raised when a retired re-run path is invoked."""


def retired_message(path_name: str) -> str:
    return (
        f"retired: {path_name} was retired on {RETIRED_ON} "
        f"(owner {RETIRED_OWNER}, card {RETIRED_CARD}). "
        "This path is not a scientific re-execution and must not be used "
        "to claim identical results. The prior Wave 1 freshness repair "
        "(deleting cached EXECUTION_RECORD.json before compare, 2026-11-08) "
        "is superseded by this retirement."
    )


def refuse_rerun(path_name: str) -> None:
    raise RerunRetired(retired_message(path_name))
