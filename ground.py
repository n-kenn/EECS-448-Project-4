from pygame import image, mask, sprite


class Ground(sprite.Sprite):
    def __init__(self, file_name, pos, color):
        super(Ground, self).__init__()
        self.image = image.load(file_name)
        self.mask = mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=pos)

    def update(self):
        # update mask to compensate for explosions occuring
        # may need to do layered updating later on
        self.mask = mask.from_surface(self.image)
