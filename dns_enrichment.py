#!/usr/bin/env python3
"""DNS and reverse-DNS enrichment for a domain or IP address."""
from __future__ import annotations

import argparse
import ipaddress
import json
import re
import socket

DOMAIN_LABEL = re.compile(r"^[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$", re.IGNORECASE)


def normalize_domain(value: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise ValueError("Domain must be a non-empty string without surrounding spaces")
    candidate = value[:-1] if value.endswith(".") else value
    if not candidate or len(candidate) > 253 or candidate.endswith("."):
        raise ValueError("Invalid domain name")
    try:
        ascii_name = candidate.encode("idna").decode("ascii").lower()
    except UnicodeError as exc:
        raise ValueError("Invalid internationalized domain name") from exc
    labels = ascii_name.split(".")
    if any(not DOMAIN_LABEL.fullmatch(label) for label in labels):
        raise ValueError("Invalid domain name")
    return ascii_name


def _ip_sort_key(value: str) -> tuple[int, int]:
    address = ipaddress.ip_address(value)
    return address.version, int(address)


def enrich(target: str) -> dict:
    if not isinstance(target, str) or not target or target != target.strip():
        raise ValueError("Target must be a non-empty domain or IP address without surrounding spaces")
    result = {"target": target, "type": None, "dns": None, "addresses": [], "rdns": None}
    try:
        address = ipaddress.ip_address(target)
    except ValueError:
        hostname = normalize_domain(target)
        result["type"] = "domain"
        try:
            records = socket.getaddrinfo(hostname, None, type=socket.SOCK_STREAM)
            result["addresses"] = sorted(
                {record[4][0] for record in records},
                key=_ip_sort_key,
            )
            ipv4 = next((item for item in result["addresses"] if ipaddress.ip_address(item).version == 4), None)
            result["dns"] = ipv4 or (result["addresses"][0] if result["addresses"] else None)
        except (socket.gaierror, OSError):
            pass
        reverse_target = result["dns"]
    else:
        result["type"] = "ip"
        result["addresses"] = [str(address)]
        reverse_target = str(address)
    if reverse_target:
        try:
            result["rdns"] = socket.gethostbyaddr(reverse_target)[0]
        except (socket.herror, socket.gaierror, OSError):
            pass
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", help="Domain name or IPv4/IPv6 address")
    args = parser.parse_args()
    try:
        result = enrich(args.target)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
