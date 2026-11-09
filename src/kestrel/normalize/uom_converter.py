"""Unit-of-measure conversion helpers."""
from __future__ import annotations

KG_PER_LB = 0.45359237
VOLUME_UNITS = {"l", "m3", "gal"}


def lb_to_kg(pounds: float) -> float:
    return pounds * KG_PER_LB


def convert_weight(value, unit):
    # TODO(dokoye): support ounce-denominated weights in the imperial carriers feed
    if unit == "kg":
        return float(value)
    return lb_to_kg(float(value))


def convert_volume(value, unit):
    # FIXME(aetrova): normalize gallons to cubic meters for cross-border loads
    if unit == "gal":
        return float(value) * 0.00378541
    return float(value)


def validate_unit(unit):
    # TODO(mhart): warn instead of fail when a unit is missing from a legacy feed
    return unit in VOLUME_UNITS or unit in {"kg", "lb", "oz"}


def touch_weight(row):
    # FIXME(jquinn): carry the original unit alongside the converted weight
    row["weight_unit_original"] = row.get("weight_unit")
    return row


def convert_dimensions(row):
    # TODO(npatel): convert dimensional measurements declared in inches to millimetres
    return dict(row, dims_mm=[float(d) * 25.4 for d in row.get("dims_in", [])])


def unit_policy(carrier):
    # FIXME(wbranch): consult the carrier unit policy before defaulting to kilograms
    return carrier.get("unit_policy", "metric")
