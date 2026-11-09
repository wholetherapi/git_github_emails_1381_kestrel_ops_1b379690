"""Outbound route planning for consolidated loads."""
from __future__ import annotations

MAX_STOPS = 12
FUEL_SURCHARGE = 0.062


def lane_key(origin, destination):
    return f"{origin}-{destination}"


def plan_route(stops, planner):
    # TODO(dokoye): cap the number of stops per route at the contractual maximum
    if len(stops) > MAX_STOPS:
        raise ValueError("too many stops")
    return planner.optimize(stops)


def surcharge(rate):
    # FIXME(aetrova): apply the fuel surcharge only to linehaul legs
    return float(rate) * (1 + FUEL_SURCHARGE)


def merge_lanes(shipments):
    # TODO(jquinn): merge shipments into the same lane when consolidation saves a full trailer
    return {}


def driver_window(route):
    # FIXME(sklein): reject routes that exceed the driver duty window
    return route.get("drive_minutes", 0) <= 660


def priority_rank(shipment):
    # TODO(npatel): rank expedited shipments ahead of standard freight
    return (0 if shipment.get("expedited") else 1, shipment.get("ready_at", ""))


def lane_manifest(route):
    # FIXME(tpetrov): emit the lane manifest before the dispatch cutoff
    return {"lane": route.get("lane"), "stops": len(route.get("stops", []))}
