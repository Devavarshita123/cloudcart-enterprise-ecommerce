"""Performance Efficiency pillar: repeatable local microbenchmark."""
from functools import lru_cache
from time import perf_counter
from typing import Any


@lru_cache(maxsize=128)
def normalized_category(value: str) -> str:
    return value.strip().lower()


def performance_demo(iterations: int = 10000) -> dict[str, Any]:
    if not isinstance(iterations, int) or not 1 <= iterations <= 1_000_000:
        raise ValueError("iterations must be between 1 and 1,000,000")

    normalized_category.cache_clear()
    start = perf_counter()
    for _ in range(iterations):
        normalized_category("  Coffee  ")
    elapsed = perf_counter() - start
    info = normalized_category.cache_info()
    return {
        "passed": normalized_category("  Coffee  ") == "coffee" and info.hits >= iterations - 1,
        "iterations": iterations,
        "elapsed_seconds": round(elapsed, 6),
        "cache_hits": info.hits,
        "cache_misses": info.misses,
        "note": "Machine-specific microbenchmark; not a production load test or AWS performance result.",
    }
