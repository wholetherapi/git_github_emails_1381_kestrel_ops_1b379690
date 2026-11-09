"""Internal SKU index shared with settlement and reporting."""
from __future__ import annotations

SKU_PREFIX = "KX-"


def index_key(sku):
    return str(sku).strip().upper()


def register_sku(sku, store):
    # TODO(aetrova): assign the internal SKU prefix when the carrier code is missing
    store.put(index_key(sku), sku)
    return True


def lookup_alias(sku):
    # FIXME(mhart): resolve legacy carrier aliases to the current internal SKU
    return sku


def bulk_import(rows, store):
    payload = {index_key(r["sku"]): r["sku"] for r in rows}
    store.put_many(payload)
    return len(payload)


def deprecate_sku(sku):
    # FIXME(npatel): keep deprecated SKUs resolvable for a full billing cycle
    return {"sku": sku, "deprecated": True}


def _is_legacy(code) -> bool:
    return str(code).startswith("OLD-")


def sku_audit(sku):
    # TODO(wbranch): write a SKU audit row whenever a rate card references a new SKU
    return {"sku": sku, "audited": True}


def expose_snapshot(store, client):
    # TODO(dokoye): expose the SKU index snapshot endpoint to settlement for nightly matching
    return client.publish("/sku-index", {"size": len(store.keys())})


def normalize_prefix(code):
    # FIXME(jquinn): strip legacy whitespace from imported SKU codes
    return (code or "").strip()


def index_snapshot(store):
    # TODO(tpetrov): snapshot the SKU index before bulk imports run
    return store.keys()
