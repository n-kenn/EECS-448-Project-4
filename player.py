<<<<<<< HEAD
from pygame import Color, mask, math, sprite
from pygame.locals import *
from animated_sprite import Animated_Sprite
=======
from pygame import sprite, Surface, image
import math
import pygame
from explosive import Explosive
>>>>>>> WeaponImplementation


class Player(Animated_Sprite):

<<<<<<< HEAD
    """ Player class that the user will control.
    """

    def __init__(self, file_name, rect, frame_rate, start_pos, speed):
        """ Initialize the player sprite.

        :param file_name: The file to be used for the picture of the sprite.
        :param size: The size of the player character.
        :param frame_rate: The frame rate for the particular player character.
        :param start_pos: Starting position for the Player.
        :param speed: The speed of the player.
        """
        super(Player, self).__init__(file_name, rect, frame_rate)
        self.vel = math.Vector2(0, 0)
        self.speed = speed
        self.landed = True
        self.animations = {
            'idle': (self.sprite_sheet.load_strip(1, 0))
        }
        self.current_animation = self.animations['idle']
        self.image = self.current_animation[0].copy()
        self.rect = self.image.get_rect(bottomleft=start_pos)
        self.mask = mask.from_surface(self.image)
        self.health = self.image.get_width()

    def check_keys(self, keys):
        if keys[K_LEFT]:
            self.vel.x -= self.speed
        elif keys[K_RIGHT]:
            self.vel.x += self.speed
        if keys[K_SPACE] and self.landed:
            self.landed = False
            self.vel.y -= 30

    def find_ground(self, ground):
        if self.rect.colliderect(ground.rect):
            if sprite.collide_mask(self, ground):
                self.rect.move_ip(0, -self.vel.y)
                self.vel.y = 0
                self.landed = True

    def draw_health(self):
        self.image.fill(Color('red') if self.health < self.image.get_width() else Color(
            'green'), ((self.image.get_rect().topleft), (self.health, 4)))

    def update(self, world):
        """ Update the Player

        :param world: The world the player inhabits.
        """
        super(Player, self).update()
        self.draw_health()
        self.vel.y += world.gravity
        self.rect.move_ip(self.vel)
        self.find_ground(world.ground)
        if not self.health:
            self.kill()
=======
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
>>>>>>> WeaponImplementation
