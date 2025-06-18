# Compiler settings
CC := gcc
CFLAGS := -Wall -Wextra -fPIC -O2
LDFLAGS := -shared

# Target library
TARGET := libsnake.so

# Source files
SRC := snake.c
OBJ := $(SRC:.c=.o)

# Default target
all: $(TARGET)

# Build the shared library
$(TARGET): $(OBJ)
	@echo "Linking $@..."
	@$(CC) $(LDFLAGS) -o $@ $^
	@echo "Library built successfully."

# Compile source files
%.o: %.c
	@echo "Compiling $<..."
	@$(CC) $(CFLAGS) -c $< -o $@

# Clean build artifacts
clean:
	@echo "Cleaning core build artifacts..."
	@rm -f $(OBJ) $(TARGET)
	@echo "Clean complete."

# Help target
help:
	@echo "Core library Makefile targets:"
	@echo "  all    - Build the shared library (default)"
	@echo "  clean  - Remove build artifacts"
	@echo "  help   - Show this help message"

.PHONY: all clean help 