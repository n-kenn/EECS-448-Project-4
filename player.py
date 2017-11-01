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
        # heights is an array of 'solid' pixels within a Rect that the player could stand on
        if self.rect.move(0, 1).colliderect(ground.rect):
            surf_mask = mask.from_surface(ground.image.subsurface(
                self.image.get_rect().move(self.rect.left, 0)))
            test_mask = mask.Mask((1, self.image.get_height()))
            # fill doesn't return a new mask
            test_mask.fill()
            heights = [surf_mask.overlap_area(
                test_mask, (i, 0)) for i in range(self.image.get_width())]
