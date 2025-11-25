Simple MCP FastAPI sample

This tiny app exposes a POST /mcp endpoint that accepts JSON of the shape:

```json
{
  "messages": [
    {"role":"system","content":"You are a helpful assistant."},
    {"role":"user","content":"Write a short poem about rain."}
  ],
  "model": "gpt-4o-mini"  // optional
}
```

It forwards the messages to LangChain's ChatOpenAI. To use OpenRouter (OpenAI-compatible):

```bash
# macOS / zsh
export OPENAI_API_KEY="<your-openrouter-key>"
export OPENAI_API_BASE="https://api.openrouter.ai/v1"

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# run dev server
uvicorn main:app --reload --port 8000
```

Then POST to http://localhost:8000/mcp with the JSON payload. Example with curl:

```bash
curl -s -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -d '{"messages":[{"role":"user","content":"Say hello"}] }'
```

Notes
- This example keeps things intentionally small: no auth, no streaming, basic error handling.
- You can replace the model name passed with a model available to your OpenRouter key.