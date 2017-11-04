from pygame import sprite
from sprite_sheet import Sprite_Sheet


class Animated_Sprite(sprite.Sprite):
    def __init__(self, file_name, rect, frame_rate, colorkey=None):
        super(Animated_Sprite, self).__init__()
        self.sprite_sheet = Sprite_Sheet(file_name, rect, colorkey)
        self.index = 0
        self.current_frame = 0
        self.frame_rate = frame_rate

    def update(self):
        self.current_frame += 1
        if self.current_frame > self.frame_rate:
            # next line keeps the index within the range of self.images
            self.index = (self.index + 1) % len(self.current_animation)
            self.image = self.current_animation[self.index]
            self.current_frame = 0
