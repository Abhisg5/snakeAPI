# Snake Game API Documentation

This document describes how to use the Snake Game API to embed the game in your own website or application.

## API Endpoints

### Game State
```http
GET /api/game/state
```
Returns the current state of the game.

Response:
```json
{
    "snake": [[x1, y1], [x2, y2], ...],  // Array of snake segment positions
    "food": [x, y],                       // Food position
    "score": 0,                           // Current score
    "game_over": false                    // Game over status
}
```

### Move Snake
```http
POST /api/game/move
```
Moves the snake one step forward.

Response:
```json
{
    "success": true
}
```

### Change Direction
```http
POST /api/game/direction
Content-Type: application/json

{
    "direction": 0  // 0: up, 1: right, 2: down, 3: left
}
```
Changes the snake's direction.

Response:
```json
{
    "success": true
}
```

### Reset Game
```http
POST /api/game/reset
```
Resets the game to its initial state.

Response:
```json
{
    "success": true
}
```

## Embedding the Game

### Option 1: Using an iframe
```html
<iframe src="http://localhost:4000" width="500" height="600" frameborder="0"></iframe>
```

### Option 2: Using the API Directly
Here's a basic example of how to use the API in your own JavaScript code:

```javascript
class SnakeGame {
    constructor(containerId) {
        this.container = document.getElementById(containerId);
        this.canvas = document.createElement('canvas');
        this.canvas.width = 400;
        this.canvas.height = 400;
        this.container.appendChild(this.canvas);
        this.ctx = this.canvas.getContext('2d');
        this.gameLoop = null;
        this.cellSize = 20;
    }

    start() {
        this.gameLoop = setInterval(() => this.update(), 200);
    }

    async update() {
        try {
            await fetch('http://localhost:4000/api/game/move', { method: 'POST' });
            const response = await fetch('http://localhost:4000/api/game/state');
            const state = await response.json();
            this.draw(state);
        } catch (error) {
            console.error('Error:', error);
            clearInterval(this.gameLoop);
        }
    }

    changeDirection(direction) {
        fetch('http://localhost:4000/api/game/direction', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ direction })
        });
    }

    draw(state) {
        // Clear canvas
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

        // Draw snake
        state.snake.forEach(([x, y]) => {
            this.ctx.fillStyle = '#4CAF50';
            this.ctx.fillRect(x * this.cellSize, y * this.cellSize, this.cellSize - 1, this.cellSize - 1);
        });

        // Draw food
        this.ctx.fillStyle = '#ff0000';
        const [foodX, foodY] = state.food;
        this.ctx.fillRect(foodX * this.cellSize, foodY * this.cellSize, this.cellSize - 1, this.cellSize - 1);
    }
}

// Usage example:
const game = new SnakeGame('game-container');
game.start();

// Add keyboard controls
document.addEventListener('keydown', (event) => {
    switch(event.key) {
        case 'ArrowUp': game.changeDirection(0); break;
        case 'ArrowRight': game.changeDirection(1); break;
        case 'ArrowDown': game.changeDirection(2); break;
        case 'ArrowLeft': game.changeDirection(3); break;
    }
});
```

## Python API

You can also use the game through the Python API:

```python
from snake_api import SnakeAPI

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

## Error Handling

All API endpoints return appropriate HTTP status codes:
- 200: Success
- 400: Bad Request (invalid parameters)
- 500: Server Error

Error responses include a message:
```json
{
    "error": "Error message"
}
```

## CORS Support

The API supports Cross-Origin Resource Sharing (CORS), allowing you to make requests from different domains. The server is configured to accept requests from any origin. 