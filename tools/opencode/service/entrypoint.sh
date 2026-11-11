#!/bin/sh
set -eu
mkdir -p /data/workspace /data/config /data/share /data/cache
if [ "$(id -u)" = "0" ]; then
  chown node:node /data /data/workspace /data/config /data/share /data/cache
  exec gosu node node /app/server.mjs
fi
exec node /app/server.mjs
