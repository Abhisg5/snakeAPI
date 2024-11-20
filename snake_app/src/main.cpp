#include "game.h"

int main() {
    GameManager gameManager(20, 20, 600, 600);
    gameManager.run();

    return 0;
}