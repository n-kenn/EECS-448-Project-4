import math as MATH
from pygame import Color, mask, sprite, math
from pygame.locals import *
from animated_sprite import Animated_Sprite


class Player(Animated_Sprite):

    """ Player class that the user will control.

        :param file_name: The file to be used for the sprite sheet of player.
        :param rect: The size of the player sprite.
        :param frame_rate: The frame rate for the particular player character.
        :param start_pos: Starting position for the Player.
        :param speed: The speed of the player.

    """

    def __init__(self, file_name, rect, frame_rate, start_pos):
        super(Player, self).__init__(file_name, rect, frame_rate)
        self.angle = 45
        self.power = 10
        self.vel = math.Vector2(0, 0)
        self.speed = 5
        self.landed = True
        self.animations = {
            'idle': (self.sprite_sheet.load_strip(1, 0))
        }
        self.current_animation = self.animations['idle']
        self.image = self.current_animation[0].copy()
        self.rect = self.image.get_rect(bottomleft=start_pos)
        self.mask = mask.from_surface(self.image)
        self.health = self.image.get_width()
        self.projectile = None

    def check_keys(self, keys):
        """Perform actions based on what keys are pressed.

        :param keys: The keys that are currently being pressed.
        """
        if keys[K_LEFT]:
            if self.landed:
                self.vel.x = -self.speed
            else:
                self.vel.x = int(-(self.speed-3))
        elif keys[K_RIGHT]:
            if self.landed:
                self.vel.x = self.speed
            else:
                self.vel.x = int(self.speed-3)

        else:
            if self.landed:
                self.vel.x = int(self.vel.x/2)

        if keys[K_SPACE] and self.landed:
            self.landed = False
            self.vel.y -= 5
        if keys[K_RETURN]:
            pass

    def find_ground(self, ground):
        """Method to keep player within the bounds of the map.

        :param ground: The ground to stay within the bounds of.
        """
        if self.rect.colliderect(ground.rect):
            if sprite.collide_mask(self, ground):
                self.rect.move_ip(0, -self.vel.y)
                self.vel.y = 0
                self.landed = True

    def draw_health(self):
        """Draws the health bar.
        """
        self.image.fill(Color('red') if self.health < self.image.get_width() else Color(
            'green'), ((self.image.get_rect().topleft), (self.health, 4)))

    def set_angle(self, (mouse_x, mouse_y)):
        """Sets the angle of the player based on mouse position
            :param (mouse_x,mouse_y): A tuple containing the x and y coordinates of the mouse
        """
        self.angle = MATH.atan2(self.rect.y - mouse_y, mouse_x - self.rect.x)

    def update(self, world):
        """ Update the Player

        :param world: The world the player inhabits.
        """
        if not self.health:
            self.kill()
        super(Player, self).update()
        self.draw_health()
        self.vel.y += world.gravity
        self.rect.move_ip(self.vel)
        self.find_ground(world.ground)
        self.rect.clamp_ip(world.rect)
