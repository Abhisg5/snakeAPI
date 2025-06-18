# Quick Start Guide

This guide will help you get started with the Snake Game API quickly.

## Running the Game

### 1. Start the API Server

```bash
# If installed via pip
python -m snake_api

# If running from source
cd snakeAPI
python app.py
```

The API server will start on `http://localhost:4000`.

### 2. Access the Game

Open your web browser and navigate to:
- Web version: `http://localhost:4000/web`
- Embed version: `http://localhost:4000/embed`

## Basic Usage

### Using the Web Interface

1. **Start a New Game**:
   - Click the "Start Game" button
   - Use arrow keys to control the snake
   - Try to eat the food to grow and increase your score

2. **Game Controls**:
   - ↑: Move Up
   - →: Move Right
   - ↓: Move Down
   - ←: Move Left
   - Space: Pause/Resume

3. **Game Over**:
   - When the game ends, your score will be displayed
   - Click "Play Again" to start a new game

### Using the API Directly

1. **Initialize the Game**:
   ```javascript
   await fetch('http://localhost:4000/api/game/reset', {
       method: 'POST'
   });
   ```

2. **Get Game State**:
   ```javascript
   const state = await fetch('http://localhost:4000/api/game/state')
       .then(r => r.json());
   ```

3. **Change Direction**:
   ```javascript
   await fetch('http://localhost:4000/api/game/direction/up', {
       method: 'POST'
   });
   ```

4. **Move Snake**:
   ```javascript
   await fetch('http://localhost:4000/api/game/move', {
       method: 'POST'
   });
   ```

## Embedding the Game

### Option 1: Using an iframe

```html
<iframe 
    src="http://localhost:4000/embed" 
    width="400" 
    height="500" 
    frameborder="0"
    allowfullscreen>
</iframe>
```

### Option 2: Using the API

```html
<div id="game-container"></div>
<script>
    class SnakeGame {
        constructor(containerId) {
            this.container = document.getElementById(containerId);
            this.canvas = document.createElement('canvas');
            this.canvas.width = 400;
            this.canvas.height = 400;
            this.container.appendChild(this.canvas);
            this.ctx = this.canvas.getContext('2d');
            this.cellSize = 20;
        }

        async start() {
            await this.reset();
            this.gameLoop = setInterval(() => this.update(), 200);
        }

        async reset() {
            await fetch('http://localhost:4000/api/game/reset', {
                method: 'POST'
            });
        }

        async update() {
            const state = await fetch('http://localhost:4000/api/game/state')
                .then(r => r.json());
            
            if (state.game_over) {
                clearInterval(this.gameLoop);
                return;
            }

            await fetch('http://localhost:4000/api/game/move', {
                method: 'POST'
            });

            this.draw(state);
        }

        draw(state) {
            this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
            
            // Draw snake
            state.snake.forEach(([x, y]) => {
                this.ctx.fillStyle = '#4CAF50';
                this.ctx.fillRect(
                    x * this.cellSize,
                    y * this.cellSize,
                    this.cellSize - 1,
                    this.cellSize - 1
                );
            });

            // Draw food
            this.ctx.fillStyle = '#ff0000';
            const [foodX, foodY] = state.food;
            this.ctx.fillRect(
                foodX * this.cellSize,
                foodY * this.cellSize,
                this.cellSize - 1,
                this.cellSize - 1
            );
        }

        changeDirection(direction) {
            fetch(`http://localhost:4000/api/game/direction/${direction}`, {
                method: 'POST'
            });
        }
    }

    // Create and start the game
    const game = new SnakeGame('game-container');
    game.start();

    // Add keyboard controls
    document.addEventListener('keydown', (e) => {
        switch(e.key) {
            case 'ArrowUp': game.changeDirection('up'); break;
            case 'ArrowRight': game.changeDirection('right'); break;
            case 'ArrowDown': game.changeDirection('down'); break;
            case 'ArrowLeft': game.changeDirection('left'); break;
        }
    });
</script>
```

## Next Steps

- [API Reference](../api/overview.md)
- [Frontend Documentation](../frontend/web.md)
- [Deployment Guide](../deployment/api.md) 