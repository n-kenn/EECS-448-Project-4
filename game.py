from itertools import cycle
from random import sample

from pygame.locals import MOUSEBUTTONDOWN, QUIT
from pygame.sprite import Group

from player import Player
from scene import Scene
from world import World


class Game(Scene):
    """Scene that implements the actual game.

    :param player_ss: spritesheet to use for the player.
    :param bg_image: surface to use for the background
    :param ground_image: surface to use for the ground
    """

    def __init__(self, player_ss, bg_image, ground_image):
        super(Game, self).__init__()
        self.world = World(bg_image, ground_image)
        self.players = Group([Player(player_ss,
                                     self.world.ground,
                                     loc) for loc in sample(self.world.start_locs, 2)])
        self.player_cycler = cycle(self.players)
        self.active = self.player_cycler.next()

    def draw(self, surf):
        """Draws players to the display using the sprites' image and rect.
        :param surf: Surface to draw to.
        """
        self.world.draw(surf)
        self.players.draw(surf)

    def game_over(self):
        """Returns true when one player remains in the players sprite group.
        """
        return len(self.players) is 1

    def process_input(self, events, keys):
        """Handles all user input
        """
        self.active.check_keys(keys)
        for event in events:
            if event.type is QUIT:
                self.switch_scene(None)
            elif event.type is MOUSEBUTTONDOWN:
                self.active.fire(event.pos,
                                 self.players.sprites() + [self.world.ground])
                self.switch_turns()

    def switch_turns(self):
        """When a player's actions are done, switch active player.
        """
        if not self.game_over():
            self.active = self.player_cycler.next()

    def update(self, display, events, keys):
        """Updates self and processes user input.
        """
        self.process_input(events, keys)
        self.world.update()
        self.players.update(self.world)
        self.draw(display)
