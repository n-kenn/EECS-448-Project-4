from pygame import Surface, sprite, mouse


class Ground(sprite.Sprite):
    def __init__(self, (width, height), color):
        super(Ground, self).__init__()
        self.image = Surface((width, height))
        self.image.fill(color)

    def update(self):
        # this is where collision detection will go
        print 'in' if self.image.get_rect().collidepoint(mouse.get_pos()) else 'out'
