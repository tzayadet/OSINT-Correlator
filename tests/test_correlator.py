import socket
import unittest
from unittest.mock import patch

from correlator import enrich


class EnrichTests(unittest.TestCase):
    @patch("correlator.socket.gethostbyaddr")
    def test_ip_address_uses_reverse_dns(self, reverse_dns):
        reverse_dns.return_value = ("host.example", [], ["203.0.113.10"])

        result = enrich("203.0.113.10")

        self.assertEqual(result["type"], "ip")
        self.assertEqual(result["target"], "203.0.113.10")
        self.assertEqual(result["rdns"], "host.example")
        reverse_dns.assert_called_once_with("203.0.113.10")

    @patch("correlator.socket.gethostbyaddr")
    @patch("correlator.socket.gethostbyname")
    def test_domain_returns_forward_and_reverse_dns(self, forward_dns, reverse_dns):
        forward_dns.return_value = "203.0.113.20"
        reverse_dns.return_value = ("edge.example", [], ["203.0.113.20"])

        result = enrich("example.test")

        self.assertEqual(result["type"], "domain")
        self.assertEqual(result["dns"], "203.0.113.20")
        self.assertEqual(result["rdns"], "edge.example")

    @patch("correlator.socket.gethostbyname", side_effect=socket.gaierror)
    def test_unresolvable_domain_returns_null_fields(self, _forward_dns):
        result = enrich("not-found.invalid")

        self.assertEqual(result["type"], "domain")
        self.assertIsNone(result["dns"])
        self.assertIsNone(result["rdns"])


if __name__ == "__main__":
    unittest.main()
