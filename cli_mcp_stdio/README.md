t cMCP stdio sample

This sample exposes a simple MCP-like protocol over stdio (newline-delimited JSON). It's useful when embedding a model-backed assistant as a subprocess that communicates via stdin/stdout.

Protocol
- Input: one JSON object per line with fields `id` (optional), `messages` (array), and optional `model`.
- Output: one JSON object per line with `id`, `response`, `model`, and `error`.

Example input (single-line):

{"messages": [{"role":"system","content":"You are a helpful assistant."},{"role":"user","content":"Write a tiny poem about the sea."}], "model":"gpt-4o-mini"}

Run locally

```bash
cd /Users/pkshrestha/git/mcp-server-samples/cli_mcp_stdio
python3 -m venv uv
source uv/bin/activate
pip install -r requirements.txt

# set OpenRouter-compatible env vars
export OPENAI_API_KEY="<your-openrouter-key>"
export OPENAI_API_BASE="https://api.openrouter.ai/v1"

# test with echo
echo '{"messages":[{"role":"user","content":"Say hi"}]}' | python mcp_stdio.py
```

Example usage from another program (pseudocode)

- Spawn `python mcp_stdio.py` as subprocess
- Write JSON lines to its stdin
- Read JSON lines from its stdout and correlate responses by `id`

Notes
- This example is intentionally synchronous and simple. For production you might add streaming token output, heartbeat/ping messages, stdin framing with length-prefix, and authentication.
