from pygame import mask
from animated_sprite import Animated_Sprite


class Player(Animated_Sprite):

    def __init__(self, file_name, size, frame_rate, start_pos):
        super(Player, self).__init__(file_name, size, frame_rate)
        self.mask = mask.from_surface(self.image)
        self.rect = self.image.get_rect(bottomleft=start_pos)

    def update(self, world):
        super(Player, self).update()
