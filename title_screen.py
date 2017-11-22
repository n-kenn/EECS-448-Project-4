from pygame import Surface
from pygame.locals import MOUSEBUTTONDOWN, QUIT

from game import Game
from scene import Scene


class Title_Screen(Scene):
    def __init__(self, size, opts, font, images, font_color=(255, 255, 0)):
        super(Title_Screen, self).__init__()
        self.image = Surface(size)
        self.rect = self.image.get_rect()
        self.opts = opts
        self.font = font
        self.font_color = font_color
        self.opt_rects = []
        self.blit_opts()
        self.game_scene = Game(
            images['player_ss'], images['sky'], images['ground'])

    def blit_opt(self, opt_surf, y):
        return self.image.blit(opt_surf, opt_surf.get_rect(center=(self.rect.centerx, y)))

    def blit_opts(self):
        split_height = self.rect.height // (1 + len(self.opts))
        for i, surf in enumerate(self.make_opt_surfs(), 1):
            self.opt_rects.append(self.blit_opt(surf, split_height * i))

    def make_opt_surfs(self):
        return [self.font.render(opt, False, self.font_color)
                for opt in self.opts]

    def process_input(self, events, keys):
        for event in events:
            if event.type is QUIT:
                self.switch_scene(None)
            elif event.type is MOUSEBUTTONDOWN:
                for rect in self.opt_rects:
                    if rect.collidepoint(event.pos):
                        self.switch_scene(self.game_scene)

    def update(self, display, events, keys):
        self.process_input(events, keys)
        display.blit(self.image, display.get_rect())
