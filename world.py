from pygame import sprite

from ground import Ground


class World(sprite.Sprite):
    """The world in the game.

    :param background_image: Surface image used for the background.
    :param ground_image: Surface image used for the ground.
    :param gravity: The gravity in the world.
    """

    def __init__(self, background_image, ground_image, gravity):
        super(World, self).__init__()
        self.background = background_image
        self.image = self.background.copy()
        self.rect = self.image.get_rect()
        self.ground = Ground(ground_image, self.rect.midleft)
        self.gravity = gravity
        self.start_positions = [
            self.ground.rect.topleft, self.ground.rect.topright]

    def update(self):
        """Updates the World
        """
        self.image = self.background.copy()
        self.image.blit(self.ground.image, self.rect.midleft)
