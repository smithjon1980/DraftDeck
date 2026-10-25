# Render probe only: no OpenBot gateway, SVG worker, approval, or custody service.
FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=10000
WORKDIR /app
RUN groupadd --system probe && useradd --system --gid probe --no-create-home --home-dir /app probe
COPY --chown=probe:probe experiments/boss-svg-gateway/probe_server.py /app/probe_server.py
USER probe
EXPOSE 10000
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 CMD ["python", "-c", "import os,urllib.request; p=os.getenv('PORT','10000'); urllib.request.urlopen('http://127.0.0.1:'+p+'/healthz',timeout=2).read()"]
CMD ["python", "/app/probe_server.py"]
