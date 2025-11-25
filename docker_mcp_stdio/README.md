Dockerized stdio MCP

This project builds a Docker image that runs the newline-delimited JSON stdio MCP at `cli_mcp_stdio/mcp_stdio.py`.

Why use this
- Reproducible environment for the stdio-based MCP
- Easy to run in CI or as a container-based worker

Prereqs
- Docker (and optionally docker-compose)
- An OpenRouter-compatible API key (or any OpenAI-compatible key)

Build the image

From the repository root (important so the build context includes `cli_mcp_stdio`):

```bash
cd /Users/pkshrestha/git/mcp-server-samples
# build the image
docker build -t mcp-stdio-image -f docker_mcp_stdio/Dockerfile docker_mcp_fastapi/..
# Note: the command above uses the repo root as build context; alternatively use:
# docker build -t mcp-stdio-image -f docker_mcp_stdio/Dockerfile .
```

(PREFERRED) Simple run — pipe a single request

```bash
export OPENAI_API_KEY="<your-openrouter-key>"
export OPENAI_API_BASE="https://api.openrouter.ai/v1"

echo '{"messages":[{"role":"user","content":"Say hi from dockerized stdio."}]}' | \
  docker run -i --rm -e OPENAI_API_KEY="$OPENAI_API_KEY" -e OPENAI_API_BASE="$OPENAI_API_BASE" mcp-stdio-image
```

Using docker-compose (useful for local dev)

```bash
# from repository root
OPENAI_API_KEY="$OPENAI_API_KEY" OPENAI_API_BASE="$OPENAI_API_BASE" docker compose -f docker_mcp_stdio/docker-compose.yml up --build

# Then you can pipe a request into the container (example)
# echo '{...}' | docker run -i --rm -e OPENAI_API_KEY="$OPENAI_API_KEY" -e OPENAI_API_BASE="$OPENAI_API_BASE" mcp-stdio-image
```

Notes & recommendations
- This container expects newline-delimited JSON input on stdin and emits newline-delimited JSON responses on stdout.
- For production, consider:
  - More robust framing (length-prefix) if your messages may contain newlines or binary data.
  - Running behind an orchestrator and using secrets rather than environment variables for API keys.
  - Adding a small HTTP or socket shim if multiple clients will call the MCP concurrently.

Test script
- `test_send.sh` shows a minimal example of piping a request into the image.
