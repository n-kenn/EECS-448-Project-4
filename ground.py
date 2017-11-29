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
        self.make_holes(24, (128, 128))
        self.mask = mask.from_surface(self.image)

    def make_holes(self, count, size):
        """Called once in the constructor to make the ground more dynamic and get the players' starting locations.

        :param count: How many holes to make.
        :param size: The size of the holes.
        """
        for i in range(count):
            self.start_locs.append(ellipse(self.image, (0, 0, 0, 0), ((
                randint(0, self.rect.width), randint(-size[0], self.rect.height - size[0])), size)).midbottom)

    def update(self):
        """Update mask to compensate for explosions occuring.
        """
        self.mask = mask.from_surface(self.image)
