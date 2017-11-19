class Menu(object):
    def __init__(self, image, font, font_color=(255, 255, 0)):
        self.options = ['Start', 'Quit']
        self.image = image
        self.rect = self.image.get_rect()
        self.font = font
        self.font_color = font_color
        self.option_rects = []
        self.blit_options()

    def blit_option(self, option_surf, spacing, index):
        return self.image.blit(option_surf, option_surf.get_rect(center=(self.rect.centerx, spacing * index)))

    def blit_options(self):
        split_height = self.rect.height // (1 + len(self.options))
        for index, option_surf in enumerate(self.make_option_surfs(), 1):
            self.option_rects.append(self.blit_option(option_surf,
                                                      split_height,
                                                      index))

    def make_option_surfs(self):
        return [self.font.render(option, False, self.font_color)
                for option in self.options]

    def mouseOver(self, mouse_pos):
        for i, rect in enumerate(self.option_rects):
            if rect.collidepoint(mouse_pos):
                self.image.blit(self.font.render(
                    self.options[i], False, (255, 255, 255)), rect)
            else:
                self.image.blit(self.font.render(
                    self.options[i], False, self.font_color), rect)
