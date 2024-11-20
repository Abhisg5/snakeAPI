#include "game.h"
#include <iostream>
#include <chrono>
#include <thread>

GameManager::GameManager(int width, int height, int screenWidth, int screenHeight)
    : game(width, height), renderer(screenWidth, screenHeight), running(true) {}

void GameManager::run() {
    std::cout << "Game started." << std::endl;

    while (running) {
        auto frameStart = std::chrono::high_resolution_clock::now();

        inputHandler.handleInput(game, running);
        game.update();

        if (game.isGameOver()) {
            running = false;
            std::cout << "Game Over! Score: " << game.getScore() << std::endl;
        }

        renderer.render(game);

        auto frameEnd = std::chrono::high_resolution_clock::now();
        auto frameDuration = std::chrono::duration_cast<std::chrono::milliseconds>(frameEnd - frameStart);
        if (frameDuration < std::chrono::milliseconds(100)) {
            std::this_thread::sleep_for(std::chrono::milliseconds(100) - frameDuration);
        }
    }

    std::cout << "Game loop exited." << std::endl;
}