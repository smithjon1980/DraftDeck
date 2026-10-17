FROM node:22-bookworm-slim
RUN apt-get update && apt-get install -y --no-install-recommends git ca-certificates && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --omit=dev
COPY server.mjs runtime-config.json ./
RUN mkdir -p /data/workspace /data/config /data/share /data/cache && chown -R node:node /data
USER node
ENV XDG_CONFIG_HOME=/data/config XDG_DATA_HOME=/data/share XDG_CACHE_HOME=/data/cache
EXPOSE 8080
CMD ["node", "server.mjs"]
