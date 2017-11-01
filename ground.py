from pygame import sprite, Surface, mask


class Ground(sprite.Sprite):
    def __init__(self, size, color, (x_loc,y_loc)):
        super(Ground, self).__init__()
        self.image = Surface(size)
        self.rect = self.image.get_rect()#top = self.image.get_rect().bottom)
        self.rect = self.rect.move(x_loc,y_loc)
        self.image.fill(color)

    def update(self):
        # update mask to compensate for explosions occuring
        # may need to do layered updating later on
        self.mask = mask.from_surface(self.image)
