from itertools import cycle

from pygame.locals import MOUSEBUTTONDOWN, QUIT
from pygame.sprite import Group

from player import Player
from scene import Scene
from world import World


class Game(Scene):
    """Handles players in the game.

    :param player_ss: spritesheet to use for the player.
    :param world: Reference to world to pass information to players.
    """

    def __init__(self, player_ss, sky_image, ground_image):
        super(Game, self).__init__()
        self.world = World(sky_image, ground_image)
        self.players = Group([Player(player_ss,
                                     self.world.ground,
                                     loc) for loc in self.world.start_locs])
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
        self.active.check_keys(keys)
        for event in events:
            if event.type is QUIT:
                self.switch_scene(None)
            elif event.type is MOUSEBUTTONDOWN:
                self.active.fire(
                    event.pos, self.players.sprites() + [self.world.ground])
                self.switch_turns()

    def switch_turns(self):
        """When a player's actions are done, switch active player.
        """
        if not self.game_over():
            self.active = self.player_cycler.next()

    def update(self, display, events, keys):
        self.process_input(events, keys)
        self.world.update()
        self.players.update(self.world)
        self.draw(display)
