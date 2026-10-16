"""Reliability pillar: health aggregation and bounded retry simulation."""
from collections.abc import Callable
from typing import Any


def aggregate_health(dependencies: dict[str, bool]) -> dict[str, Any]:
    if not dependencies:
        return {"status": "unhealthy", "dependencies": {}, "failed": ["no dependencies configured"]}
    failed = sorted(name for name, healthy in dependencies.items() if not healthy)
    return {
        "status": "healthy" if not failed else "degraded",
        "dependencies": dict(dependencies),
        "failed": failed,
    }


def retry(operation: Callable[[], Any], attempts: int = 3) -> dict[str, Any]:
    """Retry a callable up to attempts; intentionally no sleeping for fast local tests."""
    if not isinstance(attempts, int) or attempts < 1 or attempts > 10:
        raise ValueError("attempts must be an integer from 1 to 10")
    errors: list[str] = []
    for attempt in range(1, attempts + 1):
        try:
            return {"success": True, "attempts": attempt, "result": operation(), "errors": errors}
        except Exception as exc:  # Demo boundary: record type, not sensitive exception contents.
            errors.append(type(exc).__name__)
    return {"success": False, "attempts": attempts, "result": None, "errors": errors}


def reliability_demo() -> dict[str, Any]:
    state = {"calls": 0}

    def succeeds_on_third_call() -> str:
        state["calls"] += 1
        if state["calls"] < 3:
            raise TimeoutError("simulated timeout")
        return "simulated dependency recovered"

    result = retry(succeeds_on_third_call, attempts=3)
    health = aggregate_health({"catalog": True, "payments-sandbox": True})
    return {
        "passed": result["success"] and result["attempts"] == 3 and health["status"] == "healthy",
        "retry_attempts": result["attempts"],
        "health": health,
        "note": "Simulation only; no real dependency, failover, or SLA is tested.",
    }
