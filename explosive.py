from pygame import sprite, Surface


class Explosive(sprite.Sprite):
    def __init__(self, size, pos, color, collidables):
        super(Explosive, self).__init__()
        self.image = Surface(size)
        self.rect = self.image.get_rect(topleft=pos)
        self.image.fill(color)
        self.collidables = collidables

    def collision_check(self, *others):
        for other in others:
            if self.rect.colliderect(other.rect):
                # here's where we'll start the explosion
                self.kill()

    def update(self):
        self.rect.move_ip((0, 5))
        self.collision_check(*self.collidables)
