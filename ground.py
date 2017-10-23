from pygame import Surface

class Ground(Surface):
    def __init__(self, (width, height), color):
        super(Ground, self).__init__((width, height))
        self.fill(color)
