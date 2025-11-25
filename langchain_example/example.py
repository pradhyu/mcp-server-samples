"""Tiny LangChain example using ChatOpenAI and OpenRouter (via OPENAI_API_BASE).

Usage:
  export OPENAI_API_KEY="<your-openrouter-key>"
  export OPENAI_API_BASE="https://api.openrouter.ai/v1"
  python example.py
"""

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage


def main():
    chat = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    msg = HumanMessage(content="Write a two-line poem about the moon.")
    resp = chat([msg])
    # resp is an AIMessage-like object in LangChain
    print("Model response:\n")
    print(resp.content)


if __name__ == "__main__":
    main()
