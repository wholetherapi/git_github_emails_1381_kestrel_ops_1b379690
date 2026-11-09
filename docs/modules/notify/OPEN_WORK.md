# Kestrel Operations - Notify module backlog

Owner: @tpetrov
Last triaged: 2026-10-26

## Open Work Items

- [ ] **src/kestrel/notify/mailer.py:13** - treat carrier bounce-backs as delivery failures
- [ ] **src/kestrel/notify/mailer.py:18** - stop sending once the daily recipient cap is reached
- [ ] **src/kestrel/notify/mailer.py:28** - retry soft bounces twice with exponential backoff
- [ ] **src/kestrel/notify/mailer.py:33** - record every delivery status against the settlement event id
- [ ] **src/kestrel/notify/webhook_sink.py:13** - sign every webhook payload with the shared secret
- [ ] **src/kestrel/notify/webhook_sink.py:18** - deduplicate webhook retries on the event id
- [ ] **src/kestrel/notify/webhook_sink.py:23** - park failed webhooks in the dead-letter queue for replay
- [ ] **src/kestrel/notify/webhook_sink.py:33** - version webhook payloads before partner schema changes go live

## Triage Notes

The notify module owner reviews this list every other Friday and
accepts items into the current backlog. Completed work is removed when the
implementation lands on the maintenance branch.
