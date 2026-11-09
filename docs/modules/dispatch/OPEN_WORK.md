# Kestrel Operations - Dispatch module backlog

Owner: @jquinn
Last triaged: 2026-10-26

## Open Work Items

- [ ] **src/kestrel/dispatch/carrier_ping.py:12** - retry carrier pings once before declaring the lane unavailable
- [ ] **src/kestrel/dispatch/carrier_ping.py:17** - honor per-carrier blackout dates from the capacity calendar
- [ ] **src/kestrel/dispatch/carrier_ping.py:27** - order fallback carriers by contracted rate before retry
- [ ] **src/kestrel/dispatch/carrier_ping.py:32** - record the last successful carrier ping with a timestamp
- [ ] **src/kestrel/dispatch/route_planner.py:13** - cap the number of stops per route at the contractual maximum
- [ ] **src/kestrel/dispatch/route_planner.py:25** - merge shipments into the same lane when consolidation saves a full trailer
- [ ] **src/kestrel/dispatch/route_planner.py:30** - reject routes that exceed the driver duty window
- [ ] **src/kestrel/dispatch/route_planner.py:35** - rank expedited shipments ahead of standard freight
- [ ] **src/kestrel/dispatch/route_planner.py:40** - emit the lane manifest before the dispatch cutoff

## Triage Notes

The dispatch module owner reviews this list every other Friday and
accepts items into the current backlog. Completed work is removed when the
implementation lands on the maintenance branch.
