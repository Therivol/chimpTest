from Game import Game


if __name__ == "__main__":
    game = Game()

    while game.is_running:
        game.capture_input()
        game.update()
        game.draw()
