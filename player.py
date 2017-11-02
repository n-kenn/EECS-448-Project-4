from pygame import mask, sprite, Surface


class Player(sprite.Sprite):

    def __init__(self, size, start_pos, color):
        super(Player, self).__init__()
        self.image = Surface(size).convert_alpha()
        self.mask = mask.from_surface(self.image)
        self.image.fill(color)
        self.rect = self.image.get_rect(bottomleft=start_pos)

    def update(self, world):
        self.rect.move_ip(0, world['gravity'])
        print sprite.collide_mask(self, world['ground']) # why is this None?
        # self.rect.bottom = world['ground'].rect.height + self.mask.overlap(world['ground'].mask, (xoff, yoff))[1]
