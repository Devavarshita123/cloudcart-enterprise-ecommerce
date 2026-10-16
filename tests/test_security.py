import unittest
from app.security import validate_order_id, redact_email, security_demo


class TestSecurity(unittest.TestCase):
    def test_valid_order_id(self):
        self.assertTrue(validate_order_id("ORD-12345")[0])

    def test_invalid_order_id_rejected(self):
        self.assertFalse(validate_order_id("ORD-123\n4")[0])
        self.assertFalse(validate_order_id("other")[0])

    def test_email_redaction(self):
        self.assertEqual(redact_email("customer@example.com"), "c***@example.com")
        self.assertEqual(redact_email("not-an-email"), "[REDACTED]")

    def test_security_demo_passes(self):
        self.assertTrue(security_demo()["passed"])


if __name__ == "__main__":
    unittest.main()
