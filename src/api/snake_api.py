"""Python API for the Snake game C library.

This module provides a Python interface to the Snake game C library.
It wraps the C functions and provides a more Pythonic interface for game
control and state management.

Example:
    ```python
    from src.api.snake_api import SnakeAPI
    # Initialize the API with the path to the compiled C library
    api = SnakeAPI("build/libsnake.so")
    # Start playing
    api.move()  # Move the snake
    api.change_direction("right")  # Change direction
    score = api.get_score()  # Get current score
    ```
"""

import os
from ctypes import CDLL, c_int, c_void_p
from ctypes import POINTER, Structure, c_bool, c_float, byref
from typing import Optional, List, Tuple

GRID_WIDTH = 20
GRID_HEIGHT = 20


# pylint: disable=too-few-public-methods
class GameState(Structure):
    """Structure to hold game state data.

    This class represents the internal game state structure used by
     the C library. It maps directly to the C structure and is used
     for data exchange between Python and C code.

    Attributes:
        snake_positions: Pointer to array of snake segment positions
        snake_length: Current length of the snake
        food_position: Pointer to array containing food position
        score: Current game score
        is_game_over: Boolean indicating if game is over
    """

    _fields_ = [
        ("snake_positions", POINTER(c_int)),
        ("snake_length", c_int),
        ("food_position", POINTER(c_int)),
        ("score", c_int),
        ("is_game_over", c_bool),
    ]


class Position(Structure):
    """Structure to hold a 2D position.

    This class represents a position in the game grid with x and y coordinates.
    It maps directly to the C structure used for position data exchange.

    Attributes:
        x: The x-coordinate
        y: The y-coordinate
    """

    _fields_ = [("x", c_int), ("y", c_int)]


