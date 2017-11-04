from pygame import mask, math, sprite
from pygame.locals import *
import pygame
from animated_sprite import Animated_Sprite


class Player(Animated_Sprite):

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
        self.image = self.current_animation[0]
        self.rect = self.image.get_rect(bottomleft=start_pos)
        self.mask = mask.from_surface(self.image)
        self.health = 100

    def keep_in_bounds(self, bounds):
        if self.rect.right > bounds.right:
            self.rect.right = bounds.right
        elif self.rect.left < bounds.left:
            self.rect.left = bounds.left

    def check_keys(self, keys):
        if keys[K_LEFT]:
            self.vel.x -= self.speed
        elif keys[K_RIGHT]:
            self.vel.x += self.speed
        else:
            self.vel.x = 0
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
       # print self.rect.x
        if (self.health > 0):
            pygame.draw.rect(self.image, pygame.Color('green'),
                             (0,0, self.health , 10))
        if (self.health < 100):    
            pygame.draw.rect(self.image, pygame.Color('red'), (0, 0, (100 - self.health) * .34, 10))
    def update(self, world):
        """ Update the Player

        :param world: The world the player inhabits.
        """
        super(Player, self).update()
        self.vel.y += world['gravity']
        self.rect.move_ip(self.vel)
        self.find_ground(world['ground'])
        self.keep_in_bounds(world['ground'].rect)
        self.draw_health()
        if (self.health <= 0):
            self.kill()
