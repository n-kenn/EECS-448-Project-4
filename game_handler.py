from copy import copy
from itertools import cycle

class Game_Handler:
    """Handles Turns in the game.

    :param players: The players in the game.
    :param world: A reference to the world.
    """

    def __init__(self, players, world):
        self.players = players
        self.collidables = copy(self.players)
        self.collidables.append(world.ground)
        self.player_cycler = cycle(self.players)
        self.active = self.player_cycler.next()
        self.winner = None

    def game_over(self):
        """Returns true when one of the players has died.
        """
        for num, player in enumerate(self.players, 1):
            if not player.alive():
                self.winner = 'Winner: Player {:d}'.format(num)
                return True

    def switch_turns(self):
        """When a player's actions are done, switch active player.
        """
        self.active = self.player_cycler.next()
