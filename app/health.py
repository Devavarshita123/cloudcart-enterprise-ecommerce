"""Health-check logic used by the local portfolio demo."""
from typing import Any


def get_app_info() -> dict[str, str]:
    return {"name": "CloudCart", "version": "1.0.0", "environment": "local"}


def health_check(app_info: dict[str, Any] | None = None) -> dict[str, str]:
    if app_info is None:
        app_info = get_app_info()
    if not isinstance(app_info, dict):
        return {"status": "unhealthy", "message": "Application information must be a dictionary."}

    name = app_info.get("name")
    version = app_info.get("version")
    if (
        isinstance(name, str) and name.strip()
        and isinstance(version, str) and version.strip()
    ):
        return {"status": "healthy", "message": "CloudCart application is running."}
    return {
        "status": "unhealthy",
        "message": "Required application information is missing or invalid.",
    }
