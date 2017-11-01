from pygame import sprite, Surface, draw, mask, Color
from projectile import Projectile

class Explosive(Projectile):
    # collidables is an iterable of sprites that the explosive can collide with
    def __init__(self, player, gravity, ground_list):
        super(Explosive, self).__init__(Color('red'),player, gravity, ground_list)
        self.mask = mask.from_surface(self.image)
        # collidables could shorten/lengthen dynamically, may use a sprite group later
        self.collidables = ground_list

    def collision_check(self):

        # this will probably get refactored somehow.
        for collidable in self.collidables:
            # check for rectangular collision
            if (self.rect.colliderect(collidable.rect) and collidable is not self):
                # then check for per pixel collision to make algorithm more efficient

                if (sprite.collide_mask(self, collidable) is not None):
                    self.kill()
                    # ellipse is relative to the Surface being drawn on
                    draw.ellipse(collidable.image, (255, 0, 0, 255), self.rect.inflate(
                        self.image.get_size()).move(0, -collidable.rect.height + self.image.get_rect().centery))
                    break


    def update(self):
        self.proj_arc()
        self.collision_check()
