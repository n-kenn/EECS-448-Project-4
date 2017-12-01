from subprocess import call

from pygame.locals import MOUSEBUTTONDOWN, MOUSEMOTION, QUIT
from pygame.transform import scale2x

from game import Game
from scene import Scene


class Title_Screen(Scene):
    """Provides a menu for UI.

    :param images: Will get passed to Game constructor.
    :param font: Which font to render opt_surfs in.
    """

    def __init__(self, images, font):
        super(Title_Screen, self).__init__()
        self.images = images
        self.image = self.images['sky'].copy()
        self.font = font
        self.rect = self.image.get_rect()
        title = self.font.render('WIZARDS', False, (70, 0, 6))
        title = scale2x(title)
        self.image.blit(title, (title.get_rect(
            center=(self.rect.centerx, self.rect.height // 3))))
        self.opts = ['PLAY', 'QUIT', 'TEST']
        self.assoc = {k: v for k, v in enumerate(self.opts)}
        self.opt_rects = []
        self.blit_opts()

    def blit_opt(self, opt_surf, x):
        """Blits a single opt_surf to self.image and returns a Rect of the effected area.

        :param opt_surf: The option to be displayed.
        :param y: The y coordinate to put the option on.
        """
        return self.image.blit(opt_surf, opt_surf.get_rect(center=(x, self.rect.height * 3 // 4)))

    def blit_opts(self):
        """Blits multiple opts by calling self.blit_opt on each opt.
        """
        split_width = self.rect.width // (1 + len(self.opts))
        for i, surf in enumerate(self.make_opt_surfs(), 1):
            self.opt_rects.append(self.blit_opt(surf, split_width * i))

    def make_opt_surf(self, opt, font_col=(70, 0, 6)):
        """Returns a new surface using the font passed into the constructor.

        :param opt: The option to be displayed.
        :param font_col: The surface to display the option on.
        """
        return self.font.render(opt, False, font_col).convert()

    def make_opt_surfs(self):
        """Returns a list of surfaces from the opts passed into the constructor
        """
        return [self.make_opt_surf(opt) for opt in self.opts]

    def process_input(self, events):
        """Handles input from the user.

        :param events: The events to be handled.
        """
        for event in events:
            if event.type is QUIT:
                self.switch_scene(None)
            elif event.type is MOUSEMOTION:
                for i, opt_rect in enumerate(self.opt_rects):
                    self.image.blit(self.make_opt_surf(self.assoc[i], (156, 68, 108) if opt_rect.collidepoint(
                        event.pos) else (70, 0, 6)), opt_rect)
            elif event.type is MOUSEBUTTONDOWN:
                for i, opt_rect in enumerate(self.opt_rects):
                    if opt_rect.collidepoint(event.pos):
                        if self.opts[i] is 'QUIT':
                            self.switch_scene(None)
                        elif self.opts[i] is 'PLAY':
                            self.switch_scene(Game(self.images, 2, self.font))
                        else:
                            call(['pytest', 'test.py'])
                            self.switch_scene(None)

    def update(self, display, events):
        """Updates self and processes user input.

        :param display: The game display.
        :param events: The events to be handled.
        """
        self.process_input(events)
        display.blit(self.image, display.get_rect())
