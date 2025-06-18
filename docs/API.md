# Snake Game API Documentation

## Overview

The Snake Game API provides a RESTful interface to control and interact with the Snake game. The API is built using Flask and provides endpoints for game state management, snake movement, and direction control.

## Base URL

```
https://snakeapi.onrender.com
```

## Authentication

The API currently does not require authentication.

## Endpoints

### Game State

#### Get Current Game State

```http
GET /api/game/state
```

Returns the current state of the game, including snake position, food position, score, and game status.

**Response**

```json
{
    "snake": [[x1, y1], [x2, y2], ...],
    "food": [x, y],
    "score": 0,
    "game_over": false,
    "direction": "right"
}
```

**Example**

```javascript
const response = await fetch('https://snakeapi.onrender.com/api/game/state');
const state = await response.json();
console.log(state);
```

### Game Control

#### Move Snake

```http
POST /api/game/move
```

Moves the snake one step in the current direction.

**Response**

```json
{
    "success": true
}
```

**Example**

```javascript
const response = await fetch('https://snakeapi.onrender.com/api/game/move', {
    method: 'POST'
});
const result = await response.json();
```

#### Change Direction

```http
POST /api/game/direction/{direction}
```

Changes the snake's direction. Valid directions are: "up", "right", "down", "left".

**Parameters**

- `direction` (path parameter): The new direction for the snake

**Response**

```json
{
    "success": true
}
```

**Example**

```javascript
const response = await fetch('https://snakeapi.onrender.com/api/game/direction/up', {
    method: 'POST'
});
const result = await response.json();
```

#### Reset Game

```http
POST /api/game/reset
```

Resets the game to its initial state.

**Response**

```json
{
    "success": true
}
```

**Example**

```javascript
const response = await fetch('https://snakeapi.onrender.com/api/game/reset', {
    method: 'POST'
});
const result = await response.json();
```

## Error Handling

The API uses standard HTTP status codes to indicate the success or failure of requests:

- `200 OK`: Request succeeded
- `400 Bad Request`: Invalid request parameters
- `404 Not Found`: Endpoint not found
- `500 Internal Server Error`: Server-side error

Error responses include a message explaining the error:

```json
{
    "error": "Error message description"
}
```

## Rate Limiting

The API currently does not implement rate limiting. However, please be mindful of server resources and avoid making excessive requests.

## CORS Support

The API supports Cross-Origin Resource Sharing (CORS) and allows requests from any origin. This enables the frontend to be hosted on different domains.

## WebSocket Support

The API does not currently support WebSocket connections. All communication is done through HTTP requests.

## Examples

### Complete Game Flow

```javascript
// Initialize game
await fetch('https://snakeapi.onrender.com/api/game/reset', {
    method: 'POST'
});

// Game loop
async function gameLoop() {
    // Get current state
    const state = await fetch('https://snakeapi.onrender.com/api/game/state')
        .then(r => r.json());
    
    if (state.game_over) {
        console.log('Game Over! Score:', state.score);
        return;
    }
    
    // Move snake
    await fetch('https://snakeapi.onrender.com/api/game/move', {
        method: 'POST'
    });
    
    // Continue loop
    setTimeout(gameLoop, 100);
}

// Start game
gameLoop();
```

### Direction Control

```javascript
// Handle keyboard input
document.addEventListener('keydown', async (e) => {
    let direction;
    switch(e.key) {
        case 'ArrowUp':
            direction = 'up';
            break;
        case 'ArrowRight':
            direction = 'right';
            break;
        case 'ArrowDown':
            direction = 'down';
            break;
        case 'ArrowLeft':
            direction = 'left';
            break;
        default:
            return;
    }
    
    await fetch(`https://snakeapi.onrender.com/api/game/direction/${direction}`, {
        method: 'POST'
    });
});
```

## Best Practices

1. **Error Handling**: Always implement proper error handling for API requests.
2. **State Management**: Keep track of the game state locally to reduce API calls.
3. **Rate Limiting**: Implement client-side rate limiting to prevent excessive requests.
4. **Caching**: Cache game state when appropriate to improve performance.

## Support

For support, please open an issue on the GitHub repository or contact the maintainers. 