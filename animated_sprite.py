from itertools import cycle

from pygame import sprite

from sprite_sheet import Sprite_Sheet


class Animated_Sprite(sprite.Sprite):
    """A sprite to be animated.

    :param sheet: The file to be loaded for an optional sprite sheet.
    """

    def __init__(self, sheet=None, frame_rate=10):
        super(Animated_Sprite, self).__init__()
        if sheet:
            self.sheet = Sprite_Sheet(sheet, (0, 0, 32, 32))
        self.frame_rate = frame_rate
        self.frame_cycler = cycle(range(0, self.frame_rate + 1))

    def update(self):
        """Cycles through a frame_counter and updates the sprite's image when time.
        """
        if self.frame_cycler.next() is self.frame_rate:
            self.image = self.current_anim.next().copy()
