

class Scene:
    def __init__(self, name, game):
        self.name = name
        self.game = game
        self.window = game.window
        self.controller = game.controller
        self.scene_manager = game.scene_manager

    def update(self, delta_time):
        pass

    def draw(self, canvas):
        pass
