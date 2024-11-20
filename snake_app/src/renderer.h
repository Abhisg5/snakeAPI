#ifndef RENDERER_H
#define RENDERER_H

#include "snake.h"
#include <SDL2/SDL.h>

class Renderer {
public:
    Renderer(int screenWidth, int screenHeight);
    ~Renderer();

    void render(const SnakeGame& game);
    void clearScreen();

private:
    SDL_Window* window;
    SDL_Renderer* renderer;
    int screenWidth, screenHeight;
};

#endif