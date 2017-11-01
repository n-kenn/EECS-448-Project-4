from pygame import sprite, Surface, draw
import pygame

class Player(sprite.Sprite):

    def __init__(self, size, start_pos, color):
        super(Player, self).__init__()
        self.image = Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(bottomleft=start_pos)
        self.vel = (0, 0)
        self.health = 100
        print size
        print size[0], size[1]
        #self.health_image = Surface(int(size[0]), int(size[1]) -10)
        #self.health_image.fill(pygame.Color('green'))

    def move(self, x, y):
        self.vel = tuple(i + j for i, j in zip(self.vel, (x, y)))

    def update(self):
        self.rect.move_ip(self.vel)
        self.vel = (0, 0)
 #       self.draw_health()

#    def draw_health(self):
  #      pygame.draw.rect((self.image), pygame.Color('green'),
   #                      (0, 0, self.health - self.rect.x, 10))

