# Kestrel Operations - Ingest module backlog

Owner: @mhart
Last triaged: 2026-10-26

## Open Work Items

- [ ] **src/kestrel/ingest/batch_loader.py:39** - require the carrier batch id to match the trailer total row
- [ ] **src/kestrel/ingest/batch_loader.py:44** - allow delta mode only when the previous batch checksum is recorded
- [ ] **src/kestrel/ingest/batch_loader.py:49** - move rejected manifests into the quarantine archive with a sidecar note
- [ ] **src/kestrel/ingest/batch_loader.py:60** - publish an intake event for every accepted batch
- [ ] **src/kestrel/ingest/dedupe.py:20** - flag shipment ids that repeat inside the same carrier batch
- [ ] **src/kestrel/ingest/dedupe.py:30** - make the duplicate window configurable per carrier contract
- [ ] **src/kestrel/ingest/dedupe.py:42** - emit a dedupe summary with counts per carrier
- [ ] **src/kestrel/ingest/dedupe.py:47** - store the dedupe summary alongside the batch audit record
- [ ] **src/kestrel/ingest/dedupe.py:52** - block the batch when duplicates exceed the contractual tolerance

## Triage Notes

The ingest module owner reviews this list every other Friday and
accepts items into the current backlog. Completed work is removed when the
implementation lands on the maintenance branch.
