from random import randint

from pygame import mask
from pygame.draw import ellipse


class Ground(object):
    """The surface on which players can stand.

    :param image: Image to use.
    :param pos: Position of the ground.
    """

    def __init__(self, image, pos):
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
        self.start_locs = []
        self.make_holes(12, (128, 128))
        self.mask = mask.from_surface(self.image)

    def make_holes(self, count, size):
        for i in range(count):
            self.start_locs.append(ellipse(self.image, (0, 0, 0, 0), ((
                randint(0, self.rect.width), randint(0, self.rect.height)), size)).midbottom)

    def update(self):
        """Update mask to compensate for explosions occuring.
        """
        self.mask = mask.from_surface(self.image)
