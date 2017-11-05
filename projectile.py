<<<<<<< HEAD
angle = math.radians(65)
power = 40
x_pos = 10
y_pos = height - 10
x_vel = power * math.cos(angle)
y_vel = -1 * power * math.sin(angle)


def update_pos(xp, yp, xv, yv):
    """Updates the position of a projectile.
    """
    if (xp + xv > width or xp + xv < 0):
        xv = 0  # (-1)*xv
    xp = xp + xv
    if (yp + yv > height or yp + yv < 0):
        yv = 0  # (-0.75)*yv
    yv = yv + 2
    yp = yp + yv

    return (int(xp), int(yp), xv, yv)
=======
from pygame import sprite, Surface
import math


class Projectile(sprite.Sprite):

    def __init__(self, color, player, gravity, ground_list):
        super(Projectile, self).__init__()
        self.angle = math.radians(player.get_angle())
        self.power = player.get_power()
        self.image = Surface((5,5))
        self.rect = self.image.get_rect()
        self.image.fill(color)
        self.gravity = gravity
        self.rect.move_ip(player.rect.center)
        self.x_vel = (self.power * math.cos(self.angle))
        self.y_vel = -1 * (self.power * math.sin(self.angle))
        self.ground_list = ground_list


    def proj_arc(self):
        self.y_vel = self.y_vel + self.gravity
        self.rect.move_ip(int(self.x_vel),int(self.y_vel))
        if (self.rect.x < 0 or self.rect.x > 1024 or self.rect.y > 512):
            self.kill()

    #def update(self):

        # if (self.rect.collidelist(self.ground_list) != -1):
        #     if(self.rect.collidelist(self.ground_list) == 2):
        #         print("Target hit")
        #     else:
        #         print ("You missed")
        #     self.kill()

        #
>>>>>>> WeaponImplementation
