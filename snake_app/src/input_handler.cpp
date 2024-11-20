#include "input_handler.h"
#include <iostream>

void InputHandler::handleInput(SnakeGame& game, bool& running) {
    SDL_Event event;
    while (SDL_PollEvent(&event)) {
        if (event.type == SDL_QUIT) {
            running = false;
            std::cout << "Quit event received. Exiting game loop." << std::endl;
            return;
        }
        if (event.type == SDL_KEYDOWN) {
            switch (event.key.keysym.sym) {
                case SDLK_UP:
                    game.setDirection("UP");
                    break;
                case SDLK_DOWN:
                    game.setDirection("DOWN");
                    break;
                case SDLK_LEFT:
                    game.setDirection("LEFT");
                    break;
                case SDLK_RIGHT:
                    game.setDirection("RIGHT");
                    break;
                case SDLK_ESCAPE:
                    running = false;
                    std::cout << "Escape key pressed. Exiting game loop." << std::endl;
                    break;
                default:
                    std::cout << "Unhandled key press: " << event.key.keysym.sym << std::endl;
                    break;
            }
        }
    }
}