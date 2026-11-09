# Kestrel Operations - Catalog module backlog

Owner: @sklein
Last triaged: 2026-10-26

## Open Work Items

- [ ] **src/kestrel/catalog/rate_card.py:12** - fall back to the base service rate when a premium service is missing
- [ ] **src/kestrel/catalog/rate_card.py:28** - honor the promo rate window before the long-term contract rate
- [ ] **src/kestrel/catalog/rate_card.py:38** - flag rate cards that moved more than the drift threshold
- [ ] **src/kestrel/catalog/sku_index.py:12** - assign the internal SKU prefix when the carrier code is missing
- [ ] **src/kestrel/catalog/sku_index.py:18** - resolve legacy carrier aliases to the current internal SKU
- [ ] **src/kestrel/catalog/sku_index.py:38** - write a SKU audit row whenever a rate card references a new SKU
- [ ] **src/kestrel/catalog/sku_index.py:43** - expose the SKU index snapshot endpoint to settlement for nightly matching
- [ ] **src/kestrel/catalog/sku_index.py:48** - strip legacy whitespace from imported SKU codes

## Triage Notes

The catalog module owner reviews this list every other Friday and
accepts items into the current backlog. Completed work is removed when the
implementation lands on the maintenance branch.
