Docker-based MCP (FastAPI) example

This small Docker setup builds and runs the `simple_mcp_fastapi` app included in this repo.

Prereqs
- Docker and docker-compose installed on your machine
- An OpenRouter-compatible API key (or any OpenAI-compatible endpoint). We'll use environment variables described below.

Build and run

From the repository root (so the Docker build context includes the other sample folders):

```bash
cd /Users/pkshrestha/git/mcp-server-samples
# set your OpenRouter/OpenAI env vars
export OPENAI_API_KEY="<your-openrouter-key>"
export OPENAI_API_BASE="https://api.openrouter.ai/v1"

# Build and start with docker-compose
docker compose -f docker_mcp_fastapi/docker-compose.yml up --build
```

The container will run Uvicorn on port 8000 and serve the MCP endpoint at `/mcp`.

Notes
- The Dockerfile uses the repository root as the build context and installs the requirements from `simple_mcp_fastapi/requirements.txt`.
- For production usage you should:
  - Pin dependency versions in `requirements.txt`.
  - Use multi-stage builds and smaller base images.
  - Pass secrets via a secrets manager or Docker secrets, not plain env vars.
  - Add healthchecks and logging configuration.
