#include "snake.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define GRID_WIDTH 20
#define GRID_HEIGHT 20

// Debug logging
#define DEBUG_LOG(fmt, ...) printf("[DEBUG] " fmt "\n", ##__VA_ARGS__)

static void place_food(Game *game) {
  bool valid_position;
  do {
    valid_position = true;
    game->food.x = rand() % GRID_WIDTH;
    game->food.y = rand() % GRID_HEIGHT;

    // Check if food is not on snake
    for (int i = 0; i < game->length; i++) {
      if (game->segments[i].x == game->food.x &&
          game->segments[i].y == game->food.y) {
        valid_position = false;
        break;
      }
    }
  } while (!valid_position);
  DEBUG_LOG("Food placed at (%d, %d)", game->food.x, game->food.y);
}

static bool check_collision(const Game *game, int x, int y) {
  // Check wall collision
  if (x < 0 || x >= GRID_WIDTH || y < 0 || y >= GRID_HEIGHT) {
    DEBUG_LOG("Wall collision at (%d, %d)", x, y);
    return true;
  }

  // Check self collision
  for (int i = 0; i < game->length; i++) {
    if (game->segments[i].x == x && game->segments[i].y == y) {
      DEBUG_LOG("Self collision at (%d, %d)", x, y);
      return true;
    }
  }

  return false;
}

static Game *create_game_internal(void) {
  Game *game = (Game *)malloc(sizeof(Game));
  if (!game)
    return NULL;

  game->capacity = 10;
  game->segments = (Position *)malloc(sizeof(Position) * game->capacity);
  if (!game->segments) {
    free(game);
    return NULL;
  }

  // Initialize snake in center
  game->segments[0].x = GRID_WIDTH / 2;
  game->segments[0].y = GRID_HEIGHT / 2;
  game->length = 1;
  game->direction = RIGHT;
  game->score = 0;
  game->game_over = false;
  game->speed = 1.0f; // Default speed

  DEBUG_LOG("Game initialized. Snake at (%d, %d), direction: %d",
            game->segments[0].x, game->segments[0].y, game->direction);

  // Place initial food
  place_food(game);

  return game;
}

static void free_game_internal(Game *game) {
  if (game) {
    free(game->segments);
    free(game);
  }
}

static bool move_snake_internal(Game *game) {
  if (!game || game->game_over)
    return false;

  // Calculate new head position
  Position new_head = game->segments[0];
  switch (game->direction) {
  case UP:
    new_head.y--;
    break;
  case RIGHT:
    new_head.x++;
    break;
  case DOWN:
    new_head.y++;
    break;
  case LEFT:
    new_head.x--;
    break;
  }

  DEBUG_LOG(
      "Moving snake. Current head: (%d, %d), New head: (%d, %d), Direction: %d",
      game->segments[0].x, game->segments[0].y, new_head.x, new_head.y,
      game->direction);

  // Check for collisions
  if (check_collision(game, new_head.x, new_head.y)) {
    game->game_over = true;
    return false;
  }

  // Check for food collision
  bool food_eaten = (new_head.x == game->food.x && new_head.y == game->food.y);
  if (food_eaten) {
    DEBUG_LOG("Food eaten at (%d, %d)", new_head.x, new_head.y);
  }

  // Move snake
  if (food_eaten) {
    // Grow snake
    if (game->length >= game->capacity) {
      game->capacity *= 2;
      Position *new_segments =
          realloc(game->segments, sizeof(Position) * game->capacity);
      if (!new_segments) {
        game->game_over = true;
        return false;
      }
      game->segments = new_segments;
    }

    // Shift segments
    for (int i = game->length; i > 0; i--) {
      game->segments[i] = game->segments[i - 1];
    }
    game->length++;

    // Update score
    game->score += 10;

    // Place new food
    place_food(game);
  } else {
    // Shift segments
    for (int i = game->length - 1; i > 0; i--) {
      game->segments[i] = game->segments[i - 1];
    }
  }

  // Update head
  game->segments[0] = new_head;

  return food_eaten;
}

