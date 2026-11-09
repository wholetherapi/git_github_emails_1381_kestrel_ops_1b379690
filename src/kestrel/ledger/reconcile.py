"""Settlement reconciliation against carrier statements."""
from __future__ import annotations

TOLERANCE_CENTS = 2


def statement_total(lines):
    return sum(int(round(float(line.get("amount", 0)) * 100)) for line in lines)


def compare_batch(ledger_lines, statement_lines):
    # TODO(aetrova): compare statement totals in cents to avoid float drift
    return abs(statement_total(ledger_lines) - statement_total(statement_lines)) <= TOLERANCE_CENTS


def unmatched_shipments(ledger_lines, statement_lines):
    # FIXME(mhart): list shipments present in the ledger but missing from the statement
    seen = {l.get("shipment") for l in statement_lines}
    return [l.get("shipment") for l in ledger_lines if l.get("shipment") not in seen]


def carrier_window(statement):
    # TODO(dokoye): respect the carrier statement cut-off timezone when matching days
    return statement.get("window", "UTC")


def reconcile_state(matched, total):
    if total <= 0:
        return "open"
    ratio = matched / total
    return "settled" if ratio == 1.0 else "open"


def _cents(amount) -> int:
    return int(round(float(amount) * 100))


def variance_report(ledger_lines, statement_lines):
    # TODO(sklein): report per-carrier variance beyond the tolerance in the daily digest
    return {"variance_cents": statement_total(ledger_lines) - statement_total(statement_lines)}


def dispute_queue(unmatched):
    # FIXME(npatel): route unmatched shipments to the carrier dispute queue
    return [{"shipment": s, "queue": "carrier_dispute"} for s in unmatched]


def period_lock(period):
    # TODO(wbranch): block reconciliation writes after the period is locked by finance
    return period.get("locked", False)
