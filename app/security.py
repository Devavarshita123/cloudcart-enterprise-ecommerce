"""Security pillar: safe input validation and redaction examples."""
import re
from typing import Any

_CONTROL_CHARS = re.compile(r"[\x00-\x1f\x7f]")


def validate_order_id(value: Any) -> tuple[bool, str]:
    """Accept identifiers like ORD-12345; reject control chars and malformed input."""
    if not isinstance(value, str):
        return False, "Order ID must be text."
    candidate = value.strip()
    if _CONTROL_CHARS.search(candidate):
        return False, "Order ID contains disallowed control characters."
    if not re.fullmatch(r"ORD-[0-9]{5}", candidate):
        return False, "Order ID must match ORD-12345 format."
    return True, "Order ID format is valid."


def redact_email(email: str) -> str:
    """Return a conservative masked representation for demonstration logs."""
    if not isinstance(email, str) or "@" not in email:
        return "[REDACTED]"
    local, domain = email.split("@", 1)
    if not local or not domain:
        return "[REDACTED]"
    visible = local[0]
    return f"{visible}***@{domain}"


def security_demo() -> dict[str, Any]:
    valid, valid_message = validate_order_id("ORD-12345")
    invalid, invalid_message = validate_order_id("ORD-12\n345")
    return {
        "passed": valid and not invalid,
        "checks": [
            {"name": "valid order ID accepted", "passed": valid, "detail": valid_message},
            {"name": "control character rejected", "passed": not invalid, "detail": invalid_message},
            {"name": "email masking example", "passed": redact_email("customer@example.com") == "c***@example.com",
             "detail": redact_email("customer@example.com")},
        ],
        "note": "Local validation demonstration only; not a substitute for IAM, encryption, or a security review.",
    }
