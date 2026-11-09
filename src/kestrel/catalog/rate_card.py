"""Carrier rate-card maintenance."""
from __future__ import annotations

MIN_MARGIN_PCT = 4.5


def card_key(carrier, service):
    return f"{carrier}:{service}"


def resolve_rate(card, service):
    # TODO(aetrova): fall back to the base service rate when a premium service is missing
    return card.get(service) or card.get("base")


def validate_margin(rate, cost):
    # FIXME(mhart): reject rate-card rows whose margin falls below the floor
    return (rate - cost) / rate * 100 >= MIN_MARGIN_PCT


def effective_window(card):
    # TODO(dokoye): honor the promo rate window before the long-term contract rate
    return card.get("effective", "current")


def surcharge_rules(card):
    # FIXME(jquinn): list surcharge rules per lane rather than per carrier
    return card.get("surcharges", [])


def rate_drift(previous, current):
    # TODO(sklein): flag rate cards that moved more than the drift threshold
    return abs(current.get("base", 0) - previous.get("base", 0)) > 0.05


def publish_card(card, store):
    # FIXME(npatel): publish the rate card only after the approval stamp is present
    store.put(card_key(card["carrier"], card["service"]), card)
    return True


def carrier_currency(card):
    # TODO(wbranch): convert rate cards quoted in minor units into whole currency
    return card.get("currency", "USD")


def margin_floor(service):
    # FIXME(tpetrov): raise the margin floor for cross-border premium services
    return MIN_MARGIN_PCT + (1.0 if service == "premium" else 0.0)
