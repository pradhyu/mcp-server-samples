from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

app = FastAPI(title="Simple MCP FastAPI sample")


class Message(BaseModel):
    role: str
    content: str


class MCPRequest(BaseModel):
    messages: List[Message]
    model: Optional[str] = None


@app.post("/mcp")
async def mcp(req: MCPRequest):
    """Accept a list of messages (role/content) and return a single assistant reply.

    Minimal "MCP-like" endpoint: it converts incoming messages to LangChain message objects
    and calls ChatOpenAI. It expects OPENAI_API_KEY and OPENAI_API_BASE in the environment
    when using OpenRouter.
    """
    model_name = req.model or "gpt-4o-mini"

    chat = ChatOpenAI(model_name=model_name, temperature=0)

    lc_messages = []
    for m in req.messages:
        if m.role.lower() == "system":
            lc_messages.append(SystemMessage(content=m.content))
        elif m.role.lower() == "assistant":
            # assistant messages are rarely sent from clients, but we include for completeness
            lc_messages.append(AIMessage(content=m.content))
        else:
            lc_messages.append(HumanMessage(content=m.content))

    # Call the model
    resp = chat(lc_messages)

    # resp is an AIMessage-like object from LangChain; return its content
    return {"response": resp.content}


@app.get("/")
def root():
    return {"msg": "Simple MCP FastAPI sample. POST /mcp with messages payload."}
