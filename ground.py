from pygame import mask


class Ground(object):
    """The surface on which players can stand.

    :param image: Image to use.
    :param pos: Position of the ground.
    """

    def __init__(self, image, pos):
        self.image = image
        self.mask = mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=pos)

    def update(self):
        """Update mask to compensate for explosions occuring.
        """
        self.mask = mask.from_surface(self.image)
