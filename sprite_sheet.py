from pygame import image


class Sprite_Sheet:
    def __init__(self, sheet, colorkey=None):
        # loads the sprite sheet onto a surface
        self.sheet = image.load(sheet)
        self.sheet.set_colorkey(colorkey)

    def get_images_at(self, rects):
        # returns a list of a surfaces from the given rects
        return [self.sheet.subsurface(rect) for rect in rects]

    def load_strip(self, rect, count, y_offset):
        # returns a list of surfaces from a strip in the sprite sheet
        return self.get_images_at([(rect[0] + rect[2] * i, rect[1] + y_offset, rect[2], rect[3])
                                   for i in range(count)])
