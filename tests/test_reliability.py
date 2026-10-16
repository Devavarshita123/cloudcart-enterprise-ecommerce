import unittest
from app.reliability import aggregate_health, retry


class TestReliability(unittest.TestCase):
    def test_health_aggregation(self):
        self.assertEqual(aggregate_health({"catalog": True})["status"], "healthy")
        self.assertEqual(aggregate_health({"catalog": False})["status"], "degraded")
        self.assertEqual(aggregate_health({})["status"], "unhealthy")

    def test_retry_eventually_succeeds(self):
        calls = {"n": 0}
        def operation():
            calls["n"] += 1
            if calls["n"] < 2:
                raise TimeoutError()
            return "ok"
        result = retry(operation, attempts=3)
        self.assertTrue(result["success"])
        self.assertEqual(result["attempts"], 2)

    def test_retry_bounds(self):
        with self.assertRaises(ValueError):
            retry(lambda: True, attempts=0)


if __name__ == "__main__":
    unittest.main()
