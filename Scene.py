

class Scene:
    def __init__(self, name, game):
        self.name = name
        self.game = game
        self.window = game.window
        self.controller = game.controller
        self.scene_manager = game.scene_manager

    def on_destroy(self):
        pass

    def on_activate(self):
        pass

    def early_update(self, delta_time):
        pass

    def update(self, delta_time):
        pass

    def late_update(self, delta_time):
        pass

    def draw(self, canvas):
        pass
