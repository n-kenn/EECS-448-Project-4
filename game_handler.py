from itertools import cycle


class Game_Handler:
    """Handles players in the game.

    :param players: Players to keep track of.
    """

    def __init__(self, players):
        self.players = players
        self.player_cycler = cycle(self.players)
        self.active = self.player_cycler.next()
        self.winner = None

    def game_over(self):
        """Returns true when one player remains.
        """
        if len(self.players) is 1:
            self.winner = 'Winner: ' + self.players.sprites()[0].name
            return True

    def switch_turns(self):
        """When a player's actions are done, switch active player.
        """
        self.active = self.player_cycler.next()
