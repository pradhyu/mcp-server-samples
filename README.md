Two small Python sample projects demonstrating a minimal "MCP" server pattern and LangChain usage with OpenRouter (OpenAI-compatible API base).

Prereqs
- Python 3.10+
- A valid OpenRouter API key (or any OpenAI-compatible key). We'll assume you use OpenRouter and set the OpenAI-compatible env vars below.

Environment variables (set these before running examples):

```bash
# OpenRouter-compatible (make sure your key is from OpenRouter)
export OPENAI_API_KEY="<your-openrouter-key>"
export OPENAI_API_BASE="https://api.openrouter.ai/v1"
```

Projects
- `simple_mcp_fastapi/` — Minimal FastAPI-based MCP endpoint that forwards messages to LangChain's ChatOpenAI (configured to use OPENAI_API_BASE).
- `langchain_example/` — Tiny script that calls LangChain ChatOpenAI directly and prints a response.

See each project's README for run instructions.# mcp-server-samples
