from pygame import sprite, Surface


class Explosive(sprite.Sprite):
    def __init__(self, size, pos, color, collidables):
        super(Explosive, self).__init__()
        self.image = Surface(size)
        self.pos = pos
        self.rect = self.image.get_rect(topleft=self.pos)
        self.image.fill(color)
        self.collidables = collidables

    def collision_check(self, other):
        if self.rect.colliderect(other.rect):
            self.kill()

    def update(self):
        self.rect.move_ip((0, 5))
        self.collision_check(*self.collidables)
