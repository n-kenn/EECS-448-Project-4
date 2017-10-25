from pygame import sprite, Surface
import math

class Projectile(sprite.Sprite):

    def __init__(self, player, gravity):
        super(Projectile, self).__init__()
        self.angle = player.get_angle()
        self.power = player.get_power()
        (self.x_pos,self.y_pos,temp, temp2) =player.rect

        self.image = Surface((5,5))
        self.rect = self.image.get_rect()
        self.image.fill((123,53,164))
        self.gravity = gravity
        self.rect = self.rect.move(self.x_pos,self.y_pos)


        self.x_vel = self.power * math.cos(self.angle)
        self.y_vel = -1 * self.power * math.sin(self.angle)
        print((self.x_pos,self.y_pos,self.x_vel,self.y_vel))

    def update(self):
        if (self.x_pos + self.x_vel > 1024 or self.x_pos + self.x_vel < 0):
            self.kill
        if (self.y_pos + self.y_vel > 512 or self.y_pos + self.y_vel < 0):
            self.kill
        self.y_vel = self.y_vel + self.gravity
        self.rect = self.rect.move(int(self.x_vel),int(self.y_vel))
