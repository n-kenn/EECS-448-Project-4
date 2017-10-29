from pygame import sprite, Surface


class Ground(sprite.Sprite):
    def __init__(self, size, pos, color, color_key):
        super(Ground, self).__init__()
        self.image = Surface(size).convert()
        self.rect = self.image.get_rect(topleft=pos)
        self.image.fill(color)
        # color_key will be used in explosion handling
        self.color_key = color_key
        self.image.set_colorkey(self.color_key)

    def update(self):
        pass
