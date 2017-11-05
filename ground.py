from pygame import mask, sprite


class Ground(sprite.Sprite):
    """ The surface on which players can stand.
    :param Sprite: The reference of the sprite.
    """

    def __init__(self, image, pos):
        """ Initializes the Ground.
        :param image: Image to use.
        :param pos: Position of the ground.
        """
        super(Ground, self).__init__()
        self.image = image
        self.mask = mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=pos)

    def update(self):
        """ Update mask to compensate for explosions occuring.
        """
        self.mask = mask.from_surface(self.image)
