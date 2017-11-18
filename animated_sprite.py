from itertools import cycle

from pygame import sprite

from sprite_sheet import Sprite_Sheet


class Animated_Sprite(sprite.Sprite):
    """A sprite to be animated.

    :param sheet: Surface for an optional sprite sheet.
    :param frame_rate: Optional frame_rate for how quickly to change sprite image.
    """

    def __init__(self, sheet=None, frame_rate=15):
        super(Animated_Sprite, self).__init__()
        if sheet:
            self.sheet = Sprite_Sheet(sheet)
        self.frame_rate = frame_rate
        self.frame_cycler = cycle(range(1, self.frame_rate + 1))

    def update(self):
        """Cycles through a frame_counter and updates the sprite's image when time.
        """
        if self.frame_cycler.next() is self.frame_rate:
            self.image = self.curr_anim.next().copy()
