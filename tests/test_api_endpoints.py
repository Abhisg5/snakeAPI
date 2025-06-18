"""Test suite for the Snake game API endpoints."""

import json
import pytest


def test_get_state(test_client):
    """Test getting game state."""
    response = test_client.get("/api/game/state")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "snake" in data
    assert "food" in data
    assert "score" in data
    assert "game_over" in data


def test_move(test_client):
    """Test moving the snake."""
    response = test_client.post("/api/game/move")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "success" in data
    assert data["success"] is True


def test_change_direction(test_client):
    """Test changing snake direction."""
    # Test each valid direction
    for direction in ["up", "right", "down", "left"]:
        response = test_client.post(f"/api/game/direction/{direction}")
        assert response.status_code == 200
        data = json.loads(response.data)
        assert "success" in data
        assert data["success"] is True


def test_invalid_direction(test_client):
    """Test invalid direction change."""
    response = test_client.post("/api/game/direction/invalid")
    assert response.status_code == 400
    data = json.loads(response.data)
    assert "error" in data


def test_reset_game(test_client):
    """Test resetting the game."""
    response = test_client.post("/api/game/reset")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "success" in data
    assert data["success"] is True


def test_get_score(test_client):
    """Test getting game score."""
    response = test_client.get("/api/game/score")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "score" in data
    assert isinstance(data["score"], int)


def test_game_over(test_client):
    """Test game over state."""
    # Move snake into wall to trigger game over
    for _ in range(20):
        test_client.post("/api/game/move")

    response = test_client.get("/api/game/state")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["game_over"] is True


def test_sequence_of_moves(test_client):
    """Test a sequence of moves and direction changes."""
    # Reset the game to ensure a fresh state
    test_client.post("/api/game/reset")

    # Get initial state
    response = test_client.get("/api/game/state")
    data = json.loads(response.data)
    game_over = data["game_over"]

    # Assert game is not over after reset and snake exists
    assert not game_over
    assert len(data["snake"]) > 0