static void change_direction_internal(Game *game, Direction new_direction) {
  if (!game || game->game_over)
    return;

  // Prevent 180-degree turns
  if ((new_direction == UP && game->direction == DOWN) ||
      (new_direction == DOWN && game->direction == UP) ||
      (new_direction == LEFT && game->direction == RIGHT) ||
      (new_direction == RIGHT && game->direction == LEFT)) {
    DEBUG_LOG("Invalid direction change: %d -> %d", game->direction,
              new_direction);
    return;
  }

  game->direction = new_direction;
  DEBUG_LOG("Direction changed to %d", new_direction);
}

static bool is_game_over_internal(Game *game) {
  return game ? game->game_over : true;
}

static int get_score_internal(Game *game) { return game ? game->score : 0; }

static int get_snake_length_internal(Game *game) {
  return game ? game->length : 0;
}

static void get_snake_positions_internal(Game *game, Position *positions) {
  if (!game || !positions)
    return;

  for (int i = 0; i < game->length; i++) {
    positions[i] = game->segments[i];
  }
}

static void get_food_position_internal(Game *game, Position *position) {
  if (!game || !position)
    return;

  position[0] = game->food;
}

static Direction get_snake_direction_internal(Game *game) {
  return game ? game->direction : RIGHT;
}

static void get_game_state_internal(Game *game, int *snake_positions,
                                    int *snake_length, int *food_position,
                                    int *score, int *direction,
                                    bool *is_game_over) {
  if (!game || !snake_positions || !snake_length || !food_position || !score ||
      !direction || !is_game_over) {
    return;
  }

  // Copy snake positions
  for (int i = 0; i < game->length; i++) {
    snake_positions[i * 2] = game->segments[i].x;
    snake_positions[i * 2 + 1] = game->segments[i].y;
  }

  // Copy other state
  *snake_length = game->length;
  food_position[0] = game->food.x;
  food_position[1] = game->food.y;
  *score = game->score;
  *direction = game->direction;
  *is_game_over = game->game_over;
}

// Externally visible wrapper functions
void *create_game(void) { return (void *)create_game_internal(); }

__attribute__((visibility("default"))) void destroy_game(void *game) {
  free_game_internal((Game *)game);
}

bool move_snake(void *game) { return move_snake_internal((Game *)game); }

void change_direction(void *game, Direction new_direction) {
  change_direction_internal((Game *)game, new_direction);
}

bool is_game_over(void *game) { return is_game_over_internal((Game *)game); }

int get_score(void *game) { return get_score_internal((Game *)game); }

int get_snake_length(void *game) {
  return get_snake_length_internal((Game *)game);
}

void get_snake_positions(void *game, Position *positions) {
  get_snake_positions_internal((Game *)game, positions);
}

void get_food_position(void *game, Position *position) {
  get_food_position_internal((Game *)game, position);
}

void set_food_position(void *game, int x, int y) {
  Game *g = (Game *)game;
  g->food.x = x;
  g->food.y = y;
}

__attribute__((visibility("default"))) void reset_game(void *game_ptr) {
  Game *game = (Game *)game_ptr;
  if (!game)
    return;

  // Reset snake to initial position and length
  game->length = 1;
  game->segments[0].x = GRID_WIDTH / 2;
  game->segments[0].y = GRID_HEIGHT / 2;
  game->direction = RIGHT;
  game->score = 0;
  game->game_over = false;

  // Place new food
  place_food(game);
}

Direction get_snake_direction(void *game) {
  return get_snake_direction_internal((Game *)game);
}

__attribute__((visibility("default"))) void
get_game_state(void *game_ptr, int *snake_positions, int *snake_length,
               int *food_position, int *score, int *direction,
               bool *is_game_over) {
  get_game_state_internal((Game *)game_ptr, snake_positions, snake_length,
                          food_position, score, direction, is_game_over);
}

__attribute__((visibility("default"))) void set_game_speed(void *game_ptr,
                                                           float speed) {
  Game *game = (Game *)game_ptr;
  if (game) {
    game->speed = speed;
  }
}

__attribute__((visibility("default"))) float get_game_speed(void *game_ptr) {
  Game *game = (Game *)game_ptr;
  if (game) {
    return game->speed;
  }
  return 1.0f;
}