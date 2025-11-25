FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Copy only the stdio MCP files to keep the image small and build fast
COPY ../cli_mcp_stdio/requirements.txt /app/requirements.txt
COPY ../cli_mcp_stdio/mcp_stdio.py /app/mcp_stdio.py

RUN python -m pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "mcp_stdio.py"]
