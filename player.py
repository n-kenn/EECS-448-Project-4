from itertools import cycle
from math import atan2

from pygame import Color, mask
from pygame.locals import *
from pygame.math import Vector2
from pygame.sprite import GroupSingle

from animated_sprite import Animated_Sprite
from explosive import Explosive


class Player(Animated_Sprite):

    """Player class that the user will control.

    :param sheet: The image used for the sprite sheet of player.
    :param ground: Reference to ground to determine if the player is grounded.
    :param start_pos: Starting position for the Player.
    :param speed: Speed at which the player can move. Both horizontal and vertical.
    :param name: String of the player name.
    """

    def __init__(self, sheet, ground, start_pos, speed=4, name='Josh'):
        super(Player, self).__init__(sheet)
        self.speed = speed
        self.vel = Vector2(0, 0)
        self.strips = {
            'idle': self.sheet.load_strip(0, 6),
            'walking_r': self.sheet.load_strip(1, 6),
            'walking_l': self.sheet.load_strip(2, 6),
            'magic': self.sheet.load_strip(3, 4)
        }
        self.curr_strip = self.strips['idle']
        self.curr_anim = cycle(self.curr_strip)
        self.image = self.curr_anim.next().copy()
        self.mask = mask.from_surface(self.image)
        self.ground = ground
        self.rect = self.image.get_rect(midbottom=start_pos)
        self.name = name
        self.health = self.image.get_width()
        self.projectile = None

    def apply_damage(self, damage):
        """Has a player take damage.

        :param damage: How much damage to take.
        """
        self.health -= damage
        if self.health <= 0:
            self.kill()

    def adjust_height(self, xoffset):
        """Adjusts the height of the player to climb slopes.

        :param xoffset: How many pixels the player wants to move left or right.
        """
        for i in range(1, self.speed + 1):
            if not self.collide_ground((xoffset, -i)):
                self.vel.y -= i
                break
        else:
            self.vel.x = 0

    def check_keys(self, keys):
        """Perform actions based on what keys are pressed.

        :param keys: The keys that are currly being pressed.
        """
        if keys[K_LEFT]:
            self.transition('walking_l', -self.speed)
        elif keys[K_RIGHT]:
            self.transition('walking_r', self.speed)
        else:
            self.change_anim('idle')
        if keys[K_SPACE]:
            if not self.collide_ground((0, -self.speed)):
                self.vel.y -= self.speed

    def collide_ground(self, offset):
        """Returns the point of collision between player and ground with the given offset.

        :param offset: Tuple that offsets the player's mask.
        """
        return self.ground.mask.overlap(self.mask,
                                        (self.rect.left - self.ground.rect.left + offset[0],
                                         self.rect.top - self.ground.rect.top + offset[1]))

    def calc_angle(self, pos):
        """Helper function to calculate angle of trajectory for projectile.

        :param pos: Position of mouse.
        """
        return atan2(self.rect.y - pos[1], self.rect.x - pos[0])

    def change_anim(self, anim_name):
        if self.curr_strip is not self.strips[anim_name]:
            self.curr_strip = self.strips[anim_name]
            self.curr_anim = cycle(self.curr_strip)

    def draw_health(self):
        """Draws the health bar.

        """
        self.image.fill(Color('red') if self.health < self.image.get_width() else Color(
            'green'), ((self.image.get_rect().topleft), (self.health, 4)))

    def fire(self, mouse_pos, collidables):
        """Fires A Projectile

        :param mouse_pos: The mouse position used to calculate the angle to fire the projectile.
        :param collidables: The objects a projectile can collide with.
        """
        if not self.projectile:
            self.projectile = GroupSingle(Explosive(cycle(self.strips['magic']),
                                                    self.rect.midtop,
                                                    self.calc_angle(mouse_pos),
                                                    collidables))

    def transition(self, new_anim, dx):
        """Helper function for updating animation and movement in check_keys

        :param new_anim: New animation to set
        :param dx: Amount that the player will move on the next frame
        """
        self.change_anim(new_anim)
        self.vel.x += dx
        if self.collide_ground((dx, 0)):
            self.adjust_height(dx)

    def update(self, world):
        """Update the Player

        :param world: The world the player inhabits.
        """
        super(Player, self).update()
        self.draw_health()
        if self.projectile:
            self.projectile.update(world)
            self.projectile.draw(world.image)
        if not self.collide_ground((0, world.gravity)):
            self.vel.y += world.gravity
        self.rect.move_ip(self.vel)
        self.vel = Vector2(0, 0)
        self.rect.clamp_ip(world.rect)
