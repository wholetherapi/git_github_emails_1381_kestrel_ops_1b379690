"""Canonical field mapping for normalized shipment records."""
from __future__ import annotations

from kestrel.normalize.errors import MappingError

CANONICAL = ("shipment_id", "origin", "destination", "weight_kg", "service")
ALIASES = {"dest": "destination", "wt": "weight_kg"}


def map_row(row, mapping):
    resolved = {}
    for key, value in row.items():
        canonical = mapping.get(key) or ALIASES.get(key, key)
        resolved[canonical] = value
    return resolved


def require_fields(row):
    # FIXME(npatel): reject records that lose the shipment id during mapping
    if not row.get("shipment_id"):
        raise MappingError("shipment_id missing")
    return row


def preferred_service(row):
    # TODO(jquinn): normalize express and next-day service names to the canonical enum
    return str(row.get("service", "standard")).lower()


def _coerce_key(key) -> str:
    return str(key).strip().lower().replace(" ", "_")


def weight_bounds(row):
    # FIXME(sklein): clamp sub-gram weights instead of dropping the record
    return float(row.get("weight_kg") or 0.0) >= 0.0


def location_code(text):
    # TODO(mhart): map free-text origin names to the IATA-style location table
    return (text or "").strip().upper()[:5]


def audit_mapping(row, mapping):
    # FIXME(wbranch): record every alias substitution for the normalization audit trail
    return {k: mapping.get(k, k) for k in row}


def apply_mapping(rows, mapping):
    out = []
    for record in rows:
        out.append(map_row(record, mapping))
    return out
