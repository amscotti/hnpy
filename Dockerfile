# Use Python 3.13 slim as base image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install uv for dependency management
RUN pip install uv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-install-project

COPY hnpy/ hnpy/
COPY main.py .

ENTRYPOINT ["uv", "run", "python", "main.py"]