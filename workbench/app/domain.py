"""GAIA Research Workbench — domain models and grid generator."""
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime

class AlchemyMode(str, Enum):
    BODY = "Body Alchemy"
    MIND = "Mind Alchemy"
    SOUL = "Soul Alchemy"
    SPIRIT = "Spirit Alchemy"
    CONSCIOUSNESS = "Consciousness Alchemy"

class BeingDomain(str, Enum):
    BODY = "Body"
    MIND = "Mind"
    SOUL = "Soul"
    SPIRIT = "Spirit"
    CONSCIOUSNESS = "Consciousness"

class Phase(str, Enum):
    DIVERGENCE = "Divergence"
    INSURGENCE = "Insurgence"
    ALLEGIANCE = "Allegiance"
    CONVERGENCE = "Convergence"
    ASCENDENCE = "Ascendence"

class EthicalLens(str, Enum):
    TRUTH = "Truth"
    INTEGRITY = "Integrity"
    LOVE = "Love"
    JUSTICE = "Justice"
    WISDOM = "Wisdom"

class InventoryStatus(str, Enum):
    PRESENT_MATCH = "present_match"
    MISSING = "missing"
    CHANGED = "changed"
    EXTRA = "extra"
    UNSUPPORTED_BINARY = "unsupported_binary"
    UNSAFE_ENTRY = "unsafe_entry"

class EvidenceStatus(str, Enum):
    PROPOSED = "PROPOSED"
    SUPPORTED = "SUPPORTED"
    MIXED = "MIXED"
    CONTRADICTED = "CONTRADICTED"
    INDETERMINATE = "INDETERMINATE"
    NOT_ASSESSED = "NOT_ASSESSED"

class LifecycleStatus(str, Enum):
    DRAFT = "DRAFT"
    IMPORTED = "IMPORTED"
    PARSED = "PARSED"
    REVIEWED = "REVIEWED"
    ARCHIVED = "ARCHIVED"

class Decision(str, Enum):
    DENY = "DENY"
    HOLD = "HOLD"
    ALLOW_SCOPED = "ALLOW_SCOPED"

class CellRecord(BaseModel):
    cell_id: str  # e.g. GAIA-A1-B1-P1-E1
    mode: AlchemyMode
    domain: BeingDomain
    phase: Phase
    lens: EthicalLens
    question: str = ""
    operational_definition: Optional[str] = None
    evidence_status: EvidenceStatus = EvidenceStatus.NOT_ASSESSED
    lifecycle_status: LifecycleStatus = LifecycleStatus.DRAFT
    claim_ids: List[str] = Field(default_factory=list)
    source_ids: List[str] = Field(default_factory=list)
    uncertainty: str = "NOT_ASSESSED"
    review_state: str = "PENDING"

def generate_canonical_grid() -> List[CellRecord]:
    """Generate all 625 cells with stable IDs. Defaults to NOT_ASSESSED."""
    modes = list(AlchemyMode)
    domains = list(BeingDomain)
    phases = list(Phase)
    lenses = list(EthicalLens)
    cells = []
    for mi, mode in enumerate(modes, 1):
        for di, domain in enumerate(domains, 1):
            for pi, phase in enumerate(phases, 1):
                for ei, lens in enumerate(lenses, 1):
                    cid = f"GAIA-A{mi}-B{di}-P{pi}-E{ei}"
                    q = f"How does {mode.value} applied to {domain.value} in {phase.value} foreground {lens.value}?"
                    cells.append(CellRecord(
                        cell_id=cid,
                        mode=mode,
                        domain=domain,
                        phase=phase,
                        lens=lens,
                        question=q,
                        operational_definition="MISSING_DEFINITION_MARKER",
                        evidence_status=EvidenceStatus.NOT_ASSESSED,
                    ))
    assert len(cells) == 625
    return cells

def base_triples() -> int:
    return 5 * 5 * 5  # 125
