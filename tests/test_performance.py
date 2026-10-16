import unittest
from app.performance import normalized_category, performance_demo


class TestPerformance(unittest.TestCase):
    def test_normalization_and_cache(self):
        normalized_category.cache_clear()
        self.assertEqual(normalized_category(" Coffee "), "coffee")
        self.assertEqual(normalized_category(" Coffee "), "coffee")
        self.assertEqual(normalized_category.cache_info().hits, 1)

    def test_demo_and_bounds(self):
        self.assertTrue(performance_demo(100)["passed"])
        with self.assertRaises(ValueError):
            performance_demo(0)


if __name__ == "__main__":
    unittest.main()
