import pygame as p
from Scene import Scene
from SceneGame import SceneGame


class SceneMenu(Scene):

    def __init__(self, game):
        super().__init__("Menu", game)

        self.font = p.font.SysFont("Segou UI", 64)

        self.play_button = p.Rect((0, 0), (300, 100))
        self.play_button.center = self.window.canvas.get_width() / 2, self.window.canvas.get_height() / 2
        self.highlighted = False

    def update(self, delta_time):
        if self.play_button.collidepoint(self.window.get_mouse_pos()):
            self.highlighted = True
            if self.controller.get_button_down("1"):
                self.scene_manager.add(SceneGame(self.game, (12, 7)))
        else:
            self.highlighted = False

    def draw(self, canvas):
        if self.highlighted:
            color = (150, 150, 150)
        else:
            color = (100, 100, 100)
        p.draw.rect(canvas, color, self.play_button)

        play_text = self.font.render("Play", True, (0, 0, 0))
        canvas.blit(play_text, self.play_button.topleft)
