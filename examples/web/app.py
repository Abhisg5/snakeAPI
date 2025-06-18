import os
import sys

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from src.api.snake_api import SnakeAPI
from flask import Flask, jsonify, request
from flask_cors import CORS
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Initialize game instance
game = None

def init_game():
    global game
    if game is None:
        lib_path = os.path.join(project_root, 'build', 'libsnake.so')
        if not os.path.exists(lib_path):
            raise RuntimeError(f"Library not found at {lib_path}")
        game = SnakeAPI(lib_path)
    return game

def cleanup_game():
    global game
    if game is not None:
        game = None
        logger.info("Game instance cleaned up")

@app.route('/')
def root():
    return jsonify({"message": "Snake Game API is running"})

@app.route('/api/game/init', methods=['POST'])
def init():
    init_game()
    return jsonify({"message": "Game initialized"})

@app.route('/api/game/state', methods=['GET'])
def get_state():
    try:
        game = init_game()
        return jsonify({
            'snake': game.get_snake_positions(),
            'food': game.get_food_position(),
            'score': game.get_score(),
            'game_over': game.is_game_over()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/game/move', methods=['POST'])
def move():
    try:
        game = init_game()
        game.move()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/game/direction/<direction>', methods=['POST'])
def change_direction(direction):
    try:
        game = init_game()
        game.change_direction(direction)
        return jsonify({'success': True})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/game/cleanup', methods=['POST'])
def cleanup():
    cleanup_game()
    return jsonify({"message": "Game cleaned up"})

@app.route('/api/game/reset', methods=['POST'])
def reset_game():
    try:
        game = init_game()
        game.reset()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/game/score', methods=['GET'])
def get_score():
    try:
        game = init_game()
        return jsonify({'score': game.get_score()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    print("Starting Snake game API server on http://localhost:4000")
    app.run(host='0.0.0.0', port=4000) 