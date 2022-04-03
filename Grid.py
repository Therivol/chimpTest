import pygame as p


class Tile:
    def __init__(self, loc, size):
        self.loc = loc
        true_loc = (loc[0] * size, loc[1] * size)
        self.rect = p.Rect(true_loc, (size, size))

    def is_pos_in(self, pos):
        return self.rect.collidepoint(pos)


class Grid:
    def __init__(self, size, tile_size):
        self.grid = []
        self.size = size
        self.tile_size = tile_size

        for row in range(self.size[1]):
            new_row = []
            for tile in range(self.size[0]):
                new_row.append(Tile((tile, row), self.tile_size))

            self.grid.append(new_row)

        print(self.grid)

    def draw(self, canvas):
        for row in self.grid:
            for tile in row:
                p.draw.rect(canvas, (0, 0, 0), tile.rect, 1)

    def get_tile_from_pos(self, pos):
        for row in self.grid:
            for tile in row:
                if tile.is_pos_in(pos):
                    return tile