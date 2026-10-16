"""Safe, local application configuration."""
from dataclasses import dataclass
import os


@dataclass(frozen=True)
class AppConfig:
    name: str = "CloudCart"
    version: str = "1.0.0"
    environment: str = "local"
    log_level: str = "INFO"

    @classmethod
    def from_environment(cls) -> "AppConfig":
        # Read only non-secret settings. Never print environment variables wholesale.
        name = os.getenv("CLOUDCART_APP_NAME", "CloudCart").strip()
        version = os.getenv("CLOUDCART_VERSION", "1.0.0").strip()
        environment = os.getenv("CLOUDCART_ENV", "local").strip().lower()
        log_level = os.getenv("CLOUDCART_LOG_LEVEL", "INFO").strip().upper()

        if not name or len(name) > 80:
            raise ValueError("CLOUDCART_APP_NAME must be 1–80 characters.")
        if not version or len(version) > 30:
            raise ValueError("CLOUDCART_VERSION must be 1–30 characters.")
        if environment not in {"local", "test", "staging", "production"}:
            raise ValueError("CLOUDCART_ENV must be local, test, staging, or production.")
        if log_level not in {"DEBUG", "INFO", "WARNING", "ERROR"}:
            raise ValueError("CLOUDCART_LOG_LEVEL is invalid.")

        return cls(name=name, version=version, environment=environment, log_level=log_level)
