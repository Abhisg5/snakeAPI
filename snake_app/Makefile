# Compiler and flags
CC = g++
CFLAGS = -O3 -Wall -std=c++17 -undefined dynamic_lookup -I/opt/homebrew/include `python3 -m pybind11 --includes`
LDFLAGS_EXEC = -L/opt/homebrew/lib -lSDL2 -lSDL2_mixer
LDFLAGS_PY = `python3-config --ldflags`
PYTHON_SUFFIX = $(shell python3-config --extension-suffix)

# Targets
EXECUTABLE = modern_snake
PYTHON_MODULE = snake_game$(PYTHON_SUFFIX)

# Directories
OUTPUT_DIR = ../snake_render_api/src

# Source files for the standalone game
SOURCES_EXEC = src/snake.cpp src/renderer.cpp src/input_handler.cpp src/sound_manager.cpp src/game.cpp src/main.cpp
HEADERS_EXEC = src/snake.h src/renderer.h src/input_handler.h src/sound_manager.h src/game.h

# Source files for Python bindings
SOURCES_PY = src/snake.cpp src/snake_bindings.cpp

all: $(EXECUTABLE) $(OUTPUT_DIR)/$(PYTHON_MODULE)

# Ensure the output directory exists
$(OUTPUT_DIR):
	mkdir -p $(OUTPUT_DIR)

# Build the standalone executable
$(EXECUTABLE): $(SOURCES_EXEC) $(HEADERS_EXEC)
	$(CC) $(CFLAGS) $(SOURCES_EXEC) -o $(EXECUTABLE) $(LDFLAGS_EXEC)

# Build the Python shared library
$(OUTPUT_DIR)/$(PYTHON_MODULE): $(SOURCES_PY) | $(OUTPUT_DIR)
	$(CC) $(CFLAGS) $(SOURCES_PY) -shared -o $(OUTPUT_DIR)/$(PYTHON_MODULE) $(LDFLAGS_PY)

# Clean rule
clean:
	rm -rf $(EXECUTABLE) $(OUTPUT_DIR)