from pygame import mask, sprite, Surface


class Ground(sprite.Sprite):
    def __init__(self, size, pos, color):
        super(Ground, self).__init__()
        self.image = Surface(size).convert_alpha()
        self.mask = mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=pos)
        self.image.fill(color)

    def update(self, gravity):
        # update mask to compensate for explosions occuring
        # may need to do layered updating later on
        self.mask = mask.from_surface(self.image)
