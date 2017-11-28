from pygame.locals import MOUSEBUTTONDOWN, MOUSEMOTION, QUIT

from input_screen import Input_Screen
from scene import Scene


class Title_Screen(Scene):
    """Provides a menu for UI.

    :param images: Will get passed to Game constructor.
    :param opts: Iterable of options as strings available to select.
    :param font: Which font to render opt_surfs in.
    """

    def __init__(self, images, font):
        super(Title_Screen, self).__init__()
        self.images = images
        self.image = self.images['sky'].copy()
        self.rect = self.image.get_rect()
        self.font = font
        self.opts = ['START', 'QUIT']
        self.opt_rects = []
        self.blit_opts()

    def blit_opt(self, opt_surf, y):
        """Blits a single opt_surf to self.image and returns a Rect of the effected area.

        :param opt_surf: The option to be displayed.
        :param y: The y coordinate to put the option on.
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
                    if opt_rect.collidepoint(event.pos):
                        self.image.blit(self.make_opt_surf(
                            self.opts[i], (70, 0, 6)), opt_rect)
                    else:
                        self.image.blit(self.make_opt_surf(
                            self.opts[i]), opt_rect)
            elif event.type is MOUSEBUTTONDOWN:
                for i, opt_rect in enumerate(self.opt_rects):
                    if opt_rect.collidepoint(event.pos):
                        if self.opts[i] is 'START':
                            self.switch_scene(
                                Input_Screen(self.images, self.font))
                        elif self.opts[i] is 'QUIT':
                            self.switch_scene(None)

    def update(self, display, events):
        """Updates self and processes user input.

        :param display: The game display.
        :param events: The events to be handled.
        """
        self.process_input(events)
        display.blit(self.image, display.get_rect())
