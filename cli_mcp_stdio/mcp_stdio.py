#!/usr/bin/env python3
"""MCP stdio sample

Protocol (simple line-delimited JSON):
- Input (one JSON object per line):
  {
    "id": "optional-client-id",
    "messages": [ {"role":"system|user|assistant", "content": "..."}, ... ],
    "model": "optional-model-name"
  }
- Output (one JSON object per line):
  { "id": "same-id", "response": "model text", "model": "used-model", "error": null }

This keeps framing simple (newline-delimited JSON) so you can pipe to/from the process.

Example:
  echo '{"messages":[{"role":"user","content":"Hello"}]}' | python mcp_stdio.py
"""

import sys
import json
import uuid
from typing import List, Optional

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage


def to_lc_messages(messages: List[dict]):
    lc = []
    for m in messages:
        role = (m.get("role") or "user").lower()
        content = m.get("content", "")
        if role == "system":
            lc.append(SystemMessage(content=content))
        elif role == "assistant":
            lc.append(AIMessage(content=content))
        else:
            lc.append(HumanMessage(content=content))
    return lc


def write_output(obj: dict):
    # Always emit a single JSON object per line and flush stdout
    sys.stdout.write(json.dumps(obj, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def main():
    # Read lines from stdin until EOF
    for raw in sys.stdin:
        line = raw.strip()
        if not line:
            continue
        try:
            data = json.loads(line)
        except Exception as e:
            write_output({"id": None, "response": None, "error": f"invalid_json: {e}"})
            continue

        id = data.get("id") or str(uuid.uuid4())
        messages = data.get("messages", [])
        model = data.get("model") or "gpt-4o-mini"

        if not isinstance(messages, list) or not messages:
            write_output({"id": id, "response": None, "model": model, "error": "no messages provided"})
            continue

        lc_msgs = to_lc_messages(messages)

        try:
            chat = ChatOpenAI(model_name=model, temperature=0)
            resp = chat(lc_msgs)
            write_output({"id": id, "response": resp.content, "model": model, "error": None})
        except Exception as e:
            write_output({"id": id, "response": None, "model": model, "error": str(e)})


if __name__ == "__main__":
    main()
