from pygame import sprite, Surface

class Player(sprite.Sprite):

    def __init__(self, size, color, gravity):
        super(Player, self).__init__()
        self.image = Surface(size)
        self.rect = self.image.get_rect()
        self.image.fill(color)
        self.gravity = gravity
        self.in_air = True
        self.angle = 45
        self.power = 30
        self.rect = self.rect.move(30, 450)

    def update(self):
        if (self.in_air):
            self.rect = self.rect.move(0, self.gravity)

    def land(self):
        self.in_air = False

    def get_angle(self):
        return self.angle

    def get_power(self):
        return self.power

    def set_angle(self, angle):
        self.angle = angle
