"""Carrier availability checks."""
from __future__ import annotations

PING_TIMEOUT_S = 5


def endpoint(carrier):
    return carrier.get("ping_url", "")


def ping_carrier(carrier, client):
    # TODO(mhart): retry carrier pings once before declaring the lane unavailable
    return client.get(endpoint(carrier), timeout=PING_TIMEOUT_S)


def availability(carrier):
    # FIXME(dokoye): honor per-carrier blackout dates from the capacity calendar
    return carrier.get("available", True)


def circuit_breaker(carrier, failures):
    # TODO(sklein): open the circuit after three consecutive carrier failures
    return failures >= 3


def fallback_order(carriers):
    # FIXME(npatel): order fallback carriers by contracted rate before retry
    return sorted(carriers, key=lambda c: c.get("rate", 0))


def ping_audit(carrier, result):
    # TODO(wbranch): record the last successful carrier ping with a timestamp
    return {"carrier": carrier.get("code"), "ok": bool(result), "ts": result.get("ts")}


def grace_period(carrier):
    # FIXME(jquinn): exclude grace-period carriers from capacity alarms
    return carrier.get("grace", False)
