# Installation Guide

This guide will help you install and set up the Snake Game API project.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.9 or higher
- GCC compiler (for building the C core)
- Make
- Git

### Installing Prerequisites

#### Ubuntu/Debian
```bash
sudo apt update
sudo apt install python3 python3-pip python3-dev build-essential make git
```

#### macOS
```bash
brew install python3 make git
```

#### Windows
1. Install [Python](https://www.python.org/downloads/)
2. Install [Git](https://git-scm.com/download/win)
3. Install [MinGW](https://www.mingw-w64.org/) for GCC and Make

## Installation Methods

### Method 1: Using pip (Recommended)

The easiest way to install the package is using pip:

```bash
pip install snake-api
```

### Method 2: Building from Source

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/snakeAPI.git
   cd snakeAPI
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   make install
   ```

4. **Build the project**:
   ```bash
   make build
   ```

## Verifying Installation

To verify that the installation was successful:

1. **Start the API server**:
   ```bash
   python -m snake_api
   ```

2. **Test the API**:
   ```bash
   curl http://localhost:4000/api/game/state
   ```

You should see a JSON response with the initial game state.

## Configuration

### Environment Variables

The following environment variables can be configured:

- `FLASK_ENV`: Set to `development` or `production` (default: `development`)
- `FLASK_APP`: Path to the Flask application (default: `app.py`)
- `PORT`: Port number for the API server (default: `4000`)

### Configuration File

You can also create a `config.py` file in the project root:

```python
class Config:
    FLASK_ENV = 'development'
    PORT = 4000
    DEBUG = True

class ProductionConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
```

## Troubleshooting

### Common Issues

1. **Build Errors**
   - Ensure GCC is properly installed
   - Check if Make is available in your PATH
   - Verify Python development headers are installed

2. **Import Errors**
   - Verify you're using the correct Python version
   - Check if the virtual environment is activated
   - Ensure all dependencies are installed

3. **Runtime Errors**
   - Check if the API server is running
   - Verify port 4000 is not in use
   - Check the logs for detailed error messages

### Getting Help

If you encounter any issues:

1. Check the [GitHub Issues](https://github.com/yourusername/snakeAPI/issues)
2. Search for similar problems in the [Discussions](https://github.com/yourusername/snakeAPI/discussions)
3. Create a new issue with:
   - Detailed error message
   - Steps to reproduce
   - System information
   - Python version

## Next Steps

- [Quick Start Guide](quickstart.md)
- [API Reference](../api/overview.md)
- [Deployment Guide](../deployment/api.md) 