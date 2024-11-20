#include "snake.h"
#include <random>
#include <algorithm>
#include <iostream>
#include <sstream>

SnakeGame::SnakeGame(int width, int height)
    : width(width), height(height), score(0), level(1), gameOver(false), currentDirection("RIGHT") {
    snake.push_back({height / 2, width / 2});
    placeFood();
    std::cout << "SnakeGame initialized with dimensions: " << width << "x" << height << std::endl;
}

void SnakeGame::update() {
    if (gameOver) {
        std::cout << "Game over. Update called after game ended." << std::endl;
        return;
    }
    moveSnake();
    checkCollisions();
}

void SnakeGame::setDirection(const std::string& direction) {
    std::cout << "Direction set to: " << direction << std::endl;
    if ((direction == "UP" && currentDirection != "DOWN") ||
        (direction == "DOWN" && currentDirection != "UP") ||
        (direction == "LEFT" && currentDirection != "RIGHT") ||
        (direction == "RIGHT" && currentDirection != "LEFT")) {
        currentDirection = direction;
    } else {
        std::cout << "Invalid direction change ignored: " << direction << std::endl;
    }
}

void SnakeGame::moveSnake() {
    auto head = snake.front();

    // Move the snake's head based on the current direction
    if (currentDirection == "UP") head.first--;
    if (currentDirection == "DOWN") head.first++;
    if (currentDirection == "LEFT") head.second--;
    if (currentDirection == "RIGHT") head.second++;

    // Wrap around the screen
    if (head.first < 0) head.first = height - 1;  // Top to bottom
    if (head.first >= height) head.first = 0;    // Bottom to top
    if (head.second < 0) head.second = width - 1; // Left to right
    if (head.second >= width) head.second = 0;   // Right to left

    snake.insert(snake.begin(), head);
    std::cout << "Snake moved to: " << head.first << ", " << head.second << std::endl;

    // Check if the snake eats food
    if (head == food) {
        score += 10;
        placeFood();
        std::cout << "Food eaten! Score: " << score << std::endl;
    } else {
        snake.pop_back(); // Remove the tail if food is not eaten
    }
}

void SnakeGame::checkCollisions() {
    auto head = snake.front();
    if (head.first < 0 || head.second < 0 || head.first >= height || head.second >= width) {
        std::cout << "Collision with wall detected. Game over." << std::endl;
        gameOver = true;
    }
    if (std::count(snake.begin(), snake.end(), head) > 1) {
        std::cout << "Self-collision detected. Game over." << std::endl;
        gameOver = true;
    }
}

std::string SnakeGame::renderGame() {
    std::ostringstream oss;
    std::vector<std::string> board(height, std::string(width, ' '));

    // Place snake on the board
    for (const auto& part : snake) {
        board[part.first][part.second] = 'O';
    }

    // Place food on the board
    board[food.first][food.second] = 'X';

    // Convert board to a string
    for (const auto& row : board) {
        oss << row << "\n";
    }

    return oss.str();
}

void SnakeGame::placeFood() {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> disX(0, width - 1);
    std::uniform_int_distribution<> disY(0, height - 1);

    do {
        food = {disY(gen), disX(gen)};
    } while (std::find(snake.begin(), snake.end(), food) != snake.end());
    std::cout << "Food placed at: " << food.first << ", " << food.second << std::endl;
}

std::string SnakeGame::render() {
    std::ostringstream oss;
    oss << "Score: " << score << " | Level: " << level << "\n";

    std::vector<std::string> board(height, std::string(width, ' '));
    for (const auto& part : snake) board[part.first][part.second] = 'O';
    board[food.first][food.second] = 'X';

    for (const auto& row : board) oss << row << "\n";
    return oss.str();
}

bool SnakeGame::isGameOver() const { return gameOver; }
int SnakeGame::getScore() const { return score; }
int SnakeGame::getLevel() const { return level; }

const std::vector<std::pair<int, int>>& SnakeGame::getSnake() const { return snake; }
const std::pair<int, int>& SnakeGame::getFood() const { return food; }
const std::vector<std::pair<int, int>>& SnakeGame::getObstacles() const { return obstacles; }