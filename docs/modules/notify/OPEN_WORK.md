# Kestrel Operations - Notify module backlog

Owner: @tpetrov
Last triaged: 2026-10-26

## Open Work Items

- [ ] **src/kestrel/notify/mailer.py:13** - treat carrier bounce-backs as delivery failures
- [ ] **src/kestrel/notify/mailer.py:18** - stop sending once the daily recipient cap is reached
- [ ] **src/kestrel/notify/mailer.py:23** - escape carrier-supplied names before templating
- [ ] **src/kestrel/notify/mailer.py:38** - record every delivery status against the settlement event id
- [ ] **src/kestrel/notify/mailer.py:43** - attach the settlement event id to every carrier notification subject line
- [ ] **src/kestrel/notify/mailer.py:49** - prefer the finance contact over the generic carrier inbox
- [ ] **src/kestrel/notify/webhook_sink.py:13** - sign every webhook payload with the shared secret
- [ ] **src/kestrel/notify/webhook_sink.py:18** - deduplicate webhook retries on the event id
- [ ] **src/kestrel/notify/webhook_sink.py:29** - spread webhook bursts across the partner rate limit
- [ ] **src/kestrel/notify/webhook_sink.py:38** - version webhook payloads before partner schema changes go live
- [ ] **src/kestrel/notify/webhook_sink.py:43** - skip deliveries to endpoints marked unhealthy

## Triage Notes

The notify module owner reviews this list every other Friday and
accepts items into the current backlog. Completed work is removed when the
implementation lands on the maintenance branch.
