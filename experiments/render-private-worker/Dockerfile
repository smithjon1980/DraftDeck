# Explicitly synthetic and disabled for arbitrary SVG/art/story payloads.
FROM python:3.12-slim-bookworm
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    HOME=/tmp \
    XDG_CACHE_HOME=/tmp/.cache \
    XDG_CONFIG_HOME=/tmp/.config \
    PORT=10000
RUN apt-get update && apt-get install -y --no-install-recommends inkscape ca-certificates && \
    rm -rf /var/lib/apt/lists/* && \
    groupadd --system svgprobe && useradd --system --no-create-home --gid svgprobe svgprobe
WORKDIR /app
COPY experiments/render-private-worker/worker_server.py /app/worker_server.py
USER svgprobe
EXPOSE 10000
CMD ["python", "/app/worker_server.py"]
