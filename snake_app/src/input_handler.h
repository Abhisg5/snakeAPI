#ifndef INPUT_HANDLER_H
#define INPUT_HANDLER_H

#include "snake.h"
#include <SDL2/SDL.h>

class InputHandler {
public:
    void handleInput(SnakeGame& game, bool& running);
};

#endif