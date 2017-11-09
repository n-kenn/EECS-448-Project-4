from math import cos, sin

from pygame import mask, math

from animated_sprite import Animated_Sprite


class Projectile(Animated_Sprite):
    """A Projectile used for weapons.

    :param size: The size of the projectile.
    :param pos: The position to be made at.
    :param color: The color of the projectile.
    """

    def __init__(self, file_name, rect, frame_rate, angle, pos, power, groups):
        super(Projectile, self).__init__(
            file_name, rect, frame_rate, groups)

        self.animations = {
            'flying': self.sprite_sheet.load_strip(4, 0)
        }
        self.current_animation = self.animations['flying']
        self.image = self.current_animation[0]
        self.power = power
        self.mask = mask.from_surface(self.image)
        self.rect = self.image.get_rect(midbottom=pos)
        self.vel = math.Vector2(
            self.power * cos(angle), -self.power * sin(angle))

    def update(self, world):
        """Updates the projectile's position

        :param world: The world the projectile exists in.
        """
        super(Projectile, self).update()
        self.vel.y += world.gravity
        self.rect.move_ip(self.vel)
