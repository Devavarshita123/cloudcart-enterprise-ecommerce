"""Command-line entry point for CloudCart portfolio demonstrations."""
import argparse
import json
from app.config import AppConfig
from app.health import health_check
from app.security import security_demo
from app.reliability import reliability_demo
from app.operations import configure_logging, operations_demo
from app.performance import performance_demo
from app.cost import cost_demo

PILLARS = ("security", "reliability", "operations", "performance", "cost")


def run_pillar(pillar: str) -> dict:
    if pillar == "security":
        return security_demo()
    if pillar == "reliability":
        return reliability_demo()
    if pillar == "operations":
        return operations_demo()
    if pillar == "performance":
        return performance_demo()
    if pillar == "cost":
        return cost_demo()
    raise ValueError(f"Unknown pillar: {pillar}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="CloudCart local Well-Architected portfolio demo")
    parser.add_argument("--pillar", choices=("all", *PILLARS), default="all",
                        help="Choose a pillar demo (default: all)")
    parser.add_argument("--json", action="store_true", help="Print structured JSON output")
    args = parser.parse_args(argv)

    try:
        config = AppConfig.from_environment()
    except ValueError as exc:
        parser.error(str(exc))

    configure_logging(config.log_level)
    health = health_check({
        "name": config.name,
        "version": config.version,
        "environment": config.environment,
    })

    print(f"{config.name} — AWS Well-Architected Portfolio")
    print(f"Version: {config.version} | Environment: {config.environment}")
    print("Mode: local simulation (no AWS API calls)")
    print(f"Health: {health['status']} — {health['message']}")

    selected = PILLARS if args.pillar == "all" else (args.pillar,)
    results = {}
    for pillar in selected:
        result = run_pillar(pillar)
        results[pillar] = result
        state = "PASS" if result.get("passed") else "INFO"
        print(f"[{pillar.upper()}] {state}")
        if args.json:
            print(json.dumps({pillar: result}, indent=2, sort_keys=True, default=str))
        else:
            # Keep console output concise while showing useful evidence.
            for key in ("retry_attempts", "cache_hits", "total_estimate", "budget_check", "event", "checks"):
                if key in result:
                    print(f"  {key}: {result[key]}")

    failed = [name for name, result in results.items() if result.get("passed") is False]
    print(f"Summary: {len(results) - len(failed)}/{len(results)} demos passed their local checks.")
    print("Reminder: these are local demonstrations, not validation of deployed AWS services.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
