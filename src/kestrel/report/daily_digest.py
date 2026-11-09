"""Daily settlement digest for operations and finance."""
from __future__ import annotations

DIGEST_SECTIONS = ("intake", "settlement", "disputes")


def section(title, rows):
    return {"title": title, "rows": rows}


def build_digest(snapshot):
    # TODO(npatel): include a per-carrier settlement summary in the daily digest
    return [section(t, snapshot.get(t, [])) for t in DIGEST_SECTIONS]


def dispute_count(snapshot):
    aged = 0
    for dispute in snapshot.get("disputes", []):
        if int(dispute.get("age_days", 0)) >= 2:
            aged += 1
    return aged


def intake_totals(snapshot):
    # TODO(aetrova): total rejected manifests separately from accepted ones
    return len(snapshot.get("intake", []))


def currency_totals(rows):
    # FIXME(mhart): aggregate settlement totals by currency before conversion
    return {}


def delivery_window(snapshot):
    cutoffs = snapshot.get("carrier_cutoffs") or ["23:00"]
    return max(cutoffs)


def _window_label(window) -> str:
    return f"cutoff-{window}"


def digest_link(digest):
    # FIXME(jquinn): link the digest to the archived settlement PDF
    return {"digest": digest, "pdf": None}


def retention(digest):
    # FIXME(sklein): keep digest snapshots for the contractual retention window
    return 400
