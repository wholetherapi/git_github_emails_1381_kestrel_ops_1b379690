# Kestrel Operations - Settlement module backlog

Owner: @npatel
Last triaged: 2026-10-26

## Open Work Items

- [ ] **src/kestrel/settlement/credit_notes.py:8** - auto-approve credit notes under the operator limit
- [ ] **src/kestrel/settlement/credit_notes.py:13** - route notes above the auto-approval limit to the settlement manager
- [ ] **src/kestrel/settlement/credit_notes.py:29** - post the credit note against the original invoice period
- [ ] **src/kestrel/settlement/credit_notes.py:34** - keep voided credit notes visible for audit without posting them
- [ ] **src/kestrel/settlement/credit_notes.py:39** - notify the carrier of approved credits in the nightly batch
- [ ] **src/kestrel/settlement/invoice_builder.py:12** - group invoice lines by charge category before rendering
- [ ] **src/kestrel/settlement/invoice_builder.py:18** - compute the due date from the contract payment terms
- [ ] **src/kestrel/settlement/invoice_builder.py:23** - add destination tax lines for cross-border invoices
- [ ] **src/kestrel/settlement/invoice_builder.py:28** - embed the carrier logo only when the branding flag is enabled
- [ ] **src/kestrel/settlement/invoice_builder.py:44** - link credit notes to the originating invoice line
- [ ] **src/kestrel/settlement/invoice_builder.py:49** - hold invoices whose shipment reconciliation is still open

## Triage Notes

The settlement module owner reviews this list every other Friday and
accepts items into the current backlog. Completed work is removed when the
implementation lands on the maintenance branch.
