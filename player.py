from pygame import sprite, Surface, Rect


class Player(sprite.Sprite):

    def __init__(self, size, start, color):
        super(Player, self).__init__()
        self.image = Surface(size)
        self.rect = self.image.get_rect(bottom=start)
        self.image.fill(color)

    def move(self, x, y):
        self.rect = self.rect.move(x, y)

    def update(self):
        pass
