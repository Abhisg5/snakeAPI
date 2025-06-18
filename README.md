# Snake Game API

A Snake game implementation with a C core, Python API, and web interface. This project demonstrates how to create a high-performance game core in C and expose it through a Python API, with an example web interface.

## Project Structure

```
snakeAPI/
├── src/                    # Source code
│   ├── core/              # C implementation of the game
│   │   ├── snake.c       # Core game logic
│   │   └── Makefile      # Build configuration
│   └── api/              # Python API wrapper
│       └── snake_api.py  # Python interface to the C core
├── examples/              # Example implementations
│   ├── web/              # Web interface example
│   │   ├── app.py        # Flask application
│   │   ├── templates/    # HTML templates
│   │   └── requirements.txt
│   └── test_snake.py     # Basic Python API usage example
└── docs/                 # Documentation
    └── API.md           # API documentation
```

## Building the Core

To build the C core library:

```bash
cd src/core
make
```

This will create `libsnake.so` in the core directory.

## Python API

The Python API provides a simple interface to the C core. Example usage:

```python
from src.api.snake_api import SnakeAPI

# Create a new game instance
game = SnakeAPI()

# Move the snake
game.move()

# Change direction (0: up, 1: right, 2: down, 3: left)
game.change_direction(1)

# Get game state
snake_positions = game.get_snake_positions()
food_position = game.get_food_position()
score = game.get_score()
is_game_over = game.is_game_over()

# Clean up when done
game.cleanup()
```

## Web Interface

To run the example web interface:

```bash
cd examples/web
pip install -r requirements.txt
python app.py
```

Then open your browser to `http://localhost:4000`

## API Documentation

For detailed API documentation, see [docs/API.md](docs/API.md).

## Development

### Prerequisites

- C compiler (gcc/clang)
- Python 3.6+
- Make

### Building

1. Build the C core:
```bash
cd src/core
make
```

2. Install Python dependencies:
```bash
cd examples/web
pip install -r requirements.txt
```

### Running Tests

To run the basic test:
```bash
cd examples
python test_snake.py
```

## License

This project is open source and available under the MIT License. 