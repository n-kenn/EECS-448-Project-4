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

    def check_keys(self, keys):
        """Perform actions based on what keys are pressed.

        :param keys: The keys that are currently being pressed.
        """
        if keys[K_LEFT]:
            self.vel.x = -self.speed / 2 if self.vel.y else -self.speed
        elif keys[K_RIGHT]:
            self.vel.x = self.speed / 2 if self.vel.y else self.speed
        if keys[K_SPACE] and not self.vel.y:
            self.vel.y -= self.speed

    def draw_health(self):
        """Draws the health bar.
        """
        self.image.fill(Color('red') if self.health < self.image.get_width() else Color(
            'green'), ((self.image.get_rect().topleft), (self.health, 4)))

    def fire(self, pos, collidables):
        """Fires A Projectile

        :param pos: The angle to fire the projectile.
        :param collidables: The objects a projectile can collide with.
        """
        collidables.append(self)
        self.explosive = Explosive(self.animations['magic'], self.rect.midtop,
                                   self.get_angle(pos), collidables, self.groups())

    def find_ground(self, ground):
        """Method to detect collision with the ground.

        :param ground: Ground surface to check collision with.
        """

        if self.mask.overlap(ground.mask, (ground.rect.left - self.rect.left, ground.rect.top - self.rect.top)):
            self.vel.y = 0

    def get_angle(self, pos):
        """Sets the angle of the player based on mouse position

        :param pos: A tuple containing the x and y coordinates.
        """
        return atan2(self.rect.y - pos[1], pos[0] - self.rect.x)

    def update(self, world):
        """Update the Player

        :param world: The world the player inhabits.
        """
        super(Player, self).update()
        self.draw_health()
        self.rect.move_ip(self.vel)
        self.vel.x = 0
        self.vel.y += world.gravity
        self.find_ground(world.ground)
        self.rect.clamp_ip(world.rect)
