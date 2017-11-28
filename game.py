from itertools import cycle
from random import sample

from pygame.key import get_pressed
from pygame.locals import KEYDOWN, MOUSEBUTTONDOWN, QUIT

from player import Player
from scene import Scene
from team import Team
from world import World


class Game(Scene):
    """Scene that implements the actual game.

    :param images: Image surfaces for various things.
    :param font: The font to load up.
    """

    def __init__(self, images, font):
        super(Game, self).__init__()
        self.world = World(images)
        self.team = Team('Wizards', [Player(images['player_ss'], loc)
                                     for loc in sample(self.world.start_locs, 4)])
        self.player_cycler = cycle(self.team)
        self.active = self.player_cycler.next()
        self.font = font
        self.render = self.make_banner()

    def draw(self, surf):
        """Draws players to the display using the sprites' image and rect.

        :param surf: Surface to draw to.
        """
        self.world.draw(surf)
        self.team.draw(surf)
        if not self.game_over():
            surf.blit(self.render,
                      self.render.get_rect(midtop=surf.get_rect().midtop))

    def game_over(self):
        """Returns true when one player remains in the team sprite group.
        """
        return len(self.team) is 1

    def process_input(self, events):
        """Handles all user input

        :param events: The events to be handled, which in this case correspond to either quit or mousebuttondown
        """
        for event in events:
            if event.type is QUIT:
                self.switch_scene(None)
            elif event.type is MOUSEBUTTONDOWN:
                self.active.fire(event.pos,
                                 self.team.sprites() + [self.world.ground])
                self.switch_turns()

    def make_banner(self):
        """Helper function to render whose turn it is.
        """
        return self.font.render('Go, {}!'.format(self.team.name),
                                False,
                                (156, 68, 108)).convert()

    def switch_turns(self):
        """When a player's actions are done, switch active player and render new text.
        """
        if not self.game_over():
            self.active = self.player_cycler.next()
            self.banner = self.make_banner()

    def update(self, display, events):
        """Updates self and processes user input.

        :param display: The game display.
        :param events: The events to be handled.
        """
        self.process_input(events)
        self.active.check_movement(self.world.ground, get_pressed())
        self.world.update()
        self.team.update(self.world)
        self.draw(display)
        if self.game_over():
            win = self.font.render('Winner: {}'.format(self.team.name),
                                   False,
                                   (156, 68, 108)).convert()
            display.blit(win, win.get_rect(center=display.get_rect().center))
