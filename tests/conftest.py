"""Shared pytest fixtures and configuration for the test suite."""

import os
import sys
import pytest
from src.api.snake_api import SnakeAPI

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Add src and examples directories to the Python path
sys.path.insert(0, os.path.join(project_root, "src"))
sys.path.insert(0, os.path.join(project_root, "examples"))


# Ensure the C library is built before running tests
@pytest.fixture(scope="session", autouse=True)
def build_library():
    """Build the C library before running tests."""
    os.makedirs("build", exist_ok=True)
    os.system("gcc -shared -o build/libsnake.so -fPIC src/core/snake.c")
    yield
    # Cleanup after all tests
    if os.path.exists("build/libsnake.so"):
        os.remove("build/libsnake.so")

@pytest.fixture
def api_instance():
    return SnakeAPI("build/libsnake.so")

@pytest.fixture
def test_client(api_instance):
    from examples.web.app import app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
