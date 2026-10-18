#!/bin/sh
set -eu
mkdir -p /data/state /data/workspace /data/logs /data/cache /data/config /data/share
chown -R node:node /data
exec gosu node node /app/gateway.mjs
