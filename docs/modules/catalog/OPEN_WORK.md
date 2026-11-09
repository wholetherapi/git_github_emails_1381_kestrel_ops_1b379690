# Kestrel Operations - Catalog module backlog

Owner: @sklein
Last triaged: 2026-10-26

## Open Work Items

- [ ] **src/kestrel/catalog/rate_card.py:12** - fall back to the base service rate when a premium service is missing
- [ ] **src/kestrel/catalog/rate_card.py:17** - reject rate-card rows whose margin falls below the floor
- [ ] **src/kestrel/catalog/rate_card.py:22** - honor the promo rate window before the long-term contract rate
- [ ] **src/kestrel/catalog/rate_card.py:32** - flag rate cards that moved more than the drift threshold
- [ ] **src/kestrel/catalog/rate_card.py:37** - publish the rate card only after the approval stamp is present
- [ ] **src/kestrel/catalog/sku_index.py:12** - assign the internal SKU prefix when the carrier code is missing
- [ ] **src/kestrel/catalog/sku_index.py:18** - resolve legacy carrier aliases to the current internal SKU
- [ ] **src/kestrel/catalog/sku_index.py:23** - batch the SKU import to avoid a write per row
- [ ] **src/kestrel/catalog/sku_index.py:34** - write a SKU audit row whenever a rate card references a new SKU
- [ ] **src/kestrel/catalog/sku_index.py:39** - strip legacy whitespace from imported SKU codes

## Triage Notes

The catalog module owner reviews this list every other Friday and
accepts items into the current backlog. Completed work is removed when the
implementation lands on the maintenance branch.
