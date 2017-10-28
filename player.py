from pygame import sprite, Surface


class Player(sprite.Sprite):

    def __init__(self, size, start_pos, color):
        super(Player, self).__init__()
        self.image = Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(bottomleft=start_pos)
        self.vel = (0, 0)

    def move(self, x, y):
        self.vel = tuple(i + j for i, j in zip(self.vel, (x, y)))

    def update(self):
        self.rect.move_ip(self.vel)
        self.vel = (0, 0)
