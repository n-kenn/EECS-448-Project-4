from pygame.locals import MOUSEBUTTONDOWN, MOUSEMOTION, QUIT

# from game import Game
from name_input import Name_Input
from scene import Scene


class Title_Screen(Scene):
    """Provides a menu for UI.

    :param images: Will get passed to Game constructor.
    :param opts: Iterable of options as strings available to select.
    :param font: Which font to render opt_surfs in.
    """

    def __init__(self, images, opts, font):
        super(Title_Screen, self).__init__()
        self.image = images['sky'].copy()
        self.rect = self.image.get_rect()
        self.opts = opts
        self.font = font
        self.opt_rects = []
        self.blit_opts()
        self.next_scene = Name_Input(images, self.font)
        # self.game_scene = Game(images, font)

    def blit_opt(self, opt_surf, y):
        """Blits a single opt_surf to self.image and returns a Rect of the effected area.
        """
        return self.image.blit(opt_surf, opt_surf.get_rect(center=(self.rect.centerx, y)))

    def blit_opts(self):
        """Blits multiple opts by calling self.blit_opt on each opt.
        """
        split_height = self.rect.height // (1 + len(self.opts))
        for i, surf in enumerate(self.make_opt_surfs(), 1):
            self.opt_rects.append(self.blit_opt(surf, split_height * i))

    def make_opt_surf(self, opt, font_col=(156, 68, 108)):
        """Returns a new surface using the font passed into the constructor.
        """
        return self.font.render(opt, False, font_col).convert()

    def make_opt_surfs(self):
        """Returns a list of surfaces from the opts passed into the constructor
        """
        return [self.make_opt_surf(opt) for opt in self.opts]

    def process_input(self, events, keys):
        """Handles input from the user.
        """
        for event in events:
            if event.type is QUIT:
                self.switch_scene(None)
            elif event.type is MOUSEMOTION:
                for i, opt_rect in enumerate(self.opt_rects):
                    if opt_rect.collidepoint(event.pos):
                        self.image.blit(self.make_opt_surf(
                            self.opts[i], (70, 0, 6)), opt_rect)
                    else:
                        self.image.blit(self.make_opt_surf(
                            self.opts[i]), opt_rect)
            elif event.type is MOUSEBUTTONDOWN:
                for i, opt_rect in enumerate(self.opt_rects):
                    if opt_rect.collidepoint(event.pos):
                        if self.opts[i] is 'Start':
                            self.switch_scene(self.next_scene)
                        elif self.opts[i] is 'Quit':
                            self.switch_scene(None)

    def update(self, display, events, keys):
        """Processes event and key input from user and blits to display self.image each frame.
        """
        self.process_input(events, keys)
        display.blit(self.image, display.get_rect())
