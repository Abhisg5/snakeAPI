# Use Python 3.9 slim image as base
FROM python:3.9-slim

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    make \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy source code
COPY src/ /app/src/
COPY examples/web/ /app/web/
COPY Makefile /app/

# Build the core library
RUN cd src/core && make

# Install Python dependencies
RUN pip install --no-cache-dir -r web/requirements.txt

# Set environment variables
ENV PYTHONPATH=/app
ENV LD_LIBRARY_PATH=/app/src/core

# Expose port
EXPOSE 4000

# Run the web server
CMD ["python", "web/app.py"] 