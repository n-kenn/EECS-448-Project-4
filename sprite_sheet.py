class Sprite_Sheet:
    """Loads the Sprite Sheet Files.

    :param sheet: The image to use.
    :param rect: The size of the Sprite Sheet.
    """

    def __init__(self, sheet, rect):
        # loads the sprite sheet onto a surface
        self.sheet = sheet
        self.rect = rect

    def get_images_at(self, rects):
        """Returns a list of surfaces from the given rects.

        :param rects: The rectangles to look at subsurfaces for.
        """
        # returns a list of a surfaces from the given rects
        return [self.sheet.subsurface(rect) for rect in rects]

    def load_strip(self, row, count):
        """Returns a list of surfaces from a strip in the sprite sheet.

        :param count: How many images are in the animation.
        :param row: Row index for the animation.
        """
        # returns a list of surfaces from a strip in the sprite sheet
        return self.get_images_at([(self.rect[0] + self.rect[2] * i,
                                    self.rect[2],
                                    self.rect[3])
                                    for i in range(count))
