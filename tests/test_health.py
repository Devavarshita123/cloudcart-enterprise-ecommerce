import unittest
from app.health import health_check


class TestHealthCheck(unittest.TestCase):
    def test_default_is_healthy(self):
        self.assertEqual(health_check()["status"], "healthy")

    def test_missing_name_is_unhealthy(self):
        self.assertEqual(health_check({"name": "", "version": "1.0"})["status"], "unhealthy")

    def test_whitespace_name_is_unhealthy(self):
        self.assertEqual(health_check({"name": "  ", "version": "1.0"})["status"], "unhealthy")

    def test_non_string_version_is_unhealthy(self):
        self.assertEqual(health_check({"name": "CloudCart", "version": 1})["status"], "unhealthy")

    def test_non_dict_is_unhealthy(self):
        self.assertEqual(health_check(None if False else [])["status"], "unhealthy")


if __name__ == "__main__":
    unittest.main()