class SnakeAPI:
    """Python wrapper for the Snake game C library.

    This class provides a high-level interface to control the Snake
     game. It handles all communication with the C library and
     provides methods for game control, state management, and error
     handling.

    Attributes:
        lib: The loaded C library instance
        game_instance: Pointer to the current game instance in C

    Example:
        ```python
        api = SnakeAPI("build/libsnake.so")
        api.move()
        api.change_direction("right")
        state = api.get_state()
        ```
    """

    def __init__(self, lib_path: Optional[str] = None):
        """Initialize the Snake API.

        Args:
            lib_path: Path to the shared library. If None, uses default path.
        """
        if lib_path is None:
            # Get the directory of the current file
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # Go up one level to the src directory
            src_dir = os.path.dirname(current_dir)
            # Go up one more level to the project root
            project_root = os.path.dirname(src_dir)
            # Construct the path to the shared library
            lib_path = os.path.join(project_root, "build", "libsnake.so")

        try:
            self.lib = CDLL(lib_path)
        except OSError as e:
            raise RuntimeError(f"Failed to load library: {lib_path}") from e
        self._setup_function_signatures()
        self.game_instance = self.lib.create_game()
        if not self.game_instance:
            raise RuntimeError("Failed to create game instance")

    def _setup_function_signatures(self):
        """Set up the function signatures for the C library."""
        # Core game functions
        self.lib.create_game.restype = c_void_p
        self.lib.create_game.argtypes = []

        self.lib.destroy_game.argtypes = [c_void_p]
        self.lib.destroy_game.restype = None

        self.lib.reset_game.argtypes = [c_void_p]
        self.lib.reset_game.restype = None

        self.lib.move_snake.argtypes = [c_void_p]
        self.lib.move_snake.restype = c_bool

        self.lib.change_direction.argtypes = [c_void_p, c_int]
        self.lib.change_direction.restype = None

        self.lib.is_game_over.argtypes = [c_void_p]
        self.lib.is_game_over.restype = c_bool

        self.lib.get_score.argtypes = [c_void_p]
        self.lib.get_score.restype = c_int

        # Snake state functions
        self.lib.get_snake_length.argtypes = [c_void_p]
        self.lib.get_snake_length.restype = c_int

        self.lib.get_snake_positions.argtypes = [c_void_p, POINTER(Position)]
        self.lib.get_snake_positions.restype = None

        self.lib.get_snake_direction.argtypes = [c_void_p]
        self.lib.get_snake_direction.restype = c_int

        # Food functions
        self.lib.get_food_position.argtypes = [c_void_p, POINTER(Position)]
        self.lib.get_food_position.restype = None

        self.lib.set_food_position.argtypes = [c_void_p, c_int, c_int]
        self.lib.set_food_position.restype = None

        # Game state functions
        self.lib.get_game_state.argtypes = [
            c_void_p,
            POINTER(c_int),
            POINTER(c_int),
            POINTER(c_int),
            POINTER(c_int),
            POINTER(c_int),
            POINTER(c_bool),
        ]
        self.lib.get_game_state.restype = None

        # Game settings functions
        self.lib.set_game_speed.argtypes = [c_void_p, c_float]
        self.lib.set_game_speed.restype = None

        self.lib.get_game_speed.argtypes = [c_void_p]
        self.lib.get_game_speed.restype = c_float

    def move(self) -> bool:
        """Move the snake in its current direction.

        Returns:
            bool: True if the move was successful, False if game over
        """
        if not self.game_instance:
            raise RuntimeError("Game instance not initialized")
        return self.lib.move_snake(self.game_instance)

    def change_direction(self, direction: str) -> None:
        """Change the snake's direction.

        Args:
            direction: New direction ('up', 'down', 'left', 'right')

        Raises:
            ValueError: If invalid direction
        """
        if not self.game_instance:
            raise RuntimeError("Game instance not initialized")
        dir_map = {"up": 0, "right": 1, "down": 2, "left": 3}
        if direction not in dir_map:
            raise ValueError("Invalid direction")
        self.lib.change_direction(self.game_instance, dir_map[direction])

    def is_game_over(self) -> bool:
        """Check if the game is over.

        Returns:
            bool: True if game is over, False otherwise
        """
        if not self.game_instance:
            raise RuntimeError("Game instance not initialized")
        return self.lib.is_game_over(self.game_instance)

    def get_score(self) -> int:
        """Get the current game score.

        Returns:
            int: Current score
        """
        if not self.game_instance:
            raise RuntimeError("Game instance not initialized")
        return self.lib.get_score(self.game_instance)

    def get_snake_length(self) -> int:
        """Get the current length of the snake.

        Returns:
            int: Current snake length
        """
        if not self.game_instance:
            raise RuntimeError("Game instance not initialized")
        return self.lib.get_snake_length(self.game_instance)

    def get_snake_positions(self) -> List[Tuple[int, int]]:
        """Get the current positions of the snake's body segments.

        Returns:
            List[Tuple[int, int]]: List of (x,y) coordinates for each segment
        """
        if not self.game_instance:
            raise RuntimeError("Game instance not initialized")
        length = self.get_snake_length()
        positions = (Position * length)()
        self.lib.get_snake_positions(self.game_instance, positions)
        return [(positions[i].x, positions[i].y) for i in range(length)]

    def get_food_position(self) -> Tuple[int, int]:
        """Get the current position of the food.

        Returns:
            tuple[int, int]: (x,y) coordinates of the food
        """
        if not self.game_instance:
            raise RuntimeError("Game instance not initialized")
        pos = Position()
        self.lib.get_food_position(self.game_instance, byref(pos))
        return (pos.x, pos.y)

    def set_food_position(self, x: int, y: int) -> None:
        """Set the position of the food.

        Args:
            x: X coordinate
            y: Y coordinate

        Raises:
            RuntimeError: If game instance is not initialized
        """
        if not self.game_instance:
            raise RuntimeError("Game instance not initialized")
        self.lib.set_food_position(self.game_instance, x, y)

    def get_snake_direction(self) -> str:
        """Get the current direction of the snake.

        Returns:
            str: Current direction ('up', 'down', 'left', 'right')
        """
        if not self.game_instance:
            raise RuntimeError("Game instance not initialized")
        dir_val = self.lib.get_snake_direction(self.game_instance)
        dir_map = {0: "up", 1: "right", 2: "down", 3: "left"}
        return dir_map.get(dir_val, "unknown")

    def set_game_speed(self, speed: float) -> None:
        """Set the game speed.

        Args:
            speed: New game speed

        Raises:
            RuntimeError: If game instance is not initialized
        """
        if not self.game_instance:
            raise RuntimeError("Game instance not initialized")
        self.lib.set_game_speed(self.game_instance, c_float(speed))

    def get_game_speed(self) -> float:
        """Get the current game speed.

        Returns:
            float: Current game speed
        """
        if not self.game_instance:
            raise RuntimeError("Game instance not initialized")
        return self.lib.get_game_speed(self.game_instance)

    def get_state(self) -> dict:
        """Get the current state of the game.

        Returns:
            dict: Dictionary containing game state
        """
        if not self.game_instance:
            raise RuntimeError("Game instance not initialized")
        max_snake = 100
        snake_positions = (c_int * (max_snake * 2))()
        snake_length = c_int()
        food_position = (c_int * 2)()
        score = c_int()
        direction = c_int()
        is_game_over = c_bool()
        self.lib.get_game_state(
            self.game_instance,
            snake_positions,
            byref(snake_length),
            food_position,
            byref(score),
            byref(direction),
            byref(is_game_over),
        )
        positions = [
            (snake_positions[i * 2], snake_positions[i * 2 + 1])
            for i in range(snake_length.value)
        ]
        dir_map = {0: "up", 1: "right", 2: "down", 3: "left"}
        return {
            "snake": positions,
            "length": snake_length.value,
            "food": (food_position[0], food_position[1]),
            "score": score.value,
            "direction": dir_map.get(direction.value, "unknown"),
            "game_over": bool(is_game_over.value),
        }

    def reset(self) -> None:
        """Reset the game to its initial state."""
        if not self.game_instance:
            raise RuntimeError("Game instance not initialized")
        self.lib.reset_game(self.game_instance)

    def cleanup(self) -> None:
        """Destroy the game instance."""
        if self.game_instance:
            self.lib.destroy_game(self.game_instance)
            self.game_instance = None
