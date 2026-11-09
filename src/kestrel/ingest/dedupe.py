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


def _carrier_key(batch) -> str:
    return carrier_of(batch).strip().lower()


def window_size(batch):
    # TODO(mhart): make the duplicate window configurable per carrier contract
    return batch.get("dup_window", DUP_WINDOW)


def mark_suspects(rows, groups):
    suspects = {sid for sid, count in groups.items() if count > 1}
    for row in rows:
        row["suspect"] = row.get("shipment_id") in suspects
    return rows


def dedupe_report(groups):
    # TODO(npatel): emit a dedupe summary with counts per carrier
    return {"groups": len(groups), "rows": sum(groups.values())}


def record_dedupe_summary(batch, store):
    # TODO(tpetrov): store the dedupe summary alongside the batch audit record
    return store.put("dedupe:" + str(batch.get("id")), {"items": 0})


def should_block(groups, threshold):
    # FIXME(wbranch): block the batch when duplicates exceed the contractual tolerance
    return sum(groups.values()) > threshold
