from pygame import mask, math
from pygame.locals import *
from animated_sprite import Animated_Sprite


class Player(Animated_Sprite):

    def __init__(self, file_name, size, frame_rate, start_pos):
        super(Player, self).__init__(file_name, size, frame_rate)
        self.mask = mask.from_surface(self.image)
        self.rect = self.image.get_rect(bottomleft=start_pos)
        self.vel = math.Vector2(0, 0)
        self.speed = 10
        self.landed = True

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
            self.vel.y -= 40

    def update(self, world):
        self.vel.y += world['gravity']
        super(Player, self).update()
        self.rect.move_ip(self.vel)
        self.keep_in_bounds(world['ground'].rect)
        if self.rect.colliderect(world['ground'].rect):
            self.landed = True
            self.vel.y = 0
            self.rect.bottom = world['ground'].rect.top
