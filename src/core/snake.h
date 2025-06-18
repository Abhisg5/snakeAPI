#ifndef SNAKE_H
#define SNAKE_H

#include <stdbool.h>

// Grid dimensions
#define GRID_WIDTH 20
#define GRID_HEIGHT 20

// Struct definitions for use in tests and other files

typedef struct {
  int x;
  int y;
} Position;

typedef enum { UP, RIGHT, DOWN, LEFT } Direction;

typedef struct {
  Position *segments;
  int length;
  int capacity;
  Direction direction;
  Position food;
  int score;
  bool game_over;
  float speed;
} Game;

// Core game functions
void *create_game(void);
void destroy_game(void *game);
bool move_snake(void *game);
void change_direction(void *game, Direction new_direction);
bool is_game_over(void *game);
int get_score(void *game);
int get_snake_length(void *game);
void get_snake_positions(void *game, Position *positions);
void get_food_position(void *game, Position *position);
void set_food_position(void *game, int x, int y); // Only for testing
void set_game_speed(void *game, float speed);
float get_game_speed(void *game);

// Wrapper functions for Python API
void *create_game_wrapper(void);
void free_game_wrapper(void *game);
bool move_snake_wrapper(void *game);
void change_direction_wrapper(void *game, Direction new_direction);
bool is_game_over_wrapper(void *game);
int get_score_wrapper(void *game);
int get_snake_length_wrapper(void *game);
void get_snake_positions_wrapper(void *game, int *positions);
void get_food_position_wrapper(void *game, int *position);

#endif // SNAKE_H