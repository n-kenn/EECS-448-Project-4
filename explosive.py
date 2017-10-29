from pygame import sprite, Surface, draw


class Explosive(sprite.Sprite):
    # collidables is an iterable of sprites that the explosive can collide with
    def __init__(self, size, pos, color, collidables):
        super(Explosive, self).__init__()
        self.image = Surface(size)
        self.pos = pos
        self.rect = self.image.get_rect(topleft=self.pos)
        self.image.fill(color)
        self.collidables = collidables

    def collision_check(self, collidables):
        for collidable in collidables:
            if self.rect.colliderect(collidable.rect):
                self.kill()
                # ellipse is relative to the Surface being drawn on
                draw.ellipse(collidable.image, collidable.color_key, self.rect.inflate(
                    self.image.get_size()).move(0, -collidable.rect.height + self.image.get_rect().centery))

    def update(self):
        # move_ip overwrites the rect
        self.rect.move_ip((0, 5))
        self.collision_check(self.collidables)
