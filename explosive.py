from pygame import draw, mask, sprite, Surface


class Explosive(sprite.Sprite):
    """ A class for any weapon that has the ability to explode.
    """
    # collidables is an iterable of sprites that the explosive can collide with
    def __init__(self, size, pos, color, collidables):
        """Initialize the Explosive weapon.
       :param size: The size of the explosive weapon.
       :param pos: The position of the explosive weapon.
       :param color: The color of the explosive weapon.
       :param collidables: The objects that an explosion can collide with.
        """
        super(Explosive, self).__init__()
        self.image = Surface(size).convert_alpha()
        self.mask = mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=pos)
        self.image.fill(color)
        # collidables could shorten/lengthen dynamically, may use a sprite group later
        self.collidables = collidables

    def collision_check(self):
        """ Looks to see if the explosive projectile has collided with anything.
            If it has, then remove the projectile, and draw an elipse to represent the blast
            of the explosion.
        """
        # this will probably get refactored somehow.
        for collidable in self.collidables:
            # check for rectangular collision
            if self.rect.colliderect(collidable.rect):
                # then check for per pixel collision to make algorithm more efficient
                if sprite.collide_mask(self, collidable):
                    self.kill()
                    # ellipse is relative to the Surface being drawn on
                    draw.ellipse(collidable.image, (0, 0, 0, 0), self.rect.inflate(
                        self.image.get_size()).move(0, -collidable.rect.height + self.image.get_rect().centery))
                    break

    def update(self, world):
        """Update the explosive weapon.
        :param world: The world in which the explosive exists.
        """
        # move_ip overwrites the rect
        self.rect.move_ip((0, world['gravity']))
        self.collision_check()
