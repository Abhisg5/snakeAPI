import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from api.snake_api import SnakeAPI
import time

def test_snake():
    print("Creating game instance...")
    game = SnakeAPI()
    
    print("\nInitial state:")
    print("Snake positions:", game.get_snake_positions())
    print("Food position:", game.get_food_position())
    print("Score:", game.get_score())
    
    print("\nMoving snake...")
    game.move()
    print("Snake positions after move:", game.get_snake_positions())
    
    print("\nChanging direction to right...")
    game.change_direction(1)
    game.move()
    print("Snake positions after direction change:", game.get_snake_positions())
    
    print("\nGame over status:", game.is_game_over())
    
    # Clean up
    game.cleanup()

if __name__ == "__main__":
    test_snake() 