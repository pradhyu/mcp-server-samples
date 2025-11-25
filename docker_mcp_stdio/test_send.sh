#!/usr/bin/env bash
set -euo pipefail

if [ -z "${OPENAI_API_KEY:-}" ]; then
  echo "Please set OPENAI_API_KEY and OPENAI_API_BASE before running."
  exit 1
fi

REQUEST='{"messages":[{"role":"user","content":"Hello from dockerized stdio MCP"}]}'

echo "$REQUEST" | docker run -i --rm -e OPENAI_API_KEY="$OPENAI_API_KEY" -e OPENAI_API_BASE="$OPENAI_API_BASE" mcp-stdio-image
