FROM node:24-bookworm-slim AS ui-build
RUN apt-get update && apt-get install -y --no-install-recommends git ca-certificates curl python3 build-essential && rm -rf /var/lib/apt/lists/*
RUN npm install -g bun@1.4.3
RUN git init /aionui && cd /aionui && git remote add origin https://github.com/iOfficeAI/AionUi.git && git fetch --depth 1 origin c140550d04e44f3d6f8a9830b40ae56e4689a977 && git checkout FETCH_HEAD
WORKDIR /aionui
RUN bun install --frozen-lockfile --ignore-scripts
RUN node --max-old-space-size=4096 node_modules/electron-vite/bin/electron-vite.js build --config packages/desktop/electron.vite.config.ts

FROM node:24-bookworm-slim
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates curl git gosu libicu72 libssl3 && rm -rf /var/lib/apt/lists/*
RUN npm install -g opencode-ai@1.19.3
RUN curl -fsSL https://github.com/iOfficeAI/AionCore/releases/download/v0.2.2/aioncore-v0.2.2-x86_64-unknown-linux-gnu.tar.gz -o /tmp/aioncore.tar.gz && echo '1c3f241c7deff8e9d6da189c1017e6b12df7b538a1f557276c79b3c33d257335  /tmp/aioncore.tar.gz' | sha256sum -c - && tar -xzf /tmp/aioncore.tar.gz -C /usr/local/bin && chmod 755 /usr/local/bin/aioncore && rm /tmp/aioncore.tar.gz
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --omit=dev
COPY gateway.mjs pilot.mjs entrypoint.sh ./
COPY --from=ui-build /aionui/out/renderer /app/renderer
COPY --from=ui-build /aionui/LICENSE /app/AionUi-LICENSE
RUN chmod 755 entrypoint.sh && mkdir -p /data && chown node:node /data
ENV NODE_ENV=production PORT=8080 AIONUI_DATA_DIR=/data/state BOSS_AIONUI_WORKSPACE=/data/workspace XDG_CONFIG_HOME=/data/config XDG_DATA_HOME=/data/share XDG_CACHE_HOME=/data/cache
EXPOSE 8080
ENTRYPOINT ["/app/entrypoint.sh"]
