CLI MCP sample

This small CLI forwards messages to LangChain ChatOpenAI. It supports either a single message or a JSON file with a `messages` array.

Setup (macOS / zsh):

```bash
cd /Users/pkshrestha/git/mcp-server-samples/cli_mcp
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Environment variables (for OpenRouter):

```bash
export OPENAI_API_KEY="<your-openrouter-key>"
export OPENAI_API_BASE="https://api.openrouter.ai/v1"
```

Examples

Single message:

```bash
python cli_mcp.py --message "Say hi in a friendly way"
```

JSON file (`messages.json`):

```json
{
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Write a haiku about coffee."}
  ],
  "model": "gpt-4o-mini"
}
```

Run:

```bash
python cli_mcp.py --file messages.json
```

Options
- `--model` to override the model
- `--system` to add a system prompt when using `--message`
- `--no-json-output` to print plain text instead of JSON

Notes
- This example is minimal and intended for local experimentation. No rate limiting or auth is provided in the CLI.
