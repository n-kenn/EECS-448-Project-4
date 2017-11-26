from pygame.locals import K_BACKSPACE, K_RETURN, KEYDOWN, QUIT

from game import Game
from scene import Scene


class Name_Input(Scene):
    def __init__(self, images, font):
        super(Name_Input, self).__init__()
        self.background = images['sky'].copy()
        self.image = self.background.copy()
        self.font = font
        self.name = ''
        self.next_scene = Game(images, self.font)

    def process_input(self, events, keys):
        for event in events:
            if event.type is QUIT:
                self.switch_scene(None)
            elif event.type is KEYDOWN:
                if event.unicode.isalpha():
                    if len(self.name) < 8:
                        self.name += event.unicode
                elif event.key == K_BACKSPACE:
                    self.name = self.name[:-1]
                elif event.key == K_RETURN:
                    self.switch_scene(self.next_scene)

    def update(self, display, events, keys):
        self.process_input(events, keys)
        self.image = self.background.copy()
        if self.name:
            name = self.font.render(self.name, False, (156, 68, 108))
            self.image.blit(name,
                            name.get_rect(center=display.get_rect().center))
        display.blit(self.image, (0, 0))
