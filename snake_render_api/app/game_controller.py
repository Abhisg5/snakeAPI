class GameController:
    def __init__(self, game):
        self.game = game

    def render(self):
        return self.game.renderGame()  # Use SnakeGame's render method

    def move_snake(self, direction):
        self.game.setDirection(direction.upper())
        self.game.moveSnake()

    def get_state(self):
        return {
            "score": self.game.getScore(),
            "is_game_over": self.game.isGameOver(),
            "rendered_state": self.render(),
        }