FROM python:3.12.7-slim
RUN groupadd --gid 10001 preview && useradd --uid 10001 --gid 10001 --create-home preview
WORKDIR /app
RUN mkdir -p /data/previews && chown -R 10001:10001 /data
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY server.py /app/server.py
USER 10001:10001
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
ENTRYPOINT ["python", "/app/server.py"]
