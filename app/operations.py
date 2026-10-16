"""Operational Excellence pillar: structured diagnostic events."""
import json
import logging
import uuid
from typing import Any

_LOGGER = logging.getLogger("cloudcart")


def configure_logging(level: str = "INFO") -> None:
    logging.basicConfig(level=getattr(logging, level, logging.INFO), format="%(message)s")


def diagnostic_event(event: str, status: str, correlation_id: str | None = None) -> dict[str, Any]:
    if not event or not event.strip():
        raise ValueError("event must be a non-empty string")
    if status not in {"ok", "warning", "error"}:
        raise ValueError("status must be ok, warning, or error")
    event_record = {
        "application": "CloudCart",
        "event": event.strip(),
        "status": status,
        "correlation_id": correlation_id or str(uuid.uuid4()),
    }
    _LOGGER.info(json.dumps(event_record, sort_keys=True))
    return event_record


def operations_demo() -> dict[str, Any]:
    record = diagnostic_event("health_check_completed", "ok", "demo-correlation-001")
    return {
        "passed": record["event"] == "health_check_completed" and bool(record["correlation_id"]),
        "event": record,
        "note": "Console structured logging only; no CloudWatch or alert integration is configured.",
    }
