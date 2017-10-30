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

    # def landed(self, ground):
    #     return self.rect.colliderect(ground.rect)

    def update(self, gravity, ground):
        # the player's position needs to be reset to the point where the two masks collide.
        # the point is indexed at (0,0) however
        if self.rect.move(0, 5).colliderect(ground.rect):
            print sprite.collide_mask(self, ground)
