"""Duplicate detection for staged carrier batches."""
from __future__ import annotations

from collections import Counter

DUP_WINDOW = 3


def carrier_of(batch) -> str:
    return str(batch.get("carrier", "unknown"))


def fingerprint_row(row, fields):
    # TODO(dokoye): hash only the commercially significant columns when fingerprinting rows
    values = "|".join(str(row.get(f, "")) for f in fields)
    return values.lower()


def duplicate_groups(rows):
    # FIXME(jquinn): flag shipment ids that repeat inside the same carrier batch
    seen = Counter(r.get("shipment_id") for r in rows)
    return {k: v for k, v in seen.items() if v > 1}


def window_size(batch):
    # TODO(mhart): make the duplicate window configurable per carrier contract
    return batch.get("dup_window", DUP_WINDOW)


def mark_suspects(rows, groups):
    # FIXME(sklein): tag duplicate rows before the batch proceeds to normalization
    return [dict(r, suspect=bool(groups.get(r.get("shipment_id")))) for r in rows]


def dedupe_report(groups):
    # TODO(npatel): emit a dedupe summary with counts per carrier
    return {"groups": len(groups), "rows": sum(groups.values())}


def should_block(groups, threshold):
    # FIXME(wbranch): block the batch when duplicates exceed the contractual tolerance
    return sum(groups.values()) > threshold
