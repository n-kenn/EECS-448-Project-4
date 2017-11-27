from math import cos, sin

from pygame import mask
from pygame.math import Vector2

from animated_sprite import Animated_Sprite


class Projectile(Animated_Sprite):
    """A Projectile used for weapons.

    :param anim: A list of surface images.
    :param start_pos: The starting position for the projectile.
    :param angle: Used to set the initial velocity.
    """

    def __init__(self, anim, start_pos, angle):
        super(Projectile, self).__init__(None, 5)
        self.curr_anim = anim
        self.image = self.curr_anim.next()
        self.mask = mask.from_surface(self.image)
        self.rect = self.image.get_rect(midbottom=start_pos)
        self.vel = -20 * Vector2(cos(angle), sin(angle))

    def update(self, world):
        """Updates the projectile's position

        :param world: The world the projectile exists in.
        """
        super(Projectile, self).update()
        self.vel.y += world.gravity
        self.rect.move_ip(self.vel)
        if not world.rect.contains(self.rect):
            self.kill()
