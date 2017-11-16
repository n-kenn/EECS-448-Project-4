from itertools import cycle
from math import atan2
from operator import sub

from pygame import Color, mask, math
from pygame.locals import *

from animated_sprite import Animated_Sprite
from explosive import Explosive


class Player(Animated_Sprite):

    """Player class that the user will control.

    :param sheet: The image used for the sprite sheet of player.
    :param start_pos: Starting position for the Player.
    :param groups: Groups that the Player Sprite gets added to.
    """

    def __init__(self, sheet, start_pos, groups, name='Josh'):
        super(Player, self).__init__(10, groups, sheet)
        self.name = name
        self.speed = 4
        self.vel = math.Vector2(0, 0)
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

    def apply_damage(self, damage):
        """Has a player take damage.

        :param damage: How much damage to take.
        """
        self.health -= damage
        if self.health <= 0:
            self.kill()

    def adjust_height(self, ground, xoffset):
        for i in range(1, self.speed + 1):
            if not self.collide_ground(ground, (xoffset, -i)):
                self.vel.y -= i

    def check_keys(self, keys, ground):
        """Perform actions based on what keys are pressed.

        :param keys: The keys that are currently being pressed.
        """

        if keys[K_LEFT]:
            if not self.collide_ground(ground, (-self.speed, 0)):
                self.vel.x -= self.speed
            else:
                self.adjust_height(ground, -self.speed)
        elif keys[K_RIGHT]:
            if not self.collide_ground(ground, (self.speed, 0)):
                self.vel.x += self.speed
            else:
                self.adjust_height(ground, self.speed)
        if keys[K_SPACE]:
            self.vel.y -= self.speed

    def collide_ground(self, ground, offset):
        return ground.mask.overlap(self.mask, (self.rect.left - ground.rect.left + offset[0], self.rect.top - ground.rect.top + offset[1]))

    def draw_health(self):
        """Draws the health bar.
        """
        self.image.fill(Color('red') if self.health < self.image.get_width() else Color(
            'green'), ((self.image.get_rect().topleft), (self.health, 4)))

    def fire(self, pos, collidables):
        """Fires A Projectile

        :param pos: The mouse position used to calculate the angle to fire the projectile.
        :param collidables: The objects a projectile can collide with.
        """
        self.projectile = Explosive(self.animations['magic'], self.rect.midtop, atan2(
            self.rect.y - pos[1], self.rect.x - pos[0]), collidables, self.groups())

    def grounded(self, ground, gravity):
        return ground.mask.overlap(self.mask, (self.rect.left - ground.rect.left, self.rect.top - ground.rect.top + gravity))

    def update(self, world):
        """Update the Player

        :param world: The world the player inhabits.
        """
        super(Player, self).update()
        self.draw_health()
        if not self.grounded(world.ground, world.gravity):
            self.vel.y += world.gravity
        self.rect.move_ip(self.vel)
        self.vel = math.Vector2(0, 0)
        self.rect.clamp_ip(world.rect)
