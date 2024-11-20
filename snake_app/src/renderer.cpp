#include "renderer.h"
#include <iostream>

Renderer::Renderer(int screenWidth, int screenHeight)
    : screenWidth(screenWidth), screenHeight(screenHeight) {
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        std::cerr << "Failed to initialize SDL: " << SDL_GetError() << std::endl;
        exit(1);
    }
    window = SDL_CreateWindow("Modern Snake Game", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, screenWidth, screenHeight, SDL_WINDOW_SHOWN);
    if (!window) {
        std::cerr << "Failed to create SDL window: " << SDL_GetError() << std::endl;
        SDL_Quit();
        exit(1);
    }
    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    if (!renderer) {
        std::cerr << "Failed to create SDL renderer: " << SDL_GetError() << std::endl;
        SDL_DestroyWindow(window);
        SDL_Quit();
        exit(1);
    }
    std::cout << "Renderer initialized successfully." << std::endl;
}

Renderer::~Renderer() {
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
    std::cout << "Renderer cleaned up successfully." << std::endl;
}

void Renderer::render(const SnakeGame& game) {
    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255); // Black background
    SDL_RenderClear(renderer);

    SDL_SetRenderDrawColor(renderer, 0, 255, 0, 255); // Snake color
    for (const auto& part : game.getSnake()) {
        SDL_Rect rect = {part.second * 20, part.first * 20, 20, 20};
        SDL_RenderFillRect(renderer, &rect);
    }

    SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255); // Food color
    auto food = game.getFood();
    SDL_Rect rect = {food.second * 20, food.first * 20, 20, 20};
    SDL_RenderFillRect(renderer, &rect);

    SDL_RenderPresent(renderer);
    std::cout << "Frame rendered." << std::endl;
}