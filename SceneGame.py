import pygame as p
from Scene import Scene
from Grid import Grid
import random
from SceneEnd import SceneEnd


class SceneGame(Scene):

    def __init__(self, game):
        super().__init__("Game", game)

        self.grid_size = (12, 7)
        self.tile_size = self.window.RES[0] / self.grid_size[0]

        self.grid = Grid(self.grid_size, self.tile_size)

        self.font = p.font.SysFont("Segoe UI", 48)

        self.sequence_number = 0
        self.round = 4
        self.started = False
        self.hidden = True

        self.game_tiles = {}
        self.generate_tile_locations(self.round)

    def generate_tile_locations(self, level):
        self.game_tiles.clear()
        self.started = False
        self.hidden = True
        self.sequence_number = 0

        if level == 4:
            self.hidden = False

        new_tile_loc = []

        for i in range(level):
            while True:
                x = random.randint(0, self.grid_size[0] - 1)
                y = random.randint(0, self.grid_size[1] - 1)
                if not (x, y) in new_tile_loc:
                    new_tile_loc.append((x, y))
                    break

            self.game_tiles[self.grid.grid[y][x]] = GameTile(i, (x, y), self)

    def on_destroy(self):
        pass

    def on_activate(self):
        pass

    def early_update(self, delta_time):
        pass

    def update(self, delta_time):
        if self.controller.get_button_down("1"):
            tile = self.grid.get_tile_from_pos(self.window.get_mouse_pos())
            if tile in self.game_tiles:
                self.click_game_tile(tile)

    def click_game_tile(self, tile):
        self.started = True
        if self.game_tiles[tile].hidden:
            return
        if self.game_tiles[tile].number == self.sequence_number:
            self.sequence_number += 1
            self.game_tiles[tile].hidden = True
            if self.sequence_number == self.round:
                self.round += 1
                self.generate_tile_locations(self.round)
        else:
            self.end()

    def end(self):
        self.scene_manager.add(SceneEnd(self.game, self.round))

    def late_update(self, delta_time):
        pass

    def draw(self, canvas):

        # self.grid.draw(self.window.canvas)
        for tile in self.game_tiles.keys():
            self.game_tiles[tile].draw(self.window.canvas, tile.rect)


class GameTile:
    def __init__(self, number, loc, game):
        self.number = number
        self.loc = loc
        self.game = game
        self.hidden = False
        self.text = game.font.render(str(self.number + 1), True, (0, 0, 0))

    def draw(self, canvas, rect):
        if self.hidden:
            return
        tile = self.game.grid.get_tile_from_pos(self.game.window.get_mouse_pos())
        if tile:
            if tile.loc == self.loc:
                p.draw.rect(canvas, (230, 230, 230), rect)
            else:
                p.draw.rect(canvas, (180, 180, 180), rect)
        p.draw.rect(canvas, (0, 0, 0), rect, 2)
        if not self.game.started or not self.game.hidden:
            canvas.blit(self.text, rect.topleft)
