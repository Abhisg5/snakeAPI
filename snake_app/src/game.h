#ifndef GAME_H
#define GAME_H

#include "snake.h"
#include "renderer.h"
#include "input_handler.h"
#include "sound_manager.h"

class GameManager {
public:
    GameManager(int width, int height, int screenWidth, int screenHeight);
    void run();

private:
    SnakeGame game;
    Renderer renderer;
    InputHandler inputHandler;
    SoundManager soundManager;
    bool running;
};

#endif