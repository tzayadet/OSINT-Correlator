# DNS Intelligence & Enrichment

A lightweight Python CLI for DNS and reverse-DNS enrichment. It accepts domain names, IPv4 and IPv6 indicators, normalizes internationalized domain names (IDNA), and returns structured results.

<p align="center">
  <a href="https://github.com/tzayadet/OSINT-Correlator"><img src="https://img.shields.io/badge/SOURCE-GITHUB-161b22?style=flat-square&logo=github" alt="Source code"></a>
  <a href="docs/index.html"><img src="https://img.shields.io/badge/SHOWCASE-SOURCE-00a86b?style=flat-square" alt="Showcase source"></a>
</p>

[![Tests](https://github.com/tzayadet/OSINT-Correlator/actions/workflows/tests.yml/badge.svg)](https://github.com/tzayadet/OSINT-Correlator/actions/workflows/tests.yml) · [![Container build](https://github.com/tzayadet/OSINT-Correlator/actions/workflows/container-build.yml/badge.svg)](https://github.com/tzayadet/OSINT-Correlator/actions/workflows/container-build.yml)

## What it does

- Resolves DNS records for a domain through the system resolver.
- Performs reverse PTR lookups for IPv4 and IPv6 addresses.
- Normalizes internationalized domain names using IDNA.
- Validates input and returns structured JSON output.
- Runs locally or in Docker.

## Run locally

**Requirements:** Python 3.10 or later. No third-party Python packages are required.

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
| `docs/` | Static showcase with illustrative output |
| `.github/workflows/` | Tests, container build and Pages workflow |

## Showcase

The static showcase source is available in [docs/index.html](docs/index.html). It uses synthetic examples and reserved documentation IP ranges. It does not perform live DNS queries in the browser. The deployment workflow is ready; GitHub Pages must first be enabled in repository settings with GitHub Actions as the source.

## Scope

This project performs DNS enrichment only. It does not scan ports, enumerate subdomains, discover assets at scale or attribute infrastructure to threat actors. Results depend on the resolver configured by the operating system and on network conditions.

## Tests

Run the test suite with:

```bash
python -m pytest
```

The repository also includes GitHub Actions checks for tests and container builds.

## License

See [LICENSE](LICENSE) for the repository's licensing terms.
