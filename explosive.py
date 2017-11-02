from pygame import draw, mask, sprite, Surface


class Explosive(sprite.Sprite):
    # collidables is an iterable of sprites that the explosive can collide with
    def __init__(self, size, pos, color, collidables):
        super(Explosive, self).__init__()
        self.image = Surface(size).convert_alpha()
        self.mask = mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=pos)
        self.image.fill(color)
        # collidables could shorten/lengthen dynamically, may use a sprite group later
        self.collidables = collidables

    def collision_check(self):
        # this will probably get refactored somehow.
        for collidable in self.collidables:
            # check for rectangular collision
            if self.rect.colliderect(collidable.rect):
                # then check for per pixel collision to make algorithm more efficient
                if sprite.collide_mask(self, collidable):
                    self.kill()
                    # ellipse is relative to the Surface being drawn on
                    draw.ellipse(collidable.image, (0, 0, 0, 0), self.rect.inflate(
                        self.image.get_size()).move(0, -collidable.rect.height + self.image.get_rect().centery))
                    break

    def update(self, world):
        # move_ip overwrites the rect
        self.rect.move_ip((0, world['gravity']))
        self.collision_check()
