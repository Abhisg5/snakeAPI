# API Overview

The Snake Game API provides a RESTful interface to control and interact with the Snake game. This document provides an overview of the API architecture, design principles, and key concepts.

## Architecture

The API is built using a layered architecture:

1. **C Core Layer**
   - High-performance game engine
   - Handles core game logic
   - Manages game state

2. **Python API Layer**
   - RESTful API endpoints
   - Bridges C core with web interface
   - Handles request/response formatting

3. **Web Interface Layer**
   - User interface
   - Game visualization
   - Input handling

## Design Principles

### 1. RESTful Design

The API follows REST principles:
- Resource-oriented URLs
- HTTP methods for operations
- Stateless communication
- JSON response format

### 2. Performance

- C-based core for optimal performance
- Minimal data transfer
- Efficient state management
- Asynchronous operations

### 3. Security

- CORS support for web clients
- Input validation
- Error handling
- Rate limiting (planned)

## Key Concepts

### Game State

The game state is represented as a JSON object:

```json
{
    "snake": [[x1, y1], [x2, y2], ...],  // Snake body positions
    "food": [x, y],                      // Food position
    "score": 0,                          // Current score
    "game_over": false,                  // Game status
    "direction": "right"                 // Current direction
}
```

### Directions

Valid directions are:
- `"up"`
- `"right"`
- `"down"`
- `"left"`

### Grid System

- Grid size: 20x20 cells
- Cell size: 20 pixels
- Origin: Top-left corner (0,0)

## API Endpoints

### Base URL

```
https://snakeapi.onrender.com
```

### Available Endpoints

1. **Game State**
   - `GET /api/game/state`
   - Returns current game state

2. **Game Control**
   - `POST /api/game/move`
   - `POST /api/game/direction/{direction}`
   - `POST /api/game/reset`

## Response Format

### Success Response

```json
{
    "success": true,
    "data": {
        // Response data
    }
}
```

### Error Response

```json
{
    "success": false,
    "error": "Error message"
}
```

## Status Codes

- `200 OK`: Request succeeded
- `400 Bad Request`: Invalid parameters
- `404 Not Found`: Endpoint not found
- `500 Internal Server Error`: Server error

## Rate Limiting

The API currently does not implement rate limiting. However, please be mindful of server resources and avoid making excessive requests.

## CORS Support

The API supports Cross-Origin Resource Sharing (CORS) and allows requests from any origin. This enables the frontend to be hosted on different domains.

## WebSocket Support

The API does not currently support WebSocket connections. All communication is done through HTTP requests.

## Best Practices

1. **Error Handling**
   - Always check response status
   - Handle network errors
   - Implement retry logic

2. **State Management**
   - Cache game state locally
   - Update state efficiently
   - Handle state synchronization

3. **Performance**
   - Minimize API calls
   - Use appropriate polling intervals
   - Implement client-side caching

## Examples

### Basic Game Flow

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
        case 'ArrowUp': direction = 'up'; break;
        case 'ArrowRight': direction = 'right'; break;
        case 'ArrowDown': direction = 'down'; break;
        case 'ArrowLeft': direction = 'left'; break;
        default: return;
    }
    
    await fetch(`https://snakeapi.onrender.com/api/game/direction/${direction}`, {
        method: 'POST'
    });
});
```

## Next Steps

- [API Endpoints](endpoints.md)
- [Authentication](authentication.md)
- [Error Handling](error-handling.md) 