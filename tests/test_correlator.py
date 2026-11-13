import socket
import unittest
from unittest.mock import patch

from dns_enrichment import enrich, normalize_domain


class DnsEnrichmentTests(unittest.TestCase):
    @patch("dns_enrichment.socket.gethostbyaddr")
    def test_ipv4_address_uses_reverse_dns(self, reverse_dns):
        reverse_dns.return_value = ("host.example", [], ["203.0.113.10"])
        result = enrich("203.0.113.10")
        self.assertEqual(result["type"], "ip")
        self.assertEqual(result["addresses"], ["203.0.113.10"])
        self.assertEqual(result["rdns"], "host.example")

    @patch("dns_enrichment.socket.gethostbyaddr")
    @patch("dns_enrichment.socket.getaddrinfo")
    def test_domain_returns_numerically_sorted_ipv4_and_ipv6(self, getaddrinfo, reverse_dns):
        getaddrinfo.return_value = [
            (socket.AF_INET, socket.SOCK_STREAM, 6, "", ("203.0.113.10", 0)),
            (socket.AF_INET6, socket.SOCK_STREAM, 6, "", ("2001:db8::2", 0, 0, 0)),
            (socket.AF_INET, socket.SOCK_STREAM, 6, "", ("203.0.113.2", 0)),
            (socket.AF_INET6, socket.SOCK_STREAM, 6, "", ("2001:db8::1", 0, 0, 0)),
        ]
        reverse_dns.return_value = ("edge.example", [], ["203.0.113.2"])
        result = enrich("example.test")
        self.assertEqual(
            result["addresses"],
            ["203.0.113.2", "203.0.113.10", "2001:db8::1", "2001:db8::2"],
        )
        self.assertEqual(result["dns"], "203.0.113.2")
        self.assertEqual(result["rdns"], "edge.example")

    @patch("dns_enrichment.socket.getaddrinfo", side_effect=socket.gaierror)
    def test_unresolvable_domain_returns_empty_address_list(self, _lookup):
        result = enrich("not-found.invalid")
        self.assertEqual(result["addresses"], [])
        self.assertIsNone(result["dns"])
        self.assertIsNone(result["rdns"])

    def test_domain_is_normalized_with_idna_and_trailing_dot(self):
        self.assertEqual(normalize_domain("Exämple.test."), "xn--exmple-cua.test")

    def test_invalid_domain_is_rejected(self):
        for value in ("bad domain.example", "", "example..test", "example.test..", "-bad.example"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    enrich(value)

    def test_normalize_domain_rejects_non_string_and_surrounding_spaces(self):
        for value in (None, " example.test", "example.test "):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    normalize_domain(value)

    def test_normalize_domain_accepts_single_fully_qualified_dot(self):
        self.assertEqual(normalize_domain("Example.TEST."), "example.test")


if __name__ == "__main__":
    unittest.main()
