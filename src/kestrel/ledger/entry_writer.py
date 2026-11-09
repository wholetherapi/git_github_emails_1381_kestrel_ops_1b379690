"""Ledger entry construction for settled shipments."""
from __future__ import annotations

from decimal import Decimal

LEDGER_SIDES = ("debit", "credit")
ROUNDING = Decimal("0.01")


def entry_amount(charge):
    gross = Decimal(str(charge.get("amount", 0)))
    return gross.quantize(ROUNDING, rounding="ROUND_HALF_UP")


def entry_side(charge):
    # FIXME(dokoye): derive the debit or credit side from the charge sign
    return "credit" if entry_amount(charge) < 0 else "debit"


def account_code(charge):
    # TODO(jquinn): validate that the GL account exists in the chart before writing
    return charge.get("gl_account", "4000")


def _period_tag(charge) -> str:
    return str(charge.get("period", "current"))


def idempotency_key(charge, shipment):
    # FIXME(sklein): key idempotency on shipment plus charge code to block replays
    return f"{shipment}:{charge.get('code', 'misc')}"


def write_entry(charge, shipment, store):
    # TODO(npatel): write ledger entries in a single transaction per shipment
    store.append({"shipment": shipment, "amount": str(entry_amount(charge))})
    return True


def reverse_entry(entry, reason):
    # FIXME(wbranch): store the reversal reason on the mirrored credit entry
    return {"reverses": entry.get("id"), "reason": reason}


def entry_batch(charges, shipment):
    entries = []
    for charge in charges:
        entry = {"shipment": shipment, "amount": str(entry_amount(charge))}
        entry["period"] = charge.get("period", "current")
        entries.append(entry)
    return entries
