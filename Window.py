import pygame as p


class Window:
    def __init__(self, size, title):

        self.RES = size
        self.canvas = p.Surface(size)
        self.window = p.display.set_mode(size)
        p.display.set_caption(title)

    def get_mouse_pos(self):
        aspect_ratio = self.canvas.get_width() / self.window.get_width()
        mouse_original = p.mouse.get_pos()
        new_pos = (mouse_original[0] * aspect_ratio,
                   mouse_original[1] * aspect_ratio)

        return new_pos
