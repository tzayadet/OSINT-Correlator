# DNS Intelligence & Enrichment

Herramienta CLI para enriquecer dominios e IP mediante resolución DNS y DNS inverso (PTR).

[![Python tests](https://github.com/tzayadet/OSINT-Correlator/actions/workflows/tests.yml/badge.svg)](https://github.com/tzayadet/OSINT-Correlator/actions/workflows/tests.yml) · [![Container build](https://github.com/tzayadet/OSINT-Correlator/actions/workflows/container-build.yml/badge.svg)](https://github.com/tzayadet/OSINT-Correlator/actions/workflows/container-build.yml)

## Requisitos

- Python 3.10 o superior.
- Sin dependencias externas.

## Uso local

```bash
python dns_enrichment.py example.com
python dns_enrichment.py 8.8.8.8
python dns_enrichment.py 2001:4860:4860::8888
```

La salida JSON incluye el objetivo, el tipo detectado, todas las direcciones IPv4/IPv6 resueltas, un campo `dns` compatible con la salida anterior y el resultado PTR cuando está disponible. Los dominios internacionalizados se normalizan mediante IDNA y las entradas inválidas se rechazan.

## Docker

Construir la imagen:

```bash
docker build -t osint-correlator .
```

Consultar un dominio:

```bash
docker run --rm osint-correlator example.com
```

La resolución utiliza el DNS disponible dentro del contenedor. Los resultados pueden variar según la red y el resolver configurado.

## Funcionamiento

- IPv4 e IPv6 se identifican mediante el módulo estándar `ipaddress`.
- Los dominios se resuelven mediante `getaddrinfo`, admitiendo registros IPv4 e IPv6, y el nombre se normaliza con IDNA.
- Para las IP se intenta una consulta de DNS inverso.
- Los errores de resolución se reflejan como campos nulos.

## Publicación de la demo

La demo está preparada en `docs/index.html`. Para publicarla, activa GitHub Pages en **Settings → Pages → Build and deployment → Source → GitHub Actions** y crea la variable de repositorio `ENABLE_PAGES=true` en **Settings → Secrets and variables → Actions → Variables**. El workflow queda deliberadamente inactivo hasta que esa configuración exista, evitando ejecuciones fallidas mientras Pages no esté habilitado.

## Limitaciones y uso responsable

No es una plataforma de atribución ni una herramienta de escaneo. Solo consulta información DNS disponible para el resolver configurado. No realiza enumeración masiva, escaneo de puertos ni atribución de infraestructura.

Realiza consultas únicamente dentro del marco legal y respetando las políticas de uso aplicables.

## Licencia

Consulta [LICENSE](LICENSE).


## Project showcase

Static overview and synthetic JSON example: https://tzayadet.github.io/OSINT-Correlator/

The page does not execute DNS queries. The CLI performs DNS and reverse-DNS lookups using the system resolver; it is not a scanner or attribution platform.
