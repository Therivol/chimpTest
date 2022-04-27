

class SceneStateMachine:
    def __init__(self):
        self.stack = []
        self.last_scene = None
        self.cur_scene = None

    def update(self, delta_time):
        self.cur_scene.update(delta_time)

    def draw(self, canvas):
        self.cur_scene.draw(canvas)

    def add(self, scene):
        self.stack.append(scene)
        self.cur_scene = scene

    def remove(self):
        self.stack.pop()
        self.cur_scene = self.stack[-1]

    def remove_all(self):
        while len(self.stack) > 1:
            self.remove()
