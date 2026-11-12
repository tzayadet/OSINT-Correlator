# DNS Intelligence & Enrichment

CLI en Python para consultar registros DNS y DNS inverso de dominios e IP. Admite IPv4, IPv6 y dominios internacionalizados.

[![Tests](https://github.com/tzayadet/OSINT-Correlator/actions/workflows/tests.yml/badge.svg)](https://github.com/tzayadet/OSINT-Correlator/actions/workflows/tests.yml) · [![Docker](https://github.com/tzayadet/OSINT-Correlator/actions/workflows/container-build.yml/badge.svg)](https://github.com/tzayadet/OSINT-Correlator/actions/workflows/container-build.yml)

**Demo:** [ver showcase](docs/index.html) · **Código:** [dns_enrichment.py](dns_enrichment.py)

> La página de muestra utiliza datos de ejemplo. Las consultas DNS se ejecutan desde la herramienta CLI, no desde el navegador.

## Funcionalidad

- Resolución DNS para IPv4 e IPv6.
- Consultas PTR para direcciones IP.
- Normalización IDNA de dominios internacionalizados.
- Validación de entradas y salida JSON.
- Ejecución local o mediante Docker.

## Requisitos y uso

Python 3.10 o superior. No necesita dependencias externas.

```bash
python dns_enrichment.py example.com
python dns_enrichment.py 8.8.8.8
python dns_enrichment.py 2001:4860:4860::8888
```

Con Docker:

```bash
docker build -t dns-intelligence .
docker run --rm dns-intelligence example.com
```

La salida incluye el objetivo, el tipo detectado, las direcciones resueltas y el resultado PTR cuando está disponible. Los resultados dependen del resolver y de la red desde la que se ejecuta.

## Publicar el showcase

El showcase estático se encuentra en [docs/index.html](docs/index.html). Para publicarlo:

1. En **Settings → Pages**, selecciona **GitHub Actions** como origen.
2. En **Settings → Secrets and variables → Actions → Variables**, crea `ENABLE_PAGES` con valor `true`.
3. Ejecuta **Deploy OSINT-Correlator showcase to GitHub Pages** desde Actions.

La demo utiliza datos de ejemplo. Las consultas DNS se ejecutan desde la herramienta CLI, no desde el navegador.

## Alcance

Esta herramienta no realiza escaneo de puertos, enumeración masiva ni atribución de infraestructura. Consulta únicamente DNS mediante el resolver del sistema.

## Licencia

Consulta [LICENSE](LICENSE).
