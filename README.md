# OSINT Correlator

Herramienta CLI sencilla para enriquecer un dominio o una dirección IP mediante resolución DNS y DNS inverso (PTR).

## Requisitos

- Python 3.10+
- Sin dependencias externas.

## Uso

```bash
python correlator.py example.com
python correlator.py 8.8.8.8
python correlator.py 2001:4860:4860::8888
```

La salida JSON contiene el objetivo, el tipo detectado, la resolución DNS y el resultado PTR cuando está disponible.

## Funcionamiento

- Las direcciones IPv4 e IPv6 se identifican con el módulo estándar `ipaddress`.
- Los dominios se resuelven mediante el resolver DNS del sistema.
- Para las IP se intenta una consulta de DNS inverso.
- Los errores de resolución se reflejan como campos nulos.

## Limitaciones

No es una plataforma de atribución ni una herramienta de escaneo. Solo consulta información DNS disponible para el resolver configurado. Los resultados pueden variar según la red y el momento de la consulta.

Realiza consultas únicamente dentro del marco legal y respetando las políticas de uso aplicables.

## Licencia

Consulta [LICENSE](LICENSE).
