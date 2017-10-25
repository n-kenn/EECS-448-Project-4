from pygame import sprite, Surface

class Player(sprite.Sprite):

    def __init__(self, size, color, gravity):
        super(Player, self).__init__()
        self.image = Surface(size)
        self.rect = self.image.get_rect()
        self.image.fill(color)
        self.gravity = gravity
        self.in_air = True

    def update(self):
        if (self.in_air):
            self.rect = self.rect.move(0, self.gravity)

    def land(self):
        self.in_air = False
