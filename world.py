from pygame import sprite


class World(sprite.Sprite):
    def __init__(self, image_file, ground, gravity):
        super(World, self).__init__()
        self.image = image_file
        self.rect = self.image.get_rect()
        self.ground = ground
        self.gravity = gravity
