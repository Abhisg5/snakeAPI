# Snake Game API

[![Build Status](https://github.com/yourusername/snakeAPI/actions/workflows/ci.yml/badge.svg)](https://github.com/yourusername/snakeAPI/actions/workflows/ci.yml)
[![Documentation Status](https://github.com/yourusername/snakeAPI/actions/workflows/docs.yml/badge.svg)](https://github.com/yourusername/snakeAPI/actions/workflows/docs.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Flask Version](https://img.shields.io/badge/flask-2.0.1-blue.svg)](https://flask.palletsprojects.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![codecov](https://codecov.io/gh/yourusername/snakeAPI/branch/main/graph/badge.svg)](https://codecov.io/gh/yourusername/snakeAPI)

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

## 🏗️ Architecture

```
snakeAPI/
├── src/
│   ├── core/           # C-based game engine
│   │   ├── snake.c     # Core game logic
│   │   └── snake.h     # Core game headers
│   └── api/            # Python API layer
│       └── snake_api.py # Python API implementation
├── frontend/
│   ├── web/           # Full-screen web version
│   └── embed/         # Embeddable version
├── tests/             # Test suite
├── docs/              # Documentation
└── examples/          # Example implementations
```

### Core Components

1. **C Game Engine** (`src/core/`):
   - Handles core game logic
   - Manages snake movement, collision detection
   - Provides high-performance game state management

2. **Python API** (`src/api/`):
   - RESTful API endpoints
   - Bridges C core with web interface
   - Handles game state and control

3. **Frontend** (`frontend/`):
   - Modern, responsive UI
   - Real-time game state updates
   - Keyboard and touch controls

## 🚀 Quick Start

### Local Development

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/snakeAPI.git
   cd snakeAPI
   ```

2. **Install dependencies**:
   ```bash
   make install
   ```

3. **Build the core library**:
   ```bash
   make build
   ```

4. **Run the API server**:
   ```bash
   make run
   ```

5. **Access the game**:
   - Web version: http://localhost:4000/web
   - Embed version: http://localhost:4000/embed

### Deployment

#### API Deployment (Render.com)

1. Create a new Web Service on Render.com
2. Connect your GitHub repository
3. Configure the service:
   - Build Command: `make build`
   - Start Command: `gunicorn app:app`
   - Environment Variables:
     - `FLASK_ENV=production`
     - `PYTHONPATH=/app`

#### Frontend Deployment (Vercel)

1. Create a new project on Vercel
2. Connect your GitHub repository
3. Configure the project:
   - Framework Preset: Other
   - Root Directory: `frontend`
   - Build Command: (leave empty)
   - Output Directory: (leave empty)

## 🎮 Game Controls

- **Arrow Keys**: Control snake direction
- **Start Game**: Begin a new game
- **End Game**: Stop current game
- **Touch Controls**: Available on mobile devices

## 📚 API Documentation

### Endpoints

- `GET /api/game/state`
  - Returns current game state
  - Response: `{ snake: [[x,y],...], food: [x,y], score: int, game_over: bool, direction: string }`

- `POST /api/game/move`
  - Moves snake one step
  - Response: `{ success: bool }`

- `POST /api/game/direction/<direction>`
  - Changes snake direction
  - Directions: "up", "right", "down", "left"
  - Response: `{ success: bool }`

- `POST /api/game/reset`
  - Resets game to initial state
  - Response: `{ success: bool }`

### Example Usage

```javascript
// Initialize game
await fetch('https://snakeapi.onrender.com/api/game/reset', {
    method: 'POST'
});

// Get game state
const state = await fetch('https://snakeapi.onrender.com/api/game/state')
    .then(r => r.json());

// Change direction
await fetch('https://snakeapi.onrender.com/api/game/direction/up', {
    method: 'POST'
});
```

## 🔧 Development

### Prerequisites

- Python 3.9+
- GCC compiler
- Make

### Building from Source

1. **Install dependencies**:
   ```bash
   make install
   ```

2. **Build the project**:
   ```bash
   make build
   ```

3. **Run tests**:
   ```bash
   make test
   ```

### Project Structure

- `src/core/`: C-based game engine
- `src/api/`: Python API implementation
- `frontend/`: Web and embeddable frontends
- `tests/`: Test suite
- `docs/`: Documentation
- `examples/`: Example implementations

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📫 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/yourusername/snakeAPI](https://github.com/yourusername/snakeAPI) 