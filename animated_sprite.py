from pygame import sprite
from sprite_sheet import Sprite_Sheet


class Animated_Sprite(sprite.Sprite):
    """ A sprite to be animated.
    """

    def __init__(self, image_file, rect, frame_rate, groups, colorkey=None):
        """Initalizes an Animated Sprite.
        :param file_name: The file to be loaded for the image."
        :param rect: The rectangle for the animated sprite to fill.
        :param frame_rate: How quickly the next frame of animation is displayed.
        :param colorkey: Initially set to unknown, but can be set later.
        """
        super(Animated_Sprite, self).__init__(groups)
        self.sprite_sheet = Sprite_Sheet(image_file, rect, colorkey)
        self.index = 0
        self.current_frame = 0
        self.frame_rate = frame_rate

    def update(self):
        self.current_frame += 1
        if self.current_frame > self.frame_rate:
            # next line keeps the index within the range of self.images
            self.index = (self.index + 1) % len(self.current_animation)
            self.image = self.current_animation[self.index].copy()
            self.current_frame = 0
