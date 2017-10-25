from pygame import sprite, image

class Player(sprite.Sprite):
    def __init__(self, file_name):
        super(Player, self).__init__()
        self.image = image.load(file_name)
    def update(self):
        pass
