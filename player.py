from pygame import mask, math, sprite
from pygame.locals import *
from animated_sprite import Animated_Sprite


class Player(Animated_Sprite):

    def __init__(self, file_name, rect, frame_rate, start_pos):
        super(Player, self).__init__(file_name, rect, frame_rate)
        self.vel = math.Vector2(0, 0)
        self.speed = 10
        self.landed = True
        self.animations = {
            'idle': (self.sprite_sheet.load_strip(1, 0))
        }
        self.current_animation = self.animations['idle']
        self.image = self.current_animation[0]
        self.rect = self.image.get_rect(bottomleft=start_pos)
        self.mask = mask.from_surface(self.image)

    def keep_in_bounds(self, bounds):
        if self.rect.right > bounds.right:
            self.rect.right = bounds.right
        elif self.rect.left < bounds.left:
            self.rect.left = bounds.left

    def check_keys(self, keys):
        self.vel.x = 0
        if keys[K_LEFT]:
            self.vel.x -= self.speed
        elif keys[K_RIGHT]:
            self.vel.x += self.speed
        if keys[K_SPACE] and self.landed:
            self.landed = False
            self.vel.y -= 30

    def update(self, world):
        super(Player, self).update()
        self.vel.y += world['gravity']
        self.rect.move_ip(self.vel)
        self.keep_in_bounds(world['ground'].rect)
        if sprite.collide_rect(self, world['ground']):
            self.rect.bottom = world['ground'].rect.top
            self.landed = True
            self.vel.y = 0
