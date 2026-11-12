FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app
COPY dns_enrichment.py .
ENTRYPOINT ["python", "dns_enrichment.py"]
