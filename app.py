"""Snake Game API Server.

This is the main API server for the Snake game. It provides endpoints for
controlling the game and retrieving game state.
"""

import os
import sys
from flask import Flask, jsonify
from flask_cors import CORS
import logging

# Add the src directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.api.snake_api import SnakeAPI

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

# Initialize game instance
game = None

def init_game():
    """Initialize the game instance if it doesn't exist."""
    global game
    if game is None:
        lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'build', 'libsnake.so')
        if not os.path.exists(lib_path):
            raise RuntimeError(f"Library not found at {lib_path}")
        game = SnakeAPI(lib_path)
    return game

@app.route('/')
def root():
    """Root endpoint that returns API status."""
    return jsonify({
        "message": "Snake Game API is running",
        "status": "active",
        "version": "1.0.0",
        "endpoints": {
            "GET /api/game/state": "Get current game state",
            "POST /api/game/move": "Move snake one step",
            "POST /api/game/direction/<direction>": "Change snake direction (up/right/down/left)",
            "POST /api/game/reset": "Reset game to initial state"
        }
    })

@app.route('/api/game/state', methods=['GET'])
def get_state():
    """Get the current game state."""
    try:
        game = init_game()
        return jsonify({
            'snake': game.get_snake_positions(),
            'food': game.get_food_position(),
            'score': game.get_score(),
            'game_over': game.is_game_over(),
            'direction': game.get_snake_direction()
        })
    except Exception as e:
        logger.error(f"Error getting game state: {str(e)}")
        return jsonify({'error': str(e)}), 400

@app.route('/api/game/move', methods=['POST'])
def move():
    """Move the snake one step forward."""
    try:
        game = init_game()
        success = game.move()
        return jsonify({'success': success})
    except Exception as e:
        logger.error(f"Error moving snake: {str(e)}")
        return jsonify({'error': str(e)}), 400

@app.route('/api/game/direction/<direction>', methods=['POST'])
def change_direction(direction):
    """Change the snake's direction."""
    try:
        game = init_game()
        game.change_direction(direction)
        return jsonify({'success': True})
    except ValueError as e:
        logger.error(f"Invalid direction: {str(e)}")
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        logger.error(f"Error changing direction: {str(e)}")
        return jsonify({'error': str(e)}), 400

@app.route('/api/game/reset', methods=['POST'])
def reset():
    """Reset the game to its initial state."""
    try:
        game = init_game()
        game.reset()
        return jsonify({'success': True})
    except Exception as e:
        logger.error(f"Error resetting game: {str(e)}")
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4000))
    app.run(host='0.0.0.0', port=port) 