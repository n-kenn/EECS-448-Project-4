from pygame import sprite
from sprite_sheet import Sprite_Sheet


class Animated_Sprite(sprite.Sprite):
    """ A sprite to be animated.
    """
    def __init__(self, file_name, rect, frame_rate, colorkey=None):
        """Initalizes an Animated Sprite.
        :param file_name: The file to be loaded for the image."
        :param rect: The rectangle for the animated sprite to fill.
        :param frame_rate: How many frames this sprite sheet has.
        :param colorkey: Initially set to unknown, but can be set later.
        """
        super(Animated_Sprite, self).__init__()
        self.sprite_sheet = Sprite_Sheet(file_name, colorkey)
        self.index = 0
        self.current_frame = 0
        self.frame_rate = frame_rate
        self.animations = {
            'running': self.sprite_sheet.load_strip(rect, 4, 0)
        }
        self.current_animation = self.animations['running']
        self.image = self.current_animation[0]

    def update(self):
        self.current_frame += 1
        if self.current_frame > self.frame_rate:
            # next line keeps the index within the range of self.images
            self.index = (self.index + 1) % len(self.current_animation)
            self.image = self.current_animation[self.index]
            self.current_frame = 0
