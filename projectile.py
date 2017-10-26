from pygame import sprite, Surface
import math

class Projectile(sprite.Sprite):

    def __init__(self, player, gravity):
        super(Projectile, self).__init__()
        self.angle = math.radians(player.get_angle())
        self.power = player.get_power()
        (self.x_pos,self.y_pos,_,_) =player.rect
        self.image = Surface((5,5))
        self.rect = self.image.get_rect()
        self.image.fill((123,53,164))
        self.gravity = gravity
        self.rect = self.rect.move(self.x_pos,self.y_pos)
        self.x_vel = self.power * math.cos(self.angle)
        self.y_vel = -1 * self.power * math.sin(self.angle)


    def update(self):
        self.y_vel = self.y_vel + self.gravity
        self.rect = self.rect.move(int(self.x_vel),int(self.y_vel))
        if (self.rect.x < 0 or self.rect.x > 1024 or self.rect.y > 512):
            self.kill()

    def __del__(self):
        print("buh-bye")
