from itertools import cycle
from random import sample

from pygame.locals import MOUSEBUTTONDOWN, QUIT
from pygame.sprite import Group

from player import Player
from scene import Scene
from world import World


class Game(Scene):
    """Scene that implements the actual game.

    :param images: Image surfaces for various things.
    :param names: List of character names.
    :param font: The font to load up.
    """

    def __init__(self, images, names, font):
        super(Game, self).__init__()
        self.world = World(images)
        self.players = Group(Player(images['player_ss'], self.world.ground, loc, names[i])
                             for i, loc in enumerate(sample(self.world.start_locs, len(names))))
        self.player_cycler = cycle(self.players)
        self.active = self.player_cycler.next()
        self.font = font
        self.render = self.render_turn(self.active.name)

    def draw(self, surf):
        """Draws players to the display using the sprites' image and rect.

        :param surf: Surface to draw to.
        """
        self.world.draw(surf)
        self.players.draw(surf)
        surf.blit(self.render, self.render.get_rect(
            midtop=surf.get_rect().midtop))

    def game_over(self):
        """Returns true when one player remains in the players sprite group.
        """
        return len(self.players) is 1

    def process_input(self, events, keys):
        """Handles all user input

        :param events: The events to be handled, which in this case correspond to either quit or mousebuttondown
        :param keys: The keys to be processed.
        """
        self.active.check_keys(keys)
        for event in events:
            if event.type is QUIT:
                self.switch_scene(None)
            elif event.type is MOUSEBUTTONDOWN:
                self.active.fire(event.pos,
                                 self.players.sprites() + [self.world.ground])
                self.switch_turns()

    def render_turn(self, name):
        """Helper function to render players' names.

        :param name: The name of the active player.
        """
        return self.font.render('{}\'s turn'.format(self.active.name),
                                False,
                                (156, 68, 108))

    def switch_turns(self):
        """When a player's actions are done, switch active player and render new text.
        """
        if not self.game_over():
            self.active = self.player_cycler.next()
            self.render = self.render_turn(self.active.name)

    def update(self, display, events, keys):
        """Updates self and processes user input.

        :param display: The size of the window.
        :param events: The events to be handled.
        :param keys: The list of all keys and whether they are pressed or not.
        """
        self.process_input(events, keys)
        self.world.update()
        self.players.update(self.world)
        self.draw(display)
        if self.game_over():
            win = self.font.render('Winner: {}'.format(
                self.active.name), False, (156, 68, 108)).convert()
            display.blit(win, win.get_rect(center=display.get_rect().center))
