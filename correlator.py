#!/usr/bin/env python3
"""Basic DNS and reverse-DNS enrichment for a domain or IP address."""
from __future__ import annotations

import argparse
import ipaddress
import json
import socket


def enrich(target: str) -> dict:
    result = {"target": target, "type": None, "dns": None, "rdns": None}
    try:
        address = ipaddress.ip_address(target)
    except ValueError:
        result["type"] = "domain"
        try:
            result["dns"] = socket.gethostbyname(target)
            result["rdns"] = socket.gethostbyaddr(result["dns"])[0]
        except (socket.gaierror, OSError):
            pass
    else:
        result["type"] = "ip"
        try:
            result["rdns"] = socket.gethostbyaddr(str(address))[0]
        except (socket.herror, socket.gaierror, OSError):
            pass
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", help="Domain name or IPv4/IPv6 address")
    args = parser.parse_args()
    print(json.dumps(enrich(args.target), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
