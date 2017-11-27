from itertools import cycle
from operator import add

from pygame import sprite

from ground import Ground


class World(sprite.Sprite):
    """The world in the game.

    :param images: Contains images use for ground and background.
    :param gravity: The gravity in the world.
    """

    def __init__(self, images, gravity=1):
        super(World, self).__init__()
        self.background = images['sky']
        self.image = self.background.copy()
        self.scroll = cycle(range(self.background.get_width()))
        self.rect = self.image.get_rect()
        self.ground = Ground(images['ground'], self.rect.midleft)
        self.gravity = gravity
        self.start_locs = [tuple(map(add, (0, self.ground.rect.height), loc))
                           for loc in self.ground.start_locs]

    def draw(self, display):
        """Draws self.image onto the surface.

        :param display: The size of the window.
        """
        display.blit(self.image, (0, 0))

    def update(self):
        """Resets the image and blits any changes to the ground to the image.
        """
        offset = self.scroll.next()
        self.image.blit(self.background, (offset, 0))
        self.image.blit(self.background,
                        (offset - self.background.get_width(), 0))
        self.image.blit(self.ground.image, self.rect.midleft)
