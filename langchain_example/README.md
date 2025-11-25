LangChain example

This tiny script shows how to call LangChain's ChatOpenAI. It expects these env vars when using OpenRouter:

```bash
export OPENAI_API_KEY="<your-openrouter-key>"
export OPENAI_API_BASE="https://api.openrouter.ai/v1"
```

Run:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python example.py
```

Expect the script to print a short poem from the model.
