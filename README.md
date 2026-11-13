<p align="center">
  <img src="https://img.shields.io/badge/OSINT-DNS_INTELLIGENCE-101010?style=for-the-badge&labelColor=050805&color=00FF41" alt="DNS Intelligence"/>
  <img src="https://img.shields.io/badge/PYTHON-CLI-101010?style=for-the-badge&labelColor=050805&logo=python&logoColor=00FF41" alt="Python CLI"/>
</p>

# DNS Intelligence & Enrichment

A small Python CLI for DNS and reverse-DNS enrichment. It accepts domain names, IPv4 and IPv6 indicators, normalizes internationalized domain names (IDNA), and returns structured JSON.

<p align="center">
  <a href="https://github.com/tzayadet/OSINT-Correlator/blob/main/docs/index.html"><strong>SHOWCASE SOURCE ↗</strong></a> ·
  <a href="https://github.com/tzayadet/OSINT-Correlator"><strong>SOURCE CODE</strong></a>
</p>

[![Tests](https://github.com/tzayadet/OSINT-Correlator/actions/workflows/tests.yml/badge.svg)](https://github.com/tzayadet/OSINT-Correlator/actions/workflows/tests.yml) · [![Container build](https://github.com/tzayadet/OSINT-Correlator/actions/workflows/container-build.yml/badge.svg)](https://github.com/tzayadet/OSINT-Correlator/actions/workflows/container-build.yml) · [![Pages](https://github.com/tzayadet/OSINT-Correlator/actions/workflows/pages.yml/badge.svg)](https://github.com/tzayadet/OSINT-Correlator/actions/workflows/pages.yml)

## Overview

- Resolves A/AAAA addresses through the system resolver.
- Performs reverse PTR lookups for IPv4 and IPv6.
- Normalizes internationalized domain names using IDNA.
- Sorts returned addresses numerically and emits structured JSON.
- Runs locally or in Docker without third-party Python packages.

## Run locally

**Requirements:** Python 3.10+.

```bash
python dns_enrichment.py example.com
python dns_enrichment.py 8.8.8.8
python dns_enrichment.py 2001:4860:4860::8888
```

## Docker

```bash
docker build -t dns-intelligence .
docker run --rm dns-intelligence example.com
```

## Project structure

| Path | Purpose |
|---|---|
| `dns_enrichment.py` | DNS and reverse-DNS CLI |
| `docs/` | Static showcase with synthetic examples |
| `tests/` | Unit tests for normalization and lookup handling |
| `.github/workflows/` | Test, container and Pages automation |

## Showcase

The [showcase source](docs/index.html) demonstrates the output format using synthetic data and reserved documentation IP ranges. It does not perform live DNS queries in the browser. To publish it, enable GitHub Pages with GitHub Actions as its source and set the repository variable `ENABLE_PAGES` to `true`. Until then, the deployment job is intentionally skipped.

## Validation

Run the tests with the Python standard library:

```bash
python -m unittest discover -s tests -v
```

GitHub Actions runs the test suite and container build. The Pages workflow publishes the static showcase when GitHub Pages is enabled with GitHub Actions as its source.

## Scope and limitations

This tool performs DNS enrichment only. It does not scan ports, enumerate subdomains, discover assets at scale or attribute infrastructure to threat actors. Results depend on the operating system's configured resolver and current network conditions. Failed lookups are represented as empty or null result fields; they are not proof that a domain or address does not exist.

## Responsible use

Use DNS data within the scope of an authorised assessment. DNS records are time-dependent and should be timestamped and independently verified before being used as evidence.

## License

See [LICENSE](LICENSE).
