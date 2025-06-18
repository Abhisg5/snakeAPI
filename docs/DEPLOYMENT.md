# Deployment Guide

This guide covers different ways to deploy the Snake API.

## Prerequisites

- Docker and Docker Compose (for containerized deployment)
- Python 3.9+ (for direct deployment)
- GCC and Make (for building the C core)

## Deployment Methods

### 1. Docker Deployment (Recommended)

The easiest way to deploy the API is using Docker:

1. Build and run using Docker Compose:
```bash
docker-compose up -d
```

2. The API will be available at `http://localhost:4000`

3. To stop the service:
```bash
docker-compose down
```

### 2. Direct Deployment

To deploy directly on a server:

1. Install dependencies:
```bash
# Install system dependencies
sudo apt-get update
sudo apt-get install -y build-essential gcc make

# Install Python dependencies
pip install -r examples/web/requirements.txt
```

2. Build the core library:
```bash
cd src/core
make
```

3. Set environment variables:
```bash
export PYTHONPATH=/path/to/project
export LD_LIBRARY_PATH=/path/to/project/src/core
```

4. Run the server:
```bash
cd examples/web
python app.py
```

### 3. Production Deployment

For production deployment, it's recommended to:

1. Use a production WSGI server like Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:4000 app:app
```

2. Set up a reverse proxy (e.g., Nginx) in front of the application:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:4000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

3. Use environment variables for configuration:
```bash
export FLASK_ENV=production
export FLASK_APP=app.py
```

## Scaling

The API can be scaled horizontally by:

1. Running multiple instances behind a load balancer
2. Using Docker Swarm or Kubernetes for container orchestration

Example Docker Swarm deployment:
```bash
docker stack deploy -c docker-compose.yml snake-api
```

## Monitoring

Monitor the API using:

1. Docker health checks (already configured in docker-compose.yml)
2. Application logs:
```bash
# Docker logs
docker-compose logs -f

# Direct deployment logs
tail -f /var/log/snake-api.log
```

## Security Considerations

1. Always run in production mode
2. Use HTTPS in production
3. Set up proper firewall rules
4. Keep dependencies updated
5. Monitor for security vulnerabilities

## Backup and Recovery

1. Backup the source code and configuration
2. Document the deployment process
3. Test recovery procedures regularly

## Troubleshooting

Common issues and solutions:

1. Library not found:
   - Check LD_LIBRARY_PATH
   - Verify library compilation

2. Port conflicts:
   - Check if port 4000 is available
   - Change port in configuration if needed

3. Memory issues:
   - Monitor memory usage
   - Adjust container resources if needed 