from itertools import cycle
from math import cos, sin

from pygame import mask, math

from animated_sprite import Animated_Sprite


class Projectile(Animated_Sprite):
    """A Projectile used for weapons.

    :param strip: A list of surface images.
    :param start_pos: The starting position for the projectile.
    :param angle: Used to set the initial velocity.
    :param power: Used to set the initial velocity.
    :param groups: Groups to add the sprite to.
    """

    def __init__(self, strip, start_pos, angle, power, groups):
        super(Projectile, self).__init__(10, groups)
        self.current_animation = cycle(strip)
        self.image = self.current_animation.next()
        self.mask = mask.from_surface(self.image)
        self.rect = self.image.get_rect(midbottom=start_pos)
        self.vel = math.Vector2(power * cos(angle), -power * sin(angle))

    def update(self, world):
        """Updates the projectile's position

        :param world: The world the projectile exists in.
        """
        super(Projectile, self).update()
        self.vel.y += world.gravity
        self.rect.move_ip(self.vel)
