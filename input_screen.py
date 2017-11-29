from pygame.locals import K_BACKSPACE, K_RETURN, KEYDOWN, QUIT

from game import Game
from scene import Scene


class Input_Screen(Scene):
    """Handles title screen input

    :param images: The images to load (sky, sprites, etc.)
    :param font: The font to load in.
    """

    def __init__(self, images, font):
        super(Input_Screen, self).__init__()
        self.images = images
        self.background = self.images['sky'].copy()
        self.image = self.background.copy()
        self.rect = self.image.get_rect()
        self.split = self.rect.height // 3
        self.font = font
        self.font_col = (156, 68, 108)
        self.input = ''
        self.gen = self.active_num = None
        self.names = []
        self.num, self.name = True, False

    def ask(self):
        """Blits to self.image a question to get num players and names of players.
        """
        q = self.font.render('How many are playing?' if self.num else 'Name of Player {}?'.format(self.active_num),
                             False,
                             self.font_col).convert()
        self.image.blit(q, q.get_rect(center=(self.rect.centerx, self.split)))

    def process_input(self, events, keys):
        """Handles all user input and checks if valid input.

        :param events: The events to be handled.
        :param keys: The list of keys and which ones are pressed down or not.
        """
        for event in events:
            if event.type is QUIT:
                self.switch_scene(None)
            elif event.type is KEYDOWN:
                if event.unicode.isalnum():
                    self.input += event.unicode
                elif event.key == K_BACKSPACE:
                    self.input = self.input[:-1]
                elif event.key == K_RETURN:
                    if self.num and self.input.isdigit() and int(self.input) > 1:
                        self.gen = (p for p in range(1, 1 + int(self.input)))
                        self.num, self.name = self.name, self.num
                        self.active_num = self.gen.next()
                    elif self.name and self.input.isalpha() and len(self.input) < 10:
                        self.names.append(self.input)
                        try:
                            self.active_num = self.gen.next()
                        except StopIteration:
                            self.switch_scene(
                                Game(self.images, self.names, self.font))
                    self.input = ''

    def update(self, display, events, keys):
        """Updates self and processes user input.

        :param display: The game display.
        :param events: The events to be handled.
        :param keys: The list of keys and which ones are pressed down or not.
        """
        self.process_input(events, keys)
        self.image = self.background.copy()
        self.ask()
        input = self.font.render(self.input, False, self.font_col)
        self.image.blit(input,
                        input.get_rect(center=(self.rect.centerx, 2 * self.split)))
        display.blit(self.image, (0, 0))
