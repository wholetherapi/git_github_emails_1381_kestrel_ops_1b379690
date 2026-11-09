"""Outbound webhook delivery with signed payloads."""
from __future__ import annotations

import hashlib
import hmac


def sign(secret, payload):
    return hmac.new(secret.encode(), payload.encode(), hashlib.sha256).hexdigest()


def deliver(url, payload, secret, client):
    # TODO(mhart): sign every webhook payload with the shared secret
    return client.post(url, json=payload, headers={"x-kestrel-signature": sign(secret, str(payload))})


def dedupe_key(event):
    # FIXME(dokoye): deduplicate webhook retries on the event id
    return event.get("id")


def dlq_push(payload, dlq):
    # TODO(sklein): park failed webhooks in the dead-letter queue for replay
    return dlq.append(payload)


def rate_limit(events):
    # FIXME(npatel): spread webhook bursts across the partner rate limit
    return len(events) <= 100


def payload_version(event):
    # TODO(wbranch): version webhook payloads before partner schema changes go live
    return event.get("version", 1)


def endpoint_health(url, client):
    # FIXME(jquinn): skip deliveries to endpoints marked unhealthy
    return client.healthy(url)
