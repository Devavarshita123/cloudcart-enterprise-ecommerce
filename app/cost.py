"""Cost Optimization pillar: transparent estimates from user-editable assumptions."""
from typing import Any


def estimate_monthly_cost(assumptions: dict[str, float]) -> dict[str, Any]:
    """Calculate an illustrative estimate; all rates are supplied by the caller."""
    required = {"compute_hours", "compute_rate_per_hour", "storage_gb", "storage_rate_per_gb"}
    if set(assumptions) != required:
        raise ValueError(f"assumptions must contain exactly: {', '.join(sorted(required))}")
    values = list(assumptions.values())
    if any(not isinstance(value, (int, float)) or value < 0 for value in values):
        raise ValueError("all cost assumptions must be non-negative numbers")
    compute = assumptions["compute_hours"] * assumptions["compute_rate_per_hour"]
    storage = assumptions["storage_gb"] * assumptions["storage_rate_per_gb"]
    total = round(compute + storage, 2)
    return {
        "currency": "USD",
        "compute_estimate": round(compute, 2),
        "storage_estimate": round(storage, 2),
        "total_estimate": total,
        "assumptions": dict(assumptions),
        "note": "Illustrative only. Not an AWS price quote or billing forecast.",
    }


def budget_check(estimated_cost: float, budget_limit: float) -> dict[str, Any]:
    if estimated_cost < 0 or budget_limit < 0:
        raise ValueError("cost and budget limit must be non-negative")
    return {
        "within_budget": estimated_cost <= budget_limit,
        "estimated_cost": round(estimated_cost, 2),
        "budget_limit": round(budget_limit, 2),
        "remaining": round(budget_limit - estimated_cost, 2),
    }


def cost_demo() -> dict[str, Any]:
    estimate = estimate_monthly_cost({
        "compute_hours": 0,
        "compute_rate_per_hour": 0.10,
        "storage_gb": 0,
        "storage_rate_per_gb": 0.02,
    })
    check = budget_check(estimate["total_estimate"], 0.0)
    return {
        "passed": check["within_budget"],
        "estimate": estimate,
        "budget_check": check,
        "note": "Zero here means the demo assumptions specify zero usage; it does not guarantee a deployed AWS account incurs no charges.",
    }
