# Welcome to Snake Game API

A modern implementation of the classic Snake game with a C-based core and Python API, featuring both web and embeddable frontends.

## 🌟 Features

- **High-Performance Core**: C-based game engine for optimal performance
- **RESTful API**: Python/Flask API for game control and state management
- **Multiple Frontends**:
  - Web version with full-screen gameplay
  - Embeddable version for integration into other websites
- **Modern UI**: Clean, responsive design with intuitive controls
- **Cross-Platform**: Works on desktop and mobile devices
- **Easy Deployment**: Ready-to-deploy on Render.com (API) and Vercel (Frontend)

## 🚀 Quick Start

1. **Install the package**:
   ```bash
   pip install snake-api
   ```

2. **Run the API server**:
   ```bash
   python -m snake_api
   ```

3. **Access the game**:
   - Web version: http://localhost:4000/web
   - Embed version: http://localhost:4000/embed

## 📚 Documentation

- [Installation Guide](getting-started/installation.md)
- [Quick Start Guide](getting-started/quickstart.md)
- [API Reference](api/overview.md)
- [Frontend Documentation](frontend/web.md)
- [Deployment Guide](deployment/api.md)

## 🎮 Game Controls

- **Arrow Keys**: Control snake direction
- **Start Game**: Begin a new game
- **End Game**: Stop current game
- **Touch Controls**: Available on mobile devices

## 🔧 Development

### Prerequisites

- Python 3.9+
- GCC compiler
- Make

### Building from Source

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/snakeAPI.git
   cd snakeAPI
   ```

2. **Install dependencies**:
   ```bash
   make install
   ```

3. **Build the project**:
   ```bash
   make build
   ```

4. **Run tests**:
   ```bash
   make test
   ```

