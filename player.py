from pygame import sprite, Surface
import math
from projectile import Projectile

class Player(sprite.Sprite):

    def __init__(self, size, start_pos, color, gravity, ground_list):
        super(Player, self).__init__()
        self.image = Surface(size)
        self.rect = self.image.get_rect(bottom=start_pos)
        self.image.fill(color)
        self.in_air = True
        self.angle = 0
        self.power = 0
        self.gravity = gravity
        self.ground_list = ground_list

    def player_move(self, x, y):
        self.rect = self.rect.move(x, y)

    def update(self):
        pass

    def land(self):
        self.in_air = False

    def get_angle(self):
        return self.angle

    def get_power(self):
        return self.power

    def set_angle(self, (x_dist,y_dist)):
        self.angle = math.degrees(math.atan2(y_dist,x_dist))

    def set_power(self, power):
        self.power = power

    def fire(self):
        proj = Projectile(self, self.gravity,self.ground_list)
        return proj
