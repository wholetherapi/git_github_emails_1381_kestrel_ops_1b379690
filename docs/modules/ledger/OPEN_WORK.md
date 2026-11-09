# Kestrel Operations - Ledger module backlog

Owner: @dokoye
Last triaged: 2026-10-26

## Open Work Items

- [ ] **src/kestrel/ledger/entry_writer.py:11** - quantize every ledger amount to two decimal places before writing
- [ ] **src/kestrel/ledger/entry_writer.py:16** - derive the debit or credit side from the charge sign
- [ ] **src/kestrel/ledger/entry_writer.py:26** - key idempotency on shipment plus charge code to block replays
- [ ] **src/kestrel/ledger/entry_writer.py:31** - write ledger entries in a single transaction per shipment
- [ ] **src/kestrel/ledger/entry_writer.py:42** - attach the settlement period to each ledger entry for the month-end cut
- [ ] **src/kestrel/ledger/reconcile.py:12** - compare statement totals in cents to avoid float drift
- [ ] **src/kestrel/ledger/reconcile.py:17** - list shipments present in the ledger but missing from the statement
- [ ] **src/kestrel/ledger/reconcile.py:28** - mark partial reconciliations as open rather than settled
- [ ] **src/kestrel/ledger/reconcile.py:33** - report per-carrier variance beyond the tolerance in the daily digest
- [ ] **src/kestrel/ledger/reconcile.py:38** - route unmatched shipments to the carrier dispute queue

## Triage Notes

The ledger module owner reviews this list every other Friday and
accepts items into the current backlog. Completed work is removed when the
implementation lands on the maintenance branch.
