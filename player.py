from pygame import Color, mask, math, sprite
from pygame.locals import *
from animated_sprite import Animated_Sprite


class Player(Animated_Sprite):

    """ Player class that the user will control.
    """

    def __init__(self, file_name, rect, frame_rate, start_pos, speed):
        """ Initialize the player sprite.

        :param file_name: The file to be used for the sprite sheet of player.
        :param size: The size of the player sprite.
        :param frame_rate: The frame rate for the particular player character.
        :param start_pos: Starting position for the Player.
        :param speed: The speed of the player.
        """
        super(Player, self).__init__(file_name, rect, frame_rate)
        self.angle = 45
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
            self.angle = 135
            self.vel.x -= self.speed
        elif keys[K_RIGHT]:
            self.angle = 45
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
        if not self.health:
            self.kill()
        super(Player, self).update()
        self.draw_health()
        self.vel.y += world.gravity
        self.rect.move_ip(self.vel)
        self.find_ground(world.ground)
        self.rect.clamp_ip(world.rect)
