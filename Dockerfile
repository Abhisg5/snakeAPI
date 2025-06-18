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

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code and app
COPY src/ src/
COPY app.py .
COPY Makefile .

# Build the core library
RUN make build

# Set environment variables
ENV PYTHONPATH=/app
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Expose port
EXPOSE 4000

# Run the API server with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:4000", "app:app"] 