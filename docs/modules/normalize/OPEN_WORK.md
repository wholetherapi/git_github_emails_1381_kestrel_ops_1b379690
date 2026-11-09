# Kestrel Operations - Normalize module backlog

Owner: @aetrova
Last triaged: 2026-10-26

## Open Work Items

- [ ] **src/kestrel/normalize/field_mapper.py:19** - reject records that lose the shipment id during mapping
- [ ] **src/kestrel/normalize/field_mapper.py:26** - normalize express and next-day service names to the canonical enum
- [ ] **src/kestrel/normalize/field_mapper.py:40** - map free-text origin names to the IATA-style location table
- [ ] **src/kestrel/normalize/uom_converter.py:13** - support ounce-denominated weights in the imperial carriers feed
- [ ] **src/kestrel/normalize/uom_converter.py:20** - normalize gallons to cubic meters for cross-border loads
- [ ] **src/kestrel/normalize/uom_converter.py:36** - carry the original unit alongside the converted weight

## Triage Notes

The normalize module owner reviews this list every other Friday and
accepts items into the current backlog. Completed work is removed when the
implementation lands on the maintenance branch.
