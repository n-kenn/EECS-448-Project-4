from itertools import cycle
from math import atan2

from pygame import Color, mask, math, sprite
from pygame.locals import *

from animated_sprite import Animated_Sprite
from explosive import Explosive


class Player(Animated_Sprite):

    """Player class that the user will control.

    :param start_pos: Starting position for the Player.
    :param groups: Groups that the Player Sprite belongs to.
    :param sheet: The image used for the sprite sheet of player.
    """

    def __init__(self, sheet, start_pos, groups):
        super(Player, self).__init__(10, groups, sheet)
        self.angle = None
        self.speed = 4
        self.vel = math.Vector2(0, 0)
        self.landed = True
        self.animations = {
            'idle': self.sprite_sheet.load_strip(1, 0),
            'magic': self.sprite_sheet.load_strip(4, 1)
        }
        self.current_animation = cycle(self.animations['idle'])
        self.image = self.current_animation.next().copy()
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
                self.vel.x = -self.speed // 2
        elif keys[K_RIGHT]:
            if self.landed:
                self.vel.x = self.speed
            else:
                self.vel.x = self.speed // 2
        if keys[K_SPACE] and self.landed:
            self.landed = False
            self.vel.y -= self.speed

    def fire(self, pos, collidables):
        """Fires A Projectile

        :param pos: The angle to fire the projectile.
        :param collidables: The objects a projectile can collide with.
        """
        collidables.append(self)
        self.set_angle(pos)
        self.explosive = Explosive(self.animations['magic'], self.rect.midtop,
                                   self.angle, collidables, self.groups())

    def take_damage(self, damage):
        """Has a player take damage.

        :param damage: How much damage to take.
        """
        self.health -= damage
        if self.health <= 0:
            self.kill()

    def find_ground(self, ground):
        """Method to keep player within the bounds of the map.

        :param ground: The ground to stay within the bounds of.
        """
        if self.mask.overlap(ground.mask, (ground.rect.left - self.rect.left, ground.rect.top - self.rect.top)):
            self.vel.y = 0

    def draw_health(self):
        """Draws the health bar.
        """
        self.image.fill(Color('red') if self.health < self.image.get_width() else Color(
            'green'), ((self.image.get_rect().topleft), (self.health, 4)))

    def set_angle(self, pos):
        """Sets the angle of the player based on mouse position
            :param pos: A tuple containing the x and y coordinates.
        """
        self.angle = atan2(self.rect.y - pos[1], pos[0] - self.rect.x)

    def update(self, world):
        """Update the Player

        :param world: The world the player inhabits.
        """
        super(Player, self).update()
        self.draw_health()
        self.vel.y += world.gravity
        self.find_ground(world.ground)
        self.rect.move_ip(self.vel)
        self.vel.x = 0
        self.rect.clamp_ip(world.rect)
