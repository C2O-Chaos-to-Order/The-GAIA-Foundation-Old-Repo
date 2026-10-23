"""Package importer and inventory for GAIA workbench."""
import hashlib
import io
import os
import zipfile
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from .domain import InventoryStatus

MAX_FILES = 500
MAX_UNCOMPRESSED = 100 * 1024 * 1024  # 100 MB
FORBIDDEN_PREFIXES = ("../", "/", "\\")

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def is_unsafe_path(name: str) -> bool:
    if any(name.startswith(p) for p in FORBIDDEN_PREFIXES):
        return True
    if ".." in Path(name).parts:
        return True
    return False

def inventory_zip(zip_path: Path, expected_manifest: Optional[Dict[str, str]] = None) -> Dict:
    """Inspect a ZIP and return inventory classifications. Does not execute anything."""
    result = {
        "status": "INCOMPLETE",
        "entries": [],
        "missing": [],
        "changed": [],
        "extra": [],
        "unsafe": [],
        "present_match": [],
        "byte_store": {},
    }
    try:
        with zipfile.ZipFile(zip_path, "r") as zf:
            infos = zf.infolist()
            if len(infos) > MAX_FILES:
                result["error"] = "excessive_file_count"
                return result
            total = sum(i.file_size for i in infos)
            if total > MAX_UNCOMPRESSED:
                result["error"] = "excessive_decompressed_size"
                return result
            for info in infos:
                name = info.filename
                if is_unsafe_path(name):
                    result["unsafe"].append(name)
                    result["entries"].append({"path": name, "status": InventoryStatus.UNSAFE_ENTRY.value})
                    continue
                data = zf.read(info)
                digest = sha256_bytes(data)
                result["byte_store"][name] = data
                status = InventoryStatus.PRESENT_MATCH.value
                if expected_manifest and name in expected_manifest:
                    if expected_manifest[name] != digest:
                        status = InventoryStatus.CHANGED.value
                        result["changed"].append(name)
                    else:
                        result["present_match"].append(name)
                else:
                    status = InventoryStatus.EXTRA.value
                    result["extra"].append(name)
                result["entries"].append({
                    "path": name,
                    "size": len(data),
                    "sha256": digest,
                    "status": status,
                })
            if expected_manifest:
                for exp in expected_manifest:
                    if exp not in result["byte_store"]:
                        result["missing"].append(exp)
                        result["entries"].append({"path": exp, "status": InventoryStatus.MISSING.value})
            if not result["missing"] and not result["changed"] and not result["unsafe"]:
                result["status"] = "VERIFIED_COMPLETE" if expected_manifest else "STRUCTURALLY_VALID"
            else:
                result["status"] = "INCOMPLETE"
    except Exception as e:
        result["error"] = str(e)
        result["status"] = "FAILED"
    return result

def inventory_directory(dir_path: Path, expected_manifest: Optional[Dict[str, str]] = None) -> Dict:
    """Similar inventory for an extracted directory."""
    result = {
        "status": "INCOMPLETE",
        "entries": [],
        "missing": [],
        "changed": [],
        "extra": [],
        "unsafe": [],
        "present_match": [],
        "byte_store": {},
    }
    for root, _, files in os.walk(dir_path):
        for f in files:
            full = Path(root) / f
            rel = str(full.relative_to(dir_path))
            if is_unsafe_path(rel):
                result["unsafe"].append(rel)
                continue
            data = full.read_bytes()
            digest = sha256_bytes(data)
            result["byte_store"][rel] = data
            status = InventoryStatus.EXTRA.value
            if expected_manifest and rel in expected_manifest:
                if expected_manifest[rel] == digest:
                    status = InventoryStatus.PRESENT_MATCH.value
                    result["present_match"].append(rel)
                else:
                    status = InventoryStatus.CHANGED.value
                    result["changed"].append(rel)
            else:
                result["extra"].append(rel)
            result["entries"].append({"path": rel, "size": len(data), "sha256": digest, "status": status})
    if expected_manifest:
        for exp in expected_manifest:
            if exp not in result["byte_store"]:
                result["missing"].append(exp)
    if not result["missing"] and not result["changed"] and not result["unsafe"]:
        result["status"] = "VERIFIED_COMPLETE" if expected_manifest else "STRUCTURALLY_VALID"
    else:
        result["status"] = "INCOMPLETE"
    return result
