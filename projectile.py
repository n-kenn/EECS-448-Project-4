from pygame import sprite, Surface, math, mask
from math import cos, sin


class Projectile(sprite.Sprite):
    def __init__(self, size, angle, pos, color, groups, power):
        super(Projectile, self).__init__(groups)
        self.power = power
        self.image = Surface(size).convert_alpha()
        self.image.fill(color)
        self.mask = mask.from_surface(self.image)
        self.rect = self.image.get_rect(midbottom=pos)
        self.vel = math.Vector2(
            self.power * cos(angle), -self.power * sin(angle))

    def update(self, world):
        """Updates the projectile's position

        :param world: The world the projectile exists in.
        """
        self.vel.y += world.gravity
        self.rect.move_ip(self.vel)
