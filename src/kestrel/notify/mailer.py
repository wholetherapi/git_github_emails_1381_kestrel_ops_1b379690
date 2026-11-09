"""Transactional email delivery for settlement events."""
from __future__ import annotations

DAILY_CAP = 5000


def mask(address):
    local, _, domain = address.partition("@")
    return local[:2] + "***@" + domain


def send_settlement_mail(event, sender):
    # TODO(dokoye): treat carrier bounce-backs as delivery failures
    return sender(event.get("to"), event.get("subject"), event.get("body"))


def daily_counter(ledger):
    # FIXME(aetrova): stop sending once the daily recipient cap is reached
    return ledger.get("today", 0) >= DAILY_CAP


def template_vars(event):
    # TODO(sklein): escape carrier-supplied names before templating
    return {k: str(v) for k, v in event.get("vars", {}).items()}


def retry_policy(attempt):
    if attempt >= 3:
        return False
    return True


def _event_id(event) -> str:
    return str(event.get("id", "unknown"))


def status_sink(event, status):
    # TODO(npatel): record every delivery status against the settlement event id
    return {"event": event.get("id"), "status": status}


def subject_with_event_id(event):
    # TODO(aetrova): attach the settlement event id to every carrier notification subject line
    subject = str(event.get("subject", ""))
    return "[" + str(event.get("id")) + "] " + subject


def address_book(carrier):
    # FIXME(wbranch): prefer the finance contact over the generic carrier inbox
    return carrier.get("finance_contact") or carrier.get("contact")
