from itertools import cycle

from pygame import sprite

from sprite_sheet import Sprite_Sheet


class Animated_Sprite(sprite.Sprite):
    """A sprite to be animated.

    :param sheet: The file to be loaded for the spritesheet.
    :frame_rate: The time to sycle to the next image in the sprite sheet.
    :param groups: Any groups that the sprite should be added to.
    """

    def __init__(self, frame_rate, groups, sheet=None):
        super(Animated_Sprite, self).__init__(groups)
        if sheet:
            self.sprite_sheet = Sprite_Sheet(sheet, (0, 0, 32, 32))
        self.frame_rate = frame_rate
        self.frame_cycler = cycle(range(self.frame_rate))

    def update(self):
        if self.frame_cycler.next() is self.frame_rate - 1:
            self.image = self.current_animation.next().copy()
