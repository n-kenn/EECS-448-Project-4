class Sprite_Sheet:
    def __init__(self, sheet, rect, colorkey=None):
        # loads the sprite sheet onto a surface
        self.sheet = sheet
        self.sheet.set_colorkey(colorkey)
        self.rect = rect

    def get_images_at(self, rects):
        # returns a list of a surfaces from the given rects
        return [self.sheet.subsurface(rect) for rect in rects]

    def load_strip(self, count, y_offset):
        # returns a list of surfaces from a strip in the sprite sheet
        return self.get_images_at([(self.rect[0] + self.rect[2] * i, self.rect[1] + y_offset, self.rect[2], self.rect[3]) for i in range(count)])
