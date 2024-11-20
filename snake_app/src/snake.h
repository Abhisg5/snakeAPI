#ifndef SNAKE_H
#define SNAKE_H

#include <vector>
#include <string>
#include <utility>

class SnakeGame {
public:
    SnakeGame(int width, int height);
    void update();
    void setDirection(const std::string& direction);
    std::string render(); // ASCII rendering for fallback
    bool isGameOver() const;
    int getScore() const;
    int getLevel() const;
    std::string renderGame(); // ASCII rendering

    // Getters for rendering
    const std::vector<std::pair<int, int>>& getSnake() const;
    const std::pair<int, int>& getFood() const;
    const std::vector<std::pair<int, int>>& getObstacles() const;

private:
    int width, height;
    int score, level;
    std::string currentDirection;
    bool gameOver;
    std::vector<std::pair<int, int>> snake;
    std::pair<int, int> food;
    std::vector<std::pair<int, int>> obstacles;

    void moveSnake();
    void placeFood();
    void checkCollisions();
};

#endif