from pygame import mask, sprite, Surface


class Player(sprite.Sprite):

    def __init__(self, size, start_pos, color):
        super(Player, self).__init__()
        self.image = Surface(size).convert_alpha()
        self.mask = mask.from_surface(self.image)
        self.image.fill(color)
        self.rect = self.image.get_rect(bottomleft=start_pos)

    def move(self, x, y):
        self.rect.move_ip(x, y)

    def update(self, gravity, ground):
        self.rect.move_ip(0, 1)
        if sprite.collide_mask(self, ground):
            self.rect.bottom = ground.rect.top + 0 # find height of the collision
