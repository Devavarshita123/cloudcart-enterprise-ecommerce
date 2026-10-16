import unittest
from app.cost import estimate_monthly_cost, budget_check, cost_demo


class TestCost(unittest.TestCase):
    def test_estimate(self):
        result = estimate_monthly_cost({
            "compute_hours": 10,
            "compute_rate_per_hour": 0.1,
            "storage_gb": 5,
            "storage_rate_per_gb": 0.02,
        })
        self.assertEqual(result["total_estimate"], 1.1)

    def test_invalid_assumptions_rejected(self):
        with self.assertRaises(ValueError):
            estimate_monthly_cost({"compute_hours": -1})

    def test_budget_check(self):
        self.assertTrue(budget_check(0, 0)["within_budget"])
        self.assertFalse(budget_check(11, 10)["within_budget"])

    def test_cost_demo(self):
        self.assertTrue(cost_demo()["passed"])


if __name__ == "__main__":
    unittest.main()
