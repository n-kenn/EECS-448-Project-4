from itertools import cycle
from math import atan2

from pygame import mask
from pygame.locals import K_SPACE, K_a, K_d
from pygame.math import Vector2
from pygame.sprite import GroupSingle

from animated_sprite import Animated_Sprite
from explosive import Explosive


class Player(Animated_Sprite):

    """Player class that the user will control.

    :param sheet: The image used for the sprite sheet of player.
    :param start_pos: Starting position for the Player.
    :param name: String of the player name.
    :param speed: Speed at which the player can move. Both horizontal and vertical.
    """

    def __init__(self, sheet, start_pos, speed=4):
        super(Player, self).__init__(sheet)
        self.strips = {
            'idle': self.sheet.load_strip(0, 6),
            'magic': self.sheet.load_strip(3, 4),
            'walking_r': self.sheet.load_strip(1, 6),
            'walking_l': self.sheet.load_strip(2, 6)
        }
        self.curr_strip = self.strips['idle']
        self.curr_anim = cycle(self.curr_strip)
        self.image = self.curr_anim.next().copy()
        self.mask = mask.from_surface(self.image)
        self.rect = self.image.get_rect(midbottom=start_pos)
        self.speed = speed
        self.vel = Vector2(0, 0)
        self.health = self.image.get_width()
        self.projectile = None
        self.power = 20

    def apply_damage(self, damage):
        """Has a player take damage.

        :param damage: How much damage to take.
        """
        self.health -= damage
        if self.health <= 0:
            for team in self.groups():
                team.reset_cycle()
            self.kill()

    def adjust_height(self, ground, xoffset):
        """Adjusts the height of the player to climb slopes.

        :param xoffset: How many pixels the player wants to move left or right.
        """
        for i in range(1, self.speed + 1):
            if not self.collide_ground(ground, (xoffset, -i)):
                self.vel.y -= i
                break
        else:
            self.vel.x = 0

    def check_movement(self, ground, keys):
        """Perform actions based on what keys are pressed.

        :param keys: The keys that are currently being pressed.
        """
        if keys[K_a]:
            self.transition('walking_l', ground, -self.speed)
        elif keys[K_d]:
            self.transition('walking_r', ground, self.speed)
        else:
            self.change_anim('idle')
        if keys[K_SPACE]:
            if not self.collide_ground(ground, (0, -self.speed)):
                self.vel.y -= self.speed

    def collide_ground(self, ground, offset):
        """Returns the point of collision between player and ground with the given offset.

        :param ground: Reference to ground.
        :param offset: Tuple that offsets the player's mask.
        """
        return ground.mask.overlap(self.mask,
                                   (self.rect.left - ground.rect.left + offset[0],
                                    self.rect.top - ground.rect.top + offset[1]))

    def calc_angle(self, pos):
        """Helper function to calculate angle of trajectory for projectile.

        :param pos: Position of mouse.
        """
        return atan2(self.rect.y - pos[1], self.rect.x - pos[0])

    def change_anim(self, anim_name):
        """Changes the current animation to something different, for example,  from idle to moving left or moving right to idle.

        :param anim_name: The name of the animation to be manipulated.
        """
        if self.curr_strip is not self.strips[anim_name]:
            self.curr_strip = self.strips[anim_name]
            self.curr_anim = cycle(self.curr_strip)

    def draw_health(self):
        """Draws the health bar.
        """
        self.image.fill((255, 0, 0) if self.health < self.image.get_width() else (0, 255, 0),
                        ((self.image.get_rect().topleft), (self.health, 4)))

    def fire(self, mouse_pos, collidables):
        """Fires A Projectile

        :param mouse_pos: The mouse position used to calculate the angle to fire the projectile.
        :param collidables: The objects a projectile can collide with.
        """
        if not self.projectile:
            self.projectile = GroupSingle(Explosive(cycle(self.strips['magic']),
                                                    self.rect.midtop,
                                                    self.calc_angle(mouse_pos),
                                                    collidables,
                                                    self.power))

    def transition(self, new_anim, ground, dx):
        """Helper function for updating animation and movement in check_movement.

        :param new_anim: New animation to set.
        :param dx: Amount that the player will move on the next frame.
        """
        self.change_anim(new_anim)
        self.vel.x += dx
        if self.collide_ground(ground, (dx, 0)):
            self.adjust_height(ground, dx)

    def update(self, world):
        """Update the Player

        :param world: The world the player inhabits.
        """
        super(Player, self).update()
        self.draw_health()
        if self.projectile:
            self.projectile.update(world)
            self.projectile.draw(world.image)
        if not self.collide_ground(world.ground, (0, world.gravity)):
            self.vel.y += world.gravity
        self.rect.move_ip(self.vel)
        self.vel = Vector2(0, 0)
        self.rect.clamp_ip(world.rect)
