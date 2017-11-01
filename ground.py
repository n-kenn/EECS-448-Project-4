from pygame import sprite, Surface, mask


class Ground(sprite.Sprite):
    def __init__(self, size, color, (x_loc,y_loc)):
        super(Ground, self).__init__()
        self.image = Surface(size)
        self.mask = mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x_loc,y_loc)
        self.image.fill(color)

    def update(self):
        3
        # update mask to compensate for explosions occuring
        # may need to do layered updating later on
