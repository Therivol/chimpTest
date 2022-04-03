import sys
import pygame as p
from Window import Window
from SceneStateMachine import SceneStateMachine
from SceneMenu import SceneMenu
from Controller import Controller


class Game:
    def __init__(self):
        p.init()

        self.RES = (768, 448)
        self.window = Window(self.RES, "Chimp Test")
        self.controller = Controller()
        self.font = p.font.SysFont("Segoe UI", 48)

        self.scene_manager = SceneStateMachine()
        self.scene_manager.add(SceneMenu(self))
        # SceneGame(self.window, self.controller, (12, 7))

        self.is_running = True

    def capture_input(self):
        for ev in p.event.get():
            if ev.type == p.QUIT:
                self.is_running = False
                p.quit()
                sys.exit()

            if ev.type == p.KEYDOWN:
                self.controller.set_key(ev.key)

            if ev.type == p.KEYUP:
                self.controller.reset_key(ev.key)

            if ev.type == p.MOUSEBUTTONDOWN or p.MOUSEBUTTONUP:
                self.controller.set_buttons()

    def update(self):
        self.scene_manager.update(0)

    def draw(self):
        self.window.canvas.fill((125, 125, 150))

        self.scene_manager.draw(self.window.canvas)

        self.window.window.blit(p.transform.scale(self.window.canvas, self.window.window.get_size()), (0, 0))
        p.display.update()
