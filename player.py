from pygame import sprite, Surface


class Player(sprite.Sprite):

    def __init__(self, size, start_pos, color):
        super(Player, self).__init__()
        self.image = Surface(size)
        self.rect = self.image.get_rect(bottom=start_pos)
        self.image.fill(color)
        self.in_air = True
        self.angle = 45
        self.power = 0
        

    def player_move(self, x, y):
        self.rect = self.rect.move(x, y)

    def update(self):
        pass

    def land(self):
        self.in_air = False

    def get_angle(self):
        return self.angle

    def get_power(self):
        return self.power

    def set_angle(self, angle):
        self.angle = angle

    def set_power(self, power):
        self.power = power
