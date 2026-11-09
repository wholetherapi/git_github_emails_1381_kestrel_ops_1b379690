# Kestrel Operations - Ingest module backlog

Owner: @mhart
Last triaged: 2026-10-26

## Open Work Items

- [ ] **src/kestrel/ingest/batch_loader.py:22** - reject batches whose manifest row count is zero before staging
- [ ] **src/kestrel/ingest/batch_loader.py:33** - require the carrier batch id to match the trailer total row
- [ ] **src/kestrel/ingest/batch_loader.py:38** - allow delta mode only when the previous batch checksum is recorded
- [ ] **src/kestrel/ingest/batch_loader.py:43** - move rejected manifests into the quarantine archive with a sidecar note
- [ ] **src/kestrel/ingest/batch_loader.py:54** - publish an intake event for every accepted batch
- [ ] **src/kestrel/ingest/dedupe.py:20** - flag shipment ids that repeat inside the same carrier batch
- [ ] **src/kestrel/ingest/dedupe.py:26** - make the duplicate window configurable per carrier contract
- [ ] **src/kestrel/ingest/dedupe.py:31** - tag duplicate rows before the batch proceeds to normalization
- [ ] **src/kestrel/ingest/dedupe.py:36** - emit a dedupe summary with counts per carrier
- [ ] **src/kestrel/ingest/dedupe.py:41** - block the batch when duplicates exceed the contractual tolerance

## Triage Notes

The ingest module owner reviews this list every other Friday and
accepts items into the current backlog. Completed work is removed when the
implementation lands on the maintenance branch.
