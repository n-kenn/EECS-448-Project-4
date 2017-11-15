from pygame import sprite

from ground import Ground


class World(sprite.Sprite):
    """The world in the game.

    :param background: Surface image used for the background.
    :param ground: Surface image used for the ground.
    :param gravity: The gravity in the world.
    """

    def __init__(self, background, ground, gravity=1):
        super(World, self).__init__()
        self.background = background
        self.image = self.background.copy()
        self.rect = self.image.get_rect()
        self.ground = Ground(ground, self.rect.midleft)
        self.gravity = gravity
        self.start_locs = [self.ground.rect.topleft, self.ground.rect.topright]

    def update(self):
        """Updates the World
        """
        self.image = self.background.copy()
        self.image.blit(self.ground.image, self.rect.midleft)
