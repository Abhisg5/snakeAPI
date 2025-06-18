"""Test suite for the Snake game API."""

import os
import pytest
from src.api.snake_api import SnakeAPI

# Path to the compiled C library
LIB_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "build", "libsnake.so"
)


@pytest.fixture
def snake_api():
    """Create a SnakeAPI instance for testing."""
    api = SnakeAPI(LIB_PATH)
    yield api
    api.cleanup()


def test_initialization(api_instance):
    """Test API initialization."""
    assert api_instance.game_instance is not None


def test_initialization_with_invalid_lib():
    """Test initialization with invalid library path."""
    with pytest.raises(RuntimeError):
        SnakeAPI("invalid_path.so")


def test_reset(api_instance):
    """Test game reset functionality."""
    # Get initial state
    initial_score = api_instance.get_score()
    initial_positions = api_instance.get_snake_positions()

    # Move snake and change score
    api_instance.move()
    api_instance.move()

    # Reset game
    api_instance.reset()

    # Verify reset state
    assert api_instance.get_score() == initial_score
    assert api_instance.get_snake_positions() == initial_positions
    assert not api_instance.is_game_over()


def test_move(api_instance):
    """Test snake movement."""
    initial_positions = api_instance.get_snake_positions()
    api_instance.move()
    new_positions = api_instance.get_snake_positions()
    assert new_positions != initial_positions


def test_change_direction(api_instance):
    """Test direction changes."""
    # Test each valid direction
    for direction in ["up", "right", "down", "left"]:
        api_instance.change_direction(direction)
        # Verify direction was changed (this would require additional methods to check)


def test_invalid_direction(api_instance):
    """Test invalid direction change."""
    with pytest.raises(ValueError):
        api_instance.change_direction("invalid")


def test_get_score(api_instance):
    """Test score retrieval."""
    score = api_instance.get_score()
    assert isinstance(score, int)
    assert score >= 0


def test_get_snake_length(api_instance):
    """Test snake length retrieval."""
    length = api_instance.get_snake_length()
    assert isinstance(length, int)
    assert length > 0


def test_get_snake_positions(api_instance):
    """Test snake positions retrieval."""
    positions = api_instance.get_snake_positions()
    assert isinstance(positions, list)
    assert len(positions) > 0
    assert all(isinstance(pos, tuple) for pos in positions)
    assert all(len(pos) == 2 for pos in positions)


def test_get_food_position(api_instance):
    """Test food position retrieval."""
    food_pos = api_instance.get_food_position()
    assert isinstance(food_pos, tuple)
    assert len(food_pos) == 2


def test_set_food_position(api_instance):
    """Test food position setting."""
    new_pos = (5, 5)
    api_instance.set_food_position(new_pos[0], new_pos[1])
    assert api_instance.get_food_position() == new_pos


def test_get_state(api_instance):
    """Test game state retrieval."""
    state = api_instance.get_state()
    assert isinstance(state, dict)
    assert "snake" in state
    assert "food" in state
    assert "score" in state
    assert "game_over" in state


def test_game_over_handling(api_instance):
    """Test game over state handling."""
    # Move snake into wall to trigger game over
    for _ in range(20):
        api_instance.move()

    assert api_instance.is_game_over()


def test_cleanup(api_instance):
    """Test cleanup of resources."""
    api_instance.cleanup()
    assert api_instance.game_instance is None
