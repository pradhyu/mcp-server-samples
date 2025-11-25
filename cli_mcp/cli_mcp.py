#!/usr/bin/env python3
"""CLI MCP sample — forward messages to LangChain ChatOpenAI (OpenRouter via OPENAI_API_BASE).

Usage examples:
  # single message
  export OPENAI_API_KEY="<key>"
  export OPENAI_API_BASE="https://api.openrouter.ai/v1"
  python cli_mcp.py --message "Say hello"

  # JSON file with messages
  python cli_mcp.py --file messages.json

messages.json example:
{
  "messages": [
    {"role":"system","content":"You are a helpful assistant."},
    {"role":"user","content":"Write a haiku about coffee."}
  ],
  "model": "gpt-4o-mini"
}
"""

import json
import sys
from typing import Optional

import click
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage


@click.command()
@click.option("--file", "file_path", type=click.Path(exists=True), help="JSON file containing messages and optional model")
@click.option("--message", "message", help="Single user message string")
@click.option("--model", "model", default="gpt-4o-mini", help="Model name to use (overridden by file if present)")
@click.option("--system", "system_msg", default=None, help="Optional system message to prepend when using --message")
@click.option("--json-output/--no-json-output", "json_output", default=True, help="Print machine-readable JSON (default) or plain text")
def main(file_path: Optional[str], message: Optional[str], model: str, system_msg: Optional[str], json_output: bool):
    messages = []

    if file_path:
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
        except Exception as e:
            click.echo(f"Failed to read/parse JSON file: {e}", err=True)
            sys.exit(2)
        messages = data.get("messages", [])
        model = data.get("model", model)

    if message:
        if system_msg:
            messages.append({"role": "system", "content": system_msg})
        messages.append({"role": "user", "content": message})

    if not messages:
        click.echo("No messages provided. Use --file or --message.", err=True)
        sys.exit(2)

    lc_msgs = []
    for m in messages:
        role = (m.get("role") or "user").lower()
        content = m.get("content", "")
        if role == "system":
            lc_msgs.append(SystemMessage(content=content))
        elif role == "assistant":
            lc_msgs.append(AIMessage(content=content))
        else:
            lc_msgs.append(HumanMessage(content=content))

    try:
        chat = ChatOpenAI(model_name=model, temperature=0)
        resp = chat(lc_msgs)
    except Exception as e:
        click.echo(f"Model call failed: {e}", err=True)
        sys.exit(3)

    out = {"response": resp.content, "model": model}

    if json_output:
        click.echo(json.dumps(out, indent=2))
    else:
        click.echo(resp.content)


if __name__ == "__main__":
    main()
