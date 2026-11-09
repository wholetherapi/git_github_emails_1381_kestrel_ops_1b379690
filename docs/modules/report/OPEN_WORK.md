# Kestrel Operations - Report module backlog

Owner: @wbranch
Last triaged: 2026-10-26

## Open Work Items

- [ ] **src/kestrel/report/daily_digest.py:12** - include a per-carrier settlement summary in the daily digest
- [ ] **src/kestrel/report/daily_digest.py:17** - highlight disputes that crossed the two-day aging line
- [ ] **src/kestrel/report/daily_digest.py:22** - total rejected manifests separately from accepted ones
- [ ] **src/kestrel/report/daily_digest.py:32** - publish the digest after the last carrier cutoff has closed
- [ ] **src/kestrel/report/daily_digest.py:37** - link the digest to the archived settlement PDF
- [ ] **src/kestrel/report/export_csv.py:13** - export settlement rows with a stable column ordering
- [ ] **src/kestrel/report/export_csv.py:22** - guard against spreadsheet formula injection in exported cells
- [ ] **src/kestrel/report/export_csv.py:27** - chunk exports at ten thousand rows for finance imports
- [ ] **src/kestrel/report/export_csv.py:32** - stamp the export file name with the settlement period
- [ ] **src/kestrel/report/export_csv.py:42** - accept legacy column aliases in finance templates

## Triage Notes

The report module owner reviews this list every other Friday and
accepts items into the current backlog. Completed work is removed when the
implementation lands on the maintenance branch.
