class Menu(object):
    def __init__(self, image, opts, font, font_color=(255, 255, 0)):
        self.image = image
        self.opts = opts
        self.rect = self.image.get_rect()
        self.font = font
        self.font_color = font_color
        self.opt_rects = []
        self.blit_opts()

    def blit_opt(self, opt_surf, y):
        return self.image.blit(opt_surf, opt_surf.get_rect(center=(self.rect.centerx, y)))

    def blit_opts(self):
        split_height = self.rect.height // (1 + len(self.opts))
        for i, surf in enumerate(self.make_opt_surfs(), 1):
            self.opt_rects.append(self.blit_opt(surf, split_height * i))

    def make_opt_surfs(self):
        return [self.font.render(opt, False, self.font_color)
                for opt in self.opts]

    def mouse_over(self, mouse_pos):
        for i, rect in enumerate(self.opt_rects):
            if rect.collidepoint(mouse_pos):
                return self.opts[i]
