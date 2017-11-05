from pygame import sprite, Surface, math, mask
from math import cos, sin


class Projectile(sprite.Sprite):

    def __init__(self, size, pos, color, groups):
        super(Projectile, self).__init__(groups)
        self.angle = 0
        self.power = 10
        self.image = Surface(size).convert_alpha()
        self.image.fill(color)
        self.mask = mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=pos)
        self.vel = math.Vector2(self.power * cos(self.angle), -
                                self.power * sin(self.angle))

    def proj_arc(self):
        self.vel = self.y_vel + self.gravity
        self.rect.move_ip(int(self.x_vel), int(self.y_vel))
        if (self.rect.x < 0 or self.rect.x > 1024 or self.rect.y > 512):
            self.kill()
