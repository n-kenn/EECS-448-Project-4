<<<<<<< HEAD
from pygame import draw, mask, sprite, Surface


class Explosive(sprite.Sprite):
    """ A class for any weapon that has the ability to explode.
    """

    def __init__(self, size, pos, color, groups):
        """Initialize the Explosive weapon.
       :param size: The size of the explosive weapon.
       :param pos: The position of the explosive weapon.
       :param color: The color of the explosive weapon.
        """
        super(Explosive, self).__init__(groups)
        self.image = Surface(size).convert_alpha()
        self.mask = mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=pos)
        self.image.fill(color)

    def collision_check(self, collidables):
        """ Looks to see if the explosive projectile has collided with anything.
            If it has, then remove the projectile, and draw an elipse to represent the blast
            of the explosion.
        """
=======
from pygame import sprite, Surface, draw, mask, Color
from projectile import Projectile

class Explosive(Projectile):
    # collidables is an iterable of sprites that the explosive can collide with
    def __init__(self, player, gravity, ground_list):
        super(Explosive, self).__init__(Color('red'),player, gravity, ground_list)
        self.mask = mask.from_surface(self.image)
        # collidables could shorten/lengthen dynamically, may use a sprite group later
        self.collidables = ground_list

    def collision_check(self):

>>>>>>> WeaponImplementation
        # this will probably get refactored somehow.
        for collidable in collidables:
            # check for rectangular collision
            if (self.rect.colliderect(collidable.rect) and collidable is not self):
                # then check for per pixel collision to make algorithm more efficient

                if (sprite.collide_mask(self, collidable) is not None):
                    self.kill()
                    # ellipse is relative to the Surface being drawn on
<<<<<<< HEAD
                    draw.ellipse(collidable.image, (0, 0, 0, 0), self.rect.inflate(map(
                        lambda x: x * 4, self.image.get_size())).move(0, self.image.get_rect().centery - collidable.rect.height))
                    break

    def update(self, world):
        """Update the explosive weapon.
        :param world: The world in which the explosive exists.
        """
        # move_ip overwrites the rect
        self.rect.move_ip((0, world.gravity))
        self.collision_check([world.ground])
=======
                    draw.ellipse(collidable.image, (255, 0, 0, 255), self.rect.inflate(
                        self.image.get_size()).move(0, -collidable.rect.height + self.image.get_rect().centery))
                    break


    def update(self):
        self.proj_arc()
        self.collision_check()
>>>>>>> WeaponImplementation
