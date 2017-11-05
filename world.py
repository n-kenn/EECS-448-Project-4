from pygame import sprite


class World(sprite.Sprite):
    def __init__(self, background, ground, gravity):
        super(World, self).__init__()
        self.background = background
        self.image = self.background.copy()
        self.rect = self.image.get_rect()
        self.ground = ground
        self.gravity = gravity

    def update(self):
        self.ground.update()
        self.image = self.background.copy()
        self.image.blit(self.ground.image, self.rect.midleft)
