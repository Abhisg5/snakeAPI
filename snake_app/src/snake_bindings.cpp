#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "snake.h"

namespace py = pybind11;

PYBIND11_MODULE(snake_game, m) {
    py::class_<SnakeGame>(m, "SnakeGame")
        .def(py::init<int, int>())
        .def("update", &SnakeGame::update)
        .def("setDirection", &SnakeGame::setDirection)
        .def("renderGame", &SnakeGame::renderGame)
        .def("isGameOver", &SnakeGame::isGameOver)
        .def("getScore", &SnakeGame::getScore)
        .def("getSnake", &SnakeGame::getSnake)
        .def("getFood", &SnakeGame::getFood);
}