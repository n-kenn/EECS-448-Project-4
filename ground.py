from pygame import sprite, Surface, mask


class Ground(sprite.Sprite):
    def __init__(self, size, pos, color):
        super(Ground, self).__init__()
        self.image = Surface(size).convert_alpha()
        self.mask = mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=pos)
        self.image.fill(color)

    def update(self):
        pass
