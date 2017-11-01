from pygame import sprite, Surface, image
import math
import pygame
from explosive import Explosive


class Player(sprite.Sprite):

    def __init__(self, size, start_pos, color, gravity):
        super(Player, self).__init__()
        self.image = image.load("images/snake_wizard.png")
        self.rect = self.image.get_rect(bottom=start_pos)
        self.in_air = True
        self.angle = 0
        self.power = 10
        self.gravity = gravity
        self.object_list = []
        self.health = 100
        self.current_weapon = 'Explosive'

    def set_collidables(self, object_list):
        self.object_list = (object_list)

    def player_move(self, x, y):
        self.rect = self.rect.move(x, y)

    def update(self):
       self.draw_health()

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
        if (self.current_weapon == 'Explosive'):
            proj = Explosive(self, self.gravity,self.object_list)
        return proj

    def draw_health(self):
        pygame.draw.rect((self.image), pygame.Color('green'),
                         (0, 0, self.health - self.rect.x, 10))
