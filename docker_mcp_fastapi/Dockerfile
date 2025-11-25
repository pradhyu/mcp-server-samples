FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Copy repository into container. The build context should be repository root.
COPY . /app

# Install minimal system deps and Python deps
RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev \
    && python -m pip install --upgrade pip setuptools wheel \
    && pip install -r simple_mcp_fastapi/requirements.txt \
    && apt-get purge -y --auto-remove gcc \
    && rm -rf /var/lib/apt/lists/* /root/.cache/pip

EXPOSE 8000

CMD ["uvicorn", "simple_mcp_fastapi.main:app", "--host", "0.0.0.0", "--port", "8000"]
