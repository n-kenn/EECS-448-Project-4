class Game_Handler:
    """Handles Turns in the game.

    :param players: The players in the game.
    """

    def __init__(self, players):
        self.players = players
        self.active, self.inactive = self.players
        self.winner = None

    def switch_turns(self):
        """When a player's actions are done, switch active player.
        """
        self.active, self.inactive = self.inactive, self.active

    def game_over(self):
        """Returns true when one of the players has died.
        """
        for num, player in enumerate(self.players, 1):
            if not player.alive():
                self.winner = 'Winner: Player {:d}'.format(num)
                return True
