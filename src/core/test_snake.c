#include "snake.h"
#include <CUnit/Basic.h>
#include <CUnit/CUnit.h>

// Test fixtures
static Game *game;

// Setup and teardown
static int init_suite(void) {
  game = create_game();
  return (game != NULL) ? 0 : -1;
}

static int clean_suite(void) {
  destroy_game(game);
  return 0;
}

// Test cases
static void test_initial_state(void) {
  CU_ASSERT_EQUAL(get_score(game), 0);
  CU_ASSERT_EQUAL(get_snake_length(game), 1);
  CU_ASSERT_FALSE(is_game_over(game));
}

static void test_movement(void) {
  Position initial_pos;
  get_snake_positions(game, &initial_pos);

  move_snake(game);

  Position new_pos;
  get_snake_positions(game, &new_pos);
  // Only one coordinate should change
  CU_ASSERT((initial_pos.x != new_pos.x) || (initial_pos.y != new_pos.y));
}

static void test_direction_change(void) {
  // Test each direction
  const Direction directions[] = {UP, RIGHT, DOWN, LEFT};
  for (int i = 0; i < 4; i++) {
    change_direction(game, directions[i]);
    Position pos1;
    get_snake_positions(game, &pos1);

    move_snake(game);

    Position pos2;
    get_snake_positions(game, &pos2);
    // Only one coordinate should change
    CU_ASSERT((pos1.x != pos2.x) || (pos1.y != pos2.y));
  }
}

static void test_food_collision(void) {
  int initial_score = get_score(game);
  int initial_length = get_snake_length(game);

  // Place food directly in front of the snake
  Position head;
  get_snake_positions(game, &head);
  Position food = head;
  switch (game->direction) {
  case UP:
    food.y--;
    break;
  case RIGHT:
    food.x++;
    break;
  case DOWN:
    food.y++;
    break;
  case LEFT:
    food.x--;
    break;
  }
  set_food_position(game, food.x, food.y);

  move_snake(game);

  CU_ASSERT(get_score(game) > initial_score ||
            get_snake_length(game) > initial_length);
}

static void test_game_over(void) {
  // Move snake into wall to trigger game over
  for (int i = 0; i < 20; i++) {
    move_snake(game);
  }

  CU_ASSERT_TRUE(is_game_over(game));
}

static void test_boundaries(void) {
  // Test that snake stays within grid boundaries until game over
  for (int i = 0; i < 100; i++) {
    if (is_game_over(game))
      break;
    move_snake(game);
    Position pos;
    get_snake_positions(game, &pos);

    CU_ASSERT(pos.x >= 0 && pos.x < GRID_WIDTH);
    CU_ASSERT(pos.y >= 0 && pos.y < GRID_HEIGHT);
  }
  CU_ASSERT_TRUE(is_game_over(game)); // Optionally assert that the game ends
}

// Test registry
int main(void) {
  CU_pSuite pSuite = NULL;

  // Initialize CUnit test registry
  if (CUE_SUCCESS != CU_initialize_registry())
    return CU_get_error();

  // Add a suite to the registry
  pSuite = CU_add_suite("Snake Game Suite", init_suite, clean_suite);
  if (NULL == pSuite) {
    CU_cleanup_registry();
    return CU_get_error();
  }

  // Add tests to the suite
  if ((NULL == CU_add_test(pSuite, "test initial state", test_initial_state)) ||
      (NULL == CU_add_test(pSuite, "test movement", test_movement)) ||
      (NULL ==
       CU_add_test(pSuite, "test direction change", test_direction_change)) ||
      (NULL ==
       CU_add_test(pSuite, "test food collision", test_food_collision)) ||
      (NULL == CU_add_test(pSuite, "test game over", test_game_over)) ||
      (NULL == CU_add_test(pSuite, "test boundaries", test_boundaries))) {
    CU_cleanup_registry();
    return CU_get_error();
  }

  // Run all tests using the CUnit Basic interface
  CU_basic_set_mode(CU_BRM_VERBOSE);
  CU_basic_run_tests();
  CU_cleanup_registry();

  return CU_get_error();
}