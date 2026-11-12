<p align="center">
  <img src="https://img.shields.io/badge/OSINT-DNS_INTELLIGENCE-101010?style=for-the-badge&labelColor=050805&color=00FF41" alt="DNS Intelligence"/>
  <img src="https://img.shields.io/badge/PYTHON-CLI-101010?style=for-the-badge&logo=python&logoColor=00FF41" alt="Python CLI"/>
</p>

# DNS Intelligence & Enrichment

Consultas DNS y reverse DNS para dominios e indicadores IP, con soporte IPv4, IPv6 y normalización IDNA. Una utilidad pequeña, directa y pensada para integrarse en flujos de análisis.

<p align="center">
  <a href="https://tzayadet.github.io/OSINT-Correlator/"><strong>LIVE SHOWCASE ↗</strong></a> ·
  <a href="https://github.com/tzayadet/OSINT-Correlator"><strong>SOURCE CODE</strong></a>
</p>

[![Tests](https://github.com/tzayadet/OSINT-Correlator/actions/workflows/tests.yml/badge.svg)](https://github.com/tzayadet/OSINT-Correlator/actions/workflows/tests.yml) · [![Docker](https://github.com/tzayadet/OSINT-Correlator/actions/workflows/container-build.yml/badge.svg)](https://github.com/tzayadet/OSINT-Correlator/actions/workflows/container-build.yml)

> El showcase utiliza resultados ficticios para enseñar el formato de salida. Las consultas reales se ejecutan desde la CLI, no desde el navegador.

## What it does

- Resuelve registros DNS para dominios.
- Consulta PTR para direcciones IPv4 e IPv6.
- Normaliza dominios internacionalizados mediante IDNA.
- Valida entradas y devuelve resultados estructurados en JSON.
- Permite ejecución local o mediante Docker.

## Quick start

**Requirements:** Python 3.10+. No external Python dependencies.

```bash
python dns_enrichment.py example.com
python dns_enrichment.py 8.8.8.8
python dns_enrichment.py 2001:4860:4860::8888
```

**Docker**

```bash
docker build -t dns-intelligence .
docker run --rm dns-intelligence example.com
```

## Project layout

| Path | Purpose |
|---|---|
| `dns_enrichment.py` | DNS and reverse-DNS CLI |
| `docs/` | Static project showcase |
| `.github/workflows/` | Tests, container build and Pages deployment |

## Scope & limitations

The tool queries DNS through the resolver configured by the operating system. It does not perform port scanning, subdomain brute forcing, bulk infrastructure enumeration or threat attribution. Results depend on resolver behaviour and network conditions.

## Deployment

The static showcase is published through GitHub Pages. The workflow is `.github/workflows/pages.yml`; it deploys the `docs/` directory when Pages is configured and the repository variable `ENABLE_PAGES=true` is set.

## License

See [LICENSE](LICENSE).
