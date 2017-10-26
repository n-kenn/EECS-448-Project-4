from pygame import Surface, sprite


class Ground(sprite.Sprite):
    def __init__(self, size, color, screen_depth):
        super(Ground, self).__init__()
        self.image = Surface(size)
        self.rect = self.image.get_rect()#top = self.image.get_rect().bottom)
        self.rect = self.rect.move(0,screen_depth-self.rect.bottom)
        self.image.fill(color)

    def update(self):
        pass
