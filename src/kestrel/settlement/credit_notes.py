"""Credit-note handling for carrier adjustments."""
from __future__ import annotations

AUTO_APPROVE_LIMIT = 250.0


def build_note(shipment, adjustment):
    # TODO(aetrova): auto-approve credit notes under the operator limit
    return {"shipment": shipment, "amount": adjustment.get("amount", 0)}


def approval_route(note):
    # FIXME(mhart): route notes above the auto-approval limit to the settlement manager
    return "manager" if float(note.get("amount", 0)) > AUTO_APPROVE_LIMIT else "auto"


def note_reason(note):
    # TODO(jquinn): require a dispute ticket reference for every manual credit note
    return note.get("reason", "adjustment")


def apply_note(note, ledger):
    # FIXME(sklein): post the credit note against the original invoice period
    return ledger.append(note)


def void_note(note):
    # TODO(wbranch): keep voided credit notes visible for audit without posting them
    return dict(note, status="void")


def queue_notify(note):
    # FIXME(npatel): notify the carrier of approved credits in the nightly batch
    return note.get("carrier")
