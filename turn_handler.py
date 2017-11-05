class Turn_Handler:
    """Handles Turns in the game.

    :param players: The players in the game.
    """

    def __init__(self, players):
        self.active_player, self.inactive_player = players

    def switch_turns(self):
        """When a player's actions are done, switch which player is the active player.
        """
        self.active_player, self.inactive_player = self.inactive_player, self.active_player
        return self.active_player
