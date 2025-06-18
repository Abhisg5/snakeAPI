# Project variables
PYTHON := python3
PIP := pip3
CORE_DIR := src/core
API_DIR := src/api
EXAMPLES_DIR := examples
WEB_DIR := examples/web
BUILD_DIR = build
DOCS_DIR = docs

# Python paths
PYTHON_SRC = src/api
PYTHON_TESTS = tests
PYTHON_FILES = $(shell find $(PYTHON_SRC) -name "*.py")
PYTHON_TEST_FILES = $(shell find $(PYTHON_TESTS) -name "test_*.py")

# C paths
C_SRC = src/core
C_FILES = $(shell find $(C_SRC) -name "*.c")
C_HEADERS = $(shell find $(C_SRC) -name "*.h")

# Default target
all: lint format test coverage c-lint c-format c-test c-coverage docs c-docs

# Build the core library
build: build-lib
	@echo "Building core library..."
	@cd $(CORE_DIR) && $(MAKE)
	@echo "Core library built successfully."

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	@cd $(CORE_DIR) && $(MAKE) clean
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name "*.pyo" -delete
	@find . -type f -name "*.so" -delete
	@echo "Clean complete."

# Install Python dependencies
deps:
	@echo "Installing Python dependencies..."
	@$(PIP) install -r $(WEB_DIR)/requirements.txt
	@echo "Dependencies installed successfully."

# Run the test example
test:
	@echo "Running test example..."
	@$(PYTHON) $(EXAMPLES_DIR)/test_snake.py

# Run the web interface
web:
	@echo "Starting web interface..."
	@$(PYTHON) $(WEB_DIR)/app.py

# Development setup
dev: deps build

# Help target
help:
	@echo "Available targets:"
	@echo "  all      - Build everything (default)"
	@echo "  build    - Build the core library"
	@echo "  clean    - Remove all build artifacts"
	@echo "  deps     - Install Python dependencies"
	@echo "  test     - Run the test example"
	@echo "  web      - Run the web interface"
	@echo "  dev      - Set up development environment"
	@echo "  help     - Show this help message"

# Build the C library
build-lib:
	@echo "Building C library..."
	@mkdir -p build
	gcc -shared -o build/libsnake.so -fPIC $(C_SRC)/snake.c

# Build Docker images
build-docker:
	@echo "Building Docker images..."
	docker-compose build

# Run the application
run:
	@echo "Starting application..."
	docker-compose up

# Run in detached mode
run-detached:
	@echo "Starting application in detached mode..."
	docker-compose up -d

# Stop the application
stop:
	@echo "Stopping application..."
	docker-compose down

# Python linting
lint:
	@echo "Running Python linting..."
	$(PYTHON) -m pylint --rcfile=.pylintrc src/

# Python formatting
format:
	@echo "Running Python formatting..."
	$(PYTHON) -m black src/

# Python testing and coverage
test:
	@echo "Running Python tests..."
	$(PYTHON) -m pytest tests/

coverage:
	@echo "Running Python coverage..."
	$(PYTHON) -m pytest --cov=src tests/

# C code linting
c-lint:
	@echo "Running C linting..."
	cppcheck $(C_SRC)/*.c

# C code formatting
c-format:
	@echo "Running C formatting..."
	clang-format -i $(C_SRC)/*.c $(C_SRC)/*.h

# C code testing
c-test:
	@echo "Running C tests..."
	@mkdir -p $(BUILD_DIR)
	gcc -I/opt/homebrew/include -L/opt/homebrew/lib -o $(BUILD_DIR)/test_snake $(C_SRC)/snake.c $(C_SRC)/test_snake.c -lcunit
	./$(BUILD_DIR)/test_snake

# C code coverage
c-coverage:
	@echo "Running C tests with coverage..."
	@mkdir -p $(BUILD_DIR)
	gcc -I/opt/homebrew/include -L/opt/homebrew/lib -fprofile-arcs -ftest-coverage -c $(C_SRC)/snake.c -o $(BUILD_DIR)/snake.o
	gcc -I/opt/homebrew/include -L/opt/homebrew/lib -fprofile-arcs -ftest-coverage -c $(C_SRC)/test_snake.c -o $(BUILD_DIR)/test_snake.o
	gcc -fprofile-arcs -ftest-coverage -o $(BUILD_DIR)/test_snake $(BUILD_DIR)/snake.o $(BUILD_DIR)/test_snake.o -L/opt/homebrew/lib -lcunit
	./$(BUILD_DIR)/test_snake
	cp $(C_SRC)/snake.c $(BUILD_DIR)/
	cd $(BUILD_DIR) && gcov -o . snake.c

# Generate Python documentation
docs:
	@echo "Generating Python documentation..."
	@mkdir -p $(DOCS_DIR)
	$(PYTHON) -m pdoc --html --output-dir $(DOCS_DIR) src/api/snake_api.py

# Generate C documentation
c-docs:
	@echo "Generating C documentation..."
	@mkdir -p $(DOCS_DIR)/c
	doxygen Doxyfile

# Install Python dependencies
install-deps:
	@echo "Installing Python dependencies..."
	$(PIP) install -r requirements.txt
	@echo "Installing C dependencies..."
	brew install cppcheck clang-format doxygen

# Run all checks
all-checks: lint format test coverage c-lint c-format c-test c-coverage docs c-docs

# Install target
install:
	@echo "Installing Python dependencies..."
	$(PIP) install -r requirements.txt
	$(PIP) install flake8 black pytest pytest-cov pdoc
	@echo "Installing C dependencies..."
	brew install cppcheck clang-format doxygen

# Pre-commit hook
setup-pre-commit:
	@echo "Setting up pre-commit hook..."
	@mkdir -p .git/hooks
	@echo '#!/bin/sh\nmake lint format test coverage c-lint c-format c-test c-coverage docs c-docs' > .git/hooks/pre-commit
	@chmod +x .git/hooks/pre-commit

.PHONY: all build clean deps test web dev help build-lib build-docker run run-detached stop install-deps all-checks install setup-pre-commit 